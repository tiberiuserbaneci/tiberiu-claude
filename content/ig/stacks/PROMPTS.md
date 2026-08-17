# Build prompts for the three trial variants

Self-contained. Each block can be pasted into another tool with no other context. The shared spec
is repeated inside every prompt on purpose, so they never have to be sent together.

---

## PROMPT A — keyword SYSTEMS

```
Build a 7 second Instagram reel, 1080x1920, from a static card. No voiceover, no music needed.

FRAME
Canvas 1080x1920, pure black background.
A white card 1080x1350 sits centred vertically: black bar 285px above it, 285px below.
The card is full width, no side margins.

CARD LAYOUT (1080x1350, background #FFFFFF, font DM Sans, mono accents in DM Mono)
Row 1, a thin strip 44px tall at the very top, centred, DM Mono 15px, weight 500,
letter-spacing .22em, uppercase, colour #77736B:
    THE FOUNDER STACK 01 / 20
with "01 / 20" in #C84623 and a half-em gap before it.

Below it a header band 206px tall, centred, two lines:
    line 1: 6 SYSTEMS EVERY FOUNDER SHOULD HAVE
            DM Sans 800, 44px, letter-spacing -1.2px, colour #111111, all caps
    line 2: (this is where a job becomes a business)
            DM Sans 400, 33px, letter-spacing -.5px, colour #3A3A38, lower case, in brackets

A solid black rule 3px tall, full width, directly under the header band.

Then six rows filling the space down to a footer strip 108px tall. Each row:
  - a 72x72 rounded square tile, radius 16, background #F5F4F1, 1px border rgba(17,17,17,.11),
    containing the tool's brand logo at 40px, or the tool's initial in DM Sans 800 if no logo
  - 22px gap, then the tool name in DM Sans 800, 32px, letter-spacing -.6px, colour #111111
  - immediately after the name, a small chip: DM Mono 15px, colour #77736B, background #F5F4F1,
    padding 4x9, radius 6
  - under the name, the description in DM Sans 500, 19.5px, colour #77736B
  - a 1px hairline rgba(17,17,17,.11) above every row except the first
Left margin 70px, right margin 70px, for every element.

THE SIX ROWS
1. Fireflies      chip: multi        Every call recorded and written up without you
2. Attio          chip: multi        The pipeline that updates itself
3. Reclaim        chip: in house     Your calendar defends itself
4. Gumloop        chip: multi        The daily jobs run whether you remember or not
5. Notion         chip: multi        One place everything lands
6. THE LOCKED ROW, styled differently and it is the point of the card:
   background rgba(200,70,35,.06), 1px border rgba(200,70,35,.32), radius 14, padding 0 14px.
   The tile shows a "?" in #C84623 on background rgba(200,70,35,.07).
   Where the NAME would be, draw a diagonally striped redacted bar instead, 250x26, radius 7,
   stripes at 115 degrees alternating rgba(200,70,35,.20) and rgba(200,70,35,.09).
   Chip: Claude, in #C84623 on rgba(200,70,35,.10).
   Description, weight 600, colour #7A5245:
       Does four of the five above, in one seat. I am not naming it here

FOOTER STRIP, 108px, centred, 1px hairline above:
a 46px circular portrait photo, then 18px gap, then in DM Sans 600, 25px, colour #161412:
    Comment SYSTEMS for the one I did not name

MOTION over 7 seconds
The header band and the footer never change; they are at full strength in frame one.
A pure black sheet covers ONLY the rows area, starting at opacity 0.98 and animating linearly to
0 over exactly 4.2 seconds, then the frame holds unchanged until 7.0 seconds.
Nothing moves, nothing cuts, nothing crossfades. Brightness only ever increases.

Deliver: reel.mp4 (1080x1920, 30fps, 7.0s, silent) and card.png (1080x1350).
```

**Caption A** (post with it):
```
Comment SYSTEMS and I will tell you the one I did not name.

Five of these six are named on the card. The sixth is the one that does most of the work.

Most founders buy tools. Very few build systems. The difference is whether the work still happens
on the days you do not show up.

Every call written up without me. The pipeline updating itself. My calendar saying no on my behalf.
The daily jobs running whether I remember them or not. All of it landing in one place.

And then the one I did not name, which quietly does four of those five in a single seat.

That is the whole reason I stopped trying to hire.

Comment SYSTEMS and it is yours.

#fyp #ai #automation #business #entrepreneur
```

