#!/usr/bin/env python3
# MAX ONLY WHEN IT COUNTS - adaptare IG "Claude Max plan" in context Ultron.
# Reframe: seat-ul flat factureaza inteligenta maxima pe fiecare tura; ROUTER-ul Ultron
# cumpara tier-ul potrivit per tura, in centi, invelit intr-un operator de 7 agenti + gate.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src26"; LIB=T2.LIB
PREMIUM=1
TITLE="MAX ONLY WHEN IT COUNTS"; T2.TITLE=TITLE
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do not need max')],[co('on every turn.')]])
T2.CONTENT=[
 ('THE FLAT SEAT', [[wo('A flat seat bills peak')],[co('all day long.')]], 'The premium plan charges maximum intelligence on lookups that need almost none.', [co('$1,200 for one seat.')], f"{M}/flatseat.png", 1.0),
 ('THE TIERS', [[wo('Three tiers, the')],[co('cheapest that fits.')]], 'Lite for quick lookups, Smart for daily work, Deep for the hard judgement calls.', [co('Cents, not a flat seat.')], f"{M}/tiers.png", 1.0),
 ('THE ROUTER', [[wo('The router reads the job')],[co('and picks the tier.')]], 'Plain English in. It hires the agent and the model tier per turn. You never choose.', [co('Zero model menus.')], f"{M}/router.png", 1.0),
 ('THE METER', [[wo('You pay for the turns')],[co('you actually run.')]], 'Pay per token. A hard Deep turn is cents, a quick Lite lookup a fraction of one.', [co('Metered, not maxed.')], f"{M}/meter.png", 1.0),
 ('THE ESCALATION', [[wo('Max intelligence fires')],[co('only when it counts.')]], 'Routine turns stay on Smart. A hard judgement call escalates to Deep, Opus grade.', [co('Opus where it matters.')], f"{M}/deep.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents, not one')],[co('bigger chat box.')]], 'CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL. Each one owns a job.', [co('A team, not a seat.')], f"{M}/roster.png", 1.0),
 ('THE GATE', [[wo('Every send waits')],[co('for your tap.')]], 'Cold emails, deals, code and contracts. Nothing leaves without a human approval.', [co('Approved, then sent.')], f"{M}/gate.png", 1.0),
 ('THE VAULT', [[wo('A short window forgets.')],[co('The vault does not.')]], 'ICP, pipeline, pricing and docs stay loaded, so every turn starts from what you built.', [co('Context that stays.')], f"{M}/memory.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the tier map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and stop', l2='paying peak all day.', q='Which turns are you overpaying for?')
MARK2="claude"
