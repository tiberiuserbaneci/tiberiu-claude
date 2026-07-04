#!/usr/bin/env python3
# s2src42 "CENTS PER BRIEF" - the $80K sales rep reframed: one Cortex command turns any company URL
# into a qualified, cited, cents-priced, gated prospect dossier. IG/TikTok 3D deck (adapt_build.py).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src42"; LIB=T2.LIB
PREMIUM=1
TITLE="CENTS PER BRIEF"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('An $80K sales rep,')],[co('or one command.')]])
T2.CONTENT=[
 ('THE COMMAND', [[wo('Not a hire.')],[co('A keystroke.')]], 'Type one slash command, drop a company URL. That is the whole rep.', [co('/cortex, then a link.')], f"{M}/command.png", 1.0),
 ('THE INTAKE', [[wo('One link in,')],[co('a full dossier out.')]], 'It reads the site, the news, the hiring and the stack, then pulls the fields that matter.', [co('No ten open tabs.')], f"{M}/intake.png", 1.0),
 ('THE DOSSIER', [[wo('A ranked brief,')],[co('cited and dated.')]], 'Every claim carries its source. One page you can act on, not a wall of tabs.', [co('Sourced, not guessed.')], f"{M}/dossier.png", 1.0),
 ('THE MATH', [[wo('An $80K desk,')],[co('down to cents.')]], 'A human SDR is eighty grand a year. A qualified brief from Cortex is a few cents.', [co('Pay per brief.')], f"{M}/price.png", 1.0),
 ('THE SCORE', [[wo('It scores the fit')],[co('and shows why.')]], 'ICP match, timing, budget signal, reachability - a number you can defend.', [co('92, with reasons.')], f"{M}/score.png", 1.0),
 ('THE GATE', [[wo('It drafts everything,')],[co('then it stops.')]], 'The brief and the outreach sit in your outbox until you tap approve.', [co('One tap to send.')], f"{M}/gate.png", 1.0),
 ('THE MEMORY', [[wo('It never asks')],[co('who you sell to.')]], 'Your ideal customer lives in one core. Every run scores against the same memory.', [co('Learns once, reuses.')], f"{M}/memory.png", 1.0),
 ('THE QUEUE', [[wo('Fifty urls in,')],[co('a ranked shortlist out.')]], 'Feed it a list, get a ranked queue - who to call first and exactly why.', [co('Sorted by who is ready.')], f"{M}/queue.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the command?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='qualify for cents.',q='What would you point it at first?')
MARK2="claude"
