#!/usr/bin/env python3
# ON-BRAND WITHOUT A DESIGNER - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/brandguard"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Every asset on-brand.')],[co('No designer on payroll.')]])
T2.CONTENT=[
 ('THE DRIFT', [[wo('Ten posts,')],[co('ten shades of you.')]], 'Without a designer, every asset negotiates its own fonts and colors.', [co('Drift reads as amateur.')], f"{M}/drift.png", 1.0),
 ('THE TOKENS', [[wo('Your look, written down')],[co('once, as law.')]], 'Colors, type, spacing, logo rules: one token file every asset obeys.', [co('Brand as configuration.')], f"{M}/tokens.png", 1.0),
 ('THE PACK', [[wo('822 components')],[co('already on-brand.')]], 'Cards, heroes, charts, covers: assembled from your pack, never from scratch.', [co('Consistency is prebuilt.')], f"{M}/pack.png", 1.0),
 ('THE OUTPUTS', [[wo('Decks, pages, posts:')],[co('one family.')]], 'The proposal matches the landing page matches the carousel.', [co('Everything rhymes.')], f"{M}/outputs.png", 1.0),
 ('THE SPEED', [[wo('On-brand became')],[co('the fast path.')]], 'No review cycles, no drift fixes: the guardrail makes the quick version the correct one.', [co('Fast and consistent, finally.')], f"{M}/speed8.png", 1.0),
 ('THE GATE', [[wo('New asset types')],[co('get one approval.')]], 'You bless the template once; every instance after inherits the blessing.', [co('Approve patterns, not pieces.')], f"{M}/gate8.png", 1.0),
 ('THE COST', [[wo('The design retainer')],[co('became a token file.')]], 'High bills live in the old workflow. This one is configuration.', [co('Paid once, in setup.')], f"{M}/cost8.png", 1.0),
 ('THE TEST', [[wo('Screenshot any two assets.')],[co('Same company?')]], 'If a stranger cannot tell, the guardrail works.', [co('Run it on your last five.')], f"{M}/test8.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the guardrail setup',l2='and lock your look.',q='What does your brand drift on?')
MARK2="strip"
