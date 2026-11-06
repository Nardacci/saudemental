"""Remessa 2 (11/11 a 17/11): carrosséis, imagens, Stories e cenas dos Reels."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *  # noqa

FOOT_F = ("\n\nAtendimento psicológico online, em português, para todo o Brasil e brasileiros(as) no exterior.\n"
          "👉 Quer conversar? Agende sua sessão pelo link na bio: @psi_flavianardacci\n\n"
          "⚠️ Em crise? No Brasil: CVV 188 (24h, gratuito) ou SAMU 192. No exterior: ligue para o número de emergência local.\n\n"
          "Flávia Nardacci · Psicóloga · CRP 05/75090\n\n")

# ===================== FLÁVIA: carrosséis e imagem =====================
FL_POSTS = {
    '2026-11-13-culpa-longe': dict(
        slides=[
            dict(title='Culpa por estar **longe**', body='Por que ela aparece e o que fazer com ela.', swipe=True),
            dict(title='Por que **acontece**', body='Você construiu uma vida nova, mas seus vínculos continuam lá. Culpa e saudade costumam andar juntas.'),
            dict(title='Como ela **aparece**', bullets=['Pensar que deveria estar presente.', 'Sentir-se mal por estar bem.', 'Evitar contar o que está difícil.']),
            dict(title='O que **ajuda**', bullets=['Combinar chamadas em horários fixos.', 'Dividir o que sente com alguém de confiança.', 'Lembrar: cuidar de si também é cuidar de quem você ama.']),
            dict(title='Quando buscar **ajuda**', body='Se a culpa vira tristeza constante, afeta o sono ou o trabalho, vale conversar com um(a) profissional.'),
            dict(title='Você não precisa carregar isso **sozinho(a).**', body='Culpa e saudade também merecem cuidado.', cta=True),
        ],
        caption=("Sentir culpa por estar longe da família é mais comum do que parece. 💜\n\n"
                 "Ela costuma vir junto com a saudade e com a vontade de cuidar de quem ficou. Entender de onde vem ajuda a lidar com ela.\n\n"
                 "📌 Salve para ler de novo.\n📤 Envie para quem precisa ouvir isso."
                 + FOOT_F + "#brasileirosnoexterior #morarfora #culpa #saudemental #psicologaonline")),
    '2026-11-17-fim-de-ano-longe': dict(
        slides=[
            dict(title='Fim de ano **longe de casa**', body='Como atravessar as festas sem se perder na saudade.', swipe=True),
            dict(title='Por que **pesa**', body='As festas mexem com memória, família e tradição. Estar longe pode intensificar a saudade.'),
            dict(title='**Antes** das festas', bullets=['Combine a chamada de vídeo com antecedência.', 'Planeje uma refeição que lembre casa.', 'Convide alguém para celebrar com você.']),
            dict(title='**No dia**', bullets=['Permita-se sentir saudade, sem se cobrar.', 'Evite se comparar com o que vê nas redes.', 'Faça uma pausa se precisar.']),
            dict(title='Sinais de **alerta**', body='Tristeza que dura semanas, isolamento ou perda de interesse. Nesse caso, busque apoio profissional.'),
            dict(title='Você não precisa passar por isso **sozinho(a).**', body='Terapia online, em português, onde você estiver.', cta=True),
        ],
        caption=("O fim de ano costuma pesar mais para quem está longe de casa. 💜\n\n"
                 "Dá para se organizar antes: combinar chamadas com a família, criar um ritual seu e pedir apoio se a tristeza durar.\n\n"
                 "📌 Salve para consultar.\n📤 Envie para quem vai passar as festas longe."
                 + FOOT_F + "#brasileirosnoexterior #fimdeano #saudemental #morarfora #psicologaonline")),
}
FL_SINGLE = {
    '2026-11-15-terapia-nao-e-so-para-quem-esta-mal': dict(
        title='Terapia não é só para quem **está mal.**',
        body='Também é para entender o que você sente, lidar com mudanças e se cuidar antes de a dor pesar.',
        caption=("Terapia não é só para quem está mal. 💜\n\n"
                 "Também serve para entender o que sente, lidar com mudanças e se cuidar antes de a dor pesar.\n\n"
                 "💬 O que te fez adiar a terapia?"
                 + FOOT_F + "#terapia #saudemental #autocuidado #psicologaonline #terapiaonline")),
}

# ===================== ANDRÉ: carrosséis e imagem =====================
AN_FOOT = "\n\n➕ Follow for more Business Analysis tips.\n\n"
AN_POSTS = {
    '2026-11-11-moscow-5-minutes': dict(
        slides=[
            dict(title='MoSCoW in **5 minutes**', body='Prioritize requirements without the drama.', swipe=True),
            dict(title='M = **Must**', body='Without it, the release fails. Non-negotiable.'),
            dict(title='S = **Should**', body='Important, but there is a workaround. Do it if you can.'),
            dict(title='C = **Could**', body='Nice to have. The first to go when time runs out.'),
            dict(title="W = **Won't** (this time)", body="Agreed as out of scope for now. Not \"never\"."),
            dict(title='**Tip:** cap the Musts', body='A common guideline: keep Musts to about 60% of the effort, so there is room for the unexpected.'),
        ],
        caption=("Too many \"top priority\" requests? Use MoSCoW: Must, Should, Could, Won't (this time). ✅\n\n"
                 "It turns a long wish list into a clear plan.\n\n"
                 "💬 Which bucket is hardest to say no to?\n📌 Save this for your next prioritization meeting."
                 + AN_FOOT + "#BusinessAnalyst #MoSCoW #Prioritization #Agile #ProductOwner")),
    '2026-11-17-stakeholder-map': dict(
        slides=[
            dict(title='Stakeholder map: **Power × Interest**', body='Who needs your attention first?', swipe=True),
            dict(title='High power, high interest', body='**Manage closely.** Involve them in decisions.'),
            dict(title='High power, low interest', body='**Keep satisfied.** Share what matters, briefly.'),
            dict(title='Low power, high interest', body='**Keep informed.** Updates and a place to give feedback.'),
            dict(title='Low power, low interest', body='**Monitor.** Revisit if the project changes.'),
            dict(title='**Tip:** revisit the map', body='People move between boxes as the project evolves. Review it at each phase.'),
        ],
        caption=("Not every stakeholder needs the same attention. 🧭\n\n"
                 "Map them by Power × Interest: manage closely, keep satisfied, keep informed, monitor.\n\n"
                 "💬 Who's in your \"manage closely\" box?\n📌 Save this."
                 + AN_FOOT + "#BusinessAnalyst #Stakeholders #StakeholderManagement #Agile #Requirements")),
}
AN_SINGLE = {
    '2026-11-15-ready-vs-done': dict(
        title='Ready ≠ **Done**',
        body='**Ready:** we understand it and can start. **Done:** the user can use it.',
        caption=("Ready means we understand it. Done means the user can use it. ✅\n\n"
                 "Mixing them up is where rework starts.\n\n"
                 "💬 How does your team define Done?\n📌 Save this."
                 + AN_FOOT + "#BusinessAnalyst #DefinitionOfDone #Agile #Scrum #UserStories")),
}

# ===================== REELS =====================
FL_REEL = dict(
    slug='2026-11-11-reel-e-quando-voce-volta',
    scenes=[
        ("POV: sua família no Brasil pergunta **\"e quando você volta?\"**", None, 3.2),
        ("Você sorri e responde: **\"ainda não sei.\"**", None, 3.2),
        ("Por dentro: **saudade, culpa e dúvida** ao mesmo tempo.", None, 3.6),
        ("As duas coisas podem ser verdade: **amar a vida aqui** e sentir falta de lá.", None, 4.0),
        ("Você não precisa decidir **sozinho(a).**", "Terapia online, em português. Link na bio.", 4.0),
    ],
    caption=("Quem mora fora conhece essa pergunta. 💛\n\n"
             "Às vezes ela vem com carinho, às vezes pesa. As duas coisas podem ser verdade.\n\n"
             "📤 Envie para alguém que mora longe de casa.\n💬 Qual pergunta da família você mais escuta?"
             + FOOT_F + "#brasileirosnoexterior #morarfora #saudade #saudemental #psicologaonline"))
AN_REEL = dict(
    slug='2026-11-13-reel-everything-is-p1',
    scenes=[
        ("Stakeholder: **\"Everything is P1.\"**", None, 3.0),
        ("BA: **\"Great. Which one first?\"**", None, 3.0),
        ("Stakeholder: **\"All of them.\"**", None, 3.0),
        ("BA: **\"Then let's rank by value and effort.\"**", None, 3.6),
        ("Priorities are **a choice,** not a list.", "Follow for more BA tips.", 4.0),
    ],
    caption=("Stakeholder: \"Everything is P1.\" 😅\nBA: \"Then nothing is.\"\n\n"
             "Prioritization is not about saying no. It's about showing the trade-off.\n\n"
             "💬 What's your go-to answer to \"it's all urgent\"?\n📌 Save this.\n➕ Follow for more Business Analysis tips (with a bit of humor).\n\n"
             "#BusinessAnalyst #TechHumor #Prioritization #Agile #Requirements"))

# ===================== STORIES =====================
DAYS = ['2026-11-11', '2026-11-12', '2026-11-13', '2026-11-14', '2026-11-15', '2026-11-16', '2026-11-17']
FL_ST = {  # 3 por dia: 18h30, 19h30, 21h30
    '2026-11-11': [('QUEM MORA FORA', 'Quem mora fora conhece a pergunta: **"e quando você volta?"**', 'Hoje às 20h30 tem Reels novo.'),
                   ('REFLEXÃO', 'Saudade não é **fraqueza.**', 'É sinal de que você construiu vínculos.'),
                   ('BOA NOITE', 'Você não precisa dar conta de **tudo hoje.**', 'Respirar também é cuidar.')],
    '2026-11-12': [('TERAPIA', 'Terapia online, em português, **onde você estiver.**', 'Brasil e exterior. Agende pelo link na bio.'),
                   ('PERGUNTA DO DIA', 'O que você mais **sente falta** do Brasil hoje?', 'Pense nisso hoje à noite.'),
                   ('CUIDADO', 'Dormir bem também é **saúde mental.**', 'Desligue as telas 30 minutos antes.')],
    '2026-11-13': [('SEXTA', 'Culpa por estar longe? Você **não está sozinho(a).**', 'Hoje às 20h30: carrossel sobre isso.'),
                   ('LEMBRETE', 'Pedir ajuda é um ato de **coragem.**', None),
                   ('BOA NOITE', 'Descanse. **Amanhã é outro dia.**', None)],
    '2026-11-14': [('FIM DE SEMANA', 'Combine uma chamada com **quem você ama.**', 'Distância não precisa virar silêncio.'),
                   ('CUIDADO', 'Hoje, faça uma coisa **só para você.**', 'Pode ser pequena.'),
                   ('REFLEXÃO', 'Você também merece ser **cuidado(a).**', None)],
    '2026-11-15': [('MITO', '"Terapia é só para quem está mal."', 'Mito. Terapia é **cuidado,** também antes de a dor pesar.'),
                   ('DOMINGO', 'Domingo à noite pesa? **É comum.**', 'Crie um pequeno ritual para começar a semana.'),
                   ('BOA NOITE', 'Uma semana nova. **Um passo de cada vez.**', 'Hoje às 20h30: post sobre terapia.')],
    '2026-11-16': [('SEGUNDA', 'Segunda começa com **um passo pequeno.**', 'Escolha uma tarefa só para hoje.'),
                   ('ACOLHIMENTO', 'Se a tristeza dura semanas, **vale buscar ajuda.**', 'Terapia online: link na bio.'),
                   ('BOA NOITE', 'Amanhã às 20h30: **fim de ano longe de casa.**', None)],
    '2026-11-17': [('FIM DE ANO', 'As festas longe de casa **podem pesar.**', 'Hoje às 20h30: carrossel para se preparar.'),
                   ('IDEIA', 'Crie um **ritual seu** para as festas.', 'Uma comida, uma música, uma chamada.'),
                   ('OBRIGADA', 'Obrigada por acompanhar a **semana.**', 'Cuide de você.')],
}
AN_ST = {  # 3 por dia: 18h, 19h, 21h
    '2026-11-11': [('BA TIP', 'Everything is a priority? **Use MoSCoW.**', 'Today 8pm: new carousel.'),
                   ('QUESTION', "What's your **toughest** stakeholder challenge?", 'Think about it tonight.'),
                   ('TIP', 'Write requirements a **tester can verify.**', None)],
    '2026-11-12': [('BA TIP', 'Ask **"why"** five times.', 'Find the real need behind the request.'),
                   ('QUICK TIP', 'Name tasks with **a verb.**', '"Review order", not "Order review".'),
                   ('REMINDER', 'A good question beats **a long document.**', None)],
    '2026-11-13': [('FRIDAY HUMOR', '"It\'s a **simple** change."', 'Narrator: it was not.'),
                   ('TODAY 8PM', 'New Reel: when **everything is P1.**', None),
                   ('WEEKEND READ', 'Reread one old requirement. **Is it still testable?**', None)],
    '2026-11-14': [('BA TIP', 'Write the **benefit** first.', 'As a user, I want X, so that Y.'),
                   ('LEARNING', 'Pick **one concept** to study this weekend.', 'BPMN, MoSCoW or user stories.'),
                   ('REMINDER', 'Rest is **part of the job** too.', None)],
    '2026-11-15': [('READY VS DONE', '**Ready:** we understand it.', 'Done: the user can use it.'),
                   ('PLAN', 'Plan your week: **three priorities,** not ten.', None),
                   ('TONIGHT 8PM', 'New post: **Ready vs Done.**', None)],
    '2026-11-16': [('MONDAY', 'Start the week with **one clear goal.**', None),
                   ('BA TIP', 'Clarify **scope** before you estimate.', None),
                   ('TOMORROW', 'Tomorrow 8pm: **stakeholder map** carousel.', None)],
    '2026-11-17': [('STAKEHOLDERS', 'Power × Interest: **who needs attention?**', 'New carousel tonight, 8pm.'),
                   ('QUESTION', "Who's in your **\"manage closely\"** box?", None),
                   ('THANK YOU', 'Thanks for following this week.', 'More BA tips soon.')],
}

FL_ST_FILES = ['h1830.jpg', 'h1930.jpg', 'h2130.jpg']
AN_ST_FILES = ['h18.jpg', 'h19.jpg', 'h21.jpg']


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text.rstrip() + '\n')


def main():
    for slug, p in FL_POSTS.items():
        n = len(p['slides'])
        for i, s in enumerate(p['slides'], 1):
            kind = 'light' if i % 2 == 1 else 'dark'
            im = flavia_slide(i, n, kind, s['title'], s.get('body'), s.get('bullets'), s.get('swipe', False), s.get('cta', False))
            save(im, os.path.join(POSTS, slug, 'slide%d.jpg' % i))
        write(os.path.join(POSTS, slug, 'caption.txt'), p['caption'])
    for slug, p in FL_SINGLE.items():
        im = flavia_slide(1, 1, 'dark', p['title'], p['body'], None, False, False, chip_text='SAÚDE MENTAL', single=True)
        save(im, os.path.join(POSTS, slug, 'slide1.jpg'))
        write(os.path.join(POSTS, slug, 'caption.txt'), p['caption'])
    for slug, p in AN_POSTS.items():
        n = len(p['slides'])
        for i, s in enumerate(p['slides'], 1):
            im = andre_slide(i, n, s['title'], s.get('body'), s.get('bullets'), s.get('swipe', False))
            save(im, os.path.join(POSTS, 'andre', slug, 'slide%d.jpg' % i))
        write(os.path.join(POSTS, 'andre', slug, 'caption.txt'), p['caption'])
    for slug, p in AN_SINGLE.items():
        im = andre_slide(1, 1, p['title'], p['body'], None, False, chip_text='AGILE', single=True)
        save(im, os.path.join(POSTS, 'andre', slug, 'slide1.jpg'))
        write(os.path.join(POSTS, 'andre', slug, 'caption.txt'), p['caption'])
    # cenas dos reels
    for reel, folder, fn in ((FL_REEL, os.path.join(POSTS, FL_REEL['slug']), flavia_scene),
                             (AN_REEL, os.path.join(POSTS, 'andre', 'reels', AN_REEL['slug']), andre_scene)):
        for i, (t, sub, dur) in enumerate(reel['scenes'], 1):
            save(fn(t, sub), os.path.join(folder, 'scenes', 'cena%d.jpg' % i))
        save(fn(*reel['scenes'][0][:2]), os.path.join(folder, 'capa.jpg'))
        write(os.path.join(folder, 'caption.txt'), reel['caption'])
    # stories
    for day in DAYS:
        for i, (c, t, s) in enumerate(FL_ST[day]):
            save(flavia_story(c, t, s), os.path.join(POSTS, 'stories-flavia', day, FL_ST_FILES[i]))
        for i, (c, t, s) in enumerate(AN_ST[day]):
            save(andre_story(c, t, s), os.path.join(POSTS, 'andre', 'stories', day, AN_ST_FILES[i]))
    print('ok')


if __name__ == '__main__':
    main()
