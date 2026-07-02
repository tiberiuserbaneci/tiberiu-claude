#!/usr/bin/env python3
# Rewrite the 9 Review LinkedIn caption kits so they match the FINAL v8/v9 posters
# (operator 2026-07-02: captions no longer match the materials). Caption 400-470w,
# ALT 80-150w, first comment 40-80w with the pinpoint link (DM'd at keyword).
import os, json, ssl, urllib.request, re, sys

ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
CA="/root/.ccr/ca-bundle.crt"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

def d1(sql):
    r=urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query",
                             json.dumps({"sql":sql}).encode(),method="POST")
    r.add_header("Authorization",f"Bearer {TOKEN}"); r.add_header("Content-Type","application/json")
    out=json.loads(urllib.request.urlopen(r,context=ctx,timeout=60).read())
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

def esc(s): return s.replace("'","''")

KITS={}

KITS["run 8 GTM jobs"]=("ROUTER","""Seven AI agents share one chat box and one memory of my business. I have not opened a second tab in six weeks.

For two years I hired point tools the way most founders do: one for research, one for copy, one for images, one for notes. Each one was smart and each one was blind to the other five, so I spent my mornings ferrying context between windows like an unpaid intern for my own software. I expected the fix to be a better tool. It was a different category: an operator instead of a toolbox. Ultron is the AI operator built on Claude, and this map is the whole system on one image: seven named agents, one router, one human gate, one bill. Every row on the poster is something that ran on my account this week, not a feature list.

-> CORTEX profiles people, companies and markets into one ranked brief. This morning: 1,284 companies pulled, 902 net-new against my CRM, 200 exported with one-page briefs in 19 minutes.
-> SPECTER drafted 240 cold emails from one sentence: one trigger per email, 62 words a step, personalised from each brief, every single one parked at the gate before sending.
-> STRIKER reads the CRM before it answers, and every reply routes back to it: qualify, handle the objection, book the call.
-> SENTINEL ships code from Crescendo, the build library of 822 components and 30+ kits. Bug to merged PR in 15 minutes, and it waits for my merge.
-> The router picks the model tier per turn: Lite for lookups, Smart as the default operator, Deep only where judgement pays, objections, code and legal. A full day of agent work costs cents, not seats.

The part nobody sells you is composition. The CORTEX brief feeds SPECTER, replies feed STRIKER, closed-won stories feed PULSE, and AMPLIFY schedules every asset per channel and timezone while COUNSEL redlines the contracts. One pipeline, zero copy-paste between tabs, because the agents share one memory of my ICP, my voice and my pipeline instead of meeting me fresh every morning. And nothing external moves without my tap: every email, post, PR and contract parks on HOLD first, and every release is stamped with a run ID I can audit send by send. The gate has already caught tone drift on 3 drafts, a wrong-tier CC and a broken merge field, before they went out, not after. That is the difference between using AI and running your company on it: the tools answer, the operator finishes, and you stay on the only switch that matters.

Follow for one AI system for founders every day.
Comment ROUTER and I will send you the full agent map plus the architecture doc it comes from.""",
"""Cream editorial map on a light background with nested group panels and no connector lines. The hook reads 'You hired tools. I hired Ultron's seven agents.' The left panel lists the seven agents in book-orange and slate rows: CORTEX research with 1,284 pulled and 200 exported in 19 minutes, SPECTER outbound with 240 drafts at 62 words, STRIKER deals, PULSE content, SENTINEL code with 822 Crescendo components, AMPLIFY publishing at 99.2 percent inboxed, COUNSEL legal, plus a Handoffs row. The right column shows the router with three model tiers, Lite, Smart and Deep, a bill row reading cents, a human gate group with your tap, real saves and an audit log, a Wired into your stack group including Crescendo with 822 parts, and six mono command chips such as 'source 200 founders'. Closes with a Comment ROUTER call to action and the Ultron logo.""",
"""One chat box, seven agents, three model tiers, one human gate. The whole Ultron system fits on this single map, and the handoffs between agents are the part no tool stack can copy.

Drop ROUTER below and I will DM you the full agent map plus the architecture doc behind it:
https://app.51ultron.com/docs/architecture

Save the map. You will reference it weekly.""")

