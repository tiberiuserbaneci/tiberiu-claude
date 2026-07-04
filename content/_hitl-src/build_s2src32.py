#!/usr/bin/env python3
# ZERO SERVERS, ONE ANSWER - adaptare IG Scraped in context Ultron (reframe of a "40+ MCP servers
# your Claude needs" listicle -> founder-GTM: you do not wire 40 servers, you ask for the outcome).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="ZERO SERVERS, ONE ANSWER"
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src32"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You would wire 40 servers.')],[co('I just asked.')]])
T2.CONTENT=[
 ('THE DETOUR', [[wo('Forty servers,')],[co('one break each.')]], 'Search, crawl, database, files, sheets. Every server is a key, a config and an outage you own.', [co('You own every break.')], f"{M}/pile.png", 1.0),
 ('ONE LINE', [[wo('No keys. No yaml.')],[co('You just ask.')]], 'One line of plain English returns a ranked answer. Nothing to wire, nothing to maintain.', [co('Plain English in.')], f"{M}/ask.png", 1.0),
 ('SEARCH + CRAWL', [[wo('It already read')],[co('the whole web.')]], 'Tavily, Brave, Firecrawl, Fetch. Four servers, or one agent that reads and ranks for you.', [co('Read, not scraped.')], f"{M}/web.png", 1.0),
 ('QUERY, NOT SQL', [[wo('It writes the query.')],[co('You read the answer.')]], 'Postgres, SQLite and Excel in one plain ask. It writes the query and runs it for cents.', [co('Cents per run.')], f"{M}/data.png", 1.0),
 ('SHARED CORE', [[wo('ICP, pipeline, pricing.')],[co('Remembered once.')]], 'Every agent reads one memory core, so you never re-brief and nothing forgets you.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents,')],[co('already wired.')]], 'Research, outbound, deals, content, code, publishing, legal. Shipped wired to one brain.', [co('Install nothing.')], f"{M}/roster.png", 1.0),
 ('THE BILL', [[wo('The stack bills monthly.')],[co('Ultron bills the job.')]], 'Forty subscriptions charge whether you use them or not. Ultron charges cents, per token used.', [co('Cents, not dollars.')], f"{M}/cents.png", 1.0),
 ('HUMAN GATE', [[wo('Strong hands.')],[co('Your tap.')]], 'Every external move parks in one queue and waits for your approval before it fires.', [co('Nothing sends alone.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Stop wiring servers.',l2='Just ask for the outcome.',q='What would you ask if the wiring was already done?')
MARK2="claude"
