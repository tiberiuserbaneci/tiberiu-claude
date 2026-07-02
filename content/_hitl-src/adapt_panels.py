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
LOCK=L.LOCK; PLANE=L.PLANE
f_podium,f_browser,f_stat=L.f_podium,L.f_browser,L.f_stat
f_battery,f_calendar,f_rings,f_shelf,f_rows=L.f_battery,L.f_calendar,L.f_rings,L.f_shelf,L.f_rows

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
  "gate": f_keys([("AGENTS","RUN THE NIGHT",False),("YOUR TAP","RUNS THE AGENTS",True)]),
  "own": f_bubble("Rented tabs forget. Owned systems compound.","The OS","ONE COMMAND CENTER","run my company",A),
 },
 "loops":{
  "oldway": f_rings("YOU, THE CRON JOB",[("Type","the prompt, again"),("Wait","watch it think"),("Paste","somewhere, by hand")],"the manual cycle: you orbit the tool instead of the tool orbiting the goal"),
  "loop": f_dial(84,"LAST WEEK","212","cycles completed","you typed three sentences total"),
  "define": f_env("THE WHOLE SETUP","One sentence.","Follow up every lead quiet for 3 days.","Flow created"),
  "trigger": f_console("Triggers","REPLACE YOUR MEMORY",[("Daily 09:00","the cadence fires",True),("On every reply","the pipe updates",True),("On usage drop","churn watch pings",True)],buttons=False),
  "verify": f_ticket("Cycle report","EVERY RUN",tick_cells([("RUN","Done",1),("CHECK","Pass",1),("GOAL","Met",1),("LOG","Filed",1),("NEXT","09:00",0)]),"CHECKED BEFORE IT COUNTS","EXITS SET, NO ZOMBIES"),
  "trap": f_receipt("LOOP WITHOUT EXIT","WHAT IT BURNS",[("Endless retries","tokens"),("No stop condition","budget"),("Silent failures","days")],"Ultron flows","capped"),
  "gate": f_vault("SEND","LOOPS RUN FREE, SENDS WAIT"),
  "scale": f_chartline("Past your hours","CYCLES PER WEEK",[16,28,44,70,104,150,182,212],"your hours stay flat: 212 cycles ran last week from three sentences"),
 },
 "aibody":{
  "difference": f_split("A CHATBOT",["Answers questions","Waits for you","Forgets at midnight"],"A BODY",["Reads your market","Writes in your voice","Ships real work"]),
  "router": f_keys([("LITE","LOOKUPS",False),("SMART","THE DAILY DRIVER",True),("DEEP","JUDGEMENT ONLY",False)]),
  "eyes": f_browser_wrap("live signals &middot; overnight",hd("The eyes","CORTEX")+row("Northwind","hiring 3 ops roles now",chip="live")+row("Globex","raised $4M in May",chip="live")+row("Initech","stack has no AI layer",chip="live")),
  "voice": f_env("DRAFT 14 &middot; YOUR VOICE","Reads like you.","Because it learned from what you wrote.","Approve"),
  "hands": f_stamp("Build log","SENTINEL","launch page &middot; from a sentence",[("Built + styled","19:04"),("42 tests passed","23:12"),("Live on your domain","23:40")],"SHIPPED"),
  "heart": f_folder("The core","EVERY AGENT DRAWS FROM IT",[row("icp.md","who you sell to",chip="loaded"),row("voice.md","how you sound",chip="loaded"),row("pipeline.live","what is moving now",chip="live")]),
  "gate": f_badge(LOCK,"YOU","Every external move waits.","you hold the reins, always"),
  "operator": f_bubble("Brain, eyes, voice, hands, heart. One login.","The body","FULLY WIRED","augment me",A),
 },
 "fivesigns":{
  "sign1": f_pills([row("Same question, 09:12","answered by a human",chip="daily"),row("Same question, 11:40","answered again",chip="daily"),row("Same question, 16:05","a flow should own this",chip="fix")]),
  "sign2": f_receipt("THE GLUE WORK","PAYROLL ON PASTE",[("CRM to sheet, by hand","2h weekly"),("Inbox to CRM, by hand","1h daily"),("Sheet to report, by hand","4h monthly")],"A flow does it","minutes"),
  "sign3": f_rows("","Waiting on you","THE BOTTLENECK",[row("Proposal draft","stuck since Tuesday",chip="held"),row("Campaign launch","stuck since Monday",chip="held"),row("Invoice batch","stuck since the 1st",chip="held"),row("With Ultron: prepped","you just tap",chip="ready")]),
  "sign4": f_chartline("Speed to lead","FIRST REPLY WINS",[95,80,68,50,34,20,10,4],"hours to seconds: the flow answers while it is still warm"),
  "sign5": f_paper("Month-end","3 DAYS, THE OLD WAY","Pulled, formatted, argued over",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">On demand now</div><div class="rs" style="color:#8a7a5e">every figure cites its source</div></div><span class="chip">Minutes</span></div>'),
  "test": f_odo(["5","/","5"],0,"YES ANSWERS OUT OF FIVE","every yes is a leak &middot; systems problem, not staffing"),
  "fix": f_calendar("Week one","START SMALL",[("M",None),("T",None),("W",None),("T",None),("F",None),("S",None),("S",None),("8","PICK"),("9","BUILD"),("10",None),("11","TEST"),("12","LIVE"),("13",None),("14",None),("15",None),("16","RUN"),("17","RUN"),("18","RUN"),("19","RUN"),("20",None),("21",None)],"one workflow first, then repeat"),
  "gate": f_vault("TAP","AUTOMATED, NEVER UNSUPERVISED"),
 },
 "contentdesk":{
  "cal": f_ticket("The plan","ONE LINE IN",tick_cells([("MON","Post",1),("TUE","Reel",1),("WED","",0),("THU","Deck",1),("FRI","News",1)]),"14 SLOTS PLANNED","10:00 LOCAL EACH"),
  "hooks": f_fan("Pick the winner","FROM YOUR HOOK BANK",[row("Hook A","the confession angle",chip="A"),row("Hook B","the number angle",chip="B"),row("Hook C","the enemy angle",chip="C")]),
  "voice": f_paper("Draft","RANKED 92","Reads like you wrote it",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Voice locked</div><div class="rs" style="color:#8a7a5e">sampled from 60 real posts</div></div><span class="chip">Publish</span></div>'),
  "repurpose": f_shelf("One brief","FIVE FORMATS OUT",[("LinkedIn post","long-form, your voice","done"),("IG + TikTok caption","CTA-first, native","done"),("Carousel","10 pages, on brand","done"),("Newsletter","inboxed at 07:00","queued")]),
  "inbox": f_gauge(99,"99.2%","land in the inbox","warm domains &middot; ramped, never blasted"),
  "desk": f_console("The desk","NO MEETINGS",[("Planner","fires Monday 07:00",True),("Writer","your voice, ranked",True),("Distributor","10:00 local, daily",True)],buttons=False),
  "gate": f_badge(LOCK,"3","Three drafts wait for you.","nothing posts without your tap"),
  "math": f_bubble("A content team, metered in cents.","The desk","PAYROLL: ZERO","run the desk",A),
 },

 "unstuck":{
  "floor": f_battery(12,"HOW MUCH OF THE MACHINE YOU USE","level 1 is ask, copy, close &middot; the other 88% never wakes up"),
  "memory": f_folder("What it keeps","LEVEL 2",[row("icp.md","who you sell to",chip="saved"),row("voice.md","how you write",chip="saved"),row("rules.md","every correction, forever",chip="grows")]),
  "jobs": f_fan("Running now","LEVEL 3",[row("Sourcing the list","one line in",chip="live"),row("Briefing accounts","1 page each",chip="live"),row("Drafting openers","gate holds them",chip="live")]),
  "ship": f_env("LEVEL 4 &middot; THE BUILD","One sentence.","Landing page built, styled, tested: live on your domain by 23:40.","Shipped"),
  "routines": f_metro("Overnight","LEVEL 5",[("23:00","triage",1),("02:00","scoring",1),("06:00","digest",1),("07:00","your coffee",0)]),
  "gap": f_podium([("L1","chat",0),("L2","memory",0),("L3","jobs",0),("L4","ship",0),("L5","auto",1)]),
  "gate": f_keys([("AUTONOMY","GROWS EVERY LEVEL",False),("YOUR TAP","NEVER SHRINKS",True)]),
  "ceiling": f_chartline("The climb","FLOOR TO CEILING",[12,20,34,50,66,80,92,100],"five levels up: autonomy grows, your tap stays on every external move"),
 },
 "hidden":{
  "myth": f_split("THE PROMPTERS",["Re-word the ask","Hope it lands","Start over daily"],"THE OPERATORS",["Install the skill","Wire the stack","Work arrives done"]),
  "decks": f_paper("Proposal","BUILT ITSELF","Northwind expansion offer",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">In your tokens</div><div class="rs" style="color:#8a7a5e">structure from decks that closed</div></div><span class="chip">Send</span></div>'),
  "sheets": f_browser("reports &middot; live numbers", hd("Month view","SOURCES ATTACHED")+row("Revenue","every figure traces to a run",chip="live")+row("Pipeline","refreshed this morning",chip="live")+row("Spend","cents, itemised",chip="live")),
  "contracts": f_stamp("NDA review","COUNSEL","risk lines flagged &middot; redlines drafted",[("Clause 4.2","flagged"),("Clause 7.1","redlined"),("Everything else","clean")],"REDLINED"),
  "visuals": f_shelf("Asset pack","822 COMPONENTS",[("Landing page","assembled from the pack, on-brand","done"),("9 visuals","your tokens on every one","done"),("Pitch one-pager","same system, zero drift","done")]),
  "connectors": f_pills([row("Mail + CRM","it acts inside them",chip="wired"),row("Calendar","knows your week",chip="wired"),row("Payments","invoices + chasing",chip="wired"),row("Docs","reads and cites",chip="wired")]),
  "result": f_console("The difference","EXECUTES",[("Creates files","decks, sheets, pages",True),("Automates work","flows on triggers",True),("Finishes tasks","not just answers",True)],buttons=False),
  "gate": f_bubble("Executes fast. Sends only on your tap.","The skills","INSTALLED ONCE","install the desk",A),
 },
 "carouselcmd":{
  "oldbill": f_receipt("DESIGN RETAINER","EVERY MONTH",[("Carousel deck x4","waited a week"),("Revision rounds","two each"),("Rush fees","surprise")],"One command now","cents"),
  "command": f_env("THE BRIEF","One line starts it.","PULSE interviews you for the angle first.","Deck started"),
  "visuals": f_folder("Brand pack","NO TEMPLATE SMELL",[row("Colors + type","your tokens exactly",chip="locked"),row("Components","from your own pack",chip="locked"),row("Covers","hook-first, on grid",chip="locked")]),
  "slides": f_rows("","The deck","TEN PAGES",[row("Page 1","hook, scroll-stop",chip="cover"),row("Pages 2-9","one beat per page",chip="body"),row("Page 10","the fixed pill",chip="cta"),row("Every page","your grid, your tokens",chip="brand")]),
  "captions": f_paper("Caption kit","SHIPS WITH IT","CTA-first, hashtags, first comment",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Nothing left to write</div><div class="rs" style="color:#8a7a5e">posting kit included</div></div><span class="chip">Copy</span></div>'),
  "clock": f_metro("Brief to done","MINUTES",[("Brief","one line",1),("Visuals","generated",1),("Slides","assembled",1),("Kit","captions in",0)]),
  "gate": f_badge(LOCK,"1","One deck waits for your tap.","review once, then it posts"),
  "math": f_dial(78,"THE METER","cents","per deck, per run","the retainer became runway"),
 },
 "patterns":{
  "react": f_metro("Every run","THINK FIRST",[("Reason","what is needed",1),("Act","tool call",1),("Observe","what came back",1),("Done","or loop",0)]),
  "codeact": f_stamp("The action","SENTINEL","fix written, tested, shipped",[("Wrote the fix","19:04"),("42 tests passed","19:11"),("PR opened","19:12")],"EXECUTED"),
  "plan": f_split("PLANNING",["Deep judgement","Once per job","Expensive, worth it"],"EXECUTION",["Light tier","Every step","Cents per run"]),
  "reflect": f_fan("Before you see it","RANKED",[row("Draft v1","against your bar",chip="72"),row("Draft v2","tightened",chip="85"),row("Draft v3","what you get",chip="92")]),
  "multi": f_pills([row("CORTEX","research, only research",chip="one job"),row("SPECTER","outbound, gated",chip="one job"),row("STRIKER","deals and replies",chip="one job"),row("PULSE","content in your voice",chip="one job")]),
  "stack": f_console("Composed per job","YOU TYPE THE GOAL",[("Reason + act","always on",True),("Plan + execute","tiered by the router",True),("Draft + refine","before you see it",True)],buttons=False),
  "gate": f_vault("YOU","THE 6TH PATTERN"),
  "operator": f_podium([("PROMPT","one-shot",0),("CHAIN","brittle",0),("AGENT","one job",0),("PATTERNS","composed",0),("WORKFORCE","yours",1)]),
 },
 "setup":{
  "connect": f_shelf("Minute 10","THE STACK, WIRED",[("Mail","two clicks, it acts inside","wired"),("CRM","reads and updates itself","wired"),("Calendar + payments","knows your week, chases invoices","wired")]),
  "init": f_env("MINUTE 12","/init my business","It interviews you once: ICP, offer, pricing, no-list.","Memory born"),
  "voice": f_paper("Voice sample","MINUTE 25","Paste your best posts",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Voice locked</div><div class="rs" style="color:#8a7a5e">every draft sounds like you</div></div><span class="chip">Saved</span></div>'),
  "permissions": f_console("The gate setup","MINUTE 35",[("Internal jobs","run free",True),("External sends","wait for your tap",True),("Spend caps","on every flow",True)],buttons=False),
  "firsttask": f_stat("20","accounts sourced and briefed &middot; minute 45 &middot; 9 minutes flat",[22,34,48,60,74,88,100]),
  "digest": f_badge(LOCK,"1","Your first digest arrived.","overnight jobs, parked approvals, hot threads"),
  "compound": f_chartline("Usefulness","EVERY SESSION",[20,30,38,52,60,74,85,100],"corrections become rules: month two beats month one alone"),
  "operator": f_bubble("Hour one is setup. Year one is leverage.","The hour","BLOCK IT TODAY","start the clock",A),
 },

 "verified":{
  "flood": f_pills([row("50 AI skills you NEED","reposted 400 times",chip="recycled"),row("The ULTIMATE list","same links, new thumbnail",chip="recycled"),row("Nobody installed one","zero receipts anywhere",chip="fact")]),
  "test": f_ticket("The bench","ONE WEEK, REAL WORK",tick_cells([("MON","Install",1),("TUE","Run",1),("WED","Run",1),("THU","Score",1),("FRI","Cut",1)]),"EVERY SKILL, REAL BRIEFS","KEPT OR CUT, NO MAYBE"),
  "fakes": f_split("THE LIST CLAIMED",["50 working skills","Plug and play","Game changers"],"THE TEST FOUND",["17 dead or renamed","9 answer, never act","24 actually run"]),
  "keepers": f_folder("The shortlist","SURVIVORS, BY JOB",[row("Writing desk","drafts in your voice",chip="kept"),row("Research desk","briefs with sources",chip="kept"),row("Build desk","pages that go live",chip="kept")]),
  "safest": f_metro("Install order","SAFE PATH",[("First","the two Anthropic ship",1),("Second","verified community layer",1),("Third","your own custom skills",1),("Never","an unverified link",0)]),
  "curated": f_browser_wrap("app.51ultron.com/techniques",hd("The library","TESTED BEFORE LISTED")+row("Every technique","run on real pipelines first",chip="verified")+row("Every skill","curated, not scraped",chip="verified")+row("Your desk","no gambling on links",chip="safe")),
  "rule": f_stamp("The filter","ONE QUESTION","does it finish work, or describe it?",[("Returns advice","a bookmark"),("Returns files","a worker"),("Only workers","made the list")],"EXECUTES"),
  "desk": f_odo(["1","2"],0,"SKILLS ON MY DESK","each tested on my own pipeline &middot; running daily"),
 },
 "fivepaid":{
  "research": f_rows("","Skill 1","RESEARCH THAT CLOSES",[row("Northwind","hiring 3 ops roles right now",chip="warm"),row("Their stack","no AI layer yet",chip="angle"),row("The opener","written from the brief",chip="ready"),row("The call","cold turned warm",chip="paid")]),
  "outbound": f_badge(PLANE,"60","One trigger per email, sixty a day.","warm domains, ramped sends: placement is the skill"),
  "content": f_paper("Skill 3","A VOICE","Recognized before the handle",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Not words. A voice.</div><div class="rs" style="color:#8a7a5e">clients spot it in the feed</div></div><span class="chip">Post</span></div>'),
  "builds": f_fan("Skill 4","BUILDS, NO BUILDERS",[row("Landing page","plain English in",chip="live"),row("Dashboard","same afternoon",chip="live"),row("Client portal","assembly, not code",chip="live")]),
  "systems": f_console("Skill 5","SYSTEMS THAT RUN",[("Follow-up flow","fires on silence",True),("Digest","lands 07:00 daily",True),("Exit conditions","set once, respected",True)],buttons=False),
  "one": f_keys([("ONE SKILL","RUN DAILY, DEEP",True),("FIVE BADGES","ON A SHELF",False)]),
  "client": f_receipt("FIRST CLIENT","YOUR OWN COMPANY",[("Ran it on my pipeline","week 1"),("Kept the receipts","week 2"),("Receipts became pitch","week 3")],"The resume","results"),
  "meter": f_dial(78,"THE SPREAD","cents","to practice the skill","the invoice runs high when you deliver"),
 },
 "installs24":{
  "stock": f_split("STOCK, DAY ONE",["Answers questions","Waits for prompts","Forgets the thread"],"INSTALLED RIGHT",["Runs whole plays","Acts in your apps","Compounds monthly"]),
  "plugins": f_shelf("Plugins","DESKS, NOT FEATURES",[("Marketing desk","campaigns, hooks, calendars","1 install"),("Research desk","briefs with sources","1 install"),("Deals + build desk","proposals, pages, dashboards","1 install")]),
  "skills": f_env("ONE LINE","/audit my funnel","A slash command that replaces a page of prompting. Same play, every time.","Play run"),
  "connectors": f_metro("Wired in","NO COPY-PASTE BRIDGE",[("Mail","it acts inside",1),("Docs","reads and cites",1),("CRM","updates itself",1),("Payments","invoices + chasing",0)]),
  "three": f_folder("Tonight","THE STARTER TRIO",[row("Marketing","the loudest job first",chip="20:00"),row("Design","decks + visuals",chip="20:10"),row("Docs","reports that cite",chip="20:20")]),
  "preinstalled": f_browser_wrap("app.51ultron.com",hd("Or skip setup","IT COMES INSTALLED")+row("71 skills","tested, loaded",chip="day 1")+row("7 agents","one chat box",chip="day 1")+row("Connectors","already wired",chip="day 1")),
  "gate": f_vault("TAP","THE BRAKE, PRE-INSTALLED"),
  "compound": f_chartline("The setup","PAYS RENT MONTHLY",[18,26,34,46,58,71,86,100],"corrections become rules: month three runs sharper than month one"),
 },
 "advisors":{
  "context": f_podium([("BLOG","generic",0),("GURU","generic",0),("COURSE","generic",0),("AVERAGES","close",0),("YOUR DATA","the moat",1)]),
  "three": f_pills([row("The pricer","unit economics, cold",chip="seat 1"),row("The editor","cuts to the spine",chip="seat 2"),row("The strategist","doors, not dollars",chip="seat 3")]),
  "books": f_folder("The unlock","THEY READ YOUR BOOKS",[row("deals.live","every open proposal",chip="loaded"),row("clients.md","who pays, who churns",chip="loaded"),row("cash.md","runway, real",chip="loaded")]),
  "pricer": f_stamp("The pricer","ON A REAL PROPOSAL","unit economics, line by line",[("Your floor","too low"),("The proof","margin math"),("The verdict","raise it")],"RAISE IT"),
  "editor": f_paper("The editor","ON THE DRAFT","Cut half. The offer was buried.",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Stripped to the spine</div><div class="rs" style="color:#8a7a5e">less closed more</div></div><span class="chip">Rewrite</span></div>'),
  "strategist": f_rings("DOES IT OPEN DOORS?",[("Doorway deals","get the yes"),("Dead-end deals","get declined"),("Better filter","better clients")],"not is the deal good: is the deal a doorway"),
  "closed": f_receipt("THE DEAL","THREE LENSES, ONE WIN",[("Repriced","the pricer"),("Rewritten","the editor"),("Requalified","the strategist")],"Signature","clean"),
  "board": f_bubble("On call at 2am. Briefed on everything. Costs cents.","The board","SEATED IN ONE CHAT","seat my board",A),
 },
 "ghosted":{
  "sent": f_split("CAMPAIGN A",["Same writer","Same offer","Crushed it"],"CAMPAIGN B",["Same writer","Same offer","Died in spam"]),
  "opens": f_gauge(12,"REPLIES","the only metric that pays","tracking pixels hurt placement and measure vanity"),
  "fresh": f_battery(8,"DOMAIN REPUTATION, DAY ONE","full blast at 8% charge lands in promotions forever &middot; charge first"),
  "onedomain": f_pills([row("outbound-one.com","carries a quarter",chip="safe"),row("outbound-two.com","carries a quarter",chip="safe"),row("outbound-three.com","one bad batch, contained",chip="safe"),row("your main domain","never touches cold",chip="rule")]),
  "spike": f_metro("The ramp","BORING WINS INBOXES",[("Week 1","60 a day, steady",1),("Week 2","60 a day, steady",1),("Week 3","60 a day, steady",1),("The blast","0 then 500: dead",0)]),
  "catchall": f_console("The list","VERIFY OR PAY",[("Verified addresses","cleared to send",True),("Catch-all addresses","poison the batch",False),("Bounce watch","kills bad batches",True)],buttons=False),
  "infra": f_odo(["9","9",".","2"],0,"PERCENT INBOXED","warm domains &middot; ramped sends &middot; watched spam rates"),
  "road": f_env("THE LOCKED MAILBOX","Great copy, dead infra.","A love letter nobody ever opens. Fix the road, then the car.","Unlocked"),
 },
 "twohours":{
  "input": f_env("14:00","One sentence.","A service for founders who hate bookkeeping. That was the entire input.","Idea in"),
  "offer": f_paper("14:20","THE OFFER","Positioning, price, guarantee",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Drafted against the niche</div><div class="rs" style="color:#8a7a5e">not a template</div></div><span class="chip">Locked</span></div>'),
  "page": f_browser_wrap("your-offer.com &middot; live",hd("14:50","THE PAGE")+row("Hero + pricing + FAQ","assembled from the pack",chip="done")+row("Brand tokens","yours, exactly",chip="done")+row("Preview, tap","live on your domain",chip="live")),
  "plan": f_calendar("15:10","THE CONTENT PLAN",[("M","POST"),("T","REEL"),("W",None),("T","DECK"),("F","POST"),("S",None),("S",None),("8","POST"),("9",None),("10","REEL"),("11","POST"),("12","NEWS"),("13",None),("14","POST")],"14 slots queued &middot; 10:00 local each"),
  "outreach": f_badge(PLANE,"20","Twenty openers, one trigger each.","parked at the gate for your tap"),
  "review": f_keys([("16:00","YOU REVIEW",True),("16:01","IT SHIPS",False)]),
  "excuse": f_stamp("The excuses","AT 13:59","all three, on the record",[("No team","one operator"),("No budget","metered in cents"),("No time","two hours flat")],"EXPIRED"),
  "moat": f_chartline("Speed","THE ONLY MOAT LEFT",[10,22,30,44,58,70,86,100],"idea to live while others plan: feedback to fix within the hour"),
 },
 "salesorg":{
  "everything": f_rows("","The mega-bot","100 NODES, 0 RESULTS",[row("Research + outreach + deals","one agent, all of it",strike=True,chip="fails"),row("Node 47","nobody knows what it does",strike=True,chip="fails"),row("One bad branch","takes the whole thing down",strike=True,chip="fails"),row("Real teams","have structure",chip="the fix")]),
  "structure": f_podium([("INTEL","research",0),("SEND","outreach",0),("PREP","enablement",0),("PIPE","revops",0),("YOU","the chief",1)]),
  "research": f_stat("847","accounts profiled, scored and briefed before a word is written",[26,38,50,62,76,90,100]),
  "outreach": f_pills([row("Email","drafted per thread, parked",chip="gated"),row("LinkedIn","drafted per profile, parked",chip="gated"),row("Follow-ups","fire on silence, parked",chip="gated")]),
  "enable": f_folder("Desk 3","THE WORK NOBODY LOVES",[row("Proposals","drafted from the call",chip="on time"),row("Scheduling","no back-and-forth",chip="on time"),row("Follow-ups","never dropped",chip="on time")]),
  "revops": f_console("Desk 4","TRUTH IN THE CRM",[("Stages move","on replies, not memory",True),("Data stays clean","deduped, enriched",True),("Digest lands","daily, 07:00",True)],buttons=False),
  "onejob": f_shelf("The rule","ONE JOB PER AGENT",[("CORTEX","research, only research","desk 1"),("SPECTER","outbound, only outbound","desk 2"),("STRIKER","deals, only deals","desk 3")]),
  "chief": f_vault("YOU","ONE TAP A DAY, ON TOP"),
 },
 "adsagency":{
  "retainer": f_receipt("THE RETAINER","WHAT IT BOUGHT",[("Research","delivered quarterly"),("Copy rounds","two week wait"),("The audit","a slide deck")],"That bill","ends here"),
  "spy": f_browser_wrap("rival ads &middot; diffed weekly",hd("Monday","THE SPY REPORT")+row("Rival A","3 new creatives, testimonial angle",chip="new")+row("Rival B","dropped price hooks",chip="shift")+row("Rival C","silent for 3 weeks",chip="gap")),
  "gap": f_rings("THE EMPTY ANGLE",[("They all hook on","price, features, promise"),("Nobody covers","the switching pain"),("You take","the angle left open")],"hooks ranked by frequency: the gap becomes yours"),
  "variations": f_fan("One description in","TWENTY VARIATIONS OUT",[row("Short","hook-first, feed native",chip="x7"),row("Medium","story arc, your voice",chip="x7"),row("Long","proof-heavy, retargeting",chip="x6")]),
  "audit": f_gauge(74,"HEALTH","186 checks, one score","fatigue, overlap, anomalies: with a fix list attached"),
  "score": f_dial(58,"BEFORE IT SPENDS","6","dimensions, every ad","weak hooks get rewritten, not launched"),
  "chain": f_metro("The chain","ONE MORNING",[("Spy","rivals diffed",1),("Gap","angle found",1),("Draft","20 variations",1),("Score","launch or rewrite",0)]),
  "sign": f_keys([("THE LAUNCH","WAITS AT THE GATE",False),("YOUR TAP","RELEASES THE SPEND",True)]),
 },
 "million":{
  "notteam": f_split("THE OLD SHAPE",["Funded startup","Team of 20","Burn and pray"],"THE NEW SHAPE",["One laptop","Meter in cents","Systems that compound"]),
  "agents": f_pills([row("Research","runs parallel",chip="working"),row("Outreach","runs parallel",chip="working"),row("Content","runs parallel",chip="working"),row("You","decide, once a day",chip="the job")]),
  "revenue": f_chartline("The curve","LINES DIVERGE",[22,30,38,44,56,68,82,100],"revenue up 32% this month: payroll unchanged since day zero"),
  "speed": f_stat("3h","idea to live offer &middot; feedback to fix in one &middot; the committee is still scheduling",[100,84,66,50,38,26,18]),
  "costs": f_receipt("THE MONTH","THE SPREAD",[("Research, 200 briefs","cents"),("Content, 14 posts","cents"),("The market pays","full price")],"The spread","the business"),
  "calendar": f_ticket("The week","NO STANDUPS",tick_cells([("MON","07:00",1),("TUE","07:00",1),("WED","07:00",1),("THU","07:00",1),("FRI","07:00",1)]),"DIGESTS, NOT MEETINGS","DECISIONS WHEN YOU CHOOSE"),
  "gated": f_vault("KEEL","AUTONOMY, KEPT"),
  "you": f_bubble("Someone builds this company this year.","The bet","WHY NOT YOU","start tonight",A),
 },
 "zerostart":{
  "barrier": f_rings("THE 2026 LIST",[("Niche","a problem people pay for"),("Distribution","show up where they look"),("Consistency","daily, made cheap")],"code fell off the list: these three are all that is left"),
  "build": f_env("THE BUILD","One sentence.","Describe the offer: Crescendo assembles the page from 822 parts.","Live today"),
  "workflow": f_console("The engine","RUNS WITHOUT YOU",[("Follow-up","fires on silence",True),("Delivery","on payment, instant",True),("Reporting","weekly, cited",True)],buttons=False),
  "problem": f_folder("The niche","BORING PRINTS MONEY",[row("Bookkeeping hate","real invoices",chip="pays"),row("Compliance dread","real invoices",chip="pays"),row("Inbox chaos","real invoices",chip="pays")]),
  "daily": f_calendar("The habit","CHEAP TO KEEP",[("M","POST"),("T","POST"),("W","POST"),("T","POST"),("F","POST"),("S",None),("S",None),("8","POST"),("9","POST"),("10","POST"),("11","POST"),("12","POST"),("13",None),("14","POST")],"14 from one line &middot; your only job is to be real"),
  "profit": f_gauge(84,"YEAR 1","profit, not promises","cost base in cents, output of a team: the math flipped"),
  "ten": f_odo(["1","0"],0,"CUSTOMERS, TEN HANDSHAKES","the machine sources and drafts: you close like a human"),
  "yours": f_stamp("The stack","ONE PERSON","build, run, approve",[("The build","yours"),("The engine","yours"),("The gate","yours")],"ALL YOURS"),
 },

 "diytrap":{
  "recipe": f_rows("","The tutorial stack","PAGE ONE OF MANY",[row("Framework + graph layer","two docs sites deep",chip="week 1"),row("Tools, state, control flow","wired by hand",chip="week 2"),row("Retry + error handling","the part nobody posts",chip="week 3"),row("Your actual company","still waiting",strike=True,chip="paused")]),
  "wiring": f_metro("The loop, DIY","EVERY ARROW IS YOURS",[("Plan","you wire it",1),("Act","you wire it",1),("Observe","you wire it",1),("Repeat","you maintain it forever",0)]),
  "breaks": f_console("Week four","NOBODY IS WATCHING",[("Edge case at 2am","silent failure",False),("Send without a gate","went out wrong",False),("State lost","starts from zero",False)],buttons=False),
  "bill": f_receipt("THE DIY INVOICE","WHAT IT REALLY COST",[("Three weekends","wiring"),("Every Monday","debugging"),("The pipeline","untouched")],"Leads produced","zero"),
  "install": f_shelf("The other path","ALREADY WIRED",[("CORTEX + SPECTER","research and outbound, composing","built"),("STRIKER + PULSE","deals and content, your voice","built"),("SENTINEL + the gate","ships work, parks sends","built")]),
  "audited": f_ticket("Every cycle","AUDITED, NOT HOPED",tick_cells([("PLAN","Set",1),("ACT","Run",1),("CHECK","Pass",1),("GATE","Park",1),("SHIP","Tap",0)]),"CHECKS ITS OWN WORK","SENDS WAIT FOR YOU"),
  "firstrun": f_odo(["2","0"],0,"BRIEFS FROM ONE SENTENCE","typed 09:14 &middot; briefed 09:23 &middot; minute ten of owning it"),
  "verdict": f_stamp("The verdict","BUILD VS INSTALL","where your weekends should go",[("Plumbing","installed"),("Product","yours"),("Distribution","yours")],"SHIP PRODUCT"),
 },
 "anatomy":{
  "trigger": f_env("09:00 &middot; THE TRIGGER","Nobody typed anything.","Three leads quiet for three days: the loop wakes itself.","Loop live"),
  "reads": f_rows("","Before it writes","LOADED FROM MEMORY",[row("The last reply","and the objection in it",chip="read"),row("Your pricing rules","the no-discount line",chip="read"),row("The relationship","every touch, dated",chip="read"),row("Then, and only then","it drafts",chip="go")]),
  "draft1": f_dial(71,"DRAFT ONE","71","its own grade","too long, weak trigger line: it redoes without asking"),
  "draft3": f_chartline("Three drafts","STOP AT PROOF",[71,82,90],"exit condition met at 90: not tired, not hopeful, verified"),
  "parked": f_badge(LOCK,"3","Three sends, parked at the gate.","autonomous inside, your tap outside"),
  "tap": f_keys([("APPROVE","TWO TAPS, TEN SECONDS",True),("KILL","ONE DRAFT, YOUR CALL",False)]),
  "reply": f_pills([row("Pipeline","moved on the reply",chip="logged"),row("Next follow-up","scheduled itself",chip="logged"),row("Digest","updated for 07:00",chip="logged")]),
  "point": f_bubble("A prompt gives you words. A loop gives you outcomes.","The loop","RECEIPTS INCLUDED","put one on repeat",A),
 },
 "mintskills":{
  "admission": f_split("THE MEGA-AGENT",["Graphs and glue","Breaks in private","Nobody owns it"],"THE SKILL",["Five folders, one file","Small enough to own","Runs the same daily"]),
  "folders": f_folder("The anatomy","THE WHOLE STACK",[row("skill.md","what it does, your rules",chip="1 file"),row("steps + checks","how it runs, how it stops",chip="owned"),row("examples","your best runs, distilled",chip="yours")]),
  "ore": f_paper("The raw material","YOU ALREADY HAVE IT","The proposal you write the same way",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Repeated monthly</div><div class="rs" style="color:#8a7a5e">that is ore, not a chore</div></div><span class="chip">Mint it</span></div>'),
  "mint": f_metro("The mint","FOUR PASSES",[("Discover","find the repeated job",1),("Scaffold","give it the folders",1),("Distill","press it into steps",1),("Audit","run it against your bar",0)]),
  "voice": f_stamp("Downloaded vs minted","THE DIFFERENCE","a minted skill carries",[("Your rules","baked in"),("Your no-list","enforced"),("Your phrasing","exact")],"YOURS"),
  "shelf": f_shelf("My shelf","SIX MINTED",[("Proposal + pricing","born from repeated deals","daily"),("Brief + audit","born from repeated research","daily"),("Follow-up + report","born from repeated chasing","daily")]),
  "compound": f_chartline("The hardening","FIX ONCE, KEEP FOREVER",[40,52,61,72,80,88,94,100],"every correction becomes a rule: month three beats month one"),
  "shift": f_podium([("SAVE","hoards",0),("DOWNLOAD","borrows",0),("TWEAK","rents",0),("MINT","owns",1),("COMPOUND","wins",1)]),
 },
 "freestack":{
  "terminal": f_receipt("THE OLD DESK","WHAT FULL PRICE BUYS",[("Market terminal","a rent, yearly"),("Ad audits","an agency, monthly"),("Every AI model","a seat, per user")],"The open twins","zero"),
  "agencyfee": f_rows("","The paid list","OPEN TWINS EXIST",[row("Terminal + charts","open clone, same feeds",chip="free"),row("Ad audit script","runs daily, yours",chip="free"),row("Model router","one app, all models",chip="free"),row("Inbox triage","reads and replies",chip="free")]),
  "catch": f_console("The catch","FREE LIKE A PUPPY",[("Setup + updates","your weekends",False),("Breakage","your 2am",False),("No memory, no gate","your risk",False)],buttons=False),
  "glue": f_rings("THE GLUE",[("Ten free tools","eleven new jobs"),("Each one alone","logged out, forgetting you"),("The glue","is the actual product")],"nobody ships the glue: that is the whole gap"),
  "layer": f_browser("one desk &middot; the whole stack",hd("The layer","ASSEMBLED, NOT COLLECTED")+row("Mail + docs + CRM","wired, one memory",chip="live")+row("The free gems","plugged in, gated",chip="live")+row("Runs overnight","digest at 07:00",chip="live")),
  "meter": f_dial(78,"THE METER","cents","per run, not per seat","high bills only live in the old stack"),
  "keep": f_keys([("FREE GEMS","WIRED INTO THE DESK",False),("YOUR TAP","ON EVERY SEND",True)]),
  "math": f_bubble("Knowledge is the discount. Assembly is the price.","The spread","YOURS TO KEEP","audit my stack",A),
 },
 "no120":{
  "hoard": f_battery(3,"OF THE HOARD EVER REOPENED","four prompts out of 120 &middot; the cheat sheet is a filing cabinet, not a system"),
  "rot": f_chartline("Prompt decay","THE HALF-LIFE",[100,84,66,48,34,22,14,8],"magic words rot when models change: skills get versioned and corrected"),
  "retype": f_paper("Every single use","THE HIDDEN TAX","Paste. Tweak. Re-word. Hope.",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">The 120 need you</div><div class="rs" style="color:#8a7a5e">every time they run</div></div><span class="chip">Tell</span></div>'),
  "twelve": f_podium([("120","saved",0),("30","tried",0),("4","reopened",0),("12","installed",1),("1","desk",1)]),
  "oneline": f_env("THE COMPRESSION","/audit my funnel","A page of instructions lives inside the skill. You type five words.","Play run"),
  "runs": f_split("SKILLS",["Fire on triggers","Run overnight","Compose with each other"],"PROMPTS",["Wait for you","Sleep when you sleep","Live in a notebook"]),
  "gate": f_vault("TAP","AUTONOMOUS INSIDE, YOURS OUTSIDE"),
  "purge": f_ticket("The purge","ONE AFTERNOON",tick_cells([("SAVE","None",1),("DELETE","120",1),("MINT","12",1),("WIRE","Gate",1),("RUN","Daily",0)]),"NOTEBOOK EMPTY, DESK FULL","THE RE-TYPING IS OVER"),
 },

 "modelwars":{
  "cycle": f_calendar("The launch cycle","A KING A WEEK",[("M",None),("T","GPT"),("W",None),("T",None),("F","GLM"),("S",None),("S",None),("8",None),("9","GEM"),("10",None),("11","NEW"),("12",None),("13",None),("14","NEXT")],"benchmark, hype thread, migration guide, repeat"),
  "switchers": f_metro("One founder, one year","FOUR STACK MOVES",[("March","moved for the benchmark",1),("June","moved for the thread",1),("September","moved back",1),("Pipeline","never noticed",0)]),
  "truth": f_split("THE MODELS",["Within points","Trade places weekly","Converging fast"],"THE SYSTEMS",["Miles apart","Compound monthly","The actual moat"]),
  "router": f_keys([("LITE","LOOKUPS",False),("SMART","THE DAILY WORK",True),("DEEP","JUDGEMENT ONLY",False)]),
  "assets": f_folder("What never expires","SURVIVES EVERY LAUNCH",[row("icp.md","who you sell to",chip="yours"),row("voice.md","how you sound",chip="yours"),row("rules.md","every correction, kept",chip="yours")]),
  "upgrade": f_env("LAUNCH DAY","A new model lands.","The router adopts it under the hood. Same commands, same memory, better engine.","Upgraded"),
  "cost": f_receipt("MODEL CHASING","THE PART-TIME JOB",[("Reinstalling","evenings"),("Re-prompting","weekends"),("Re-learning quirks","weeks")],"Revenue touched","zero"),
  "position": f_podium([("HYPE","weekly",0),("BENCHES","noisy",0),("MODELS","fight",0),("ROUTER","picks",0),("YOU","own the layer",1)]),
 },
 "dayone":{
  "teach": f_env("PLAY 1 &middot; MINUTE 10","/init my business","One interview: ICP, offer, pricing, no-list. Every answer after gets sharper.","Memory born"),
  "read": f_browser("first research run &middot; live",hd("Play 2","READ BEFORE IT SPEAKS")+row("20 accounts","profiled against YOUR customer",chip="scored")+row("Top 5","hiring, raising, moving now",chip="warm")+row("Briefs","one page each, sourced",chip="done")),
  "voice": f_paper("Play 3","FEED IT YOUR VOICE","Paste your five best posts",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Voice locked</div><div class="rs" style="color:#8a7a5e">every draft sounds like you on a good day</div></div><span class="chip">Set once</span></div>'),
  "chore": f_console("Play 4","ONE CHORE, ONE TRIGGER",[("Follow up quiet leads","fires daily",True),("Exit conditions","set, no zombies",True),("Every send","parked for your tap",True)],buttons=False),
  "digest": f_badge(LOCK,"1","Play 5: your first digest.","everything done, everything parked, tomorrow queued"),
  "hour": f_odo(["6","0"],0,"MINUTES, ALL FIVE PLAYS","not a course, not a certification: one hour on the desk"),
  "trap": f_stamp("The trap","PLAY ONE SKIPPED","every disappointment traces here",[("Generic context","generic drafts"),("Weak briefs","weak calls"),("The fix","redo the interview")],"REDO IT"),
  "curve": f_chartline("After day one","IT ONLY COMPOUNDS",[15,24,36,50,63,77,89,100],"corrections become rules, rules become skills, weekly"),
 },
 "neverhire":{
  "leadgen": f_rows("","Role 1: lead gen","FROZEN, ABSORBED",[row("Sourcing","overnight, on your ICP",chip="CORTEX"),row("Scoring","against real customers",chip="CORTEX"),row("Briefing","one page per account",chip="CORTEX"),row("The job posting","never went up",chip="frozen")]),
  "support": f_console("Role 2: support triage","FIRST REPLY IN SECONDS",[("Inbox read + sorted","every message",True),("Replies drafted","waiting for your tap",True),("Hard cases","escalate with context",True)],buttons=False),
  "content": f_calendar("Role 3: content ops","NEVER MISSES MONDAY",[("M","POST"),("T","POST"),("W",None),("T","DECK"),("F","POST"),("S",None),("S",None),("8","POST"),("9","REEL"),("10","POST"),("11",None),("12","NEWS"),("13",None),("14","POST")],"14 slots from one line &middot; 10:00 local"),
  "followups": f_pills([row("Quiet 3 days","chased on the trigger",chip="gated"),row("Post-call","recap drafted same hour",chip="gated"),row("Post-invoice","politely persistent",chip="gated")]),
  "reviews": f_env("ROLE 5 &middot; REVIEWS","Asked at the right moment.","Timed after the win, chased politely, logged where you see it.","Collected"),
  "math": f_stat("5","salaries that stayed in the company &middot; systems run around the clock",[30,42,55,66,78,90,100]),
  "line": f_split("FREEZE",["Everything repetitive","Everything on a checklist","Everything overnight"],"HIRE",["Taste and judgement","Relationships","The closing call"]),
  "test": f_bubble("Would a checklist do this job? Then it is a flow, not a hire.","The test","BEFORE EVERY POSTING","freeze one role",A),
 },
 "boring":{
  "window": f_dial(17,"THE WINDOW","1.7s","per post, scrolling","safe and predictable beats smart and subtle, every time"),
  "proof": f_split("CLEVER",["Asymmetric distribution","Optimised organic reach","800 views"],"BORING",["Post daily for 30 days","Watch what happens","47,000 views"]),
  "rules": f_folder("The rulebook","THE WHOLE RELIGION",[row("One idea","per post, exactly one",chip="rule"),row("Plain words","a 12-year-old gets it",chip="rule"),row("Known format","payoff visible in 2s",chip="rule")]),
  "ego": f_keys([("CLEVER","FOR YOUR EGO",False),("BORING","FOR THEIR SCROLL",True)]),
  "fourtest": f_ticket("Before every post","THE 4-SECOND TEST",tick_cells([("2S","Point",1),("ONE","Idea",1),("DAD","Gets it",1),("FEED","Knows it",1),("SHIP","Or redo",0)]),"FAIL ONE, REWRITE","PASS FOUR, POST"),
  "skill": f_browser("drafts &middot; ranked before review",hd("The desk","RUNS THE TEST FOR ME")+row("Draft A","one idea, plain, 2s payoff",chip="92")+row("Draft B","two ideas, split it",chip="74")+row("Draft C","clever, rewritten",chip="61")),
  "client": f_chartline("One switch","2K TO 30K IN 25 DAYS",[7,9,12,16,21,26,30],"one trade idea per post instead of technical essays: same expertise"),
  "reframe": f_stamp("The reframe","BORING, DEFINED","legible at scroll speed",[("Low value","no"),("Plain delivery","yes"),("Expert core","intact")],"SIMPLE"),
 },
 "loweffort":{
  "pitch": f_pills([row("Faceless clips","the guru starter pack",chip="sold"),row("Recycled quotes","ten minutes a day",chip="sold"),row("Template farms","drowning the feed",chip="sold")]),
  "catchg": f_gauge(9,"REACH","the template ceiling","audiences smell recycled: recycled content gets recycled reach"),
  "reframe2": f_split("EFFORT AS INPUT",["Grind every post","Improvise daily","Burn out by March"],"EFFORT AS SYSTEM",["Build once, heavy","Post light, daily","Compound by March"]),
  "heavy": f_shelf("Build once","THE HONEST WEEKEND",[("Your voice","sampled from your best posts","set"),("Your hook bank","stocked, three angles per idea","set"),("Your cadence","wired to 10:00 local","set")]),
  "light": f_env("THEN, DAILY","One line and one tap.","The desk plans, drafts to your bar, queues. You approve from your phone.","Ten minutes"),
  "difference": f_podium([("SKIP","guru way",0),("RECYCLE","farm",0),("PLATEAU","ceiling",0),("SYSTEM","front-load",1),("COMPOUND","fly",1)]),
  "receipts": f_rows("","The receipts","LIGHT HANDS, HEAVY SYSTEM",[row("14 posts a week","from one planning line",chip="live"),row("Every draft","in my voice, my niche",chip="live"),row("Every one","passes the boring test first",chip="live"),row("My daily cost","ten real minutes",chip="live")]),
  "verdictl": f_bubble("Work hard once. Post easy forever.","Low effort","THE HONEST VERSION","front-load my desk",A),
 },

 "wrongaisle":{
  "aisle": f_rows("","The plugin aisle","WRITTEN FOR ENGINEERS",[row("Repo knowledge graphs","impressive, irrelevant",strike=True,chip="toy"),row("Code navigators","for codebases you do not have",strike=True,chip="toy"),row("God-node detectors","genuinely cool, still a toy",strike=True,chip="toy"),row("Your quarter","unmoved by all three",chip="fact")]),
  "tell": f_keys([("COOL DEMO","NO REVENUE PATH",False),("NAMED OUTCOME","INSTALL IT",True)]),
  "flip": f_shelf("The founder aisle","DESKS, NOT TOOLS",[("Research + outbound","briefs in, replies out","desk"),("Deals + content","proposals and posts, your voice","desk"),("Paperwork","contracts read, risks flagged","desk")]),
  "deskcheck": f_pills([row("CORTEX","what lands: briefs",chip="named"),row("SPECTER","what lands: replies",chip="named"),row("STRIKER","what lands: closes",chip="named")]),
  "stackp": f_podium([("INTEL","desk",0),("REACH","desk",0),("DEALS","desk",0),("PAPER","desk",0),("YOU","the gate",1)]),
  "testrun": f_ticket("The 48 hours","EARN THE SLOT",tick_cells([("H0","Install",1),("H12","20 briefs",1),("H24","10 drafts",1),("H48","1 proposal",1),("ELSE","Uninstall",0)]),"DEMAND A RECEIPT","NO RECEIPT, NO SLOT"),
  "trapb": f_console("Ten plugins later","STILL DRAFTING ALONE",[("Graph mapper","running, pretty",True),("Repo navigator","running, unused",True),("Your follow-ups","still hand-written",False)],buttons=False),
  "rule7": f_stamp("The rule","SHOP BY OUTCOME","the plugin page is the tell",[("Shows code","wrong aisle"),("Shows pipeline","install"),("Shows demos","walk away")],"BUY DESKS"),
 },
 "selflearn":{
  "amnesia7": f_battery(2,"WHAT IT REMEMBERS TOMORROW","task done, context dead, same mistakes queued for the morning"),
  "tax": f_receipt("THE FORGETTING TAX","PAID IN ATTENTION",[("Same correction","40th time"),("Same context","re-pasted daily"),("Same disappointment","weekly")],"Your patience","drained"),
  "looplearn": f_metro("The learning loop","EVERY CYCLE",[("Evaluate","grades its own output",1),("Reflect","writes what went wrong",1),("Store","files the lesson",1),("Apply","next run starts smarter",0)]),
  "file7": f_folder("The file","YOUR FEEDBACK, KEPT",[row("rules.md","no discounts: said once",chip="forever"),row("style.md","the fix that generalized",chip="forever"),row("filters.md","who we never pitch",chip="forever")]),
  "curve7": f_chartline("The curve","RUN 1 TO RUN 100",[38,46,55,64,73,82,91,100],"same flow, months later: writes like you, prices like you, filters like you"),
  "proof7": f_odo(["3","4"],0,"RULES IN MY NO-LIST","each from a single correction that never needed repeating"),
  "gate7": f_vault("TAP","IT LEARNS ALONE, SENDS WITH YOU"),
  "question7": f_bubble("If it cannot remember you, why are you training it daily?","The bar","MEMORY BEFORE IQ","test its memory",A),
 },
 "carouselcode":{
  "myth7": f_split("EIGHT MONTHS AGO",["Prettier templates","Smarter phrasing","Zero movement"],"EIGHT MONTHS LATER",["Five patterns","Same effort","Growth as consequence"]),
  "pat1": f_env("PATTERN 1 &middot; THE COVER","One promise. No cleverness.","Its only job is the next slide. Doormen do not do poetry.","Swiped"),
  "pat2": f_pills([row("One beat per page","two ideas is one too many",chip="rhythm"),row("Cut the second point","move it to its own slide",chip="rhythm"),row("The swipe cadence","is the retention",chip="rhythm")]),
  "pat3": f_rings("THE OPEN LOOP",[("Slide two","opens the tension"),("The middle","carries it"),("The last page","closes it")],"they finish because something is unresolved"),
  "pat4": f_paper("Pattern 4","THE SAVE PAGE","One page they will need again",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">The list, the test, the map</div><div class="rs" style="color:#8a7a5e">saves are the algorithm</div></div><span class="chip">Built in</span></div>'),
  "grade7": f_ticket("The review","THIRTY SECONDS",tick_cells([("COVER","Promise",1),("BEAT","One/page",1),("LOOP","Open",1),("SAVE","Page in",1),("CTA","One",1)]),"FIVE BOXES PER POST","GROWTH AS A CHECKLIST"),
  "desk7": f_browser("drafts &middot; patterned by default",hd("PULSE","BUILDS TO THE CODE")+row("Cover","one promise, graded",chip="pass")+row("Pages","one beat each",chip="pass")+row("Save page","built in, always",chip="pass")),
  "payoff7": f_stat("8","months of posting to crack it &middot; five patterns, zero luck",[22,30,38,50,62,80,100]),
 },
 "onetool":{
  "list7": f_pills([row("Inbox tool","one slice of your day",chip="login 1"),row("Calendar tool","another slice",chip="login 2"),row("Meeting + note tools","two more bills",chip="3 and 4")]),
  "seams": f_rows("","The seams","NOBODY KNOWS ANYBODY",[row("Inbox tool","cannot see the deal",strike=True,chip="blind"),row("Meeting tool","never met your pipeline",strike=True,chip="blind"),row("Note tool","writes to nowhere",strike=True,chip="blind"),row("The integration","is you, at 23:00",chip="truth")]),
  "cost7": f_gauge(8,"CONTEXT","retained across five tools","you re-explain yourself to software all day"),
  "desk7b": f_shelf("One desk","ONE MEMORY UNDER ALL",[("Inbox","read, drafted, in your voice","wired"),("Calendar","booked, protected, briefed","wired"),("Pipeline","moved on every reply","wired")]),
  "compound7": f_metro("The thread","CONTEXT COMPOUNDS",[("The follow-up","references the call",1),("The call","references the deal",1),("The deal","references the history",1),("Tool five","references nothing",0)]),
  "sleep7": f_console("The night shift","UNIFIED",[("23:00 triage","inbox cleared",True),("06:00 drafts","in your voice",True),("07:00 digest","parked for your tap",True)],buttons=False),
  "price7": f_dial(74,"THE BILL","one","meter, cents per run","five subscriptions became a single line"),
  "rule7b": f_stamp("The filter","BEFORE TOOL SIX","one question kills the listicle",[("Shares memory","welcome"),("Brings its own silo","declined"),("Needs a sixth login","declined")],"MEMORY OR NOTHING"),
 },
 "oneskill":{
  "mythos": f_split("THE HUNT",["New skill, new course","New niche, new reset","Zero compounding"],"THE RESHAPE",["One skill you own","Five income shapes","Each feeds the next"]),
  "service": f_paper("Shape 1","THE SERVICE","Your skill, done for them",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Highest price, first cash</div><div class="rs" style="color:#8a7a5e">the desk briefs, delivers, chases</div></div><span class="chip">Sell it</span></div>'),
  "product": f_shelf("Shape 2","PACKAGED ONCE",[("Templates","from your own workflow","auto"),("Audits","your checklist, productized","auto"),("Systems","your process, boxed","auto")]),
  "contents": f_browser("your feed &middot; proof in public",hd("Shape 3","CONTENT")+row("Client work","turned into daily posts",chip="PULSE")+row("Your voice","sampled, locked",chip="PULSE")+row("Shapes 1 + 2","sold by shape 3",chip="flywheel")),
  "teaching": f_ticket("Shape 4","THE METHOD, PRICED",tick_cells([("W1","Frame",1),("W2","Cases",1),("W3","Reps",1),("W4","Review",1),("RUN","Cohort",0)]),"YOUR PROCESS, STRUCTURED","BY THE DESK THAT RUNS IT"),
  "tool5": f_badge(PLANE,"1","Your method, shipped as a skill.","no code: your judgement, packaged and runnable"),
  "engine5": f_rings("ONE DESK",[("Service + product","same memory"),("Content + teaching","same voice"),("The tool","same gate")],"five incomes, one login, zero context lost"),
  "order5": f_chartline("The sequence","EACH SHAPE FUNDS THE NEXT",[18,26,40,52,68,84,100],"service first for cash, tool last for scale: sequence beats ambition"),
 },

 "firstpass":{
  "chatbox": f_split("THE CHAT BOX",["One prompt at a time","One person typing","Nine roles unfilled"],"THE ORG CHART",["Ten roles installed","Working in parallel","One human on top"]),
  "roster": f_rows("","The roster","REAL JOBS, NOT NICKNAMES",[row("Researcher + analyst","reads, scores, briefs",chip="skill"),row("Editor + art director","drafts and visuals, your bar",chip="skill"),row("Deck builder + CRM lead","proposals and pipeline",chip="skill"),row("Media + video + SEO","distribution, prepped",chip="skill")]),
  "split8": f_keys([("IT DRAFTS","THE VOLUME WORK",False),("YOU DECIDE","THE JUDGEMENT",True)]),
  "morning": f_badge(LOCK,"9","Nine first passes, waiting at 07:00.","your day starts at the decision layer"),
  "craft": f_podium([("TYPE","before",0),("SORT","before",0),("DRAFT","before",0),("DIRECT","now",1),("DECIDE","now",1)]),
  "skillmaker": f_env("THE SKILL MAKER","Spot a repeated job.","One roster skill mints new skills: on the org chart by Friday.","Minted"),
  "line8": f_vault("FINISH","ALWAYS HUMAN, ALWAYS YOURS"),
  "result8": f_stat("3x","throughput, same headcount &middot; the grind layer does itself",[34,46,58,70,82,92,100]),
 },
 "studyyou":{
  "archive": f_folder("The archive","TRAINING DATA YOU OWN",[row("50 winning posts","sitting in your profile",chip="unused"),row("Their numbers","reach, saves, replies",chip="attached"),row("Their patterns","waiting to be read",chip="goldmine")]),
  "extract": f_browser("your top posts &middot; collected",hd("The extract","EVERY WINNER, DATED")+row("Post + metrics","pulled as pairs",chip="done")+row("Sorted by saves","the honest ranking",chip="done")+row("Corpus ready","for the autopsy",chip="done")),
  "autopsy": f_split("MY TASTE SAID",["Long storytelling","Clever framing","Polished endings"],"THE DATA SAID",["Short openers","One number per post","Questions that end"]),
  "distill": f_stamp("The distill","FINDINGS TO PLAY","not notes: an installed skill",[("Patterns","extracted"),("Rules","written"),("Every future draft","runs them")],"EXECUTABLE"),
  "fifty1": f_paper("The 51st post","MY BEST DAY, ON DEMAND","Drafted against my own winners",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Ranked before I saw it</div><div class="rs" style="color:#8a7a5e">me, on repeat</div></div><span class="chip">Post</span></div>'),
  "refresh": f_calendar("The refresh","MONTHLY RERUN",[("M",None),("T",None),("W",None),("T",None),("F",None),("S",None),("S",None),("1","STUDY"),("2",None),("3",None),("4",None),("5",None),("6",None),("7",None)],"new winners join the corpus: the skill updates itself"),
  "moat8": f_rings("YOUR ARCHIVE",[("Generic AI","writes averages"),("This skill","writes from evidence"),("The evidence","only you own it")],"nobody can copy your history"),
  "order8": f_metro("The order","OPERATORS REVERSE IT",[("Study","the archive first",1),("Distill","patterns to a skill",1),("Generate","from evidence",1),("Ask AI to write","the amateur order",0)]),
 },
 "proofstack":{
  "trapd": f_receipt("THE DEMO PORTFOLIO","WHAT IT EARNED",[("Tutorial agent","12 stars"),("Portfolio repo","3 forks"),("Recruiter DMs","two, polite")],"Deposits","zero"),
  "build1": f_console("Build 1: lead machine","LIVE IN A WEEKEND",[("Sources your ICP","nightly",True),("Briefs every account","one page",True),("Openers","parked for your tap",True)],buttons=False),
  "build2": f_metro("Build 2: follow-up loop","ZERO DROPPED THREADS",[("On silence","fires the chase",1),("On reply","drafts the answer",1),("On close","logs to the pipe",1),("On you","one tap",0)]),
  "build3": f_pills([row("14 posts a week","from one planning line",chip="build 3"),row("Your voice","sampled, locked",chip="build 3"),row("Every send","gated",chip="build 3")]),
  "stack8": f_shelf("The stack","EACH FEEDS THE NEXT",[("Content desk","warms the leads","feeds"),("Lead machine","fills the loops","feeds"),("Follow-up loop","closes the deals","feeds")]),
  "receipts8": f_chartline("The receipts","IN MONEY TERMS",[12,20,30,42,56,72,88,100],"briefs became calls, threads became invoices, posts became inbound"),
  "time8": f_odo(["3"],0,"EVENINGS, ALL THREE BUILDS","plain English in, assembled by the desk, tested on your real pipeline"),
  "filter8": f_keys([("INVOICE","A CLIENT WOULD PAY",True),("HOBBY","LABEL IT HONESTLY",False)]),
 },
 "tokendiet":{
  "leak": f_gauge(24,"THE METER","habits, not prices","same tool, same work: one founder pays cents, another pays multiples"),
  "habit1": f_env("HABIT 1","Clear between tasks.","Dragging yesterday into today makes every answer heavier and worse.","Fresh slate"),
  "habit2": f_dial(60,"THE TIER","smart","for the daily work","light for lookups, deep only where judgement pays"),
  "habit3": f_rows("","Habit 3","SIGNAL, NOT BULK",[row("Raw logs","summarized before reading",chip="filtered"),row("Data dumps","key rows only",chip="filtered"),row("Long threads","the last turn, distilled",chip="filtered"),row("Whole-file swallowing","the expensive habit",strike=True,chip="cut")]),
  "habit4": f_paper("Habit 4","THE LEAN FILE","Short memory beats bloated memory",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Trim monthly</div><div class="rs" style="color:#8a7a5e">cost and quality move together</div></div><span class="chip">Lean</span></div>'),
  "habit5": f_ticket("Habit 5","BUNDLE, THEN FIRE",tick_cells([("COLLECT","10 asks",1),("BUNDLE","One run",1),("FIRE","Once",1),("REVIEW","Once",1),("REPEAT","Weekly",0)]),"TEN TINY ASKS COST MORE","THAN ONE STRUCTURED PASS"),
  "autopilot": f_console("On the desk","DISCIPLINE BY DEFAULT",[("Router tiers","every single turn",True),("Context resets","per task",True),("Spend caps","on every flow",True)],buttons=False),
  "reframe8": f_bubble("The habits that cut cost are the ones that raise quality.","The discipline","PAYS TWICE","check my habits",A),
 },
 "brandguard":{
  "drift": f_fan("The drift","TEN SHADES OF YOU",[row("Monday deck","one blue, one font",chip="drift"),row("Wednesday post","another blue",chip="drift"),row("Friday proposal","a third, bolder",chip="drift")]),
  "tokens": f_folder("The tokens","YOUR LOOK, AS LAW",[row("colors.tokens","the exact palette",chip="law"),row("type.tokens","faces and sizes",chip="law"),row("logo.rules","where and never-where",chip="law")]),
  "pack": f_browser("the component pack &middot; on-brand by birth",hd("822 pieces","NEVER FROM SCRATCH")+row("Cards + heroes","assembled, obedient",chip="pack")+row("Charts + covers","same family",chip="pack")+row("New asset","minutes, not briefs",chip="pack")),
  "outputs": f_split("BEFORE",["Every asset negotiates","Ten shades of you","Review cycles"],"AFTER",["One token file rules","One visual family","Zero drift fixes"]),
  "speed8": f_chartline("The unlock","FAST BECAME CORRECT",[20,32,44,58,70,84,100],"no review cycles, no drift fixes: the quick version is the right one"),
  "gate8": f_stamp("The gate","APPROVE PATTERNS","not pieces",[("New template","one blessing"),("Every instance","inherits it"),("Your time","spent once")],"BLESSED"),
  "cost8": f_receipt("THE OLD WAY","DESIGN AS A BILL",[("Retainer","monthly"),("Rush fees","surprise"),("Revisions","two rounds each")],"This way","a token file"),
  "test8": f_badge(LOCK,"2","Screenshot any two assets.","if a stranger cannot tell the company, it works"),
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
