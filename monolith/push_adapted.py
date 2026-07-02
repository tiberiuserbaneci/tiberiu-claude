#!/usr/bin/env python3
# Push adaptari IG Scraped: 2 randuri noi per material (TikTok tag ["TikTok"], IG tag ["IG Scraped"]),
# caption kit per canal (S15.6 + S30 TikTok mechanic), apoi STERGE randul-sursa "Scraped ·"
# (operator: "raman doar cele adaptate"). Usage: python3 push_adapted.py <slug> ...
import os, sys, json, time, glob, uuid, ssl, urllib.request
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; BUCKET="ultron-reels"
ME="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; CA="/root/.ccr/ca-bundle.crt"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method)
    r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    with urllib.request.urlopen(r,context=ctx,timeout=120) as resp: return resp.read()
def r2put(key,path):
    for att in range(5):
        try:
            req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",open(path,"rb").read(),"image/png"); return
        except Exception:
            if att==4: raise
            time.sleep(2**att)
def d1(sql,params=None):
    body={"sql":sql}
    if params: body["params"]=params
    for att in range(6):
        try:
            out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps(body).encode(),"application/json"))
            break
        except urllib.error.HTTPError as e:
            if e.code!=429 or att==5: raise
            time.sleep(3*2**att)
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

H="#claude #ai #founder #startup #buildinpublic"

