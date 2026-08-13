# Run this anywhere (new terminal, Google VM, laptop)

The repo IS the state. Everything is committed and pushed to
`claude/analyze-connected-repo-rfx1r6`. Clone it, add the keys, start Claude Code, and a fresh
session reads `CLAUDE.md` and knows the whole operation. Nothing lives only in a chat.

## 1. Claude Code CLI  (needs Node 18+)

    npm install -g @anthropic-ai/claude-code
    # or the official installer:  curl -fsSL https://claude.ai/install.sh | sh

## 2. The repo + the working branch

    git clone https://github.com/tiberiuserbaneci/tiberiu-claude.git
    cd tiberiu-claude
    git checkout claude/analyze-connected-repo-rfx1r6

## 3. Python tooling  (render + image generation)

    pip install playwright pillow numpy requests
    playwright install chromium        # skip on a sandbox that pre-ships chromium; see note

## 4. Keys  (environment variables)

    export ARK_API_KEY=...             # BytePlus Seedream - the picture generator
    export ELEVENLABS_API_KEY=...      # ElevenLabs voice (only for films with voice)
    export ELEVEN_VOICE_ID=oNgAbp1vIDxEggnThC63   # your cloned voice

Optional overrides, only if needed:

    export ARK_BASE_URL=...            # force one BytePlus region
    export ARK_IMAGE_MODEL=...         # override the Seedream model id
    export PW_CHROMIUM=/path/to/chrome # point at a preinstalled Chromium

Keys never go in the repo. Put them in your shell profile or a local `.env` you do not commit.

## 5. Start

    claude                             # opens Claude Code in the repo; CLAUDE.md loads the rules

## Make one reveal reel (the house format)

    # a) generate the titleless picture
    python3 content/_seedream.py "<prompt>" --out content/ig/<slug>/picture.jpg

    # b) composite the band + hook + footer and render the mp4
    python3 content/_reveal.py content/ig/<slug>/picture.jpg "line one" "line two" \
      --accent WORD --out <slug> --render

    # c) scrub metadata before posting
    python3 content/_scrub.py content/ig/<slug>/reel.mp4

## Note on Chromium

`content/_film.py` finds a browser in this order: `PW_CHROMIUM` env, then a preinstalled
`/opt/pw-browsers/chromium-*`, then Playwright's own. On a normal machine (Google VM, laptop),
`playwright install chromium` in step 3 is enough and you set nothing. On a locked sandbox that
blocks the download but ships a browser, set `PW_CHROMIUM` to that browser instead.
