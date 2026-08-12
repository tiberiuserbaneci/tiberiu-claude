# Instagram - ready to post

One folder per post. Open it, upload the files, paste the caption.
Every carousel ships twice: `01.png` to `07.png` is the 1080x1920 upload, and
`tiktok-4x5/` is the same deck at 1080x1350 for TikTok's photo carousel.
Captions follow CLAUDE.md 15.6: one beat per paragraph, exactly five hashtags.

## Carousels

| Folder | Post | Keyword | Slides |
|---|---|---|---|
| `01-ceo` | BECOME A CEO IN 24 HOURS | CEO | 7 |
| `02-launch` | LAUNCH YOUR PRODUCT IN 24 HOURS | LAUNCH | 7 |
| `03-48h` | YOUR FIRST PAYING CUSTOMER IN 48 HOURS | 48H | 7 |
| `04-night` | CLOSE THE LAPTOP AT 11. WAKE UP SHIPPED. | NIGHT | 7 |
| `05-posts` | 30 DAYS OF POSTS IN ONE HOUR | POSTS | 7 |
| `06-72h` | IDEA MONDAY. REVENUE THURSDAY. | 72H | 7 |
| `07-ten` | WORK FOUR HOURS. SHIP LIKE A TEAM OF TEN. | TEN | 7 |
| `08-investors` | BECOME THE FOUNDER INVESTORS CALL BACK | INVESTORS | 7 |
| `09-engineer` | THE JOB THAT DID NOT EXIST TWO YEARS AGO | ENGINEER | 7 |
| `10-setup` | THREE THINGS MAKE CLAUDE FEEL SMARTER | SETUP | 7 |
| `11-sender` | YOUR AI NOW HAS TO SAY IT IS AN AI | SENDER | 7 |
| `12-pitch` | YOU BUILT SOMETHING GOOD | PITCH | 7, photographic |

## Reels

| Folder | Post | Keyword | Note |
|---|---|---|---|
| `toolkit-6s` | AI CREATOR TOOLKIT | TOOLKIT | ready, 6s silent. Title holds 2.5s, then the sheet fills under it. Names five third party products by operator decision (CLAUDE.md 21 suspended for this one material) |
| `film-15-pipeline` | FORTY ONE DEALS. NINE REAL. | PIPELINE | ready, first film on real geometry |
| `film-12-contract` | FOURTEEN PAGES. THREE PROBLEMS. | CONTRACT | ready, run-board model |
| `film-11-inbound` | THREE CAME IN. ONE WAS REAL. | INBOUND | ready, run-board model |
| `film-10-maybe` | ONE STALLED DEAL. ONE YES. | MAYBE | ready, run-board model |
| `film-09-pitch` | YOU BUILT SOMETHING GOOD | PITCH | ready, slate ground |
| `film-08-sender` | YOUR AI NOW HAS TO SAY IT IS AN AI | SENDER | ready |
| `film-07-setup` | THREE THINGS MAKE CLAUDE FEEL SMARTER | SETUP | ready |
| `film-06-engineer` | THE JOB THAT DID NOT EXIST TWO YEARS AGO | ENGINEER | ready, light ground |
| `film-05-48h` | YOUR FIRST PAYING CUSTOMER IN 48 HOURS | 48H | ready |
| `film-04-survive` | 88% OF AI AGENTS NEVER LEAVE THE DEMO | SURVIVE | Names two internal terms on screen (SENTINEL, HUMAN GATE). Strip before posting. |
| `film-03-price` | TEN TIMES THE PRICE FOR WORK THE SMALL MODEL FINISHES | PRICE | rebuilt, ready |
| `film-02-overnight` | YOUR STARTUP SLEEPS WHEN YOU DO | 24H | ready |
| `film-01-research` | RESEARCH EATS THE FIRST HOUR OF EVERY DEAL | CORTEX | POSTED AND UNDERPERFORMED. Names an internal term on screen. Kept for reference only. |

## LinkedIn

Reels do not go to LinkedIn as they are. The 9:16 master reserves 632px for the TikTok and
Instagram overlays and LinkedIn paints nothing there, so a third of the post is reserve
protecting nothing while the feed still scales the frame to the column width. `content/li/`
holds the 4:5 recut, its thumbnail and a long-form caption written to CLAUDE.md 15 rather
than 15.6. Cut a new one with:

    python3 content/_licut.py content/ig/<folder>/reel.mp4 content/li/<folder>/ --thumb <sec>

| Folder | Post | Keyword |
|---|---|---|
| `li/film-15-pipeline` | FORTY ONE DEALS. NINE REAL. | PIPELINE |
| `li/film-12-contract` | FOURTEEN PAGES. THREE PROBLEMS. | CONTRACT |
| `li/film-11-inbound` | THREE CAME IN. ONE WAS REAL. | INBOUND |
| `li/film-10-maybe` | ONE STALLED DEAL. ONE YES. | MAYBE |
| `li/film-09-pitch` | YOU BUILT SOMETHING GOOD | PITCH |
| `li/film-08-sender` | YOUR AI NOW HAS TO SAY IT IS AN AI | SENDER |
