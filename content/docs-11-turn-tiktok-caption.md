# docs-11 - The Chat Loop (turn) - TikTok / social caption

Keyword: TURN

---

Most AI replies once. Claude runs a loop until the job is done.

Now I watch a single message turn into a finished job before a word comes back.

One turn is one pass of the tool-calling loop:

Claude routes the message to one of 56 skills, picks a model tier (Haiku, Sonnet or Opus), builds a scoped tool catalog, then loops: it returns tool_use, the tool runs, the result is appended, it sends again, and only tool_use keeps it going until stop_reason is end_turn, then every message and tool result is persisted to the database.

This is the chat loop on the Ultron platform, one AI operating system for founders.

Comment TURN and I will send you the full Claude chat-loop breakdown.

#claude #ai #founder #startup #buildinpublic
