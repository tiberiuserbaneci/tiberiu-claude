#!/usr/bin/env python3
# THE SOLO STACK - Dark Ultron gleam of catalin's imported "9 tool stack / $389 stack" reference.
# 1080x1350 editorial (via build_ed45). OWN 2.5D coded elements (models_25d, NOT recycled Vertex objects),
# role-replacement angle: each tool = a role a founder would hire, now one chat. Team = $15k/mo -> cents.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/solostack"; LIB=T2.LIB
PREMIUM=1   # coded clay3d panels
T2.ACCENT=(204,120,92); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/solostack.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("I fired my whole team.")],[co("One chat took the jobs.")]])
# 6-tuple: (eyebrow, hook, SUBHOOK, FOOT idea, object, fill)
T2.CONTENT=[
 ("THE RESEARCHER", [[wo("1,284 leads found.")],[co("Before my coffee.")]], "Live lead data and account briefs, pulled the moment you ask.", [co("No researcher to hire.")], f"{M}/apollo.png",     1.0),
 ("THE SDR",        [[wo("240 emails written.")],[co("I typed nine words.")]],        "The whole sequence is written and sent from one message.",      [co("No SDR to hire.")],        f"{M}/gmail_sent.png", 1.0),
 ("THE OPS LEAD",   [[wo("Nobody drags the cards.")],[co("The pipe moves itself.")]],   "Deals move by asking. The pipeline updates itself.",            [co("No ops seat.")],          f"{M}/hubspot.png",    1.0),
 ("THE DESIGNER",   [[wo("9 assets shipped.")],[co("Zero briefs written.")]],   "On-brand posts and assets come out of the same chat.",          [co("No designer to brief.")], f"{M}/designer.png",   1.0),
 ("THE DEVELOPER",  [[wo("The agency said 3 weeks.")],[co("It shipped tonight.")]],  "Pages ship straight from the chat, no builder to learn.",       [co("No dev to wait on.")],    f"{M}/developer.png",  1.0),
 ("THE TEAM",       [[wo("$15,000 a month.")],[co("Now: cents.")]], "Every role above, for the price of a chat, not a payroll.", [mu("$15k/mo in salaries."),co("  Now cents.")], f"{M}/bill.png", 1.0),
 ("THE GATE",       [[wo("AI does the work.")],[co("I keep the trigger.")]], "Nothing sends until you say go. You stay in control.",          [co("You approve every send.")], f"{M}/gate.png",     1.0),
 ("THE OPERATOR",   [[wo("Headcount: one.")],[co("Revenue: growing.")]],"The whole company runs behind a single subscription.",         [co("Run it solo.")],          f"{M}/ultron_real.png",     1.0),
]
T2.CTA=("RUN IT SOLO", [[wo("Run it solo,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this to",l2="run lean.",q="Which hire would you skip first?")


MARK2="strip"
STRIP="/home/user/tiberiu-claude/content/_hitl-src/covers/solostack_strip.png"
