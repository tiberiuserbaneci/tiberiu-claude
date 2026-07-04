#!/usr/bin/env python3
# SIX MONTHS BUILDING - adaptare IG/TikTok in context Ultron (structura clonata din build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="SIX MONTHS BUILDING"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s26monthsbuilding"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Six months building AI agents.')],[co('Everything I knew is outdated.')]])
T2.CONTENT=[
 ('THE LOG', [[wo('Six months. Six rewrites.')],[co('Clever prompts died first.')]], 'Everything I shipped last year is already outdated. The rewrite never stops.', [co('Prompts age in weeks.')], f"{M}/timeline.png", 1.0),
 ('THE LOOP', [[wo('A prompt answers once.')],[co('A loop keeps working.')]], 'Plan, act, check, adapt, repeat. The loop is what survived from month one.', [co('Loops beat prompts.')], f"{M}/loops.png", 1.0),
 ('THE MEMORY', [[wo('Context windows forget.')],[co('Memory does not.')]], 'ICP, pipeline, pricing, docs. Every agent reads the same core, nothing re-explained.', [co('Memory beats context.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Full autonomy scared me.')],[co('So I kept the reins.')]], 'Every external move parks for your tap. The HUMAN GATE, augmented not unsupervised.', [co('The gate beats autopilot.')], f"{M}/gate.png", 1.0),
 ('THE ROUTER', [[wo('One model for everything')],[co('is one bill you cannot pay.')]], 'The router reads each job and picks the tier. Cents per turn, never dollars.', [co('Routing beats one model.')], f"{M}/router.png", 1.0),
 ('THE FIELD', [[wo("Last year's playbook")],[co('is already stale.')]], 'What worked in January was gone by June. The field moves weekly, so relearn.', [co('Relearn every quarter.')], f"{M}/radar.png", 1.0),
 ('THE KEEPERS', [[wo('Four rules survived')],[co('every single rewrite.')]], 'Loops over prompts. Memory over context. Gate over autopilot. Routing over one model.', [co('The four that kept.')], f"{M}/stack.png", 1.0),
 ('THE SYSTEM', [[wo('Stop shipping prompts.')],[co('Ship a system.')]], 'Seven agents, one memory, one gate, one router. That is the whole lesson.', [co('One system, seven agents.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the six lessons?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='build the system.',q='Which lesson did you learn the hard way?')
MARK2="claude"
