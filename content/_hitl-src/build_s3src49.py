#!/usr/bin/env python3
# IT CLONED MY VOICE - adaptare IG Scraped (s3src49, "Sound like you") in context Ultron.
# NARROW: the voice-CLONING mechanic - sampling your real posts, matching cadence, enforcing your
# banned words, generic-vs-you before/after. The training/sampling mechanic is the hero.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src49"; LIB=T2.LIB
PREMIUM=1
TITLE="IT CLONED MY VOICE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('It writes like me.')],[co('Nobody can tell.')]])
T2.CONTENT=[
 ('THE PROBLEM', [[wo('Every AI draft')],[co('sounds the same.')]], 'Left alone, it polishes you into a stranger with everyone else voice.', [co('Same flat hum.')], f"{M}/flatten.png", 1.0),
 ('THE SAMPLE', [[wo('It read 200')],[co('of my real posts.')]], 'Your feed, not a training set. Your own words become the reference draft.', [co('Sampled from you.')], f"{M}/ingest.png", 1.0),
 ('THE RHYTHM', [[wo('It matches')],[co('my cadence.')]], 'Short. Short. Then one long line that lands. Your pattern, kept intact.', [co('Not the model hum.')], f"{M}/cadence.png", 1.0),
 ('THE BLOCKLIST', [[wo('The words')],[co('I never say.')]], 'Delve, leverage, synergy. Every draft scanned against your blocklist first.', [co('Killed before you see it.')], f"{M}/banned.png", 1.0),
 ('VOICE DNA', [[wo('My voice has')],[co('a fingerprint.')]], 'Cadence, lexicon, taboo words, punctuation, openers. One profile, only yours.', [co('A style it cannot fake.')], f"{M}/dna.png", 1.0),
 ('BEFORE / AFTER', [[wo('Same brief.')],[co('Two writers.')]], 'One reads like a press release. One reads like you. The brief was identical.', [co('One sounds like you.')], f"{M}/compare.png", 1.0),
 ('ENFORCED', [[wo('Every draft')],[co('scored on voice.')]], 'Off-voice sentences rewritten until the match clears. Nothing ships below bar.', [co('96 percent or rewrite.')], f"{M}/gauge.png", 1.0),
 ('MULTIPLIED', [[wo('It signs')],[co('in my hand.')]], 'One profile signs every post, email and page. All unmistakably you, at volume.', [co('You, at any volume.')], f"{M}/signature.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the voice kit?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='clone your own voice.',q='Would anyone know your last post was not you?')
MARK2="claude"
