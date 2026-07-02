#!/usr/bin/env python3
# STOP PAYING FOR SOFTWARE - Dark Ultron gleam of catalin's imported "paid tools you can replace" reference.
# 1080x1350 editorial (via build_ed45). OWN coded-3D objects (models_solo3d, distinct from SOLO STACK),
# angle: each paid SaaS subscription = one chat. $202/mo of software -> cents on one subscription.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(212,162,127); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/stopsoftware.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("Stop paying")],[co("for software.")]])
# 6-tuple: (eyebrow, hook, SUBHOOK, FOOT idea, object, fill)
T2.CONTENT=[
 ("THE SCHEDULER",     [[wo("A scheduler?")],[co("One chat.")]],     "Post to every channel from one message, queued for the week.", [mu("Buffer, $15/mo."),co("  Now cents.")],    f"{M}/scheduler.png",   1.0),
 ("THE DELIVERABILITY",[[wo("A warmup tool?")],[co("One chat.")]],   "Domains warm, inboxes clean, mail lands where it should.",     [mu("Instantly, $97/mo."),co("  Now cents.")],  f"{M}/warmup.png",      1.0),
 ("THE WRITER",        [[wo("A copywriter?")],[co("One chat.")]],    "On-brand, ranked content written straight from the chat.",     [mu("Jasper, $49/mo."),co("  Now cents.")],     f"{M}/seowriter.png",   1.0),
 ("THE BOOKING",       [[wo("A booking app?")],[co("One chat.")]],   "Meetings booked and confirmed without a second tool.",         [mu("Calendly, $16/mo."),co("  Now cents.")],   f"{M}/calendly.png",    1.0),
 ("THE OUTREACH",      [[wo("An outreach tool?")],[co("One chat.")]],"The whole sequence written and sent from one message.",        [co("No sender to pay for.")],                  f"{M}/gmail_sent.png",  1.0),
 ("THE BILL",          [[wo("Five subscriptions.")],[co("One chat.")]],"Every tool above, on one bill, for the price of a chat.",    [mu("$202/mo in software."),co("  Now cents.")],f"{M}/softwarebill.png",1.0),
 ("THE GATE",          [[wo("And I approve")],[co("every send.")]],  "Nothing ships until you say go. You stay in control.",         [co("You approve every move.")],                f"{M}/gate.png",        1.0),
 ("THE OPERATOR",      [[wo("One subscription.")],[co("No stack.")]],"The whole toolset runs behind a single chat.",                 [co("Cancel the rest.")],                       f"{M}/ultron_real.png",      1.0),
]
T2.CTA=("RUN IT SOLO", [[wo("Cancel the stack,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this before",l2="your next renewal.",q="Which tool would you cancel first?")