KITS["replace six AI tabs"]=("TABS","""The $129 AI stack is not expensive because of the price. It is expensive because you are the router between six tabs.

I added up my own subscriptions in March: ChatGPT $20, Claude $20, Perplexity $20, Jasper $49, Midjourney $10, Notion AI $10. Six tools, $129 a month, and every one of them met my business for the first time every morning. I thought I was running a modern stack. I was actually running a relay race alone, handing the baton to myself six times per task. The poster is the full swap, priced line by line, exactly as it sat on my card statement.

-> Context dies inside every tab. You re-paste your ICP all day, six histories hold zero shared memory of your business, and five renewal dates hide in five inboxes.
-> Every tab returns answers. None of them returns finished work: no briefs in the CRM, no sends queued, no PR opened.
-> The swap is one chat box. The router reads each job, hires the agent, picks the model tier. Write the cold sequence, audit my GTM, build my landing page: three jobs, zero model menus.
-> One context sits under everything: my ICP, my voice, my live pipeline, my pricing and my banned-word list, loaded in every single run.
-> The bill drops from $129 in seats to cents per day of metered work. One login, one history, one number to watch, and no renewal ambush in month four.

The uncomfortable truth about tab stacks is that the most expensive component is you. You are the one carrying context between windows, translating one tool's output into the next tool's input, all day, and that job does not show up on any invoice. An operator model deletes that job instead of speeding it up: work lands done, briefs in the CRM, sends queued, PRs opened. Most teams will keep paying the $129 because six small charges feel safer than one decision. Run the math on your own stack once and the decision makes itself. And the safety question has one answer: every external step waits at the human gate, I read, I tap, it releases, and every run carries an audit ID. AI that finishes work, with a human on the only switch that matters.

Follow for one AI system for founders every day.
Comment TABS and I will send you the migration map plus the cost calculator.""",
"""Dark blueprint infographic on a slate background with a numbered spine. The hook reads 'You pay $129/mo to babysit AI tabs. Ultron does the work for cents.' The left column stacks the current bill in rows: ChatGPT, Claude and Perplexity at $20 each, Jasper $49, Midjourney and Notion AI at $10, a total row of $129, followed by six x-marked failures including context dies inside every tab and you are the router. The right column shows the swap: three terminal commands such as 'write the cold sequence', a one-context card with ICP, voice, pipeline, pricing and no-list rows marked SET, and a payoff checklist ending in cents not seats with an audit ID. A cheat-sheet strip lists the six agent slash commands. Closes with a Comment TABS call to action and the Ultron logo.""",
"""Six AI subscriptions, $129 a month, and the real cost is the founder carrying context between the tabs. One operator, one context, cents per day of metered work.

Drop TABS below and I will DM you the migration map. Run your own stack through the cost calculator first:
https://work.51ultron.com/calculator

Save the breakdown before your next renewal date hits.""")

