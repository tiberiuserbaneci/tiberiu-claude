#!/usr/bin/env python3
# THE ONE-PERSON COMPANY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="THE ONE-PERSON COMPANY"
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src22"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('One founder.')],[co('One laptop, one operator.')]])
T2.CONTENT=[
 ('THE OLD WAY', [[wo('Ten tools, taped')],[co('together, breaking weekly.')]], 'A scraper, a chat box, a dialer, a CRM. Stitched by hand for hundreds a month.', [co('Ultron replaces the stack.')], f"{M}/stack.png", 1.0),
 ('THE BRAIN', [[wo('A brain that budgets')],[co('its own thinking.')]], 'It reads each job and picks the model tier per turn. Cents, never dollars.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE TEAM', [[wo('Seven specialists.')],[co('One login.')]], 'Research, outreach, deals, content, code, publishing, legal. Each callable by name.', [co('A team, not a chatbot.')], f"{M}/agents.png", 1.0),
 ('THE RESEARCH', [[wo('No more copy-paste')],[co('into a chat box.')]], 'CORTEX profiles the person, company and market into one ranked brief.', [co('One brief, not ten tabs.')], f"{M}/research.png", 1.0),
 ('THE SYSTEM', [[wo('Systems, not prompts')],[co('you paste and lose.')]], 'Every workflow is saved, reused and improved. Nothing copied into a strange app.', [co('Reusable, not disposable.')], f"{M}/systems.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every outbound move parks at the human gate. Augmented, never unsupervised.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE MEMORY', [[wo('Cut the memory')],[co('and it goes blind.')]], 'ICP, pipeline, pricing, docs and your voice. Every agent draws from one shared core.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE PRICE', [[wo('The old stack, hundreds.')],[co('Ultron, cents.')]], 'Pay per token through one router. Cents per thousand rows, not a monthly tax.', [co('Cents, not subscriptions.')], f"{M}/price.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the whole company lean.',q='What are you still paying ten tools to do?')
MARK2="claude"
