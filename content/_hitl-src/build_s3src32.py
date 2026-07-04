#!/usr/bin/env python3
# THE SPAM DIAGNOSTIC - adaptare IG Scraped (s3src32) in context Ultron (generat de adapt_build.py)
# Reframe: the 5 named mistakes that sort cold email to spam, and the exact fix for each (a diagnostic).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src32"; LIB=T2.LIB
PREMIUM=1
TITLE="THE SPAM DIAGNOSTIC"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('It did not fail.')],[co('It never arrived.')]])
T2.CONTENT=[
 ('THE VERDICT', [[wo('Every send gets')],[co('a silent verdict.')]], 'Four of five cold emails are sorted to spam before a human ever sees them.', [co('Spam, not seen.')], f"{M}/verdict.png", 1.0),
 ('MISTAKE ONE', [[wo('You track opens.')],[co('Opens are ghosts.')]], 'Bots and privacy proxies inflate opens. Reply rate is the only number that pays.', [co('Track replies.')], f"{M}/opens.png", 1.0),
 ('MISTAKE TWO', [[wo('You blasted 300')],[co('from a newborn domain.')]], 'A domain with no history has no trust. Age it 90 plus days and warm it slowly.', [co('Age it first.')], f"{M}/domain.png", 1.0),
 ('MISTAKE THREE', [[wo('Your mail is')],[co('unsigned.')]], 'No SPF, DKIM or DMARC reads as a stranger. Publish all three to sign every send.', [co('Sign all three.')], f"{M}/auth.png", 1.0),
 ('MISTAKE FOUR', [[wo('Free. Guarantee.')],[co('Act now.')]], 'Trigger words, five links and heavy images spike your spam score. Write it plain.', [co('Cut the triggers.')], f"{M}/content.png", 1.0),
 ('MISTAKE FIVE', [[wo('You sent 300')],[co('on day one.')]], 'A cold-start spike burns your reputation. Ramp the volume and clean the list first.', [co('Ramp, do not blast.')], f"{M}/volume.png", 1.0),
 ('THE FIX STACK', [[wo('Five checks.')],[co('Green before you send.')]], 'Run every fix as one pre-send checklist and placement climbs back to the inbox.', [co('All green, then send.')], f"{M}/fixstack.png", 1.0),
 ('THE GUARD', [[wo('SPECTER scores it')],[co('before it sends.')]], 'Every draft is scored on all five, and only clean sends pass the human gate.', [co('Caught before send.')], f"{M}/guard.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the spam checklist?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='fix all five before you send.',q='Which mistake is burning your inbox right now?')
MARK2="claude"
