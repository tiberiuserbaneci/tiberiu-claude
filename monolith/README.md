# Monolith vault ops

Tooling for the Ultron Monolith Library (app: **edits.51ultron.com**), driven headlessly
via Cloudflare `wrangler` + the R2 REST API. Storage of materials lives **exclusively** in
this account now (see CLAUDE.md §2); this repo is the reference/model archive.

## Account
- **Owner (Tiberiu):** `x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3` = tiberiu@nexitynetwork.org
- **D1 (Library):** `opencut-vault` (binding `VAULT_DB`) - table `vault_items`
- **R2 (media):** `ultron-reels`, keys under `imports/` (served by the app's import-from-url route)
- **Categories = tags:** `LinkedIn` / `TikTok` / `Instagram` (Browse sidebar = distinct `tags`)
- **Title status convention:** `Posted <name>` / `Review <name>` (drives the sort below)

## Credentials (never committed)
Set in the session env (e.g. `source scratchpad/cfenv`):
```
CLOUDFLARE_API_TOKEN=<monolith-operator token, scoped>
CLOUDFLARE_ACCOUNT_ID=9329dd27959dfe8804ff27e1d5d50b29
```

## restamp_sort.py - on-demand Browse ordering
Browse sorts `ORDER BY created_at DESC` (static). This re-stamps `created_at` from the LIVE
vault so non-posted items (newest first) sit on top and posted items sink to the bottom.
Run it **after** renaming items `Review -> Posted` in the UI:
```
source scratchpad/cfenv
python3 monolith/restamp_sort.py            # dry-run, prints top/bottom
python3 monolith/restamp_sort.py --apply    # writes
```
A just-posted item lands at the top of the posted block (right below the review list).