KITS["source 200 founders"]=("SOURCE","""47 minutes from one sentence to 200 briefed accounts. The laptop was closed for 46 of them, Claude did the reading.

This is the unedited run from Tuesday morning, timestamps on the poster. No list vendor, no VA, no export-import dance between a scraper and a spreadsheet. I used to lose the first week of every month to exactly this: pulling lists, deduping them by hand, writing openers that smelled like mail merge. One sentence into the Ultron chat box, and a briefed, queued pipeline came out the other side while I was in a customer call.

-> 09:14 I typed: source 200 founders matching my ICP. The router read the job and hired CORTEX. No menus, no setup, no picking a model.
-> CORTEX pulled 1,284 companies matching the niche, deduped them to 902 net-new against my CRM, scored 471 through the full ICP filter, founder or CEO, 2 to 50 seats, IT services and software, US and UK, and exported the top 200 ranked, each with a one-page brief. Time on the clock: 19 minutes.
-> SPECTER picked the list up on auto-handoff: 200 openers, one trigger per email, 62 words a step, personalised from each brief. No mail-merge smell.
-> 09:47 the queue parked at the human gate: 37 accounts flagged deal-ready, sends scheduled 10:00 local per prospect. I read 12 of the drafts, spot-checked the rest, and released the batch with one tap.

Sourcing used to be a skill you hired for. Now it is a sentence you type, and the skill moved one level up: knowing your ICP sharply enough to write that sentence, and reading the 12 drafts that matter before the tap. Everything below that line, the pulling, deduping, scoring, briefing and queueing, runs while your laptop is shut. The gate means the speed never turns into an accident: nothing in that queue could fire until I touched it, and every send that eventually fired is logged with a run ID I can audit. The cost of the entire run sat in cents on the meter, which is the part that still feels illegal compared to what a list vendor charges for worse data. That is what AI sourcing looks like when the output is a pipeline instead of a CSV.

Follow for one AI system for founders every day.
Comment SOURCE and I will send you the exact sourcing sentence plus the techniques link.""",
"""Dark blueprint infographic on a slate background. The hook reads 'Ultron sourced 200 founders. I typed one sentence.' The left column opens with a terminal card holding the command 'source 200 founders matching my ICP', an ICP filter card with four rows, founder or CEO, 2-50 seats, IT services and software, US plus UK, a SPECTER handoff terminal and a payoff checklist with 200 briefs, 200 openers and 37 deal-ready accounts. The right column shows the CORTEX run in kraft-badged rows, 1,284 pulled, 902 net-new, 471 scored, 200 exported, a gate card with 240 sends parked on HOLD, and a clock card running 09:14 to 09:47 with the laptop closed for 46 of the 47 minutes. A cheat-sheet strip lists six commands. Closes with a Comment SOURCE call to action and the Ultron logo.""",
"""1,284 companies scanned, 200 briefed and queued, 47 minutes end to end. The sentence that started it is nine words long.

Drop SOURCE below and I will DM you the exact sentence plus the technique it runs on:
https://app.51ultron.com/techniques

Save this one. It replaces a week of list building every time you run it.""")

KITS["stop briefing your AI"]=("BRAIN","""Every AI chat you open starts with 15 minutes of re-briefing. Two sessions a day, that is a full working day burned every month on introductions.

The poster is the brain map: everything Ultron memorises about my business, and where each piece pays me back. It is the least glamorous part of the system and the reason everything else works. I ran the same experiment most founders run, pasting a context doc into every new chat, and it failed the same way every time: the doc went stale, the AI read half of it, and by Thursday I was correcting the same mistake I corrected on Monday. Memory that persists and compounds is a different product from memory you paste.

-> Who I sell to: founder or CEO, 2-50 employees, IT services and software, US and UK, loaded in every run. CORTEX sources inside it, STRIKER scores against it, SPECTER never writes outside it. The audit flagged 31% of my old pipeline as outside that band.
-> How I sound: the voice sample comes from my real posts, sentence length, cadence, the words I lean on. Banned words are enforced on every draft, every channel, including the website copy Crescendo builds.
-> What I charge: three tiers, Starter free, Max $19, Enterprise $297, quoted correctly every time. There is a discount floor the gate blocks, even against my own late-night generosity.
-> What it wires: the CRM and inbox are read before every answer, the calendar is known before anything is scheduled, and 2,140 send logs mean every claim it makes traces to a run ID.
-> The math: 15 minutes a session, two sessions a day, a full working day refunded every month. That is the quiet ROI nobody screenshots.

The compounding is the real product. Elsewhere, your corrections die at midnight and you re-teach the same lesson forever, which is why every other AI tool feels equally smart and equally generic a year in. Here, every correction becomes a rule: no discounts becomes a gate check, the banned words become a filter, the champion who signs becomes account memory. It sounds more like you every month, and the setup is not a project: it starts from three typed lines, /init my business, remember: no discounts, what do you know about me?

Follow for one AI system for founders every day.
Comment BRAIN and I will send you the brain setup plus the BCP link.""",
"""Cream editorial map on a warm sand background with nested group panels and no connector lines. The hook reads 'Your AI forgets you at midnight. Ultron never asks twice.' The left side groups Who you sell to, with rows for the ICP filter, 200 named accounts, deal stages, buying signals, disqualifiers and champions, including 31% of the old pipe flagged outside the band, and How you sound, with voice sample, banned words, brand tokens, channel formats and a hook bank. The right side groups What you charge, three tiers with an objection bank and a guarded discount floor, What it wires, CRM, 2,140 send logs, calendar and citable docs, and Why it matters, 15 minutes elsewhere versus rules here and a full day refunded monthly. Three mono chips show the seed commands. Closes with a Comment BRAIN call to action and the Ultron logo.""",
"""The unsexy math: 15 minutes of re-briefing per AI session, two sessions a day, a working day lost every month. Memory is the feature that pays rent, not the model.

Drop BRAIN below and I will DM you the brain setup plus the Business Common Profile layer it lives on:
https://app.51ultron.com/bcp

Save the map and seed yours tonight, it is three lines.""")

