#!/usr/bin/env python3
# THE PERMISSIONLESS TWO - adaptare IG Scraped (Naval's four leverages) in context Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src42"; LIB=T2.LIB
PREMIUM=1
TITLE="THE PERMISSIONLESS TWO"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Four leverages exist.')],[co('Two need no permission.')]])
T2.CONTENT=[
 ('THE MAP', [[wo('Four leverages.')],[co('Two you can own alone.')]], 'Labor and capital need permission. Code and media do not.', [co('The bottom row is yours.')], f"{M}/quadmap.png", 1.0),
 ('LEVERAGE 01', [[wo('Labor needs')],[co('permission.')]], 'People work for you only if you hire, manage, pay and retain them.', [co('Payroll before profit.')], f"{M}/labor.png", 1.0),
 ('LEVERAGE 02', [[wo('Capital needs')],[co('permission too.')]], 'Money works for you after an investor says yes and takes your equity.', [co('Dilution before scale.')], f"{M}/capital.png", 1.0),
 ('LEVERAGE 03', [[wo('Code works')],[co('while you sleep.')]], 'Build once and it runs everywhere, for free, with no one to manage.', [co('Permissionless. Yours.')], f"{M}/code.png", 1.0),
 ('LEVERAGE 04', [[wo('Media works')],[co('at zero marginal cost.')]], 'Publish once and it reaches thousands while you do something else.', [co('Permissionless. Yours.')], f"{M}/media.png", 1.0),
 ('THE UNLOCK', [[wo('Ultron is both')],[co('at once.')]], 'Code that ships product and media that ships reach, from one login.', [co('No hire. No raise.')], f"{M}/both.png", 1.0),
 ('HOW IT RUNS', [[wo('One job splits')],[co('two ways.')]], 'SENTINEL builds the code. PULSE and AMPLIFY run the media. The router splits it.', [co('Both leverages, one turn.')], f"{M}/route.png", 1.0),
 ('THE OPERATOR', [[wo('One founder.')],[co('Two leverages.')]], 'You wield code and media alone, without a team or a term sheet.', [co('Permissionless by default.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the leverage map?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='own the two that scale.',q='Which leverage are you still stuck on?')
MARK2="claude"
