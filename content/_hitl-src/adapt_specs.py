#!/usr/bin/env python3
# ADAPTARI IG SCRAPED (operator 2026-07-02): 20 surse din vaultul lui Catalin, retraduse in
# context ULTRON. Fiecare deck: hooks virale, panouri clay cu utilitate distincta, CTA pe una
# din cele 3 pastile fixe (OPERATOR/FOUNDER/BUILDER, §30), marci de cover contextuale.
# Acest modul tine DOAR datele; build files + panourile se genereaza din el.

# (slug, TITLE, accent, mark, pill, cover(w,a), slides[8](eyebrow,hw,ha,sub,foot,stem), close(l1,l2,q))
# stem = cheia panoului din adapt_panels.SPECS[slug]

BATCH1=[
 dict(slug="aios", title="THE AI OPERATING SYSTEM", accent=(204,120,92), mark="claude", pill="operator",
  cover=("Your AI has amnesia.","Mine has an OS."),
  close=("Save this to","own your OS.","Rented tools or your own command center?"),
  slides=[
   ("THE BOTTLENECK",("Close the tab.","It forgets everything."),"Every chat starts from zero. That is the real bottleneck, not the model.",("The tab is not a system.",),"amnesia"),
   ("THE BRAIN",("Ultron keeps","one brain."),"Your ICP, voice, pricing and pipeline live in one memory, loaded in every run.",("Set once. Never re-briefed.",),"brain"),
   ("THE DASHBOARD",("One command center.","Yours, not rented."),"Every agent, flow and approval in one place, built on your own data.",("No tab zoo.",),"command"),
   ("THE HOURS",("It runs 24/7.","You do not."),"Flows fire on triggers around the clock, even with the laptop shut.",("Overnight is work time now.",),"always"),
   ("THE MEMORY",("Every correction","becomes a rule."),"Say no discounts once and the gate blocks them forever.",("It compounds monthly.",),"rules"),
   ("THE PROOF",("This morning:","1,284 leads read."),"The OS briefed 200 accounts before the first coffee. One typed sentence.",("While you slept.",),"proof"),
   ("THE GATE",("An OS with brakes.","Your tap."),"Nothing external fires alone. You read, you tap, it moves.",("Power, gated.",),"gate"),
   ("THE OPERATOR",("Stop renting tabs.","Own the system."),"One subscription, one memory, one command center behind a chat.",("Build yours today.",),"own"),
  ]),
 dict(slug="loops", title="PROMPTS ARE DEAD, LOOPS RUN", accent=(200,70,35), mark="claude", pill="builder",
  cover=("Typing prompts all day?","You are the bottleneck."),
  close=("Save this before","your next prompt.","Which task would you loop first?"),
  slides=[
   ("THE OLD WAY",("Prompt. Wait. Paste.","Repeat forever."),"If you type prompt after prompt, you work backwards, one output at a time.",("You are the cron job.",),"oldway"),
   ("THE LOOP",("Set one goal.","It runs itself."),"An Ultron flow has a goal, a checker and an exit. It cycles until done.",("24/7, no typing.",),"loop"),
   ("STEP 1",("Define the job","in plain English."),"Follow up every lead that goes quiet for 3 days. One sentence, one flow.",("That is the whole setup.",),"define"),
   ("STEP 2",("Put it on","a trigger."),"Daily 09:00, on every reply, on usage drop. Triggers replace your memory.",("No reminders app.",),"trigger"),
   ("STEP 3",("Let it verify","its own work."),"Every cycle checks the result before it reports. Failures retry, not repeat.",("The checker is built in.",),"verify"),
   ("THE TRAP",("No checker?","It burns budget."),"A loop without an exit spends while you sleep. Ultron caps every flow.",("Guardrails by default.",),"trap"),
   ("THE GATE",("Loops run free.","Sends do not."),"Anything external still parks on HOLD for your tap. Speed with brakes.",("You stay the exit.",),"gate"),
   ("THE SCALE",("Your hours are fixed.","Loops are not."),"Nine flows ran 212 cycles last week. You typed three sentences.",("Scale past your hours.",),"scale"),
  ]),
 dict(slug="aibody", title="THE COMPLETE AI BODY", accent=(212,162,127), mark="orb", pill="founder",
  cover=("Chatbot founders type.","Operators are augmented."),
  close=("Save this and","augment every part.","Which part of you needs the upgrade first?"),
  slides=[
   ("THE DIFFERENCE",("A chatbot answers.","A body works."),"Most founders rent one mouth. The top operators wire every organ.",("Augment, not chat.",),"difference"),
   ("THE BRAIN",("The router thinks","before it spends."),"It reads each job, hires the right agent, picks the model tier per turn.",("You never pick a model.",),"router"),
   ("THE EYES",("CORTEX reads","1,284 companies."),"Funding, hiring, stack, intent. Signals you would never spot by hand.",("Overnight, every night.",),"eyes"),
   ("THE VOICE",("PULSE writes","like you."),"Sampled from your real posts. Banned words enforced on every draft.",("Your voice, multiplied.",),"voice"),
   ("THE HANDS",("SENTINEL ships","real product."),"Pages, dashboards and fixes from plain English, tested before you see them.",("Built while you sleep.",),"hands"),
   ("THE HEART",("One memory keeps","it all alive."),"ICP, pipeline, pricing, docs. Every agent draws from the same core.",("Nothing forgets you.",),"heart"),
   ("THE GATE",("The body is strong.","You hold the reins."),"Every external move parks for your tap. Augmented, not replaced.",("Still your company.",),"gate"),
   ("THE OPERATOR",("Stop typing.","Start operating."),"One chat wires brain, eyes, voice, hands and heart into one operator.",("The full body, one login.",),"operator"),
  ]),
 dict(slug="fivesigns", title="5 SIGNS YOU NEED AI NOW", accent=(204,120,92), mark="orb", pill="founder",
  cover=("Your business is leaking.","Here are the 5 signs."),
  close=("Save this checklist","and score yourself.","How many of the 5 did you tick?"),
  slides=[
   ("SIGN 1",("Same questions,","every single day."),"If support answers repeat daily, a flow should answer them in seconds.",("Ultron replies 24/7.",),"sign1"),
   ("SIGN 2",("Your team is","a copy-paste bridge."),"Hours spent moving data between apps is payroll spent on glue work.",("Flows move it instantly.",),"sign2"),
   ("SIGN 3",("Everything stops","until you approve."),"You are the bottleneck. Ultron preps everything, you just tap.",("Approval, not assembly.",),"sign3"),
   ("SIGN 4",("Leads wait hours.","Deals die quietly."),"Speed to lead decides the meeting. The flow answers in seconds, gated.",("First reply wins.",),"sign4"),
   ("SIGN 5",("Month-end reports","take days."),"The numbers already exist. Ultron assembles them on demand, with sources.",("Reports in minutes.",),"sign5"),
   ("THE TEST",("Count your yes.","Every one is a leak."),"Five yes answers is not a staffing problem. It is missing systems.",("Friction, not headcount.",),"test"),
   ("THE FIX",("One workflow.","Then repeat."),"Automate the worst leak first. Ultron sets it up from one sentence.",("Start small, compound.",),"fix"),
   ("THE GATE",("Automated,","never unsupervised."),"Every flow that touches a customer parks for your tap first.",("You stay in control.",),"gate"),
  ]),
 dict(slug="contentdesk", title="THE 500K CONTENT DESK", accent=(200,70,35), mark="claude", pill="operator",
  cover=("My content desk runs","on five skills."),
  close=("Save the desk","and steal the setup.","Which of the five would you run first?"),
  slides=[
   ("SKILL 1",("The calendar","plans itself."),"One line in, 14 slots out, spread across channels at 10:00 local.",("Zero coordinators.",),"cal"),
   ("SKILL 2",("Hooks rotate.","Never repeat."),"Three angles per post from your proven hook bank. You pick the winner.",("A/B/C, one tap.",),"hooks"),
   ("SKILL 3",("Drafts arrive","in your voice."),"Sampled from your real posts, banned words enforced, ranked before you read.",("No AI-speak.",),"voice"),
   ("SKILL 4",("One post becomes","five formats."),"LinkedIn long-form, caption, carousel, newsletter, script. Same brief.",("Native per channel.",),"repurpose"),
   ("SKILL 5",("Newsletters land","in the inbox."),"Warm domains, ramped sends, 99.2% placement. Content nobody reads is free.",("Delivery is the job.",),"inbox"),
   ("THE DESK",("Five skills.","One desk, no meetings."),"The whole pipeline runs behind one chat with one memory of your brand.",("PULSE owns it.",),"desk"),
   ("THE GATE",("Nothing posts","without your tap."),"Every draft parks first. You approve the batch in one read.",("Your feed, your call.",),"gate"),
   ("THE MATH",("A content team","for cents."),"Planner, writer, designer, distributor: one subscription, metered by use.",("Payroll: zero.",),"math"),
  ]),
]

BATCH2=[]  # levels50, skills16, carouselcmd, architectures, onehour
BATCH3=[]  # verified, fivepaid, installs24, advisors, ghosted
BATCH4=[]  # twohours, salesorg, adsagency, million, zerostart

ALL=BATCH1+BATCH2+BATCH3+BATCH4