KITS["audit your entire GTM"]=("AUDIT","""The most useful thing AI ever told me was that my funnel scores 61 out of 100. The consultants wanted three weeks and five figures to say less.

Three words into the Ultron chat box, audit my GTM, and the whole funnel came back graded: 8 checks, a score each, and the exact move per fix. Six of the checks are on the poster. I expected a generic health check. What came back was scored against my own data, 2,140 sends and a 214-deal CRM scan, which is why every verdict below survived me trying to argue with it.

-> Outbound scored 44. The openers were generic: winners carry one trigger and 62 words, and mine carried adjectives. SPECTER rewrote the batch from the account briefs the same day.
-> Follow-up scored 39, the worst of the 8. 68% of my threads died after touch one, and the analysis shows touch 2 is where the meetings live. The cadence turned on with the gate intact.
-> ICP match scored 58. 31% of the pipeline sits outside the 2-50 band I set, 67 misfit deals listed by name with the rule each one breaks: too big, wrong niche, wrong geo.
-> Pipeline hygiene scored 51. 14 deals stale past 30 days, each with a verdict, revive with a named next step or kill and free the week.
-> Deliverability scored 83, the one green light. Four warm domains, 99.2% inboxing, bounce under 0.3%, verdict KEEP, do not touch the ramp. It re-checks placement weekly and pings before a ramp break, not after a campaign dies.

The habit beats the report. A deck from an agency gets shelved the week you receive it; a score gets re-run. Mine re-runs every Monday, takes 4 minutes, and diffs against last week: what moved, what regressed, which fix actually paid. The funnel score became my operating metric the way MRR is, one number that tells me where this week goes. Two of the five fixes shipped the same afternoon they were flagged, because each verdict arrives with the move attached, not with a recommendation to think about. That is the gap between a diagnosis and a to-do list, and it is why 61/100 was the most productive bad grade I have ever received.

Follow for one AI system for founders every day.
Comment AUDIT and I will send you the audit sentence plus the rubric behind the 8 checks.""",
"""Cream clearly-explained infographic with an era row across the top and six color-coded check cards. The hook reads 'Three words. Ultron graded my funnel: 61/100.' The era row runs from gut feel through dashboards and consultants to one sentence. Six cards each carry an icon flow, a mono command chip and a why line: Outbound scored 44 in book-orange with a fix-cadence flow, Follow-up scored 39 in slate with 68% of threads dying at touch one, ICP match scored 58 in kraft with 31% of pipeline outside the band, Pipeline hygiene scored 51 with 14 stale deals, Deliverability scored 83 in green with 99.2% inboxing marked KEEP, and the verdict card reading 61/100 with 3 keep, 5 fix, re-run every Monday. Closes with a Comment AUDIT call to action and the Ultron logo.""",
"""Eight checks, one score per check, the exact move per fix, and a Monday re-run that takes 4 minutes. That is the whole audit, and it graded my funnel 61/100 from three typed words.

Drop AUDIT below and I will DM you the audit sentence plus the rubric:
https://app.51ultron.com/resources

Save it and run yours before Monday.""")

