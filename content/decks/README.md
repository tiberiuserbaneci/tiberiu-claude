# Decks - ready to assemble

TWO FORMATS, and they are NOT the same picture cropped. Each is rendered at its own size
because the chrome differs.

## `reel-1080x1920/` - for the reel you cut in Edits

Nine slides, one second each, dropped in after your filmed reaction. No header, no footer,
no badge: it is your cut, so my furniture stays out of it. Slide 1 carries a large centred
Claude mark, which identifies what this is without a sentence claiming it. Content sits
inside 300 top / 130 right / 330 bottom / 70 left, so the platform UI never covers a word.

## `carousel-1080x1350/` - a standalone carousel post

The same nine, rebuilt for a post rather than a cut. Header and footer stay, margins are
even at 76px because nothing overlays a carousel, and slide 1 carries a SWIPE cue.

## The reaction opener

- `reaction-overlay.png` - RGBA with a real alpha channel, goes over your filmed reaction.
  Not a slide. Check it in any viewer: the top of the frame is see-through.
- `reaction-preview.png` - how it reads, against a stand-in plate
- `reaction.md` - the on-screen line, what you say, and the viral pattern it came from with
  its view count

## Order of a reel

1. Your filmed reaction, with `reaction-overlay.png` on top
2. `reel-1080x1920/` 01 to 09, one second each. Slide 01 does NOT repeat the reaction line.
3. Slide 09 is the ask.

## The run

Designs and themes rotate under `content/_deckguard.py`, which refuses any deck that would
make the feed predictable. One deck in every four is a BREAK, because three dense decks in a
row is a pattern and a pattern is what an audience learns to skip.

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
