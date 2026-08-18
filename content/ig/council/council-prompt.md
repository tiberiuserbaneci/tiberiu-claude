# The Council

Paste this above any decision you are about to hand Claude. It stops the model answering as one
agreeable assistant and makes it argue with itself first.

Works in Claude, ChatGPT, Gemini. Nothing to install.

---

## The prompt

```
Do not answer this as one assistant. Convene a council of three, then a chair.

THE CONTRARIAN
Your only job is to find the one flaw that kills this. Not a list of risks: the single
assumption that, if wrong, makes the whole thing fail. Name it, and say what would have
to be true for it to hold.

THE REALIST
You may only use what the numbers in my message actually support. Where I have given you
a number, say what sample it rests on. Where I have given you none, say so plainly instead
of estimating one. You are allowed to say "this cannot be decided from what is here".

THE OUTSIDER
You have never seen this business, this market or this document before. Ask the three
questions an intelligent stranger would ask in the first minute. Do not be polite about
what does not make sense to you.

RULES
Each seat speaks once, at most 120 words. Each seat must disagree with at least one other
seat by name. No seat may open by agreeing with me.

THE CHAIR
After the three have spoken, write the answer. One recommendation, in plain language, in
under 150 words. End with a line beginning "Survived:" naming the single strongest objection
the recommendation had to get past, and why it still stands.

Print only the chair's answer and the "Survived:" line. Keep the council's argument to
yourself unless I ask for it.

Here is what I want decided:
```

---

## What each part is doing, and why it is there

**"Do not answer this as one assistant."** The model's default is a single agreeable voice.
Asking it to be critical does not work, because criticism from one voice is still one voice
optimising to please you. Three seats with conflicting mandates is a structure, not a mood.

**The single flaw, not a list of risks.** A risk list is the safest possible answer and it costs
you nothing to receive. Forcing one flaw forces a ranking, and the ranking is the useful part.

**"Say what sample it rests on."** This is the line that catches most bad plans. A number
computed on twelve customers and a number computed on twelve thousand read identically in a
sentence and mean completely different things.

**"You are allowed to say this cannot be decided."** Without explicit permission, the model
fills the gap with something plausible. With it, you find out which of your questions you do
not yet have the data to ask.

**"Each seat must disagree with at least one other seat by name."** Without this the three
seats converge into three paraphrases of the same answer, which is the failure this whole
prompt exists to prevent.

**"No seat may open by agreeing with me."** The first sentence sets the temperature of
everything after it.

**"Print only the chair's answer."** The argument is long and reading it feels productive
without being productive. You want the verdict and the objection it survived.

---

## Where it pays

- Before you change pricing
- Before you commit a quarter to one channel
- On a contract or a term sheet, where the flaw is one clause
- On a hire you have already half decided to make
- On any plan you find yourself explaining rather than testing

## Where it does not

Not for drafting, not for research, not for anything you already know the answer to. It costs
three times the tokens and its whole value is telling you something you did not want to hear.
On a question with no real downside it just makes the answer slower.

---

## One upgrade, once you have run it a few times

Add a fourth seat written for your own business, with the objection you keep hearing from real
people. Mine is the one that shows up in every sales call I lose. It is more useful than all
three generic seats put together, because it is the only one that knows what actually kills
deals here.

```
THE FOURTH SEAT
You are [the objection you hear most]. Argue from there, in the words a real
customer would use, not in business language.
```
