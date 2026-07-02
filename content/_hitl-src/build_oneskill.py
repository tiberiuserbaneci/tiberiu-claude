#!/usr/bin/env python3
# ONE SKILL, FIVE INCOMES - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/oneskill"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do not need a new skill.')],[co('You need five shapes of it.')]])
T2.CONTENT=[
 ('THE MYTH', [[wo('Everyone hunts')],[co('a new skill.')]], 'The money was in the one you already have, reshaped five ways.', [co('Look again, differently.')], f"{M}/mythos.png", 1.0),
 ('SHAPE 1', [[wo('The service:')],[co('done for them.')]], 'Your skill, applied to their business. The desk handles briefs, delivery and chasing.', [co('Highest price, first cash.')], f"{M}/service.png", 1.0),
 ('SHAPE 2', [[wo('The product:')],[co('packaged once.')]], 'Templates, audits, systems from your own workflow, assembled and delivered automatically.', [co('Sell while you sleep.')], f"{M}/product.png", 1.0),
 ('SHAPE 3', [[wo('The content:')],[co('proof in public.')]], 'The desk turns your client work into daily posts in your voice. Content sells shapes one and two.', [co('The flywheel spins here.')], f"{M}/contents.png", 1.0),
 ('SHAPE 4', [[wo('The teaching:')],[co('the method, priced.')]], 'Your process, structured into a course or cohort by the same desk that runs it.', [co('Expertise, multiplied.')], f"{M}/teaching.png", 1.0),
 ('SHAPE 5', [[wo('The tool:')],[co('your method, executable.')]], 'Mint the workflow as a skill others run. No code, just your judgement packaged.', [co('The 2026 shape.')], f"{M}/tool5.png", 1.0),
 ('THE ENGINE', [[wo('One desk runs')],[co('all five shapes.')]], 'Same memory, same voice, same gate: service, product, content, teaching, tool.', [co('Five incomes, one login.')], f"{M}/engine5.png", 1.0),
 ('THE ORDER', [[wo('Service first.')],[co('Tool last.')]], 'Cash from shape one funds the rest; each shape feeds the next.', [co('Sequence beats ambition.')], f"{M}/order5.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], f"{LIB}/cta3d-founder.png", 0.92)
T2.CLOSE=dict(l1='Save the five shapes',l2='and pick your second one.',q='Which shape is your skill missing?')
MARK2="claude"