KITS["ship a fix and open the PR"]=("SHIP","""The launch funnel my agency quoted at three weeks went live tonight. Claude assembled it from a library of 822 components while I ate dinner.

I typed one line into Ultron: build the launch funnel for the 200 list. SENTINEL, the code agent, picked the kit and built. No Figma round, no template hunt, no kickoff call, no shared Slack channel that dies after the invoice. I have bought this exact deliverable three times before, at three price points, and the slowest part was never the building: it was the waiting between revisions. The poster is the whole build path, from the sentence to the ship command.

-> The library is Crescendo: 822 pre-built components, 30+ site and app kits, 15 live dashboards, and blueprints rebuilt from linear.app-class sites. It picks parts instead of generating guesses.
-> Kits exist for the niche: AI Startup with the gradient orb hero and waitlist, Fintech with the compliance blocks, Dev Tool with the terminal hero, B2B Enterprise with pillars and ROI.
-> It assembles, then verifies: screenshots every page and reviews its own output against the brief. No AI-template look, because the sections come from the pack, styled in my tokens.
-> The copy is not lorem or generic AI voice: it comes from the brain, my voice sample and banned-word list, the same ones every other agent uses.
-> Preview link first, always. I clicked through it, typed ship, and it went live on my domain the same evening. Cost beyond the plan: $0.

Here is what reframed it for me: the agency was never selling design, it was selling assembly, and assembly is now a sentence. The three weeks in the quote were coordination, revisions and queue time, not craft. When the components already exist at production quality and the system knows your brand tokens and your voice, the remaining human job is judgement: look at the preview, say ship or say fix the hero. That job takes one evening, and it is the only one worth keeping. The same library also means the next build starts from the same standard, not from a blank page: the funnel, the pricing page and the onboarding flow all pull from one pack, so the brand never drifts between deliverables. Speed was the headline for me; consistency turned out to be the compounding part.

Follow for one AI system for founders every day.
Comment SHIP and I will send you the build playbook plus the Crescendo link.""",
"""Dark blueprint infographic on a slate background with a numbered spine. The hook reads 'Your agency quoted 3 weeks. Ultron shipped my funnel tonight.' The left column opens with a terminal card holding 'build the launch funnel for the 200 list', a Crescendo library card with rows for 822 components, 30+ kits, 15 dashboards and blueprints marked GOLD, and a kit picker listing AI Startup, Fintech, Dev Tool and B2B Enterprise. The right column shows a verification checklist, sections from the pack, screenshots of every page, copy in your voice, an app-screens card covering mail, kanban, CRM, onboarding and settings, and a gate card with a preview link, the typed word ship and $0 beyond the plan. A cheat-sheet strip lists six build commands. Closes with a Comment SHIP call to action and the Ultron logo.""",
"""822 components, 30+ kits, preview before anything ships, live the same evening. The three weeks in the agency quote were coordination, not craft.

Drop SHIP below and I will DM you the build playbook plus the library it pulls from:
https://app.51ultron.com/crescendo

Save this before your next landing page quote arrives.""")

KITS["let AI touch outbound"]=("GATE","""The scary part of AI outbound is not the writing, it is the sending. The whole trick is a gate between the two.

Most founders freeze at this exact line: they will let AI draft, but never let it near the send button, so they stay the bottleneck for 240 emails a week and call the bottleneck quality control. I froze there too, for a month, reading every draft like a proofreader with a pipeline to feed. The ladder on the poster is how I let Ultron write everything and still sleep: five steps, one human tap, and the tap is the architecture, not an afterthought.

-> 09:38, SPECTER drafted 240 emails from one typed sentence: 4-step sequences per account, one trigger per email pulled from the account brief, 62 words a step. Drafts, not sends.
-> All 240 parked on HOLD at the gate. I read 12, spot-checked the rest, and had three buttons: approve all, hold, edit 3. One tap total.
-> The gate caught tone drift on 3 drafts, a wrong CC on one thread and a broken merge field, before they went out, not after.
-> AMPLIFY queued the release at 10:00 local per prospect, ramped 60 a day over 4 days on warm domains. 99.2% landed in the inbox, because ramps keep domains alive and blasts kill them.
-> Every reply routes to STRIKER: qualify, handle the objection, book the call. I read a digest with hot threads flagged first, not an inbox.

The principle underneath: AI speed with zero accidents is an architecture decision, not a model feature. Nothing external ever fires alone, every release is stamped with a run ID, and hold parks a batch with zero loss while edit fixes inline. The gate is also why the math works: the whole 240-email batch cost cents on the meter, and the only minutes I spent were the twelve drafts I actually read. You keep the judgement, the system keeps the throughput. And the asymmetry is the point: the model writes 240 emails in the time it takes me to read one, but I can read the 12 that matter faster than any model can earn my trust. Put the human where the leverage is highest, on the release, and both sides of that trade get what they are best at.

Follow for one AI system for founders every day.
Comment GATE and I will send you the gated outbound setup plus the architecture doc.""",
"""Dark ladder infographic on a slate background, read bottom to top in five color bands. The hook reads 'I let Ultron write 240 emails. Zero left without my tap.' Step 1 in book-orange: SPECTER writes 240 four-step sequences from one sentence at 09:38. Step 2 in kraft: one trigger per email, 62 words, no merge smell. Step 3 in sand: sends queued 10:00 local, ramped 60 a day over 4 days at 99.2% inboxed. Step 4 in green, marked the whole trick: all 240 on HOLD, read 12, one tap across approve all, hold and edit 3, with tone drift on 3 drafts caught. Step 5 in slate: replies route to STRIKER and arrive as a digest with a run id on every send. Each band carries ghost pills tracing its flow. Closes with a Comment GATE call to action and the Ultron logo.""",
"""240 AI-written emails, 12 actually read by a human, 1 tap, 0 accidents. The gate caught tone drift, a wrong CC and a broken merge field before any of them left.

Drop GATE below and I will DM you the gated outbound setup plus the architecture doc:
https://app.51ultron.com/docs/architecture

Save the ladder, it is the answer to the only real objection to AI outbound.""")