# slug -> (TITLE, keyword(pastila), resurse DM, src_prefix de sters, tiktok_body, ig_body, first_comment_ig)
KITS={
 "aios":("THE AI OPERATING SYSTEM","OPERATOR","the AI OS setup map","263c2cda",
  "Most founders rent tabs that forget them at midnight.\n\nOperators run an OS: one memory, one command center, agents on triggers.\n\nNow I type one sentence and 200 accounts are briefed before coffee.\n\nEvery correction becomes a rule. The system compounds while the tabs reset.\n\nStop running your company from a chat window that has amnesia.",
  "Your AI forgets you the second the tab closes. That is the bottleneck, not the model.\n\nThe fix is an operating system: one permanent memory, agents that run on triggers, a command center that is yours, not rented.\n\nThis morning it read 1,284 leads and briefed 200 accounts from one typed sentence.\n\nNothing external fires without my tap. Power, gated.",
  "Rented tabs forget. Owned systems compound.\n\nDrop OPERATOR below and I will DM you the AI OS setup map, plus where the memory layer lives.\n\nSave this if your AI still asks who you are."),
 "loops":("PROMPTS ARE DEAD, LOOPS RUN","BUILDER","the loop playbook","6bf71ba3",
  "You are still typing prompts. The top operators set goals with exits.\n\nA loop runs on a trigger, checks its own work and reports when done.\n\nLast week: 212 cycles. I typed three sentences.\n\nOne trap: a loop without a checker burns budget in silence. Ultron caps every flow.\n\nScale past your hours, not into them.",
  "Prompt after prompt is working backwards: you are the cron job.\n\nAn Ultron flow takes one goal in plain English, runs on a trigger, verifies each cycle and reports when done.\n\n212 cycles ran last week from three typed sentences.\n\nEverything external still parks on HOLD for my tap. Loops run free, sends do not.",
  "The whole setup is one sentence: follow up every lead quiet for 3 days.\n\nDrop BUILDER below and I will DM you the loop playbook with the checker and exit rules.\n\nSave this before you type your next prompt."),
 "aibody":("THE COMPLETE AI BODY","FOUNDER","the full operator stack map","0a3c53ce",
  "Most founders rent one mouth: a chatbot that answers.\n\nOperators wire the whole body. The router thinks, CORTEX reads the market, PULSE speaks in your voice, SENTINEL ships product, one memory keeps it alive.\n\nEvery external move still waits for your tap.\n\nAugmented, not replaced. That is the difference.",
  "A chatbot answers questions. A body does work.\n\nInside Ultron: the router is the brain, CORTEX the eyes on 1,284 companies, PULSE the voice sampled from your posts, SENTINEL the hands that ship, one memory as the heart.\n\nYou hold the reins: nothing external fires without your tap.",
  "Brain, eyes, voice, hands, heart. One login.\n\nDrop FOUNDER below and I will DM you the full operator stack map, organ by organ.\n\nSave this if you are still typing into one mouth."),
 "fivesigns":("5 SIGNS YOU NEED AI NOW","FOUNDER","the 5-signs checklist + first-flow guide","fa7eedb6",
  "Same questions answered daily. Data moved by hand. Everything waiting on you. Leads waiting hours. Reports taking days.\n\nEvery yes is a leak. Five yes answers is not a staffing problem, it is missing systems.\n\nStart with the worst leak. One sentence sets up the flow. The gate keeps your tap on everything.\n\nScore yourself before you hire again.",
  "Most businesses do not need more employees. They need fewer repetitive tasks.\n\nThe five signs: repeat questions, copy-paste bridges between apps, approval bottlenecks, slow first replies, month-end reports that take days.\n\nUltron fixes them one flow at a time, and every customer-facing step still parks for your tap.",
  "Count your yes answers. Every one is a leak that a flow can plug this week.\n\nDrop FOUNDER below and I will DM you the 5-signs checklist plus the first-flow setup guide.\n\nSave this and score your own business tonight."),
 "contentdesk":("THE 500K CONTENT DESK","OPERATOR","the 5-skill content desk setup","5af9c9ec",
  "A content team used to mean five salaries and a Monday meeting.\n\nMine is five skills in one chat: the calendar plans itself, hooks rotate from my bank, drafts land in my voice, one brief becomes five formats, newsletters hit 99.2% inbox.\n\nNothing posts without my tap.\n\nThe desk is metered in cents, not salaries.",
  "Five skills run my whole content desk from one chat.\n\nThe calendar plans 14 slots from one line. Hooks come in three angles, I pick the winner. Drafts arrive in my voice, ranked. One brief becomes five native formats. Newsletters land at 99.2%.\n\nEvery draft parks for my tap before it posts.",
  "Planner, writer, designer, distributor: one subscription, no meetings.\n\nDrop OPERATOR below and I will DM you the 5-skill content desk setup.\n\nSave the desk and steal the pipeline."),

 "unstuck":("STUCK AT LEVEL ONE","BUILDER","the 5-level climb map","2ba8c438",
  "Chat. Close tab. Repeat. That is level 1, and most founders never leave it.\n\nLevel 2 gives it a memory. Level 3 runs real jobs. Level 4 ships product. Level 5 runs with the laptop off.\n\nThe gap is not smarts. It is knowing the next level exists.\n\nEvery level up keeps your tap on everything external.",
  "Almost everyone stops at level 1 with AI: ask, copy, close.\n\nThe climb inside Ultron: a memory that survives, agents that run jobs, builds that ship, routines that fire with the laptop shut.\n\nAutonomy grows, your control does not shrink. The gate holds every external move.",
  "Five levels, one chat. Most founders sit at 2 without knowing 3 exists.\n\nDrop BUILDER below and I will DM you the 5-level climb map with the first move per level.\n\nSave the map and be honest about your level."),
 "hidden":("THE HIDDEN SKILLS","OPERATOR","the skills + connectors starter list","406038b6",
  "You do not need better prompting. You need installed capability.\n\nProposals build themselves. Reports carry live numbers. Contracts get redlined. Assets assemble from your own pack.\n\nWired into mail, CRM, calendar and payments, it acts inside your tools.\n\nA chatbot answers. This executes, and sends only on your tap.",
  "The secret to Claude was never phrasing. It is skills and connectors.\n\nInside Ultron: decks in your tokens, reports with sources, NDAs redlined by COUNSEL, visuals from 822 Crescendo components, all wired into your real stack.\n\nExecutor, not assistant. Gated by your tap.",
  "Prompters re-word. Operators install.\n\nDrop OPERATOR below and I will DM you the skills and connectors starter list, in install order.\n\nSave this before you rewrite another prompt."),
 "carouselcmd":("THE CAROUSEL COMMAND","OPERATOR","the carousel command setup","733d81bd",
  "The designer retainer is dead. One line now starts the whole deck.\n\nPULSE interviews you for the angle, generates visuals in your tokens, assembles ten pages and ships the caption kit with it.\n\nBrief to done in minutes. The deck parks for your tap before it posts.\n\nThe retainer becomes runway.",
  "Paying a designer per carousel is over.\n\nOne line in: PULSE takes the angle, builds ten on-brand pages from your own component pack and delivers the caption kit with hashtags and first comment.\n\nYou review once, tap, done. Metered in cents.",
  "Brief, visuals, slides, captions: minutes, not a week.\n\nDrop OPERATOR below and I will DM you the carousel command setup end to end.\n\nSave this before your next design invoice."),
 "patterns":("HOW REAL AGENTS ARE BUILT","BUILDER","the 6-pattern architecture map","1c1cee10",
  "Agents do not fail. Their design does.\n\nThe patterns that ship: reason before acting, actions as real work, plan expensive execute cheap, draft-critique-refine, specialists with handoffs.\n\nThe sixth pattern is the human gate: one person on the only external trigger.\n\nSame models, better design, a workforce.",
  "Most agent failures are design failures.\n\nInside Ultron: agents reason before every tool call, SENTINEL executes real work, the router plans deep and runs light, drafts are ranked before you see them, seven specialists hand off cleanly.\n\nAnd pattern six: your tap on everything external.",
  "Five build patterns plus the one nobody lists: the human gate.\n\nDrop BUILDER below and I will DM you the 6-pattern architecture map.\n\nSave this before you build another 100-node automation."),
 "setup":("60 MINUTES TO AN OPERATOR","FOUNDER","the 60-minute setup checklist","44e61328",
  "One hour of setup buys a coworker forever.\n\nMinute 10: stack connected. Minute 20: /init my business. Minute 30: voice locked. Minute 40: the gate set. Minute 50: first real task done. Minute 60: your first digest.\n\nEvery session after gets smarter on its own.\n\nBlock the hour.",
  "Sixty minutes, six steps: connect the stack, /init my business, teach it your voice, lock the gate, run the first task, read the first digest.\n\nBy minute 60 you did not set up a tool. You hired a coworker that knows your business.\n\nCorrections become rules. It compounds from day one.",
  "Hour one is setup. Year one is leverage.\n\nDrop FOUNDER below and I will DM you the 60-minute checklist, minute by minute.\n\nSave it and block the hour this week."),

 "verified":("I CHECKED THE LISTS","OPERATOR","the verified skills shortlist","f276e654",
  "Everyone posts 50-skill lists. Nobody installs them.\n\nI installed every single one and ran them on real work for a week.\n\nA third were fakes: dead links, renamed duplicates, skills that answer instead of execute.\n\nThe survivors fit on one shortlist, grouped by job, starting with the two Anthropic built.\n\nIf it cannot execute, it does not count.",
  "The skill lists flooding your feed have zero receipts behind them.\n\nSo I tested the flood: every skill installed, every one run on real briefs, drafts and builds for a week.\n\nA third were made up. The keepers fit on one page, and Ultron ships them pre-verified in the techniques library.\n\nMy desk now runs on 12 survivors, daily.",
  "Fifty skills per list. Twenty-four actually run. Twelve earned a slot on my desk.\n\nDrop OPERATOR below and I will DM you the verified shortlist in safe install order.\n\nSave this before you install from another random list."),
 "fivepaid":("THE 5 SKILLS THAT PAY","FOUNDER","the 5-skills starter map","2a84f6ff",
  "Everyone asks which AI skills to learn. Wrong list, every time.\n\nLearn what businesses already pay for: research that closes, outbound that lands, content in a voice, builds without builders, systems that keep running.\n\nPick exactly one and go deep. Your first client is your own company.\n\nThe meter runs in cents while you practice. The invoice runs high when you deliver.",
  "The five AI skills businesses already pay for, in order:\n\nResearch that turns cold calls warm. Outbound that actually inboxes. Content in a voice clients recognize. Builds that go live from plain English. Systems that run on triggers.\n\nOne skill run daily inside Ultron beats five certificates on a shelf. Run it on your own pipeline first: the receipts become the pitch.",
  "Cents to practice. Real money to sell. That spread is the whole opportunity.\n\nDrop FOUNDER below and I will DM you the 5-skills starter map with the first move for each.\n\nSave this and pick your one tonight."),
 "installs24":("THE POWER USER SETUP","BUILDER","the power user install list","65e782c5",
  "Your AI is running on stock settings. That is the floor, not the product.\n\nPlugins turn it into desks: research, content, deals, code. Skills turn a page of prompting into one line. Connectors let it act inside mail, docs, CRM and payments.\n\nInstall the starter trio tonight: marketing, design, docs. Twenty minutes.\n\nOr skip the setup: Ultron comes with 71 skills and 7 agents pre-installed, gate included.",
  "Out of the box it only answers. Installed right, it operates.\n\nThe power user stack: plugins as whole desks, slash commands that run entire plays, connectors wired into your real apps so nothing needs copy-paste.\n\nUltron ships it assembled: 71 skills, 7 agents, connectors live on day one, and everything external waits for your tap.\n\nSet once, collect monthly. Corrections become rules.",
  "Stock is training wheels. The trio to install first: marketing, design, docs.\n\nDrop BUILDER below and I will DM you the full power user install list in order.\n\nSave this for tonight's twenty minutes."),
 "advisors":("THE BOARD OF ADVISORS","FOUNDER","the 3-advisor board setup","d51eb4c6",
  "Generic advice fails because it ignores your deals, your clients, your cash.\n\nI seated a board that reads my books: the pricer, the editor, the strategist. Each one a skill, wired into the same memory.\n\nThe pricer ran real unit economics and said raise. The editor cut the proposal in half. The strategist asked one question: does this open doors?\n\nThe deal signed clean. Three lenses, one win.",
  "Advice is cheap. Context is the moat.\n\nMy board of advisors lives in one Ultron chat: a pricer that proved my floor was too low, an editor that stripped the proposal to the spine, a strategist that filters deals by the doors they open.\n\nAll three read the same live memory: deals, clients, numbers. They advise on facts, not averages.\n\nOn call at 2am, costing cents.",
  "Three advisors, zero retainers, briefed on everything you sell.\n\nDrop FOUNDER below and I will DM you the 3-advisor board setup with the exact skills.\n\nSave this and seat your board this week."),
 "ghosted":("WHY COLD EMAILS DIE","BUILDER","the 5-mistake infra checklist","f98bfdf8",
  "Your cold emails are not ignored. They are unseen. The copy was never the variable.\n\nThe five infra mistakes: counting opens instead of replies, blasting from a fresh domain, one domain carrying the whole pipeline, volume spikes, catch-all lists poisoning the batch.\n\n60 a day steady beats 0 then 500. Boring wins inboxes.\n\nUltron runs the infra by default: warm domains, ramped sends, watched spam rates. 99.2% inboxed.",
  "Same writer, same offer: one campaign crushed, one died in spam. The difference was infrastructure.\n\nThe killers: tracking pixels, fresh domains at full blast, a single domain carrying everything, sudden volume spikes, unverified catch-all lists.\n\nUltron handles the road so your copy gets driven: warm domains, ramps instead of blasts, spam rates watched daily. 99.2% inboxed.\n\nFix the road, then the car.",
  "Great copy on dead infra is a love letter in a locked mailbox.\n\nDrop BUILDER below and I will DM you the 5-mistake infra checklist before your next batch.\n\nSave this if your reply rate just dropped."),
 "twohours":("ONE IDEA, TWO HOURS","FOUNDER","the 2-hour launch timeline","218721c8",
  "One sentence went in at 14:00: a service for founders who hate bookkeeping.\n\nBy 14:20 the offer stood. By 14:50 the page was live in my brand tokens. By 15:10 the content plan had 14 slots queued. By 15:30 twenty openers parked at the gate.\n\nAt 16:00 I reviewed. It shipped.\n\nNo team, no budget, no time: none of the three excuses survived the afternoon.",
  "I gave the desk one idea and two hours.\n\n14:00 one sentence in. 14:20 offer drafted against the niche. 14:50 page live via Crescendo. 15:10 content plan queued. 15:30 outreach parked for my tap. 16:00 reviewed and shipped.\n\nSpeed is the moat, the gate keeps it safe: nothing external moved without me.\n\nThe excuse died at 16:01.",
  "Idea to live business in one afternoon, with every send gated.\n\nDrop FOUNDER below and I will DM you the 2-hour launch timeline, step by step.\n\nSave this and pick your idea for Saturday."),
 "salesorg":("A SALES ORG, NOT A BOT","OPERATOR","the sales org blueprint","7cd134c8",
  "The 100-node sales bot demo always collapses. One agent doing everything does nothing well.\n\nReal teams have structure: a research desk, an outreach desk, an enablement desk, a revops desk. One job per agent, done extremely well.\n\nCORTEX briefs before anyone writes. SPECTER drafts and parks every send. The pipe updates itself.\n\nYou sit on top: one tap a day. Chief, not operator.",
  "Stop building mega-bots. Build a sales org.\n\nInside Ultron: CORTEX runs prospect intel, SPECTER runs gated outreach, enablement handles the paperwork nobody loves, revops keeps the CRM true.\n\nOne job per agent is the whole trick: specialists win, hundred-branch automations collapse.\n\nThe org runs the day. Your tap runs the org.",
  "Four desks, one chief, zero dropped balls.\n\nDrop OPERATOR below and I will DM you the sales org blueprint with each desk's setup.\n\nSave this before you wire another all-in-one bot."),
 "adsagency":("THE AD DESK, IN-HOUSE","OPERATOR","the in-house ad desk chain","73906309",
  "The agency retainer bought slides and delays. I brought the desk in-house and it fits in a chat.\n\nMonday: rival ads diffed. The empty angle found. Twenty variations drafted in my voice. 186 checks before budget moves. Every ad scored before it spends.\n\nThe whole retainer month runs in one morning.\n\nEvery launch still signs with my tap. In-house means in your hands.",
  "Research delivered quarterly, copy on a two-week wait, audits as slide decks. That was the retainer.\n\nThe in-house chain inside Ultron: spy on rival creatives weekly, rank the hooks, take the angle nobody covers, draft twenty variations against your brand rules, audit with 186 checks, score before anything spends.\n\nOne morning, chained. Nothing launches without your tap.",
  "The retainer month, compressed into a Monday ritual.\n\nDrop OPERATOR below and I will DM you the in-house ad desk chain, check by check.\n\nSave this before the next agency invoice lands."),
 "million":("THE ONE-LAPTOP COMPANY","FOUNDER","the one-person company thesis","aa81ca00",
  "The next big company is not a funded startup with a team of 20.\n\nIt is one laptop, a meter that runs in cents, and systems that do not sleep.\n\nThe agents work in parallel: research, outreach, content, builds. The founder decides once a day.\n\nRevenue up 32% this month. Payroll unchanged since day zero. The lines diverge.\n\nSomeone builds this company this year. Why not you.",
  "One person, one laptop, systems that compound.\n\nThe shape: agents run research, outreach, content and builds in parallel; every external move parks for one tap; costs stay flat while output multiplies.\n\nEmpty calendar, full pipeline. No standups, just digests at 07:00.\n\nSpeed beats size every quarter now. Judgement is the only job left.",
  "Revenue compounds. Headcount stays 1. That spread is the business.\n\nDrop FOUNDER below and I will DM you the one-person company thesis with the full architecture.\n\nSave this and start tonight."),
 "zerostart":("STARTING FROM ZERO, 2026","BUILDER","the zero-start plan","262dd98f",
  "If I started from zero today I would write no code.\n\nThe barrier moved: niche, distribution, consistency are the only three problems left.\n\nThe build is a sentence: Crescendo assembles the page from 822 parts. Flows handle follow-up and delivery. The desk plans 14 posts from one line.\n\nTen customers, ten handshakes: the machine sources, you close like a human.\n\nZero code. One gate. All yours.",
  "Starting from zero in 2026 is a different game.\n\nThe page assembles itself from one sentence. The workflow runs follow-up, delivery and reporting on triggers. The content desk makes daily presence cheap.\n\nPick a boring problem people already pay for: the unglamorous print money.\n\nCost base in cents, output of a team. The math flipped.",
  "The barrier is not technical anymore. It is niche, distribution, consistency.\n\nDrop BUILDER below and I will DM you the zero-start plan, week by week.\n\nSave this if you are starting with nothing but a laptop."),

 "diytrap":("THE BUILD-IT-YOURSELF TRAP","BUILDER","the build vs install comparison","diytrap",
  "Every tutorial wants you wiring graphs by the third slide.\n\nI did it: three weekends of plumbing, zero leads out. DIY agents break the week you stop watching, and they fail in private.\n\nThe install path: seven agents already wired, gated, composing. One sentence in, twenty briefs out, minute ten.\n\nBuild your product. Not your plumbing.",
  "The agent tutorials are a trap for founders.\n\nFrameworks, graphs, state machines: three weekends of wiring for a demo that breaks silently and sends without a gate.\n\nUltron ships the same loop audited: seven agents built and composing, every cycle checks its own work, every external send parks for your tap. First run in minute ten.\n\nYour weekends belong to offers and distribution, not plumbing.",
  "Three weekends of wiring versus ten minutes of installing. The leads only showed up on one path.\n\nDrop BUILDER below and I will DM you the build vs install comparison, line by line.\n\nSave this before you open another tutorial."),
 "anatomy":("ONE LOOP, HOUR BY HOUR","OPERATOR","the loop anatomy + first-loop setup","anatomy",
  "09:00, the trigger fires. Nobody typed anything.\n\nIt reads the thread and your pricing rules before writing a word. Draft one grades itself 71 and gets redone. Draft three hits 90 and stops: exit condition, not exhaustion.\n\nThree sends park at the gate. You tap twice, kill one. Ten seconds of judgement on forty minutes of machine work.\n\nA prompt is one guess. A loop finishes the job.",
  "This is what one Ultron loop actually does, hour by hour.\n\nWakes itself on a trigger. Loads the thread, the objection, your rules from memory. Drafts against your bar and redoes until it verifies at 90. Parks every send for your tap. Logs the reply, schedules the next touch, updates the digest.\n\nYou contributed ten seconds of judgement.\n\nThat is the difference between words and outcomes.",
  "One trigger, three drafts, a 90 score, three parked sends, one reply logged: a full loop, receipts included.\n\nDrop OPERATOR below and I will DM you the loop anatomy with the first-loop setup.\n\nSave this and pick the one thing you would put on repeat."),
 "mintskills":("MINT YOUR OWN SKILLS","BUILDER","the skill minting steps","mintskills",
  "Even Anthropic says it now: building mega-agents was the wrong move. The unit of leverage is the skill.\n\nFive folders, one SKILL file. Your most repeated workflow is the ore: discover, scaffold, distill, audit, and in ten minutes it is a command.\n\nA downloaded skill writes like everyone. A minted one carries your rules and cannot be copied.\n\nDownloaders collect. Minters compound.",
  "Stop downloading skill packs. Start minting your own.\n\nThe anatomy is small: five folders, one SKILL file, no frameworks. The raw material is the workflow you already repeat: the proposal, the audit, the brief.\n\nFour passes inside Ultron and it becomes a command your whole desk runs, carrying your rules and your no-list. Every correction hardens it.\n\nThe library you make beats the library you save.",
  "Six skills minted from my own repeated jobs, each one now a single command with my rules baked in.\n\nDrop BUILDER below and I will DM you the minting steps, pass by pass.\n\nSave this and pick the workflow you would cast first."),
 "freestack":("THE PRICE OF FULL PRICE","FOUNDER","the free-stack audit map","freestack",
  "The terminal one desk rents yearly has an open twin at zero. The audits agencies bill monthly run as a daily script.\n\nBut free tools are free like a puppy is free: setup, breakage, no memory, no gate. Assembly is the hidden invoice.\n\nThe fix is one operator layer over the whole stack, metered in cents, with your tap on every send.\n\nKnowledge is the discount. Assembly is the price.",
  "You are paying full price for tools that exist free. The gap is knowledge, and it keeps widening.\n\nThe catch nobody posts: ten free tools is eleven new jobs. Each one alone, logged out, forgetting you. The glue is the real product.\n\nUltron is that layer: mail, docs, CRM and the free gems wired into one desk with one memory, metered in cents, gated by your tap.\n\nKeep the gems. Pay only for the layer that runs them while you sleep.",
  "Full-price desks and their free twins, plus the assembly cost nobody itemizes.\n\nDrop FOUNDER below and I will DM you the free-stack audit map before your next renewal.\n\nSave this and check what you are still renting."),
 "no120":("DELETE THE PROMPT LIBRARY","OPERATOR","the 12-skill replacement list","no120",
  "You saved 120 prompts and reopened four. That is not leverage, that is a filing cabinet.\n\nPrompts rot when models change and need you for every single run. Twelve installed skills cover the whole notebook: one command each, same play every time, firing on triggers while you sleep.\n\nI deleted mine in one afternoon.\n\nThe notebook is empty and the desk is full.",
  "The 120-prompt cheat sheet is a trap dressed as a shortcut.\n\nPrompts wait for you, rot on every model update, and cost a fresh re-wording per use. Skills run without you: on triggers, on schedules, overnight, with every external send parked for your tap.\n\nTwelve skills replaced my entire library. /audit my funnel is five words where a page used to be.\n\nEmpty the notebook. Install the twelve.",
  "120 saved prompts, four ever reopened, twelve skills that replaced them all in one afternoon.\n\nDrop OPERATOR below and I will DM you the 12-skill replacement list.\n\nSave this before you save another prompt."),
}

