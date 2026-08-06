# LinkedIn cuts

One folder per post, holding the 4:5 recut, its thumbnail and the LinkedIn caption.

## Why 1080x1350 and not the 9:16 master

The 9:16 master is built to CLAUDE.md 9's vertical safe zones: 300px reserved at the top for
TikTok's tabs and search bar, 330px at the bottom for the caption and progress rail. That is
632px, a third of the frame, deliberately left empty so the platform UI has somewhere to sit.

LinkedIn paints nothing there. Uploading the 9:16 master to LinkedIn is valid - its feed video
accepts anything from 1:2.4 to 2.4:1, so 0.5625 is well inside - but the feed scales the whole
frame to the column width, so a third of the height the post occupies is reserve that no longer
protects anything, and the content renders smaller for it.

So the LinkedIn cut is a crop, never a re-render: `crop=1080:1350:0:<top>`, where the top is
chosen to centre the measured content band. Measured on episode 08, content spans y 300 to 1588
of 1920, which is 1288 tall and fits 1350 with 32px clear top and bottom. Verify per film before
publishing - a film whose captions roam wider than the safe band would clip:

    python3 content/_licut.py content/ig/<folder>/reel.mp4 content/li/<folder>/

The caption is not the reel caption. Reels run CLAUDE.md 15.6 - one beat per paragraph, short.
LinkedIn runs 15: five blocks, 400 to 470 words, an arrow list, the fixed CTA, plus ALT text and
a first comment carrying the link.
