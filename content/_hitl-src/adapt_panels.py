#!/usr/bin/env python3
# Panouri clay pentru adaptarile IG Scraped - importa builderii din clay3d_v4 (guarded main).
# Usage: python3 adapt_panels.py [slugs...]
import sys, os, importlib.util
ROOT="/home/user/tiberiu-claude"
def _load(name,p):
    s=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
L=_load("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
S=_load("S",f"{ROOT}/content/_hitl-src/adapt_specs.py")
from playwright.sync_api import sync_playwright

hd,row=L.hd,L.row
f_rows,f_fan,f_pills,f_dial,f_paper,f_receipt,f_ticket,tick_cells,f_console,f_bubble=(
 L.f_rows,L.f_fan,L.f_pills,L.f_dial,L.f_paper,L.f_receipt,L.f_ticket,L.tick_cells,L.f_console,L.f_bubble)
f_env,f_badge,f_metro,f_split,f_gauge,f_odo,f_vault,f_folder,f_stamp,f_chartline,f_keys=(
 L.f_env,L.f_badge,L.f_metro,L.f_split,L.f_gauge,L.f_odo,L.f_vault,L.f_folder,L.f_stamp,L.f_chartline,L.f_keys)
LOCK=L.LOCK

def panels_for(slug,acc):
    A=acc
    P={
 "aios":{
  "amnesia": f_split("EVERY OTHER TAB",["Forgets your ICP","Forgets your voice","Forgets yesterday"],"THE ULTRON OS",["One permanent memory","Loaded in every run","Compounds monthly"]),
  "brain": f_browser_wrap("app.51ultron.com/bcp",hd("The memory","ALWAYS LOADED")+row("Your ICP","founder / CEO &middot; 2-50 seats",chip="set")+row("Your voice","sampled from real posts",chip="set")+row("Your pipeline","live, not pasted",chip="live")),
  "command": f_fan("Command center","YOURS, NOT RENTED",[row("7 agents","one chat box",chip="on"),row("9 flows","running on triggers",chip="on"),row("1 gate","everything external",chip="you")]),
  "always": f_metro("Overnight","LAPTOP SHUT",[("23:00","triage ran",1),("02:00","leads scored",1),("06:00","digest ready",1),("07:00","you wake up",0)]),
  "rules": f_pills([row("No discounts","said once, blocked forever",chip="rule"),row("No fluff words","enforced on every draft",chip="rule"),row("Deep tier on legal","spend where it pays",chip="rule")]),
  "proof": f_odo(["1",",","2","8","4"],3,"LEADS READ BEFORE COFFEE","one typed sentence &middot; 200 briefed by 07:00"),
  "gate": f_vault("OS","POWER, GATED"),
  "own": f_bubble("Rented tabs forget. Owned systems compound.","The OS","ONE COMMAND CENTER","run my company",A),
 },
 "loops":{
  "oldway": f_split("YOU, TODAY",["Type the prompt","Wait for output","Paste it somewhere"],"A LOOP",["Runs on a trigger","Checks its own work","Reports when done"]),
  "loop": f_dial(84,"LAST WEEK","212","cycles completed","you typed three sentences total"),
  "define": f_env("THE WHOLE SETUP","One sentence.","Follow up every lead quiet for 3 days.","Flow created"),
  "trigger": f_console("Triggers","REPLACE YOUR MEMORY",[("Daily 09:00","the cadence fires",True),("On every reply","the pipe updates",True),("On usage drop","churn watch pings",True)],buttons=False),
  "verify": f_stamp("Cycle report","EVERY RUN","checked before it counts",[("Goal met","yes"),("Output verified","yes"),("Next run","09:00")],"VERIFIED"),
  "trap": f_receipt("LOOP WITHOUT EXIT","WHAT IT BURNS",[("Endless retries","tokens"),("No stop condition","budget"),("Silent failures","days")],"Ultron flows","capped"),
  "gate": f_keys([("LOOP","RUNS FREE, INTERNAL",False),("SEND","WAITS FOR YOUR TAP",True)]),
  "scale": f_bubble("Your hours are fixed. Loops are not.","The loop","PAST YOUR HOURS","set one goal",A),
 },
 "aibody":{
  "difference": f_split("A CHATBOT",["Answers questions","Waits for you","Forgets at midnight"],"A BODY",["Reads your market","Writes in your voice","Ships real work"]),
  "router": f_keys([("LITE","LOOKUPS",False),("SMART","THE DAILY DRIVER",True),("DEEP","JUDGEMENT ONLY",False)]),
  "eyes": f_browser_wrap("live signals &middot; overnight",hd("The eyes","CORTEX")+row("Northwind","hiring 3 ops roles now",chip="live")+row("Globex","raised $4M in May",chip="live")+row("Initech","stack has no AI layer",chip="live")),
  "voice": f_env("DRAFT 14 &middot; YOUR VOICE","Reads like you.","Because it learned from what you wrote.","Approve"),
  "hands": f_stamp("Build log","SENTINEL","launch page &middot; from a sentence",[("Built + styled","19:04"),("42 tests passed","23:12"),("Live on your domain","23:40")],"SHIPPED"),
  "heart": f_folder("The core","EVERY AGENT DRAWS FROM IT",[row("icp.md","who you sell to",chip="loaded"),row("voice.md","how you sound",chip="loaded"),row("pipeline.live","what is moving now",chip="live")]),
  "gate": f_vault("YOU","THE REINS"),
  "operator": f_bubble("Brain, eyes, voice, hands, heart. One login.","The body","FULLY WIRED","augment me",A),
 },
 "fivesigns":{
  "sign1": f_pills([row("Same question, 09:12","answered by a human",chip="daily"),row("Same question, 11:40","answered again",chip="daily"),row("Same question, 16:05","a flow should own this",chip="fix")]),
  "sign2": f_fan("The glue work","PAYROLL SPENT ON PASTE",[row("CRM to sheet","by hand, weekly",chip="2h"),row("Inbox to CRM","by hand, daily",chip="1h"),row("Sheet to report","by hand, monthly",chip="4h")]),
  "sign3": f_console("Waiting on you","THE BOTTLENECK",[("Proposal draft","stuck since Tuesday",False),("Campaign launch","stuck since Monday",False),("With Ultron: prepped","you just tap",True)]),
  "sign4": f_chartline("Speed to lead","FIRST REPLY WINS",[95,80,68,50,34,20,10,4],"hours to seconds: the flow answers while it is still warm"),
  "sign5": f_receipt("MONTH-END","THE OLD WAY",[("Pull the numbers","2 days"),("Format the deck","1 day"),("Argue the sources","1 day")],"Ultron, on demand","minutes"),
  "test": f_gauge(100,"5/5","every yes is a leak","not a staffing problem, a systems problem"),
  "fix": f_ticket("Week one","START SMALL",tick_cells([("MON","Pick",1),("TUE","Build",1),("WED","",0),("THU","Test",1),("FRI","Live",1)]),"ONE WORKFLOW FIRST","THEN REPEAT"),
  "gate": f_bubble("Automated, never unsupervised.","The gate","YOUR TAP FIRST","fix the worst leak",A),
 },
 "contentdesk":{
  "cal": f_ticket("The plan","ONE LINE IN",tick_cells([("MON","Post",1),("TUE","Reel",1),("WED","",0),("THU","Deck",1),("FRI","News",1)]),"14 SLOTS PLANNED","10:00 LOCAL EACH"),
  "hooks": f_fan("Pick the winner","FROM YOUR HOOK BANK",[row("Hook A","the confession angle",chip="A"),row("Hook B","the number angle",chip="B"),row("Hook C","the enemy angle",chip="C")]),
  "voice": f_paper("Draft","RANKED 92","Reads like you wrote it",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Voice locked</div><div class="rs" style="color:#8a7a5e">sampled from 60 real posts</div></div><span class="chip">Publish</span></div>'),
  "repurpose": f_metro("One brief","FIVE FORMATS",[("Post","LinkedIn",1),("Caption","IG + TikTok",1),("Carousel","10 pages",1),("Newsletter","inboxed",0)]),
  "inbox": f_gauge(99,"99.2%","land in the inbox","warm domains &middot; ramped, never blasted"),
  "desk": f_console("The desk","NO MEETINGS",[("Planner","fires Monday 07:00",True),("Writer","your voice, ranked",True),("Distributor","10:00 local, daily",True)],buttons=False),
  "gate": f_badge(LOCK,"3","Three drafts wait for you.","nothing posts without your tap"),
  "math": f_bubble("A content team, metered in cents.","The desk","PAYROLL: ZERO","run the desk",A),
 },
    }[slug]
    return {k:v.replace("{acc}",A) for k,v in P.items()}

def f_browser_wrap(url,inner): return L.f_browser(url,inner)

if __name__=="__main__":
    slugs=sys.argv[1:] or [d["slug"] for d in S.ALL]
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":900,"height":1100},device_scale_factor=2)
        for d in S.ALL:
            if d["slug"] not in slugs: continue
            acc="%d,%d,%d"%d["accent"]
            outd=f"{ROOT}/content/_hitl-src/models_clay/{d['slug']}"; os.makedirs(outd,exist_ok=True)
            for stem,bodyhtml in panels_for(d["slug"],acc).items():
                html=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{L.css(acc)}</style></head><body>{bodyhtml}</body></html>"
                pg.set_content(html); pg.wait_for_timeout(280)
                pg.screenshot(path=f"{outd}/{stem}.png",omit_background=True,full_page=True)
            print("panels OK",d["slug"])
        b.close()
    print("done")
