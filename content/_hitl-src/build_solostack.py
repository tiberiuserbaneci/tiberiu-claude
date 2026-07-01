#!/usr/bin/env python3
# THE SOLO STACK - Dark Ultron gleam of the imported "9 tool stack / $389 stack" reference.
# 1080x1350 editorial (via build_ed45). Reuses the rival dark objects; role-replacement angle:
# each tool = a role a founder would hire, now one chat. $389/mo stack -> cents. Defensible copy
# (no "$500K at 23" personal claim). Rendered with: build_ed45.py build_solostack.py solostack
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
R=f"{T2.OBJ}/models_rival"; V=f"{T2.OBJ}/models_team/v3"; LIB=T2.LIB

T2.COVER=dict(head=[[wo("I replaced my team")],[co("with one chat.")]])
# 6-tuple: (eyebrow, hook, SUBHOOK, FOOT idea, object, fill)
T2.CONTENT=[
 ("THE RESEARCHER", [[wo("The researcher?")],[co("One chat.")]],  "Live lead data and account briefs, pulled the moment you ask.", [co("No researcher to hire.")], f"{R}/research.png", 0.95),
 ("THE SDR",        [[wo("The SDR?")],[co("One chat.")]],          "The whole sequence is written and sent from one message.",     [co("No SDR to hire.")],        f"{R}/outreach.png", 0.95),
 ("THE OPS LEAD",   [[wo("The ops lead?")],[co("One chat.")]],     "Deals move by asking. The pipeline updates itself.",           [co("No ops seat.")],          f"{R}/crm.png",      0.95),
 ("THE DESIGNER",   [[wo("The designer?")],[co("One chat.")]],     "On-brand posts and assets come out of the same chat.",          [co("No designer to brief.")], f"{R}/content.png",  0.95),
 ("THE DEVELOPER",  [[wo("The developer?")],[co("One chat.")]],    "Pages ship straight from the chat, no builder to learn.",       [co("No dev to wait on.")],    f"{R}/site.png",     0.95),
 ("THE TEAM",       [[wo("A five-person team.")],[co("One chat.")]],"Every role above runs through a single subscription.",         [mu("$15k/mo in salaries."),co("  Now one chat.")], f"{R}/stack.png", 0.90),
 ("THE GATE",       [[wo("And I approve")],[co("every move.")]],   "Nothing sends until you say go. You stay in control.",          [co("You approve every send.")], f"{V}/gate.png",   0.62),
 ("THE BILL",       [[wo("The stack was")],[co("a monthly bill.")]],"Nine tools was a bill every month. Mine is pay-per-use, cents.",[mu("$186.99 every month."),co("  Now cents.")], f"{R}/cost.png", 0.93),
]
T2.CTA=("RUN IT SOLO", [[wo("Run it solo,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this to",l2="run lean.",q="Which hire would you skip first?")
