# docs-11 - The Chat Loop (turn) - LinkedIn copy

Keyword: TURN
Link (first comment only): app.51ultron.com/docs

---

## CAPTION

One question to Claude. Three model turns, two tool calls, and a finished competitor table before it said a single word back.

Most people picture an AI agent typing one reply. The useful ones run a loop instead.

- - -

I went through how a single turn actually runs inside Ultron, end to end. I expected a request to the model and a response. What I found was a five step path and a loop that does not stop until the work is finished, not until the model has talked.

- - -

→ Every request runs the same five steps: authenticate the user, route to one of 56 skills, pick a model tier, build a scoped tool catalog, then run the loop.

→ The router is cheap. A slash command shortcuts straight to the persona. With no command, a tiny Haiku call classifies the message in about 200ms and hands it to the right skill.

→ The model is never hardcoded. The skill declares a tier, Haiku, Sonnet or Opus, and the handler resolves it to a real model at request time. Swapping models is a one line change.

→ One turn is one pass of the loop. Claude returns tool_use, the tools run, the result is appended, and it sends again. Only tool_use keeps the loop alive.

→ Four things end a turn: end_turn goes idle, max_tokens goes idle with a warning, an error fails, and a pause waits for your approval. Every message and tool result is written to the database, which is the source of truth.

- - -

The reply you read is the last step, not the whole job. The real work happens in the loop between your message and that reply, where the model picks tools, reads the results and decides whether it is done. Build the loop well and the agent finishes the task instead of describing it.

- - -

Follow for one AI system for founders every day.
Comment TURN and I will send you the exact Claude chat-loop breakdown we run inside Ultron.

---

## ALT TEXT

Dark editorial visual on slate background. The headline reads 'Most AI replies once. Claude loops until the job is done.' next to a wide stat tile showing 5 steps per request, 3 model tiers and 91 native tools. Below sits a two pane Ultron app window. On the left, a chat session labeled cortex with a Sonnet badge shows one turn running: a user asks for the top 3 fintech rivals, then two book-orange tool-call cards, turn 1 web_search and turn 2 canvas.comparison_table, then a final message marked stop_reason end_turn. A footer strip reads one turn equals one loop pass. On the right, the Ultron menu shows Today Wednesday, a Recommended /Striker card, a week calendar with the 10th highlighted, Workspace, and an Agents list with CORTEX, SPECTER and STRIKER. Closes with a Comment TURN call to action and the Ultron logo.

---

## FIRST COMMENT

One message in. Claude routed it, picked the Sonnet tier, exposed 14 tools, then ran a loop: two tool calls across three model turns before the answer streamed back. That is one turn.

Comment TURN and I will send you the full chat-loop breakdown, the five steps every request takes and the four ways a turn ends.

app.51ultron.com/docs