---

## PROMPT B — keyword SECRET

```
Build a 7 second Instagram reel, 1080x1920, from a static card. No voiceover, no music needed.

FRAME
Canvas 1080x1920, pure black. A white card 1080x1350 centred vertically, 285px of black above and
below. Card is full width.

CARD LAYOUT (1080x1350, #FFFFFF, DM Sans, mono accents DM Mono, left and right margins 70px)
Top strip 44px, centred, DM Mono 15px weight 500, letter-spacing .22em, uppercase, #77736B:
    THE FOUNDER STACK 02 / 20
with "02 / 20" in #C84623, half-em gap before it.

Header band 206px, centred, two lines:
    3 AI TOOLS I WOULD NEVER TELL          DM Sans 800, 44px, -1.2px, #111111, caps
    (a competitor about)                   DM Sans 400, 33px, -.5px, #3A3A38, lower case

Solid black rule 3px, full width, under the band.

Five rows down to a 108px footer. Row anatomy: an 84x84 rounded tile (radius 16, #F5F4F1, 1px
border rgba(17,17,17,.11)) holding the brand logo at 47px or the initial in DM Sans 800; 22px gap;
name in DM Sans 800 36px -.6px #111111; a chip after the name in DM Mono 15px #77736B on #F5F4F1;
description under it in DM Sans 500 21px #77736B. 1px hairline above each row except the first.

THE FIVE ROWS
1. Perplexity   chip: multi      The obvious one. Research with sources you can check
2. Canva        chip: multi      The other obvious one. Everything visual, fast
3. REDACTED ROW: tile shows "?" in #C84623 on rgba(200,70,35,.07). Where the name goes, draw a
   grey diagonally striped bar 190x26, radius 7, stripes at 115 degrees alternating #E6E3DE and
   #F2F0EC. Chip: multi. Description in #8C877E:
       Turns one call into the proposal before you stand up
4. REDACTED ROW, same styling. Chip: in house. Description:
       Finds the accounts your competitors have not called yet
5. THE LOCKED ROW, the point of the card: background rgba(200,70,35,.06), 1px border
   rgba(200,70,35,.32), radius 14, padding 0 14px. Tile "?" in #C84623. Redacted name bar 250x26
   in terracotta stripes, alternating rgba(200,70,35,.20) and rgba(200,70,35,.09). Chip: Claude in
   #C84623 on rgba(200,70,35,.10). Description weight 600, #7A5245:
       Runs the two above overnight and waits for your yes

FOOTER 108px, centred, hairline above: 46px circular portrait, 18px gap, DM Sans 600 25px #161412:
    Comment SECRET and I will name all three

MOTION over 7 seconds
Header and footer are at full strength from frame one and never change.
A pure black sheet over ONLY the rows area goes from opacity 0.98 to 0, linearly, over exactly
4.2 seconds, then holds to 7.0s. No cuts, no crossfades, brightness only rises.

Deliver: reel.mp4 (1080x1920, 30fps, 7.0s, silent) and card.png (1080x1350).
```

**Caption B**:
```
Comment SECRET and I will name all three.

Two of the five on this card are obvious. I left three of them blank on purpose.

Not because they are clever. Because they are the reason I quote faster than firms with ten people,
and I would rather my competitors kept doing it by hand.

One turns a call into the proposal before I stand up. One finds the accounts nobody has called yet.
And the third runs both of those overnight and waits for me to say yes before anything sends.

That last one is the only reason the first two are worth having.

Comment SECRET and you get all three names.

#fyp #ai #automation #business #entrepreneur
```

---

## PROMPT C — keyword EIGHT

