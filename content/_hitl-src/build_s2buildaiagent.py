#!/usr/bin/env python3
# STOP BUILDING AGENTS - adaptare IG/TikTok in context Ultron a unui tutorial LangChain/LangGraph
# "build an AI agent from scratch": fondatorii nu codeaza agenti, opereaza sapte pre-cablati in engleza.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="STOP BUILDING AGENTS"
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2buildaiagent"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Building an AI agent')],[co('is the wrong job.')]])
T2.CONTENT=[
 ('FROM SCRATCH', [[wo('You wired it')],[co('by hand.')]], 'Framework, memory, evals, glue. Months of engineering before it says hello.', [co('That is not your job.')], f"{M}/scratch.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents,')],[co('already wired.')]], 'Cortex, Specter, Striker, Pulse, Sentinel, Amplify, Counsel. Composed, not coded.', [co('Nothing to assemble.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('You type plain English.')],[co('It hires the worker.')]], 'The router reads the job, picks the right agent and the model tier per turn.', [co('No config, no code.')], f"{M}/router.png", 1.0),
 ('ONE THREAD', [[wo('They hand off')],[co('to each other.')]], 'Cortex researches, Specter writes, Striker closes, then it parks for your tap.', [co('A team, not a bot.')], f"{M}/compose.png", 1.0),
 ('YOU SKIP IT', [[wo('The whole stack,')],[co('collapsed to one.')]], 'Framework, vector store, evals, orchestration. Pre-wired so you never touch them.', [co('One block, not six.')], f"{M}/stack.png", 1.0),
 ('THE PRICE', [[wo('Priced in cents,')],[co('not headcount.')]], 'Pay per token through the router. A full run lands in cents, not a salary.', [co('Cents per job.')], f"{M}/cents.png", 1.0),
 ('THE CORE', [[wo('One memory,')],[co('shared by all seven.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same core.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('LIVE SIGNALS', [[wo('The eyes are')],[co('already on.')]], 'Cortex watches funding, hiring, stack and intent while you sleep.', [co('Built in, not bolted on.')], f"{M}/watch.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the map?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and stop',l2='building from scratch.',q='Which agent would you wire up first?')
MARK2="claude"
