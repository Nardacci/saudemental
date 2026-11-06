"""Biblioteca de renderização dos posts (Pillow). Estilo igual ao dos posts anteriores."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FD = '/usr/share/fonts/opentype/inter/'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
POSTS = os.path.join(ROOT, 'posts')


def font(weight, size):
    return ImageFont.truetype(FD + 'Inter-%s.otf' % weight, size)


# ---------- paletas ----------
LIGHT_BG = (230, 243, 236)
DARK_BG = (15, 76, 69)
FL_DARK_TXT = (14, 62, 52)
FL_GREEN = (16, 138, 95)
FL_YELLOW = (244, 196, 48)
FL_MUTED_L = (90, 130, 115)
FL_MUTED_D = (150, 196, 184)
FL_BODY_L = (48, 90, 78)
FL_BODY_D = (205, 232, 224)

AN_TEAL = (45, 196, 184)
AN_TXT = (200, 215, 240)
AN_CHIP_TXT = (10, 40, 60)

ST_CORAL = (255, 122, 118)
ST_TXT = (226, 216, 246)


# ---------- fundos ----------
def _grid(w, h):
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    return x / w, y / h


def navy(w, h):
    x, y = _grid(w, h)
    base = np.zeros((h, w, 3), np.float32)
    base[:] = (11, 36, 68)
    g1 = np.exp(-(((x - 1.0) ** 2) + ((y - 0.0) ** 2)) / 0.22)
    g2 = np.exp(-(((x - 0.0) ** 2) + ((y - 1.0) ** 2)) / 0.20)
    base += g1[..., None] * np.array([8, 18, 34], np.float32)
    base += g2[..., None] * np.array([8, 40, 30], np.float32)
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))


def purple(w, h):
    x, y = _grid(w, h)
    base = np.zeros((h, w, 3), np.float32)
    base[:] = (62, 38, 92)
    g1 = np.exp(-(((x - 0.1) ** 2) + ((y - 0.05) ** 2)) / 0.25)
    g2 = np.exp(-(((x - 1.0) ** 2) + ((y - 1.0) ** 2)) / 0.25)
    base += g1[..., None] * np.array([12, 14, 22], np.float32)
    base += g2[..., None] * np.array([30, 6, -4], np.float32)
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))


def green(w, h):
    x, y = _grid(w, h)
    base = np.zeros((h, w, 3), np.float32)
    base[:] = (13, 70, 62)
    g1 = np.exp(-(((x - 0.1) ** 2) + ((y - 0.15) ** 2)) / 0.3)
    base += g1[..., None] * np.array([6, 22, 18], np.float32)
    im = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im, 'RGBA')
    d.ellipse((902, 222, 1202, 522), fill=(20, 110, 85, 150))
    d.ellipse((-170, 1345, 340, 1765), fill=(60, 110, 60, 120))
    return im


# ---------- texto ----------
def smart(text):
    out, openq = [], True
    for i, ch in enumerate(text):
        if ch == '"':
            out.append('\u201c' if openq else '\u201d')
            openq = not openq
        elif ch == "'":
            out.append('\u2019')
        else:
            out.append(ch)
    return ''.join(out)


def parse(text):
    """'a **b** c' -> [(palavra, destaque?)]"""
    text = smart(text)
    out, hl = [], False
    for i, part in enumerate(text.split('**')):
        hl = (i % 2 == 1)
        for wd in part.split(' '):
            if wd:
                out.append((wd, hl))
    return out


def wrap(text, fnt, maxw):
    words = parse(text)
    lines, cur, curw = [], [], 0
    sp = fnt.getlength(' ')
    for wd, hl in words:
        w = fnt.getlength(wd)
        add = w if not cur else sp + w
        if cur and curw + add > maxw:
            lines.append(cur)
            cur, curw = [(wd, hl)], w
        else:
            cur.append((wd, hl))
            curw += add
    if cur:
        lines.append(cur)
    return lines


def block_height(text, fnt, maxw, lh):
    return len(wrap(text, fnt, maxw)) * lh


def draw_block(d, x, y, text, fnt, color, hl_color, maxw, lh):
    sp = fnt.getlength(' ')
    for line in wrap(text, fnt, maxw):
        cx = x
        for wd, hl in line:
            d.text((cx, y), wd, font=fnt, fill=hl_color if hl else color)
            cx += fnt.getlength(wd) + sp
        y += lh
    return y


def stack(d, x, y, items, maxw):
    """items: list of dict(text,weight,size,color,hl,lh,gap)"""
    for it in items:
        f = font(it['weight'], it['size'])
        y = draw_block(d, x, y, it['text'], f, it['color'], it.get('hl', it['color']), maxw, it['lh'])
        y += it.get('gap', 0)
    return y


def stack_height(items, maxw):
    h = 0
    for it in items:
        f = font(it['weight'], it['size'])
        h += block_height(it['text'], f, maxw, it['lh']) + it.get('gap', 0)
    return h


def spaced(d, x, y, text, fnt, fill, spacing=2.5):
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += fnt.getlength(ch) + spacing
    return x


def spaced_width(text, fnt, spacing=2.5):
    return sum(fnt.getlength(c) + spacing for c in text) - spacing


def chip(d, x, y, text, bg, fg, size=28, pad=26, h=None):
    f = font('Bold', size)
    w = spaced_width(text, f) + pad * 2
    h = h or int(size * 2.1)
    d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=bg)
    spaced(d, x + pad, y + (h - size) // 2 - 3, text, f, fg)
    return w, h


def center_y(items, maxw, top, bottom):
    h = stack_height(items, maxw)
    return top + max(0, (bottom - top - h) // 2)


# ---------- avatar / foto ----------
def crops():
    src_l = Image.open(os.path.join(POSTS, '2026-10-15-luto-migratorio', 'slide1.jpg')).convert('RGB')
    src_d = Image.open(os.path.join(POSTS, '2026-10-15-luto-migratorio', 'slide2.jpg')).convert('RGB')
    src_c = Image.open(os.path.join(POSTS, '2026-10-15-luto-migratorio', 'slide6.jpg')).convert('RGB')
    return {
        'av_l': src_l.crop((100, 1194, 194, 1288)),
        'av_d': src_d.crop((100, 1194, 194, 1288)),
        'photo': src_c.crop((140, 680, 310, 850)),
    }


# ---------- Flávia: carrossel / post ----------
def flavia_slide(n, total, kind, title, body=None, bullets=None, swipe=False, cta=False,
                 chip_text='SÉRIE · QUEM MORA FORA', single=False):
    dark = (kind == 'dark')
    W, H = 1080, 1350
    bg = DARK_BG if dark else LIGHT_BG
    im = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(im)
    if dark:
        chip(d, 100, 56, chip_text, FL_YELLOW, (15, 76, 69), size=26, h=55)
        tcol, hl, bcol = (255, 255, 255), FL_YELLOW, FL_BODY_D
        muted = FL_MUTED_D
    else:
        chip(d, 100, 56, chip_text, FL_GREEN, (255, 255, 255), size=26, h=55)
        tcol, hl, bcol = FL_DARK_TXT, FL_GREEN, FL_BODY_L
        muted = FL_MUTED_L
    items = [dict(text=title, weight='ExtraBold', size=84 if n == 1 else 70, color=tcol, hl=hl,
                  lh=96 if n == 1 else 82, gap=26)]
    if body:
        items.append(dict(text=body, weight='Regular', size=42, color=bcol, hl=hl, lh=58, gap=22))
    if bullets:
        for b in bullets:
            items.append(dict(text='•  ' + b, weight='Medium', size=42, color=bcol, hl=hl, lh=58, gap=18))
    if swipe:
        items.append(dict(text='Arraste para o lado →', weight='Bold', size=34, color=hl, hl=hl, lh=48, gap=0))
    if cta:
        top = 230
    else:
        top = center_y(items, 880, 150, 1150)
    stack(d, 100, top, items, 880)
    cr = crops()
    if not cta:
        im.paste(cr['av_d' if dark else 'av_l'], (100, 1194))
        d.text((216, 1204), 'Flávia Nardacci', font=font('Bold', 28), fill=tcol)
        x2 = 216 + font('Bold', 28).getlength('Flávia Nardacci')
        d.text((x2, 1204), ' · Psicóloga · CRP 05/75090', font=font('Regular', 28), fill=tcol)
        d.text((216, 1243), '@psi_flavianardacci', font=font('Regular', 27), fill=muted)
    if cta:
        d.rounded_rectangle((100, 700, 980, 942), radius=24, fill=(24, 94, 84))
        d.rounded_rectangle((100, 700, 124, 942), radius=12, fill=FL_YELLOW)
        d.rectangle((112, 700, 124, 942), fill=(24, 94, 84))
        d.rectangle((100, 712, 112, 930), fill=FL_YELLOW)
        im.paste(cr['photo'], (145, 740))
        d.text((332, 735), 'Flávia Nardacci', font=font('Bold', 34), fill=(255, 255, 255))
        d.text((332, 783), 'Psicóloga clínica e hospitalar', font=font('Regular', 32), fill=(215, 240, 232))
        d.text((332, 823), 'CRP 05/75090 · Online: Brasil e exterior', font=font('Regular', 32), fill=(215, 240, 232))
        d.text((332, 867), 'Agende pelo link na bio', font=font('Bold', 34), fill=FL_YELLOW)
        d.rounded_rectangle((100, 982, 980, 1118), radius=26, fill=(255, 255, 255))
        f1, f2 = font('Bold', 29), font('Regular', 29)
        x = 134
        d.text((x, 1004), 'Em crise?', font=f1, fill=FL_GREEN)
        x += f1.getlength('Em crise? ')
        d.text((x, 1004), 'No Brasil: ', font=f2, fill=(40, 40, 40))
        x += f2.getlength('No Brasil: ')
        d.text((x, 1004), 'CVV 188', font=f1, fill=(20, 20, 20))
        x += f1.getlength('CVV 188')
        d.text((x, 1004), ' (24h, gratuito) ou ', font=f2, fill=(40, 40, 40))
        x += f2.getlength(' (24h, gratuito) ou ')
        d.text((x, 1004), 'SAMU 192', font=f1, fill=(20, 20, 20))
        d.text((134, 1048), 'No exterior: ligue para o número de emergência local.', font=f2, fill=(40, 40, 40))
        im.paste(cr['av_d'], (100, 1194))
        d.text((216, 1204), 'Flávia Nardacci', font=font('Bold', 28), fill=(255, 255, 255))
        x2 = 216 + font('Bold', 28).getlength('Flávia Nardacci')
        d.text((x2, 1204), ' · Psicóloga · CRP 05/75090', font=font('Regular', 28), fill=(255, 255, 255))
        d.text((216, 1243), '@psi_flavianardacci', font=font('Regular', 27), fill=muted)
    if not single:
        cnt = '%d/%d' % (n, total)
        f = font('Regular', 30)
        d.text((980 - f.getlength(cnt), 1228), cnt, font=f, fill=muted)
    return im


# ---------- André: carrossel / post ----------
def andre_slide(n, total, title, body=None, bullets=None, swipe=False, chip_text='BUSINESS ANALYSIS',
                single=False):
    W, H = 1080, 1350
    im = navy(W, H)
    d = ImageDraw.Draw(im)
    chip(d, 90, 80, chip_text, AN_TEAL, AN_CHIP_TXT, size=26, h=53)
    if not single:
        cnt = '%d/%d' % (n, total)
        f = font('Regular', 30)
        d.text((990 - f.getlength(cnt), 90), cnt, font=f, fill=AN_TXT)
    items = [dict(text=title, weight='ExtraBold', size=104 if n == 1 else 72, color=(255, 255, 255), hl=AN_TEAL,
                  lh=108 if n == 1 else 84, gap=28)]
    if body:
        items.append(dict(text=body, weight='Regular', size=44, color=AN_TXT, hl=AN_TEAL, lh=60, gap=22))
    if bullets:
        for b in bullets:
            items.append(dict(text='•  ' + b, weight='Medium', size=42, color=AN_TXT, hl=AN_TEAL, lh=58, gap=16))
    if swipe:
        items.append(dict(text='Swipe →', weight='Bold', size=44, color=AN_TEAL, hl=AN_TEAL, lh=56, gap=0))
    top = center_y(items, 900, 160, 1150)
    stack(d, 90, top, items, 900)
    d.text((90, 1245), '@andre.nardacci', font=font('Medium', 30), fill=AN_TXT)
    f = font('Medium', 30)
    t = 'Business Analyst · PSPO I · PSM I'
    d.text((990 - f.getlength(t), 1245), t, font=f, fill=AN_TXT)
    return im


# ---------- Stories ----------
def flavia_story(chip_text, title, sub=None):
    W, H = 1080, 1920
    im = purple(W, H)
    d = ImageDraw.Draw(im)
    chip(d, 90, 260, chip_text, ST_CORAL, (60, 30, 70), size=30, h=64)
    items = [dict(text=title, weight='ExtraBold', size=88, color=(255, 255, 255), hl=ST_CORAL, lh=104, gap=34)]
    if sub:
        items.append(dict(text=sub, weight='Regular', size=46, color=ST_TXT, hl=ST_CORAL, lh=66))
    top = 500
    stack(d, 90, top, items, 900)
    d.text((90, 1530), 'Flávia Nardacci · Psicóloga · CRP 05/75090', font=font('Bold', 34), fill=ST_CORAL)
    d.text((90, 1580), 'Em crise? CVV 188 (24h) · SAMU 192 · No exterior:', font=font('Regular', 33), fill=ST_TXT)
    d.text((90, 1628), 'emergência local', font=font('Regular', 33), fill=ST_TXT)
    return im


def andre_story(chip_text, title, sub=None):
    W, H = 1080, 1920
    im = navy(W, H)
    d = ImageDraw.Draw(im)
    chip(d, 90, 260, chip_text, AN_TEAL, AN_CHIP_TXT, size=30, h=64)
    items = [dict(text=title, weight='ExtraBold', size=88, color=(255, 255, 255), hl=AN_TEAL, lh=104, gap=34)]
    if sub:
        items.append(dict(text=sub, weight='Regular', size=46, color=AN_TXT, hl=AN_TEAL, lh=66))
    stack(d, 90, 500, items, 900)
    d.text((90, 1580), '@andre.nardacci', font=font('Bold', 36), fill=AN_TEAL)
    d.text((90, 1630), 'Business Analyst · PSPO I · PSM I', font=font('Regular', 33), fill=AN_TXT)
    return im


# ---------- Reels (cenas 1080x1920) ----------
def flavia_scene(text, sub=None, chip_text='QUEM MORA FORA'):
    W, H = 1080, 1920
    im = green(W, H)
    d = ImageDraw.Draw(im)
    chip(d, 90, 120, chip_text, FL_YELLOW, (15, 76, 69), size=30, h=62)
    items = [dict(text=text, weight='ExtraBold', size=100, color=(255, 255, 255), hl=FL_YELLOW, lh=116, gap=36)]
    if sub:
        items.append(dict(text=sub, weight='Regular', size=48, color=FL_BODY_D, hl=FL_YELLOW, lh=68))
    top = center_y(items, 900, 260, 1560)
    stack(d, 90, top, items, 900)
    return im


def andre_scene(text, sub=None, chip_text='BUSINESS ANALYSIS'):
    W, H = 1080, 1920
    im = navy(W, H)
    d = ImageDraw.Draw(im)
    chip(d, 90, 120, chip_text, AN_TEAL, AN_CHIP_TXT, size=30, h=62)
    items = [dict(text=text, weight='ExtraBold', size=100, color=(255, 255, 255), hl=AN_TEAL, lh=116, gap=36)]
    if sub:
        items.append(dict(text=sub, weight='Regular', size=48, color=AN_TXT, hl=AN_TEAL, lh=68))
    top = center_y(items, 900, 260, 1560)
    stack(d, 90, top, items, 900)
    d.text((90, 1700), '@andre.nardacci', font=font('Bold', 36), fill=AN_TEAL)
    return im


def save(im, path, q=92):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, quality=q)
