#!/usr/bin/env python3
# THE 5 SKILLS THAT PAY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/fivepaid"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop learning AI skills')],[co('nobody will pay for.')]])
T2.CONTENT=[
 ('SKILL 1', [[wo('Research')],[co('that closes.')]], 'Account briefs that turn cold calls warm. Companies pay retainers for this.', [co('CORTEX does it daily.')], f"{M}/research.png", 1.0),
 ('SKILL 2', [[wo('Outbound')],[co('that lands.')]], 'Sequences with one trigger per email and domains that stay warm.', [co('Placement is the skill.')], f"{M}/outbound.png", 1.0),
 ('SKILL 3', [[wo('Content')],[co('in a voice.')]], 'Not words. A voice clients recognize in the feed before the handle.', [co('Voice is the asset.')], f"{M}/content.png", 1.0),
 ('SKILL 4', [[wo('Builds')],[co('without builders.')]], 'Landing pages and dashboards from plain English, live the same day.', [co('Assembly, not code.')], f"{M}/builds.png", 1.0),
 ('SKILL 5', [[wo('Systems')],[co('that keep running.')]], 'Flows on triggers, digests at 07:00. The skill is setting exits, not typing.', [co('Loops beat prompts.')], f"{M}/systems.png", 1.0),
 ('THE PICK', [[wo('Pick exactly one.')],[co('Go deep.')]], 'One skill run daily inside Ultron beats five certificates on a shelf.', [co('Depth sells.')], f"{M}/one.png", 1.0),
 ('THE PROOF', [[wo('Your first client is')],[co('your own company.')]], 'Run the skill on your business first. The receipts become the pitch.', [co('Results are the resume.')], f"{M}/client.png", 1.0),
 ('THE MATH', [[wo('Cents to practice.')],[co('Real money to sell.')]], 'The meter runs in cents while you learn. The invoice runs high when you deliver.', [co('Practice is free now.')], f"{M}/meter.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='pick your one.',q='Which of the 5 fits you?')
MARK2="claude"
