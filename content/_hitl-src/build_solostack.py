#!/usr/bin/env python3
# THE SOLO STACK - Dark Ultron gleam of catalin's imported "9 tool stack / $389 stack" reference.
# 1080x1350 editorial (via build_ed45). OWN 2.5D coded elements (models_25d, NOT recycled Vertex objects),
# role-replacement angle: each tool = a role a founder would hire, now one chat. Team = $15k/mo -> cents.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.OBJ_THR=20   # 2.5D windows have a dark body close to the bg -> lower crop threshold than Vertex tablets

T2.COVER=dict(head=[[wo("I replaced my team")],[co("with one chat.")]])
# 6-tuple: (eyebrow, hook, SUBHOOK, FOOT idea, object, fill)
T2.CONTENT=[
 ("THE RESEARCHER", [[wo("The researcher?")],[co("One chat.")]], "Live lead data and account briefs, pulled the moment you ask.", [co("No researcher to hire.")], f"{M}/apollo.png",     1.0),
 ("THE SDR",        [[wo("The SDR?")],[co("One chat.")]],        "The whole sequence is written and sent from one message.",      [co("No SDR to hire.")],        f"{M}/gmail_sent.png", 1.0),
 ("THE OPS LEAD",   [[wo("The ops lead?")],[co("One chat.")]],   "Deals move by asking. The pipeline updates itself.",            [co("No ops seat.")],          f"{M}/hubspot.png",    1.0),
 ("THE DESIGNER",   [[wo("The designer?")],[co("One chat.")]],   "On-brand posts and assets come out of the same chat.",          [co("No designer to brief.")], f"{M}/designer.png",   1.0),
 ("THE DEVELOPER",  [[wo("The developer?")],[co("One chat.")]],  "Pages ship straight from the chat, no builder to learn.",       [co("No dev to wait on.")],    f"{M}/developer.png",  1.0),
 ("THE TEAM",       [[wo("A five-person team.")],[co("One chat.")]], "Every role above, for the price of a chat, not a payroll.", [mu("$15k/mo in salaries."),co("  Now cents.")], f"{M}/bill.png", 1.0),
 ("THE GATE",       [[wo("And I approve")],[co("every move.")]], "Nothing sends until you say go. You stay in control.",          [co("You approve every send.")], f"{M}/gate.png",     1.0),
 ("THE OPERATOR",   [[wo("One operator.")],[co("No headcount.")]],"The whole company runs behind a single subscription.",         [co("Run it solo.")],          f"{M}/ultron.png",     1.0),
]
T2.CTA=("RUN IT SOLO", [[wo("Run it solo,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this to",l2="run lean.",q="Which hire would you skip first?")