KITS["prove your research"]=("PROOF","""My co-founder stopped challenging my research the day every number started carrying its own source. The AI writes the claim, the run ID ends the debate.

I used to defend three weeks of research with 30 screenshots pasted into a chat thread. Then slide decks, stale in a week. Then Notion dumps nobody re-opened. Every format failed the same test: the moment someone asked where a number came from, I was reconstructing evidence instead of pointing at it, and the argument outlived the data. The poster shows the replacement: an evidence brief where every claim is stamped at write time by the agent that produced it.

-> Reply timing: US and UK founders reply 3.1x more at 10:00 local time. Measured on my own 2,140 sends, stamped run #4411. Click the run ID and the cohort, window and lift recompute in front of you.
-> One-trigger openers beat template openers 4.4x on booked calls. A 201-send A/B, same list, same offer, only the opener varied. Run #4390, a controlled result, not a copywriting opinion.
-> ICP drift: 31% of the pipeline sat outside the band. A 214-deal CRM scan with row-level evidence, run #4402, every misfit listed with the exact rule it breaks.
-> Follow-up: touch 2 books 58% of all meetings. Read from 100% of 90 days of threads, not a sample, run #4407.
-> The share is one live link. It replaced the deck, the dump and the debate entirely: my co-founder challenged claim 4, clicked the run ID, watched the cohort and the lift recompute in front of him, and the thread ended right there. Argue with the method, not with me.

The habit is the product: every number in every brief carries source, run ID and confidence, attached automatically by the agent that produced it. It costs zero minutes, because stamping happens at write time, not at defend time. And because the link is live rather than a PDF, the brief moves when the data moves; nobody re-litigates a number that updates itself. There is a second-order effect I did not expect: my own claims got sharper, because a number you know will carry its source gets checked before it gets written. Proof by default beats proof on demand in every argument that matters, including the ones you have with yourself.

Follow for one AI system for founders every day.
Comment PROOF and I will send you the evidence-brief template.""",
"""Cream clearly-explained infographic with an era row and six color-coded claim cards. The hook reads 'I replaced 30 screenshots with one Ultron link.' The era row runs from screenshots through slide decks and Notion dumps to one live link. Six cards each carry an icon flow, a mono source chip and a why line: reply timing at 3.1x lift on 2,140 sends with run #4411 in book-orange, ICP drift at 31% of pipeline from a 214-deal scan with run #4402 in slate, one-trigger openers at 4.4x on a 201-send A/B with run #4390 in kraft, follow-up with touch 2 booking 58% of meetings from 90 days of threads with run #4407, the share card in green holding the live brief link with a convinced co-founder, and the habit card, every claim stamped with source, run ID and confidence. Closes with a Comment PROOF call to action and the Ultron logo.""",
"""Four claims, four run IDs, one live link instead of 30 screenshots. The co-founder debate ended at claim 4, one click into the source run.

Drop PROOF below and I will DM you the evidence-brief template plus where the stamping lives:
https://app.51ultron.com/docs

Save this if you have ever lost an argument you were right about.""")

