#!/usr/bin/env python3
# THE HOURS LEDGER - adaptare IG Scraped ("Claude Workflows That Save 10+ Hours a Week") in context
# Ultron founder-services. Angle: TIME COLLAPSE - fiecare job recurent de founder, ore inainte vs
# minute/centi dupa, cablat ca un sistem Ultron reutilizabil. (generat manual pe modelul build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src45"; LIB=T2.LIB
PREMIUM=1
TITLE="THE HOURS LEDGER"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('My week cost 40 hours.')],[co('Now it costs cents.')]])
T2.CONTENT=[
 ('THE LEDGER', [[wo('Ten founder jobs.')],[co('Hours each, every week.')]], 'Research, outbound, deals, content, code. The same week, priced in hours.', [co('Billed by the hour.')], f"{M}/ledger.png", 1.0),
 ('THE ROUTER', [[wo('One brain reads the job')],[co('and picks the tier.')]], 'Lite for lookups, Smart for the work, Deep for hard calls. You never choose.', [co('Cents, not dollars.')], f"{M}/router.png", 1.0),
 ('THE RESEARCH', [[wo('Fifteen tabs collapse')],[co('into one ranked brief.')]], 'CORTEX reads the company, the market and the person into a single page.', [co('Two hours to two minutes.')], f"{M}/research.png", 1.0),
 ('THE CONTENT', [[wo('One post becomes')],[co('a week of channels.')]], 'PULSE repurposes a single asset into every format, written in your voice.', [co('Written, not chatted.')], f"{M}/repurpose.png", 1.0),
 ('THE CODE', [[wo('Built, tested, shipped.')],[co('You just read the PR.')]], 'SENTINEL turns plain English into a page, tests it, opens the pull request.', [co('An afternoon to minutes.')], f"{M}/ship.png", 1.0),
 ('THE DEALS', [[wo('It answered the objection')],[co('before I typed back.')]], 'STRIKER qualifies, handles the pushback and drafts the close plan for you.', [co('Every deal, same rigor.')], f"{M}/deals.png", 1.0),
 ('THE MEMORY', [[wo('Why each job repeats')],[co('in a single tap.')]], 'ICP, pipeline, pricing and docs live in one core every agent reads.', [co('Nothing starts cold.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Hours refunded.')],[co('Control kept.')]], 'Every external move parks for your tap before anything sends.', [co('Still your company.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the ledger?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='refund your week.',q='Which hours would you buy back first?')
MARK2="claude"
