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
f_podium,f_browser,f_stat=L.f_podium,L.f_browser,L.f_stat

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

 "unstuck":{
  "floor": f_split("LEVEL 1, TODAY",["Ask a question","Copy the answer","Close the tab"],"WHAT IT COULD BE",["Work arrives done","Memory persists","Runs overnight"]),
  "memory": f_folder("What it keeps","LEVEL 2",[row("icp.md","who you sell to",chip="saved"),row("voice.md","how you write",chip="saved"),row("rules.md","every correction, forever",chip="grows")]),
  "jobs": f_fan("Running now","LEVEL 3",[row("Sourcing the list","one line in",chip="live"),row("Briefing accounts","1 page each",chip="live"),row("Drafting openers","gate holds them",chip="live")]),
  "ship": f_stamp("Build log","LEVEL 4","landing page &middot; from a sentence",[("Built + styled","19:04"),("Tests passed","23:12"),("Live on your domain","23:40")],"SHIPPED"),
  "routines": f_metro("Overnight","LEVEL 5",[("23:00","triage",1),("02:00","scoring",1),("06:00","digest",1),("07:00","your coffee",0)]),
  "gap": f_podium([("L1","chat",0),("L2","memory",0),("L3","jobs",0),("L4","ship",0),("L5","auto",1)]),
  "gate": f_keys([("AUTONOMY","GROWS EVERY LEVEL",False),("YOUR TAP","NEVER SHRINKS",True)]),
  "ceiling": f_bubble("The floor is chat. The ceiling runs itself.","Level 5","LAPTOP OFF","climb one level",A),
 },
 "hidden":{
  "myth": f_split("THE PROMPTERS",["Re-word the ask","Hope it lands","Start over daily"],"THE OPERATORS",["Install the skill","Wire the stack","Work arrives done"]),
  "decks": f_paper("Proposal","BUILT ITSELF","Northwind expansion offer",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">In your tokens</div><div class="rs" style="color:#8a7a5e">structure from decks that closed</div></div><span class="chip">Send</span></div>'),
  "sheets": f_browser("reports &middot; live numbers", hd("Month view","SOURCES ATTACHED")+row("Revenue","every figure traces to a run",chip="live")+row("Pipeline","refreshed this morning",chip="live")+row("Spend","cents, itemised",chip="live")),
  "contracts": f_stamp("NDA review","COUNSEL","risk lines flagged &middot; redlines drafted",[("Clause 4.2","flagged"),("Clause 7.1","redlined"),("Everything else","clean")],"REDLINED"),
  "visuals": f_folder("Asset pack","822 COMPONENTS",[row("Landing page","assembled, on-brand",chip="done"),row("9 visuals","your tokens, every one",chip="done"),row("Pitch one-pager","from the same pack",chip="done")]),
  "connectors": f_pills([row("Mail + CRM","it acts inside them",chip="wired"),row("Calendar","knows your week",chip="wired"),row("Payments","invoices + chasing",chip="wired"),row("Docs","reads and cites",chip="wired")]),
  "result": f_console("The difference","EXECUTES",[("Creates files","decks, sheets, pages",True),("Automates work","flows on triggers",True),("Finishes tasks","not just answers",True)],buttons=False),
  "gate": f_bubble("Executes fast. Sends only on your tap.","The skills","INSTALLED ONCE","install the desk",A),
 },
 "carouselcmd":{
  "oldbill": f_receipt("DESIGN RETAINER","EVERY MONTH",[("Carousel deck x4","waited a week"),("Revision rounds","two each"),("Rush fees","surprise")],"One command now","cents"),
  "command": f_env("THE BRIEF","One line starts it.","PULSE interviews you for the angle first.","Deck started"),
  "visuals": f_folder("Brand pack","NO TEMPLATE SMELL",[row("Colors + type","your tokens exactly",chip="locked"),row("Components","from your own pack",chip="locked"),row("Covers","hook-first, on grid",chip="locked")]),
  "slides": f_fan("The deck","TEN PAGES",[row("Hook page","scroll-stop first",chip="1"),row("Body pages","one beat per page",chip="2-9"),row("CTA page","the fixed pill",chip="10")]),
  "captions": f_paper("Caption kit","SHIPS WITH IT","CTA-first, hashtags, first comment",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Nothing left to write</div><div class="rs" style="color:#8a7a5e">posting kit included</div></div><span class="chip">Copy</span></div>'),
  "clock": f_metro("Brief to done","MINUTES",[("Brief","one line",1),("Visuals","generated",1),("Slides","assembled",1),("Kit","captions in",0)]),
  "gate": f_badge(LOCK,"1","One deck waits for your tap.","review once, then it posts"),
  "math": f_bubble("The retainer became runway.","One command","METERED IN CENTS","build the deck",A),
 },
 "patterns":{
  "react": f_metro("Every run","THINK FIRST",[("Reason","what is needed",1),("Act","tool call",1),("Observe","what came back",1),("Done","or loop",0)]),
  "codeact": f_stamp("The action","SENTINEL","fix written, tested, shipped",[("Wrote the fix","19:04"),("42 tests passed","19:11"),("PR opened","19:12")],"EXECUTED"),
  "plan": f_split("PLANNING",["Deep judgement","Once per job","Expensive, worth it"],"EXECUTION",["Light tier","Every step","Cents per run"]),
  "reflect": f_fan("Before you see it","RANKED",[row("Draft v1","against your bar",chip="72"),row("Draft v2","tightened",chip="85"),row("Draft v3","what you get",chip="92")]),
  "multi": f_pills([row("CORTEX","research, only research",chip="one job"),row("SPECTER","outbound, gated",chip="one job"),row("STRIKER","deals and replies",chip="one job"),row("PULSE","content in your voice",chip="one job")]),
  "stack": f_console("Composed per job","YOU TYPE THE GOAL",[("Reason + act","always on",True),("Plan + execute","tiered by the router",True),("Draft + refine","before you see it",True)],buttons=False),
  "gate": f_vault("YOU","THE 6TH PATTERN"),
  "operator": f_bubble("Same models. Better design. A workforce.","The patterns","ARCHITECTURE WINS","check my stack",A),
 },
 "setup":{
  "connect": f_pills([row("Mail","two clicks",chip="wired"),row("CRM","two clicks",chip="wired"),row("Calendar","two clicks",chip="wired"),row("Payments","two clicks",chip="wired")]),
  "init": f_env("MINUTE 12","/init my business","It interviews you once: ICP, offer, pricing, no-list.","Memory born"),
  "voice": f_paper("Voice sample","MINUTE 25","Paste your best posts",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Voice locked</div><div class="rs" style="color:#8a7a5e">every draft sounds like you</div></div><span class="chip">Saved</span></div>'),
  "permissions": f_console("The gate setup","MINUTE 35",[("Internal jobs","run free",True),("External sends","wait for your tap",True),("Spend caps","on every flow",True)],buttons=False),
  "firsttask": f_stamp("First task","MINUTE 45","source 20 accounts and brief them",[("Found","20 matches"),("Briefed","1 page each"),("Time","9 minutes")],"DONE"),
  "digest": f_badge(LOCK,"1","Your first digest arrived.","overnight jobs, parked approvals, hot threads"),
  "compound": f_chartline("Usefulness","EVERY SESSION",[20,30,38,52,60,74,85,100],"corrections become rules: month two beats month one alone"),
  "operator": f_bubble("Hour one is setup. Year one is leverage.","The hour","BLOCK IT TODAY","start the clock",A),
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