KITS["score any company"]=("INDEX","""Two of the 40 accounts sitting in my CRM were ready to buy this quarter. The AI index found both before lunch, manual research finds them in week 3.

That is the entire pitch for scoring on AI-readiness, and the poster walks the run in 9 steps. One sentence in, a ranked and briefed call list out, 62 minutes on the clock. I had touched both of those accounts before and filed them as someday. The signals that made them call-now this quarter, a fresh raise and an ops hire, never crossed my CRM because CRMs record what already happened, not what is about to.

-> Drop the list: 40 accounts from a CRM export, deduped against open deals first so nothing double-touches a live thread. The same sentence works from 10 accounts to 4,000.
-> It reads public signals only: hiring for ops and RevOps right now, no AI layer in the stack, founder posting about scaling pain in the last 90 days, raised in the last 18 months, inside the 2-50 seat band. Each signal weighted, not a checkbox.
-> Every account lands a 0-100 score and every point traces to a signal: Northwind 86, Globex 81, Initech 74, down to Oscorp 28. Ties break on intent recency, not alphabet.
-> Verdicts, not vibes: 2 CALL NOW ready this quarter, 3 WARM on the weekly re-score track, 3 SKIP with zero further time spent. A verdict is a decision you act on the same day.
-> The call-nows ship with one-page briefs, champion, signals, opener angle, next step, and SPECTER drafts openers for those two only, one trigger each, parked at the gate before anything sends.

The part that changed my week planning is the loop, not the list. Scores decay and spike with the news cycle, so the run repeats every Monday at 07:00: a warm account crossing 80 pings me the same morning, new raises and new hires re-rank the list on their own. Set once, cents per run, and the selling time goes where the readiness already is. The old way was not just slower, it was misallocated: week 3 of manual research is time spent confirming accounts that were never going to buy, while the two that would have answered the phone go cold. Ranking is not the deliverable. The reclaimed weeks are.

Follow for one AI system for founders every day.
Comment INDEX and I will send you the rubric plus the scoring run.""",
"""Cream nine-cell grid infographic with a checkered flow band at the bottom. The hook reads 'Ultron found 2 buyers hiding in my list of 40.' The nine numbered cells alternate book-orange, kraft, sand, green and slate: drop your list with a paste-this prompt, the five weighted public signals, every account scored 0-100 with Northwind 86 and Globex 81 shown, verdicts split 2 CALL NOW, 3 WARM, 3 SKIP, one-page briefs attached per call-now, the week-3 test won before lunch in 62 minutes, outreach wired for call-nows only, the human gate before any send, and the Monday 07:00 re-score with pings on movers. The bottom band traces the loop, score, rank, brief, call. Closes with a Comment INDEX call to action and the Ultron logo.""",
"""40 accounts, 62 minutes, 2 verdicts worth a call this quarter, and both were invisible in the CRM. The index reads five public signals and shows the why behind every point.

Drop INDEX below and I will DM you the rubric plus the scoring run:
https://app.51ultron.com/resources

Save it and run your own list Monday morning.""")

BAD=re.compile("[—–…‘’“”]")

if __name__=="__main__":
    apply="--apply" in sys.argv
    for frag,(kw,cap,alt,fc) in KITS.items():
        full=f"{cap}\n\nALT TEXT:\n{alt}\n\nFIRST COMMENT (cu link pinpoint, se trimite si in DM la {kw}):\n\n{fc}"
        if BAD.search(full): raise SystemExit(f"charscan FAIL in {frag}")
        wc=len(cap.split()); awc=len(alt.split()); fwc=len(fc.split())
        print(f"{frag:28s} kw={kw:7s} caption={wc}w alt={awc}w fc={fwc}w")
        if not (380<=wc<=500): print("  !! caption word count out of band")
        if not (75<=awc<=160): print("  !! alt word count out of band")
        if not (35<=fwc<=105): print("  !! first comment word count out of band")
        if apply:
            rows=d1(f"SELECT id,name FROM vault_items WHERE owner='{OWNER}' AND name LIKE 'Review%HOW TO: {esc(frag)}%'")
            if not rows: print("  MISS row"); continue
            d1(f"UPDATE vault_items SET caption='{esc(full)}' WHERE id='{rows[0]['id']}'")
            print(f"  OK -> {rows[0]['name'][:60]}")
    print("dry-run done" if not apply else "APPLIED")
