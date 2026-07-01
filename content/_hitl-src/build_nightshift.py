#!/usr/bin/env python3
# WHILE I SLEPT - 9:16 (1080x1920) evolving lock-screen scene, TikTok + Instagram (Type 2, S31).
# Same engine/feel as LOCK SCREEN, ONE DAY (build_lockscreen.py) but a DISTINCT scenario: a single
# iPhone lock screen filling with OVERNIGHT Ultron outcome notifications from lights-out to the alarm.
# Reuses the lockscreen helpers (wallpaper, status row, sphere app-icon, notification stack); switches
# to deck_close (no poll slide, two account closing pages @tiberiu.ai / @51ultron, per operator).
import importlib.util
spec=importlib.util.spec_from_file_location("L","/home/user/tiberiu-claude/content/_hitl-src/build_lockscreen.py")
L=importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
T2=L.T2
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)

# Cover hook + overnight scene
T2.COVER=dict(head=[[wo("While I slept,")],[co("my company worked.")]])
L.TODAY="Tuesday, June 30"

# (clock, eyebrow context, title, subtitle) - newest stacks on top, time = newest's clock
L.NOTIFS=[
 ("23:10", "23:10 · LIGHTS OUT",     "Outbound queued",   "240 emails scheduled for the morning."),
 ("00:40", "00:40 · FAST ASLEEP",    "Replies drafted",   "9 leads answered. All drafted for you."),
 ("02:15", "02:15 · DEEP SLEEP",     "Research done",     "60 accounts scored and ranked."),
 ("03:30", "03:30 · STILL DARK",     "Bug fixed",         "Checkout error patched and shipped."),
 ("04:45", "04:45 · PRE-DAWN",       "Content ready",     "Today's post, written in your voice."),
 ("05:30", "05:30 · FIRST LIGHT",    "Call booked",       "Thursday 11:00 added to your calendar."),
 ("06:10", "06:10 · ALMOST UP",      "Invoice paid",      "Acme paid. Cash is in."),
 ("06:50", "06:50 · ALARM",          "Morning brief",     "11 done overnight. 1 needs you."),
]
T2.CONTENT=[(L.NOTIFS[i][1],[[wo("x")]],"",1.0) for i in range(len(L.NOTIFS))]
T2.CLOSE=dict(l1="Save this for",l2="your first quiet night.",q="What would you run overnight?")

# Date rolls over at midnight: the 23:10 slide is Tue Jun 30, everything from 00:40 on is Wed Jul 1.
def _statusrow_ns(d, page):
    y=300; col=(225,225,220)
    hh=int(L.NOTIFS[page-2][0].split(":")[0])
    date="Tuesday, June 30" if hh>=20 else "Wednesday, July 1"
    d.text((L.MX,y),date,font=T2.dm(500,34),fill=col)
    batt=max(10,80-(page-2)*10); bx=L.W-L.MX-52; by=y+5; L._battery(d,bx,by,batt/100,col)
    pf=T2.mono(28); pt=f"{batt}%"; pw=d.textlength(pt,font=pf)
    d.text((bx-22-pw,y+2),pt,font=pf,fill=col); L._wifi(d, bx-22-pw-42, y+30, col)
L._statusrow=_statusrow_ns

# mids use the lock-screen scene; deck_close: TikTok -> 2 closing pages, IG -> CTA-pill (_last_body)
T2.body_slide=L.body_slide

if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/night_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/night_ig",True)
    T2.montage(f"{T2.OUTBASE}/night_tt","night_tt",a); T2.montage(f"{T2.OUTBASE}/night_ig","night_ig",b)
    print("tt",a,"ig",b)
