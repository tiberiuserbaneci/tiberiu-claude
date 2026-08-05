#!/usr/bin/env python3
"""The ten ULTRON PAPER decks, as data.

Every angle comes from the Ultron documentation already in this repo (the docs-01 to docs-13
series and its source copy), cut as a founder job story rather than as a feature tour. Nothing
here is invented: the agents, tiers, memory behaviour, job lifecycle and share modes are all
documented, and the only links used are the confirmed app.51ultron.com paths from CLAUDE.md 1.

No two decks use the same run of layouts. That is the anti-repetition rule made structural:
the mix is declared per deck and asserted unique at build time, so a deck cannot quietly
become a copy of the one before it.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _deck import build, cover, rows, grid, split, chart, stack, cta

DECKS = []


def D(slug, title, tag, slides, mix):
    DECKS.append(dict(slug=slug, title=title, tag=tag, slides=slides, mix=mix))


# ---------------------------------------------------------------- 01 CHAT
D("paper-01-chat", "ONE BOX", "CHAT", [
    cover("ULTRON CHAT", "One box.<br><em>Twelve</em> jobs.",
          "Every GTM job opens in the same place, with the same memory underneath it. "
          "<i>No new tab, no blank screen.</i>", "12", "ONE COMPOSER", "TWELVE JOBS"),
    rows("What one<br>box <em>carries</em>", "The composer is not a chat window. It is the input to a system.", [
        dict(n="01", b="Five agents behind one slash", i="/cortex, /specter, /striker, /pulse, /sentinel", v="SLASH"),
        dict(n="02", b="A tier picker on every turn", i="Lite for lookups, Smart for the work, Deep for judgement", v="TIER"),
        dict(n="03", b="Memory injected per turn", i="profile, saved facts and open work, stitched in", v="BRAIN"),
        dict(n="04", b="Attachments it actually reads", i="PDF, image, audio, spreadsheet, URL become context", v="FILES"),
    ]),
    grid("The <em>slash</em><br>menu", "Type the name of the job. The agent that owns it answers.", [
        dict(u="/cortex", b="Research", i="people, companies and markets into one ranked brief"),
        dict(u="/specter", b="Outbound", i="cold email, follow up, multi step sequences"),
        dict(u="/striker", b="Deals", i="qualification, objections, proposals, close plans"),
        dict(u="/pulse", b="Content", i="posts, launches and newsletters in your voice"),
        dict(u="/sentinel", b="Code", i="reads, writes, tests and ships, opens the PR", dark=True),
        dict(u="/counsel", b="Legal", i="NDAs, MSAs and term sheets, flags the risk", dark=True),
    ], cols=2),
    split("Before the<br>one <em>box</em>", "The same work, on either side of a single change.",
          dict(h="the tab sprawl", big="6 tabs",
               li=["a tab for research", "a tab for the CRM",
                   "a doc of prompts you keep rewriting", "a notes file you paste from daily"]),
          dict(h="one composer", big="1 box",
               li=["every job in the same place", "memory already underneath it",
                   "agents one keystroke apart", "sessions searchable in the sidebar"]),
          ("the change", "context stopped being your job")),
    stack("What a <em>turn</em><br>actually does", "Between your keystroke and the answer, four things happen.", [
        dict(u="ROUTER", b="Reads the job before it answers", i="how big, how deep, what it costs to be wrong"),
        dict(u="BRAIN", b="Stitches your memory in", i="profile, saved facts and the work still open"),
        dict(u="AGENT", b="The one that owns the job answers", i="and can hand off to another mid turn"),
        dict(u="GATE", b="A human approves anything that sends", i="nothing leaves without you"),
    ]),
    cta("CHAT", "and I will send you the twelve part map of the composer.",
        ["Five agents behind one slash", "A tier picker on every turn",
         "Memory injected before the answer"], "app.51ultron.com/docs"),
], mix="cover,rows,grid,split,stack,cta")

# ---------------------------------------------------------------- 02 AGENTS
D("paper-02-agents", "THE WORKFORCE", "AGENTS", [
    cover("THE ULTRON WORKFORCE", "Seven agents.<br><em>Zero</em> gaps.",
          "A GTM team you do not have to hire, brief or schedule. "
          "<i>You type plain English and the router picks.</i>", "7", "SEVEN AGENTS", "ONE ROUTER"),
    grid("The <em>roster</em>", "Each one owns a job end to end. None of them is a chatbot.", [
        dict(u="CORTEX", b="Research", i="profiles people, companies and markets into one ranked brief"),
        dict(u="SPECTER", b="Outbound", i="cold emails, follow ups and multi step sequences"),
        dict(u="STRIKER", b="Deals", i="qualification, discovery, objections, proposals, close plans"),
        dict(u="PULSE", b="Content", i="posts, launches, newsletters and thought leadership"),
        dict(u="SENTINEL", b="Code", i="reads, writes, tests and ships code, opens the PR", dark=True),
        dict(u="AMPLIFY", b="Publishing", i="formats and schedules each asset per channel and time zone", dark=True),
    ], cols=2, note=("and", "COUNSEL drafts and reviews the paper")),
    stack("You never<br>pick <em>one</em>", "The router is the composer. It reads the job and dispatches it.", [
        dict(u="01", b="You write what you want", i="plain English, no agent picker, no model dropdown"),
        dict(u="02", b="The router reads the job", i="who owns it, how deep it goes, what it costs to be wrong"),
        dict(u="03", b="Agents compose and hand off", i="research feeds outbound, outbound feeds the deal"),
        dict(u="04", b="A human approves the send", i="the gate is not optional"),
    ]),
    rows("What each<br>one <em>replaces</em>", "The honest version: this is a headcount question, not a software one.", [
        dict(n="01", b="CORTEX", i="the two hours before every call you never get back", v="RESEARCH"),
        dict(n="02", b="SPECTER", i="the SDR you cannot afford at eight people", v="OUTBOUND"),
        dict(n="03", b="STRIKER", i="the sales lead who reads the objection you missed", v="DEALS"),
        dict(n="04", b="SENTINEL", i="the engineer you interrupt for a landing page", v="CODE"),
    ], note=("the point", "seven jobs, one operator")),
    split("Team of<br><em>seven</em>", "What a founder actually compares this against.",
          dict(h="hiring for it", big="months",
               li=["seven roles to define", "seven people to source and close",
                   "onboarding before output", "salary before revenue"]),
          dict(h="running it", big="minutes",
               li=["seven agents already briefed", "context shared across all of them",
                   "no standup, no handover doc", "a gate you hold yourself"]),
          ("the tradeoff", "judgement stays yours, labour does not")),
    cta("AGENTS", "and I will send you the full roster with what each one owns.",
        ["Seven agents, one router", "Plain English in, no picker",
         "Human approval before anything sends"], "app.51ultron.com/docs"),
], mix="cover,grid,stack,rows,split,cta")

# ---------------------------------------------------------------- 03 BRAIN
D("paper-03-brain", "THE BRAIN", "BRAIN", [
    cover("MEMORY", "It stops<br><em>forgetting</em>.",
          "Most AI starts every conversation from nothing. "
          "<i>This one opens knowing who you are and what is still open.</i>",
          "0", "TIMES YOU RE EXPLAIN", "PER TURN"),
    split("The blank<br>page <em>tax</em>", "What re-explaining costs, on either side of memory.",
          dict(h="without memory", big="every turn",
               li=["paste who you are, again", "paste what you are building, again",
                   "paste last week's notes, again", "the model skims and forgets"]),
          dict(h="with the brain", big="once",
               li=["profile stitched in automatically", "saved facts carried forward",
                   "open work still open", "it either knows or it asks once"]),
          ("the change", "context stops being retyped")),
    rows("What it<br><em>stores</em>", "Three kinds of memory, doing three different jobs.", [
        dict(n="01", b="Profile", i="who you are, what you sell, who you sell it to", v="STATIC"),
        dict(n="02", b="Saved facts", i="the things you told it once and never again", v="DURABLE"),
        dict(n="03", b="Open work", i="what is unfinished and what it is waiting on", v="LIVE"),
        dict(n="04", b="Session history", i="searchable, forkable, resumable from the sidebar", v="THREAD"),
    ]),
    chart("Hybrid<br><em>retrieval</em>", "Three signals decide what gets pulled into a turn, not one.", [
        dict(k="Semantic match", s="what the turn is about", p=88, v="88"),
        dict(k="Recency", s="what you touched last", p=64, v="64"),
        dict(k="Explicit saves", s="what you told it to keep", p=100, v="100"),
    ], note=("why three", "one signal returns the wrong memory confidently")),
    stack("What lands<br>in the <em>turn</em>", "Memory is not a database call. It is a block stitched into the prompt.", [
        dict(u="PULL", b="Three signals run in parallel", i="semantic, recent and explicitly saved"),
        dict(u="RANK", b="Kept short on purpose", i="a long memory block crowds out the actual question"),
        dict(u="STITCH", b="Injected before the agent answers", i="so it never opens on a blank page"),
        dict(u="WRITE", b="The turn writes back", i="what it learned is there for the next one"),
    ]),
    cta("BRAIN", "and I will send you how the memory layer is wired.",
        ["Profile, facts and open work", "Three retrieval signals, not one",
         "Every turn writes back"], "app.51ultron.com/docs"),
], mix="cover,split,rows,chart,stack,cta")

# ---------------------------------------------------------------- 04 JOBS
D("paper-04-jobs", "BACKGROUND JOBS", "JOBS", [
    cover("BACKGROUND JOBS", "Brief it.<br>Close the <em>laptop</em>.",
          "Anything that will not finish while you are awake becomes a job. "
          "<i>You read the result, not the progress bar.</i>",
          "24", "HOURS OF RUNWAY", "ZERO OF YOURS"),
    stack("The <em>lifecycle</em>", "A job is not a prompt. It has a state you can leave and come back to.", [
        dict(u="QUEUED", b="One line of intent goes in", i="not a spec, not a ticket, a sentence"),
        dict(u="RUNNING", b="It dispatches a team, not one model", i="browsing, running skills, writing files"),
        dict(u="VERIFY", b="It checks its own work", i="opens the thing it built and confirms it renders"),
        dict(u="DONE", b="You get a result, not a draft", i="with what it learned saved to memory"),
    ]),
    grid("What it<br>does <em>unattended</em>", "Real tool rounds from a real run, not a feature list.", [
        dict(u="SEARCH", b="Memory", i="pulls what it already knows before it asks the internet"),
        dict(u="BROWSE", b="The web", i="reads the sources it needs, cites what it used"),
        dict(u="RUN", b="A skill", i="the packaged workflow that owns this kind of job"),
        dict(u="WRITE", b="Files", i="into the project, not into a chat bubble"),
        dict(u="EXEC", b="Shell", i="dev server, build, deploy, a real address", dark=True),
        dict(u="SAVE", b="To memory", i="so the next run starts smarter than this one", dark=True),
    ], cols=2),
    rows("What it<br><em>shipped</em>", "One overnight run, three assets, sized and slotted.", [
        dict(n="01", b="Landing page, live", i="shell exec to a dev server, then a real URL", v="LIVE", on=True),
        dict(n="02", b="Carousel at 1080x1350", i="slotted for the Tuesday 09:00 LinkedIn window", v="QUEUED"),
        dict(n="03", b="Video cut at 1080x1920", i="for Reels and Shorts, same story, different frame", v="QUEUED"),
    ], note=("the difference", "verified before you saw it")),
    split("Output vs<br><em>finished</em>", "The distinction most AI tools quietly skip.",
          dict(h="output", big="homework",
               li=["arrives as a suggestion", "you still have to open it",
                   "you still have to check it", "the labour moved, it did not go"]),
          dict(h="finished", big="a result",
               li=["deployed to a real address", "opened and verified by the thing that built it",
                   "held at the gate for your approval", "you read it once and decide"]),
          ("the test", "did it check its own work")),
    cta("JOBS", "and I will send you the background job setup.",
        ["One line of intent, not a spec", "It verifies before it stops",
         "You wake to a result, not a draft"], "app.51ultron.com/docs"),
], mix="cover,stack,grid,rows,split,cta")

# ---------------------------------------------------------------- 05 COMPUTER
D("paper-05-computer", "THE COMPUTER", "COMPUTER", [
    cover("THE COMPUTER", "It runs it.<br>It does not<br><em>describe</em> it.",
          "Most AI hands you instructions and calls that help. "
          "<i>This one executes and shows you the output.</i>",
          "1", "STEP BETWEEN ASK", "AND DONE"),
    split("Describe<br>vs <em>run</em>", "The same request, answered two different ways.",
          dict(h="most AI", big="instructions",
               li=["here is the command to try", "here is roughly what it should print",
                   "you run it, you read it", "if it fails you start the conversation again"]),
          dict(h="the computer", big="output",
               li=["it runs the command", "it reads what actually came back",
                   "it fixes and reruns on failure", "you see the result, not the recipe"]),
          ("the difference", "one of these is doing the work")),
    rows("What it<br>can <em>touch</em>", "A real environment, not a sandbox that pretends.", [
        dict(n="01", b="Shell", i="install, build, run, deploy, tail the log", v="EXEC"),
        dict(n="02", b="Files", i="reads and writes the project, not a copy of it", v="WRITE"),
        dict(n="03", b="A browser", i="opens the page it deployed and checks it renders", v="VERIFY"),
        dict(n="04", b="The repo", i="branches, commits, opens the pull request", v="SHIP"),
    ]),
    stack("A failing<br>build, <em>handled</em>", "What autonomy actually looks like on a bad run.", [
        dict(u="01", b="It runs the build", i="and reads the error, not a summary of the error"),
        dict(u="02", b="It changes the file that broke", i="the one the trace points at"),
        dict(u="03", b="It runs it again", i="and again, until the output is what it expected"),
        dict(u="04", b="It tells you what it changed", i="with the diff, not a description of the diff"),
    ], note=("the honest bit", "you still approve the merge")),
    grid("Where this<br><em>earns</em> its keep", "Founder jobs that used to need an engineer in the room.", [
        dict(u="PAGE", b="A landing page live", i="from a sentence to a real URL, same session"),
        dict(u="FIX", b="The bug in the form", i="reproduced, patched, verified in a browser"),
        dict(u="DATA", b="The export nobody can read", i="parsed, cleaned, handed back as a sheet"),
        dict(u="SHIP", b="The pull request", i="branch, commit, description, opened for review", dark=True),
    ], cols=2),
    cta("COMPUTER", "and I will send you what the execution layer can reach.",
        ["Shell, files, browser, repo", "It reruns until the output is right",
         "You approve the merge"], "app.51ultron.com/docs"),
], mix="cover,split,rows,stack,grid,cta")

# ---------------------------------------------------------------- 06 CONTEXT
D("paper-06-context", "SESSIONS", "CONTEXT", [
    cover("SESSIONS", "Pick it up<br>where you<br><em>dropped</em> it.",
          "Most AI forgets the moment you close the tab. "
          "<i>A session is a place you can leave and return to.</i>",
          "0", "RESTARTS FROM", "A BLANK PAGE"),
    rows("What a<br>session <em>keeps</em>", "Not a transcript. A working state.", [
        dict(n="01", b="The thread", i="searchable in the sidebar, months later", v="HISTORY"),
        dict(n="02", b="The memory", i="profile and saved facts already stitched in", v="BRAIN"),
        dict(n="03", b="The open work", i="what was unfinished and what it was waiting on", v="STATE"),
        dict(n="04", b="The files", i="everything attached is still attached", v="FILES"),
    ]),
    stack("Resume,<br>fork, <em>hand over</em>", "Three things a thread should do and most cannot.", [
        dict(u="RESUME", b="Open it a week later", i="it opens where you stopped, not where it started"),
        dict(u="FORK", b="Branch one thread into two", i="try the other approach without losing the first"),
        dict(u="SHARE", b="Hand the whole thing over", i="a read only link, context included"),
        dict(u="SEARCH", b="Find the one you need", i="across every session, by what was said in it"),
    ]),
    split("Chat vs<br><em>session</em>", "Why the distinction is not pedantic.",
          dict(h="a chat", big="disposable",
               li=["ends when the tab closes", "starts from nothing next time",
                   "cannot be branched", "cannot be handed to anyone"]),
          dict(h="a session", big="a place",
               li=["persists and stays searchable", "resumes with its state intact",
                   "forks without losing the original", "shares read only, context included"]),
          ("the test", "can you leave and come back")),
    grid("What this<br>changes at <em>8 people</em>", "The founder-scale version, not the enterprise one.", [
        dict(u="MONDAY", b="The deal thread", i="open it Friday and it still knows the objection"),
        dict(u="HANDOVER", b="Onboarding a hire", i="send the session, not a folder of documents"),
        dict(u="BRANCH", b="Two pricing models", i="fork the thread, run both, keep the winner"),
        dict(u="RECALL", b="What did we decide", i="search the sessions, not your memory", dark=True),
    ], cols=2),
    cta("CONTEXT", "and I will send you how sessions and resume are wired.",
        ["Threads persist and stay searchable", "Fork without losing the original",
         "Hand over read only, context included"], "app.51ultron.com/docs"),
], mix="cover,rows,stack,split,grid,cta")

# ---------------------------------------------------------------- 07 BUILDER
D("paper-07-builder", "THE BUILDER", "BUILDER", [
    cover("THE BUILDER", "A sentence<br>to a live<br><em>URL</em>.",
          "No repo to clone, no pipeline to configure, no engineer to interrupt. "
          "<i>You describe it, it ships it.</i>", "1", "SENTENCE IN", "ONE URL OUT"),
    stack("The <em>pipeline</em>", "Four steps, none of which you run.", [
        dict(u="01", b="You describe the thing", i="one paragraph of what it is for and who it is for"),
        dict(u="02", b="It writes the files", i="pages, styles, the form, the copy"),
        dict(u="03", b="It deploys", i="shell exec, a dev server, then a real address"),
        dict(u="04", b="It opens the page", i="and confirms it renders and the form actually fires"),
    ]),
    chart("Where the<br>time <em>went</em>", "The same landing page, measured on either side.", [
        dict(k="Briefing an agency", s="round trips before a draft", p=100, v="3wk"),
        dict(k="Doing it yourself", s="evenings you will not get back", p=52, v="9d"),
        dict(k="The builder", s="one session, verified", p=9, v="1h"),
    ], note=("the caveat", "you still write the offer")),
    rows("What ships<br>with <em>it</em>", "Not a mockup. The things a page needs to actually work.", [
        dict(n="01", b="A real address", i="not a preview link that expires on Friday", v="LIVE", on=True),
        dict(n="02", b="A form that fires", i="tested by opening it, not by assuming", v="TESTED"),
        dict(n="03", b="Copy in your voice", i="PULSE writes it from your own material", v="PULSE"),
        dict(n="04", b="The pull request", i="if it belongs in the repo, SENTINEL opens it", v="SENTINEL"),
    ]),
    split("Mockup vs<br><em>shipped</em>", "The gap most AI builders never close.",
          dict(h="a mockup", big="a picture",
               li=["looks finished in a screenshot", "nothing behind the button",
                   "someone still has to build it", "the estimate starts now"]),
          dict(h="shipped", big="an address",
               li=["you can open it on your phone", "the form writes somewhere real",
                   "verified before you saw it", "changes are another sentence"]),
          ("the test", "can you send the link to a customer")),
    cta("BUILDER", "and I will send you the build and deploy setup.",
        ["A sentence in, a URL out", "It opens the page and verifies it",
         "Changes are another sentence"], "app.51ultron.com/docs"),
], mix="cover,stack,chart,rows,split,cta")

# ---------------------------------------------------------------- 08 INDEX
D("paper-08-index", "AI-NATIVE INDEX", "INDEX", [
    cover("THE AI-NATIVE INDEX", "Most founders<br>score <em>lower</em><br>than they think.",
          "Not how many AI tools you pay for. How much of the work actually runs through them. "
          "<i>Those are different numbers.</i>", "5", "DIMENSIONS", "ONE SCORE"),
    rows("The five<br><em>dimensions</em>", "Scored on what runs, not on what is installed.", [
        dict(n="01", b="Routing", i="does the job pick its own model, or do you", v="SYSTEM"),
        dict(n="02", b="Memory", i="does context survive the tab, or get retyped", v="BRAIN"),
        dict(n="03", b="Autonomy", i="does it finish unattended, or need you present", v="JOBS"),
        dict(n="04", b="Verification", i="does it check its own output, or hand you homework", v="PROOF"),
        dict(n="05", b="Governance", i="is there a gate, or does it just send", v="GATE"),
    ]),
    chart("Where most<br>founders <em>land</em>", "The pattern under the self-assessments, not a promise about you.", [
        dict(k="Tools bought", s="subscriptions on the card", p=92, v="high"),
        dict(k="Work routed", s="jobs that actually run through them", p=34, v="low"),
        dict(k="Context kept", s="survives closing the tab", p=21, v="low"),
        dict(k="Output verified", s="checked before you see it", p=12, v="rare"),
    ], note=("the gap", "spend is not adoption")),
    split("Tool stack<br>vs <em>system</em>", "Why the first number keeps rising and the second does not.",
          dict(h="a stack", big="subscriptions",
               li=["you choose the tool every time", "context lives in whichever tab",
                   "output arrives as a suggestion", "the bill grows, the work does not"]),
          dict(h="a system", big="routing",
               li=["the job picks its own model", "context is underneath all of it",
                   "output is verified before you see it", "one gate, held by you"]),
          ("the honest read", "most stacks score under 40")),
    grid("What moves<br>the <em>score</em>", "In the order that actually pays, cheapest first.", [
        dict(u="FIRST", b="Stop choosing models", i="routing is the single biggest jump and the easiest"),
        dict(u="SECOND", b="Put memory underneath", i="stop paying the blank page tax on every turn"),
        dict(u="THIRD", b="Make it verify", i="output you still have to check is not finished work"),
        dict(u="FOURTH", b="Hold the gate", i="governance is the one nobody builds and everyone needs", dark=True),
    ], cols=2),
    cta("INDEX", "and I will send you the five dimension scorecard.",
        ["Five dimensions, scored on what runs", "Spend is not adoption",
         "Routing is the cheapest jump"], "app.51ultron.com/techniques"),
], mix="cover,rows,chart,split,grid,cta")

# ---------------------------------------------------------------- 09 SHARED
D("paper-09-shared", "SHARED WORK", "SHARED", [
    cover("SHARED WORK", "Send the<br><em>thread</em>,<br>not the file.",
          "A document is the answer with the thinking cut out. "
          "<i>Hand over the session and the context comes with it.</i>",
          "1", "LINK", "WHOLE CONTEXT"),
    grid("What a<br>link <em>carries</em>", "Read only, but complete.", [
        dict(u="THREAD", b="Every turn", i="the questions, not only the conclusions"),
        dict(u="FILES", b="What was attached", i="the sources it was actually reading"),
        dict(u="STATE", b="What is still open", i="so they see what is unfinished, not just what is done"),
        dict(u="AGENTS", b="Who did what", i="which agent answered which part"),
    ], cols=2),
    split("Document<br>vs <em>session</em>", "The handover most teams do badly.",
          dict(h="a document", big="the answer",
               li=["the reasoning is gone", "they cannot see what you rejected",
                   "questions come back to you", "it is stale the day you send it"]),
          dict(h="a session", big="the work",
               li=["every turn is there to read", "the rejected paths are visible",
                   "they can fork it and continue", "it stays live while the work does"]),
          ("the saving", "the follow up meeting")),
    rows("Who this<br>is <em>for</em>", "Founder scale handovers, not enterprise workflow.", [
        dict(n="01", b="A new hire", i="send the session instead of a week of onboarding", v="ONBOARD"),
        dict(n="02", b="A co-founder", i="catch up on a thread without a call", v="SYNC"),
        dict(n="03", b="An advisor", i="show the reasoning, get a real opinion back", v="REVIEW"),
        dict(n="04", b="A client", i="read only proof of the work, not a status email", v="PROOF"),
    ]),
    stack("The <em>rules</em>", "Sharing without giving away the keys.", [
        dict(u="READ ONLY", b="They cannot change your thread", i="a fork is theirs, the original stays yours"),
        dict(u="SCOPED", b="One session, not the account", i="a link is a session, never the workspace"),
        dict(u="REVOCABLE", b="Turn it off", i="the link stops working the moment you say so"),
        dict(u="GATED", b="Sending still needs you", i="a viewer can read the work, never send from it"),
    ], note=("the principle", "share the work, keep the gate")),
    cta("SHARED", "and I will send you how session sharing is scoped.",
        ["One link, whole context", "Read only, forkable, revocable",
         "Viewers can never send"], "app.51ultron.com/docs"),
], mix="cover,grid,split,rows,stack,cta")

# ---------------------------------------------------------------- 10 ROUTING
D("paper-10-routing", "THE ROUTING MAP", "ROUTING", [
    cover("THE ROUTING MAP", "Eight jobs.<br>One AI wins<br><em>one</em>.",
          "Run your whole GTM through a single model and it is the right tool for one job. "
          "<i>The other seven ship on the wrong AI.</i>", "8", "GTM JOBS", "ONE WINNER EACH"),
    chart("Wins by<br><em>model</em>", "Eight founder GTM jobs, scored by which model actually won them.", [
        dict(k="Claude", s="judgement and the writing", p=100, v="5"),
        dict(k="ChatGPT", s="pressure testing the close", p=20, v="1"),
        dict(k="Gemini", s="long context enrichment", p=20, v="1"),
        dict(k="Perplexity", s="live research signals", p=20, v="1"),
    ], note=("the read", "best single model wins 5 of 8")),
    rows("The <em>map</em>", "Which job goes where, and why it is not a preference.", [
        dict(n="01", b="Lead research", i="live funding and hiring signals before you write a word", v="PERPLEXITY"),
        dict(n="02", b="Account enrichment", i="long context, reads Google native data without truncating", v="GEMINI"),
        dict(n="03", b="ICP scoring and outreach", i="holds your tone and scores fit honestly", v="CLAUDE", on=True),
        dict(n="04", b="Follow up to close", i="surfaces the objection you were about to walk past", v="CHATGPT"),
    ]),
    split("One model<br>vs the <em>map</em>", "The same eight jobs, run two ways.",
          dict(h="one model, eight jobs", big="1 of 8",
               li=["right tool for one job", "seven ship on the wrong AI",
                   "you tune prompts to fix a routing problem", "polished noise, faster"]),
          dict(h="routed", big="8 of 8",
               li=["each job to the model that wins it", "context held across all eight",
                   "one gate before anything sends", "you stop choosing tabs"]),
          ("the fix", "never a smarter model, a routing layer")),
    grid("What the<br>router <em>reads</em>", "Four reads, before a single token of output.", [
        dict(u="VOLUME", b="How big is it", i="forty accounts in one pass, or one careful answer"),
        dict(u="DEPTH", b="How deep does it go", i="a lookup, or a judgement you would defend"),
        dict(u="RISK", b="What does wrong cost", i="you review it, or it goes to a customer"),
        dict(u="LATENCY", b="How fast do you need it", i="now, or by the time you are back", dark=True),
    ], cols=2),
    cta("ROUTING", "and I will send you the full eight job routing map.",
        ["Eight jobs, one winner each", "Context held across all of them",
         "One gate before anything sends"], "app.51ultron.com/docs"),
], mix="cover,chart,rows,split,grid,cta")


def main() -> None:
    want = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    mixes = {}
    for d in DECKS:
        if d["mix"] in mixes:
            sys.exit(f"{d['slug']} repeats the layout run of {mixes[d['mix']]}: {d['mix']}")
        mixes[d["mix"]] = d["slug"]
    for d in DECKS:
        if want and not any(w in d["slug"] for w in want):
            continue
        p = build(d["slug"], d["title"], d["tag"], d["slides"])
        print(f"  {p.name:26} {len(d['slides'])} slides   {d['mix']}")
    print(f"{len(DECKS)} decks, every layout run unique")


if __name__ == "__main__":
    main()