```
Build a 7 second Instagram reel, 1080x1920, from a static card. No voiceover, no music needed.

FRAME
Canvas 1080x1920, pure black. White card 1080x1350 centred vertically, 285px black above and below,
card full width.

CARD LAYOUT (1080x1350, #FFFFFF, DM Sans, mono accents DM Mono, margins 70px both sides)
Top strip 44px, centred, DM Mono 15px weight 500, .22em, uppercase, #77736B:
    THE FOUNDER STACK 03 / 20
with "03 / 20" in #C84623, half-em gap before it.

Header band 206px, centred, two lines:
    8 APPS I USED TO GROW WITHOUT HIRING     DM Sans 800, 44px, -1.2px, #111111, caps
    (you can start with the same eight today) DM Sans 400, 33px, -.5px, #3A3A38, lower case

Solid black rule 3px, full width.

Eight rows down to a 108px footer. Row anatomy: a 60x60 rounded tile (radius 16, #F5F4F1, 1px
border rgba(17,17,17,.11)) with the brand logo at 34px or the initial in DM Sans 800; 22px gap;
name DM Sans 800 27px -.6px #111111; chip after the name in DM Mono 13px #77736B on #F5F4F1;
description DM Sans 500 17.5px #77736B. 1px hairline above each row except the first.

THE EIGHT ROWS
1. Apollo      chip: in house   Finds who is worth talking to
2. Instantly   chip: in house   Sends it and keeps the inbox warm
3. Gamma       chip: multi      The deck, in a minute
4. Framer      chip: multi      The site, live the same afternoon
5. Krea        chip: multi      Images fast enough to iterate on a call
6. Mem         chip: multi      Everything you capture, sorted without you
7. Cal.com     chip: none       Books the meeting while you sleep
8. THE LOCKED ROW, the point of the card: background rgba(200,70,35,.06), 1px border
   rgba(200,70,35,.32), radius 14, padding 0 14px. Tile shows "?" in #C84623 on
   rgba(200,70,35,.07). Instead of a name, a diagonally striped redacted bar 250x26, radius 7,
   stripes at 115 degrees alternating rgba(200,70,35,.20) and rgba(200,70,35,.09). Chip: Claude in
   #C84623 on rgba(200,70,35,.10). Description weight 600, #7A5245:
       The eighth is the SDR I never hired. Ask me for it

FOOTER 108px, centred, hairline above: 46px circular portrait, 18px gap, DM Sans 600 25px #161412:
    Comment EIGHT for the eighth one

MOTION over 7 seconds
Header and footer at full strength in frame one, never changing.
Pure black sheet over ONLY the rows area, opacity 0.98 to 0, linear, exactly 4.2 seconds, then hold
to 7.0s. No cuts, no crossfades. Brightness only increases.

Deliver: reel.mp4 (1080x1920, 30fps, 7.0s, silent) and card.png (1080x1350).
```

**Caption C**:
```
Comment EIGHT and I will send you the eighth one.

Seven of these are named on the card. The eighth is the one that made the other seven worth paying
for.

I was three weeks from posting a job ad. A salesperson wanted more per month than this whole stack
costs me per year, and I could not honestly say I had run out of options yet.

So I stopped looking for a person and went looking for the gap. Apollo finds who is worth talking
to. Instantly sends it and keeps the inbox warm. Gamma makes the deck. Framer puts the site up the
same afternoon. Krea does the images while I am still on the call. Mem sorts everything I capture.
Cal.com books the meeting while I sleep.

The eighth one does the part I was going to hire for, and it waits for me to approve before
anything leaves.

Comment EIGHT and I will tell you what it is.

Send this to whoever you were about to hire.

#fyp #ai #automation #business #entrepreneur
```

---

## The three DM replies, written before they are needed

If somebody comments and gets only a product name, the mechanic reads as a trick and we lose exactly
the people who made the effort. Each DM leads with the job, names the tool second, and ends with a
question that starts a conversation rather than a pitch.

**SYSTEMS**
```
The sixth one is Ultron. It runs on Claude.

It does the outbound, the research on the account and the deal itself in one place, so the four
systems above it stop being four separate logins. Nothing sends until you approve it, which is the
only reason I trust it with a client.

What are you doing for outbound right now? If it is manual I will tell you exactly where to start.
```

**SECRET**
```
All three, in order.

The one that turns a call into a proposal is Granola for the notes and Claude for the draft.
The one that finds uncalled accounts is Clay.
And the third, the one that runs both overnight and waits for your yes, is Ultron, on Claude.

The third is the one that matters. The first two produce material; it produces sent work.

What does your follow up look like today?
```

**EIGHT**
```
The eighth is Ultron. It runs on Claude.

It is the SDR I was about to hire: it researches the account, writes the sequence, runs the
follow ups and stops at your approval before anything sends. That is why I never posted the job.

How many people are you selling to a month right now? That decides whether it is worth your time.
```
