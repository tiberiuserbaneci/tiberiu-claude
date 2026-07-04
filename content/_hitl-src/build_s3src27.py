#!/usr/bin/env python3
# THE REGISTRY AUDIT - adaptare IG Scraped (s3src27) in context Ultron (structura build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src27"; LIB=T2.LIB
PREMIUM=1
TITLE="THE REGISTRY AUDIT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I read the whole registry.')],[co('You install what won.')]])
T2.CONTENT=[
 ('THE PILE', [[wo('812 skills in the registry.')],[co('You will read none.')]], 'A public database no founder has time to open. CORTEX reads every entry.', [co('Nobody reads 812 pages.')], f"{M}/pile.png", 1.0),
 ('THE READ', [[wo('Every row, actually read.')],[co('Not the top ten links.')]], 'It opens each entry, tests the claim, keeps only the skills that hold up.', [co('Read, not skimmed.')], f"{M}/ledger.png", 1.0),
 ('THE RANK', [[wo('Ranked, not just listed.')],[co('Best fit at the top.')]], 'Each skill scored on fit, evidence and freshness. The shortlist sorts itself.', [co('A brief, not a dump.')], f"{M}/rank.png", 1.0),
 ('THE PROOF', [[wo('Every pick shows its receipt.')],[co('Where it actually wins.')]], 'No blind recommendation. Each entry carries the source that earned its rank.', [co('Sourced and dated.')], f"{M}/cite.png", 1.0),
 ('BY THE JOB', [[wo('Grouped by the job.')],[co('Not by the vendor.')]], 'Writing, design, research, outreach, deals. Mapped to what you need done.', [co('Find it by the task.')], f"{M}/group.png", 1.0),
 ('THE CUT', [[wo('812 in.')],[co('Fifteen out.')]], 'Copies, dead links and empty wrappers fall at the first gates. Signal only.', [co('The rest did not survive.')], f"{M}/sieve.png", 1.0),
 ('STILL LIVE', [[wo('The registry moved.')],[co('So did your shortlist.')]], 'New skills land weekly, old ones die. CORTEX rechecks so the brief never rots.', [co('Never a stale list.')], f"{M}/fresh.png", 1.0),
 ('THE BRIEF', [[wo('One page. Ranked. Cited.')],[co('Yours to approve.')]], 'The whole registry compressed to the handful worth your time. You tap approve.', [co('Your tap ships it.')], f"{M}/brief.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the ranked brief?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='skip the registry.',q='How many skills did you install without reading the other 811?')
MARK2="claude"
