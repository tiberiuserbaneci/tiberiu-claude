#!/usr/bin/env python3
# SEVEN DEPARTMENTS, ONE DESK - adaptare IG Scraped (s3src19) in context Ultron. Reframe: Ultron
# este stratul de OPERATII al companiei - cei 7 agenti tin departamente, coada + workflow-urile
# tin back-office-ul (unghi diferit de s3src15 memory/second-brain).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src19"; LIB=T2.LIB
PREMIUM=1
TITLE="SEVEN DEPARTMENTS, ONE DESK"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your notes app is not')],[co('your operations team.')]])
T2.CONTENT=[
 ('THE ROSTER', [[wo('Not one assistant.')],[co('A full staff.')]], 'Seven agents, each one owning a department of the company.', [co('Research to legal, staffed.')], f"{M}/departments.png", 1.0),
 ('THE THROUGHPUT', [[wo('Drop the ask in one')],[co('folder. Collect the work.')]], 'You fill the queue. The workflow fills the generated folder.', [co('Work in, done out.')], f"{M}/queue.png", 1.0),
 ('THE AUTOMATION', [[wo('New lead lands.')],[co('The line runs itself.')]], 'Enriched, scored and drafted before you open the tab.', [co('Triggers, not clicks.')], f"{M}/workflow.png", 1.0),
 ('THE STRUCTURE', [[wo('The org chart')],[co('is just folders.')]], 'Clients, operations, finances, queue - the company, on disk.', [co('Built like a business.')], f"{M}/structure.png", 1.0),
 ('THE DISPATCH', [[wo('Every task to the')],[co('right desk, right tier.')]], 'The router reads each job, assigns the agent, picks the model.', [co('Cents, never dollars.')], f"{M}/router.png", 1.0),
 ('THE OUTPUT', [[wo('Queued at nine.')],[co('Cleared by noon.')]], 'One operator clears a backlog that used to need a team.', [co('A shift of output.')], f"{M}/throughput.png", 1.0),
 ('THE GATE', [[wo('Strong staff.')],[co('You still sign off.')]], 'Every outbound move parks for your tap before it fires.', [co('Approve, then it sends.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop opening ten tabs.')],[co('Run one desk.')]], 'Seven departments, one queue, one login - the operating system.', [co('The whole company, one screen.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the whole company.',q='Which department would you staff first?')
MARK2="claude"
