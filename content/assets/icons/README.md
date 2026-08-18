# Brand marks for third party products

Only for materials where the operator has explicitly approved naming third party products
(CLAUDE.md 21 allows Claude, AI and Ultron by default, and CLAUDE.md 18 treats a third party
logo in a commercial piece as a separate permission). Drop a mark here and the material can
inline it; the renderer has no network, so it must be a local file.

## What is reachable from this environment

The agent proxy refuses most CDNs on the CONNECT tunnel. Measured 2026-08-12:

| host | result |
|---|---|
| `raw.githubusercontent.com` | 200, works |
| `registry.npmjs.org` | 200, works |
| `cdn.jsdelivr.net` | 403 on the tunnel |
| `unpkg.com` | unreachable |
| `cdn.simpleicons.org` | unreachable |
| `api.iconify.design` | unreachable |

So Simple Icons is fetchable one file at a time off raw.githubusercontent:

    curl -s -o content/assets/icons/<slug>.svg \
      https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/<slug>.svg

## What is actually here, and what is missing

`notion.svg` is the real Simple Icons mark.

Simple Icons does NOT carry openai, canva, midjourney or copy.ai under those slugs (all 404 on
2026-08-12), and those four are what the creator toolkit reel needs. They have to come from the
operator as files. A hand drawn approximation was tried and rejected on sight, correctly: an
inaccurate mark inside an infographic about that exact product is the first thing anyone sees.
