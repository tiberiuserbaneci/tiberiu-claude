#!/usr/bin/env python3
# THE CANCELLATION RECEIPT - adaptare IG Scraped (s3src65) in context Ultron
# 4 named subscriptions (ClickUp / Mailchimp / Zapier / Pipedrive) each swapped for the exact Ultron agent.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src65"; LIB=T2.LIB
PREMIUM=1
TITLE="THE CANCELLATION RECEIPT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Cancel four apps.')],[co('Keep one operator.')]])
T2.CONTENT=[
 ('THE RECEIPT', [[wo('You pay $191 a month')],[co('for four logins.')]], 'ClickUp, Mailchimp, Zapier and Pipedrive. One job each, four bills stacked.', [co('$2,292 a year.')], f"{M}/receipt.png", 1.0),
 ('CLICKUP', [[wo('Cancelled ClickUp.')],[co('Kept the work.')]], 'Tasks, triggers and live dashboards in one workspace, on data you own.', [co('No per-seat fee.')], f"{M}/workspace.png", 1.0),
 ('MAILCHIMP', [[wo('Cancelled Mailchimp.')],[co('SPECTER sends it.')]], 'It writes the sequence and follows up until it books, from your own inbox.', [co('No send caps.')], f"{M}/specter.png", 1.0),
 ('ZAPIER', [[wo('Cancelled Zapier.')],[co('AMPLIFY moves it.')]], 'One agent formats each asset and fires it at the right hour, per channel.', [co('No zaps to wire.')], f"{M}/amplify.png", 1.0),
 ('PIPEDRIVE', [[wo('Cancelled Pipedrive.')],[co('STRIKER closes it.')]], 'It qualifies, handles objections and drafts the close plan, pipeline in memory.', [co('Your deals, your DB.')], f"{M}/striker.png", 1.0),
 ('THE ROUTER', [[wo('Four apps became')],[co('one login.')]], 'Type plain English. The ROUTER hires the agent and the model tier that fits.', [co('One operator.')], f"{M}/router.png", 1.0),
 ('THE MATH', [[wo('$2,292 a year')],[co('turned into cents.')]], 'Four SaaS bills gone. Ultron bills pennies per run, only when the work lands.', [co('Pay per token.')], f"{M}/tally.png", 1.0),
 ('YOU OWN IT', [[wo('Strong system.')],[co('Your reins.')]], 'Every external move parks for your tap. Your data, your DB, your approval.', [co('Nothing sends alone.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the swap list?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='cancel the four.',q='Which subscription do you cancel first?')
MARK2="claude"
