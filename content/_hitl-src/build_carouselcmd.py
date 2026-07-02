#!/usr/bin/env python3
# THE CAROUSEL COMMAND - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/carouselcmd"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('My designer invoice')],[co('died mid-month.')]])
T2.CONTENT=[
 ('THE OLD BILL', [[wo('A week per deck.')],[co('Plus revision rounds.')]], 'Briefs, revisions, queue time. A week per deck, every deck.', [co('That bill ends today.')], f"{M}/oldbill.png", 1.0),
 ('THE COMMAND', [[wo('It interviews me.')],[co('Then builds alone.')]], 'PULSE interviews you for the angle, then owns the build end to end.', [co('It asks, you answer.')], f"{M}/command.png", 1.0),
 ('THE VISUALS', [[wo('My tokens, my type.')],[co('No template smell.')]], 'Brand colors, brand type, brand components. No template smell.', [co('Yours, not a template.')], f"{M}/visuals.png", 1.0),
 ('THE SLIDES', [[wo('Ten pages assembled')],[co('on proven bones.')]], 'Hook, body, CTA: structured like the decks that already performed.', [co('Built on receipts.')], f"{M}/slides.png", 1.0),
 ('THE CAPTIONS', [[wo('The caption kit')],[co('writes itself in.')]], 'CTA-first caption, hashtags, first comment. The whole posting kit.', [co('Nothing left to write.')], f"{M}/captions.png", 1.0),
 ('THE CLOCK', [[wo('Coffee brewed.')],[co('Deck done.')]], 'Cover, slides, captions, sized per channel. While the coffee brews.', [co('A week becomes minutes.')], f"{M}/clock.png", 1.0),
 ('THE GATE', [[wo('One review. One tap.')],[co('Then it posts.')]], 'You review the batch once. Nothing posts alone.', [co('Your feed, your call.')], f"{M}/gate.png", 1.0),
 ('THE MATH', [[wo('Retainer money')],[co('became runway.')]], 'Metered by use, not by seats. The retainer becomes runway.', [co('Cancel, then compound.')], f"{M}/math.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save this before',l2='your next invoice.',q='What would you build with the saved retainer?')
MARK2="claude"
