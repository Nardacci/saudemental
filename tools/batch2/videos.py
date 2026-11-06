import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import FL_REEL, AN_REEL, POSTS  # noqa

FADE = 0.4


def make(reel, folder, wav, out):
    durs = [d for _, _, d in reel['scenes']]
    n = len(durs)
    cmd = ['ffmpeg', '-v', 'error', '-y']
    for i, d in enumerate(durs, 1):
        cmd += ['-loop', '1', '-t', str(d + FADE), '-i', os.path.join(folder, 'scenes', 'cena%d.jpg' % i)]
    cmd += ['-i', wav]
    fc, prev, acc = [], '[0:v]', 0.0
    for i in range(1, n):
        acc += durs[i - 1] - FADE + FADE  # início da transição = soma das durações anteriores - (i)*FADE
    # offsets: cada cena dura d; a transição i começa em sum(d[:i]) - i*FADE
    parts = []
    for i in range(n):
        parts.append('[%d:v]setsar=1,fps=30,format=yuv420p[v%d]' % (i, i))
    fc = ';'.join(parts) + ';'
    cum = 0.0
    prev = '[v0]'
    for i in range(1, n):
        cum += durs[i - 1]
        off = cum - i * FADE
        nxt = '[x%d]' % i
        fc += '%s[v%d]xfade=transition=fade:duration=%s:offset=%.2f%s;' % (prev, i, FADE, off, nxt)
        prev = nxt
    total = sum(durs) - (n - 1) * FADE
    fc += '[%d:a]volume=0.6,afade=t=out:st=%.2f:d=1.5[aud]' % (n, total - 1.5)
    cmd += ['-filter_complex', fc, '-map', prev, '-map', '[aud]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
            '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-t', '%.2f' % total, '-movflags', '+faststart', out]
    subprocess.check_call(cmd)
    print(out, total)


if __name__ == '__main__':
    wavdir = sys.argv[1]
    f1 = os.path.join(POSTS, FL_REEL['slug'])
    make(FL_REEL, f1, os.path.join(wavdir, 'flavia.wav'), os.path.join(f1, 'video.mp4'))
    f2 = os.path.join(POSTS, 'andre', 'reels', AN_REEL['slug'])
    make(AN_REEL, f2, os.path.join(wavdir, 'andre.wav'), os.path.join(f2, 'video.mp4'))
