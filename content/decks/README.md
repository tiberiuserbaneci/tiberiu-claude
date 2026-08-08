# Decks - ready to assemble

One folder per deck. Each contains:

- `01.png` to `09.png` - 1080x1920, drop straight into Edits at 1 second each
- `carousel-4x5/` - the same nine at 1080x1350 for a carousel post
- `reaction-overlay.png` - RGBA with a real alpha channel, goes over your filmed
  reaction. Not a slide. Verify with any viewer: the top of the frame is see-through.
- `reaction-preview.png` - how the reaction reads, against a stand-in plate
- `reaction.md` - the on-screen line, what you say, and the viral pattern it came from

## Order of a reel

1. Your filmed reaction, with `reaction-overlay.png` on top
2. Slides 01 to 09, one second each. Slide 01 does NOT repeat the reaction line.
3. Slide 09 is the ask.

## The run

Designs and themes rotate under `content/_deckguard.py`, which refuses any deck that would
make the feed predictable. One deck in every four is a BREAK - a thin graphic piece that
interrupts the rhythm, because three dense decks in a row is a pattern and a pattern is what
an audience learns to skip.

| Deck | Design | Theme | Family | Keyword | |
|---|---|---|---|---|---|
| `deck-a-year` | verdict | black | regret | YEAR | |
| `deck-b-bill` | receipt | white | money | BILL | |
| `deck-c-dayone` | trace | black | speedrun | DAYONE | |
| `deck-d-typed` | console | white | whatItypes | TYPED | **BREAK** |
| `deck-e-rules` | ledger | black | rules | RULES | |
| `deck-f-hire` | score | white | hiring | HIRE | |
| `deck-g-turned` | verdict | black | sayingno | TURNED | |
| `deck-h-2am` | console | white | worry | 2AM | **BREAK** |
| `deck-i-monday` | ledger | black | dashboard | MONDAY | |
