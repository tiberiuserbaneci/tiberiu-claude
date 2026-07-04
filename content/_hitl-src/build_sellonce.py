#!/usr/bin/env python3
# CREATE ONCE, SELL FOREVER - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/sellonce"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do not need 50 ideas.')],[co('You need one, shipped.')]])
T2.CONTENT=[
 ('THE LIST TRAP', [[wo('Fifty ideas saved.')],[co('Zero products live.')]], 'Idea lists feel like progress. Shipping is the only progress.', [co('Lists are procrastination.')], f"{M}/listtrap.png", 1.0),
 ('THE PICK', [[wo('Sell what you already')],[co('get asked about.')]], 'The template, the checklist, the audit you explain weekly: that is the product.', [co('Demand is already visible.')], f"{M}/pick9.png", 1.0),
 ('THE BUILD', [[wo('Described in a sentence.')],[co('Assembled by the desk.')]], 'Your workflow becomes the template pack, the guide, the system: from your own files.', [co('An evening, not a launch.')], f"{M}/build9.png", 1.0),
 ('THE PAGE', [[wo('The offer page')],[co('went live the same day.')]], 'Hero, pricing, FAQ from the component pack, in your brand tokens.', [co('No designer, no delay.')], f"{M}/page9.png", 1.0),
 ('THE DELIVERY', [[wo('Paid at 03:14.')],[co('Delivered at 03:14.')]], 'The flow sends the product, the receipt and the follow-up while you sleep.', [co('Inventory of nothing.')], f"{M}/delivery.png", 1.0),
 ('THE LOOP9', [[wo('Feedback becomes')],[co('version two.')]], 'Every buyer question funnels into the next update, drafted for your tap.', [co('The product self-improves.')], f"{M}/loop9.png", 1.0),
 ('THE SPREAD', [[wo('One product funds')],[co('the second.')]], 'Validate one niche, then let the desk clone the pipeline sideways.', [co('Library, not lottery.')], f"{M}/spread.png", 1.0),
 ('THE MATH9', [[wo('Created once.')],[co('Sold while you slept.')]], 'The digital shelf never closes and never reorders stock.', [co('Ship idea number one.')], f"{M}/math9.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save the pipeline',l2='and ship idea number one.',q='Which product have you been postponing?')
MARK2="claude"