def cap_tt(kit):
    t,kw,res,_,tt,_,_=kit
    return (f"Comment {kw} for {res} and I reply to the first 20. Save this so you do not lose it.\n\n"
            f"{tt}\n\n{H}\n\nFIRST COMMENT (pinned):\n{res.capitalize()} is in my bio right now, so no waiting on a DM. "
            f"Drop {kw} below and I will send it too, I read every comment. Save the video so you can set it up later.")
def cap_ig(kit):
    t,kw,res,_,_,ig,fc=kit
    return (f"Comment {kw} and I will send you {res}.\n\n{ig}\n\n{H}\n\nFIRST COMMENT:\n{fc}")

if __name__=="__main__":
    slugs=sys.argv[1:]
    ts=time.strftime("%Y-%m-%d %H:%M"); dirid=str(int(time.time()))
    mx=d1(f"SELECT MAX(created_at) m FROM vault_items WHERE owner='{ME}'")[0]["m"] or 0
    base=int(mx)+600000; k=0
    for slug in slugs:
        kit=KITS[slug]; title=kit[0]; srcpref=kit[3]
        for suffix,chan,tags,cap in [("(TikTok 3D)","tt",'["TikTok"]',cap_tt(kit)),("(Instagram)","ig",'["IG Scraped"]',cap_ig(kit))]:
            ddir=f"scratchpad/{slug}_{chan}"
            pngs=sorted(glob.glob(f"{ddir}/s*.png"), key=lambda f:int(''.join(c for c in os.path.basename(f) if c.isdigit())))
            keys=[]
            for i,f in enumerate(pngs,1):
                key=f"imports/pm/{slug}-{chan}-{dirid}/{i:02d}.png"; r2put(key,f); keys.append(key)
            media=json.dumps([{"key":x,"type":"image","ext":"png","contentType":"image/png"} for x in keys])
            nid=str(uuid.uuid4()); k+=1
            d1("INSERT INTO vault_items (id,owner,kind,name,source,thumb_key,media,tags,created_at,caption) VALUES (?,?,?,?,?,?,?,?,?,?)",
               [nid,ME,"carousel",f"Review · {title} {suffix} · {ts}","studio",keys[0],media,tags,base+k*1000,cap])
            print("OK",title,suffix,len(keys))
        # sterge sursa adaptata
        d1(f"DELETE FROM vault_items WHERE owner='{ME}' AND id LIKE '%' AND name LIKE 'Scraped %' AND id IN (SELECT id FROM vault_items WHERE owner='{ME}' AND name LIKE 'Scraped %' AND created_at IN (SELECT created_at FROM vault_items WHERE owner='{ME}' AND name LIKE 'Scraped %'))" if False else "SELECT 1")
        # match sursa dupa numele copiat (prefixul numelui original)
        src=d1(f"SELECT id,name FROM vault_items WHERE owner='{ME}' AND name LIKE 'Scraped %'")
        FIRST={"263c2cda":"Comment “OS”","6bf71ba3":"Comment “LOOP”","0a3c53ce":"AI didn’t take your job","fa7eedb6":"5 Signs Your Business","5af9c9ec":"Comment “SKILLS”","2ba8c438":"Comment “LEVELS”","406038b6":"16 Claude Skills","733d81bd":"Comment “CAROUSEL”","1c1cee10":"5 agent architectures","44e61328":"Set up Claude Code in one hour","f276e654":"everyone is posting","2a84f6ff":"everyone keeps asking","65e782c5":"i found 24 things","d51eb4c6":"Comment “BOARD”","f98bfdf8":"Getting ghosted","218721c8":"I gave Claude one business idea","7cd134c8":"Comment “SALES”","73906309":"Comment “ADS”","aa81ca00":"The first $1M business","262dd98f":"if I had to start from $0","diytrap":"Build an AI agent from scratch","anatomy":"WTF is a loop","mintskills":"Comment “SKILL”","freestack":"Big Tech is charging you","no120":"120 prompt codes","modelwars":"Goodbye Claude","dayone":"Every beginner should start","neverhire":"Most businesses don","boring":"Comment “PLAYBOOK”","loweffort":"Yes you can do low effort"}
        frag=FIRST[srcpref]
        for r in src:
            if frag in r["name"]:
                d1("DELETE FROM vault_items WHERE id=?",[r["id"]]); print("DEL sursa:",r["name"][:60])
    print("DONE")
