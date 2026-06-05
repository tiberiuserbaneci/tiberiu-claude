# Ultron Content Portal

Maps every material produced in this repo into one dashboard.

## Online access — recommended (secure, no public exposure)

Run it in a **GitHub Codespace** on the work branch. The portal then lives in GitHub's cloud,
on this repo, behind your GitHub login. No third-party host, no token in the browser, no public URL.

1. github.com/NexityNetwork/tiberiu-claude -> switch to branch `claude/epic-davinci-eGOGS`
2. green **Code** button -> **Codespaces** tab -> **Create codespace on claude/epic-davinci-eGOGS**
3. wait ~30s. The `.devcontainer` auto-pulls the latest materials and starts the server.
4. open the **PORTS** tab -> click **Ultron Content Portal** (port 8753). It is **Private** —
   only your GitHub login can open it.
5. use it. Mark-posted / analytics upload / cross-post auto-commit and push back to the branch.
   Click **Rescan** to pull in any new materials added since.
6. **share with Catalin:** PORTS tab -> right-click 8753 -> Port Visibility (keep Private, add
   him as a collaborator) — or he opens his own Codespace on the branch.
7. **stop when done** (saves the free Codespaces quota): Codespaces list -> ... -> Stop.

Why Codespaces and not GitHub Pages: this repo is private on a user account, so Pages would
publish the site publicly. Codespaces keeps a Private, login-gated URL with zero public exposure.

## Run locally (alternative)
```
python3 portal/server.py        # then open http://127.0.0.1:8753
```
The server is autonomous: marking a post as posted, uploading analytics, or cross-posting writes
`content/portal/manifest.json` and auto-commits (and pushes to the work branch).
Env: `PORTAL_PUSH=0` (no push), `PORTAL_PORT=xxxx`, `PORTAL_HOST=0.0.0.0` (used by Codespaces).

## Rebuild the index (after adding materials)
```
python3 portal/scan.py          # or the "Rescan" button in the UI (also git-pulls first)
```
Scans `content/`, groups materials by channel/type, parses caption files, zips carousels, renders
thumbnails for the 72 reference materials (tagged `needs-revision`), and merges with the existing
manifest so posted/analytics state is preserved. (Thumbnail rendering needs Playwright; thumbs are
already committed, so a Codespace does not need it for normal use.)

## Layout
- `.devcontainer/devcontainer.json`  Codespaces config (auto-start, Private port)
- `portal/codespace-start.sh`        pull + start the server on attach
- `portal/scan.py`                   builds the manifest
- `portal/server.py`                 serves + autonomous API (save / analytics / rescan)
- `content/portal/index.html`        the dashboard
- `content/portal/manifest.json`     the database
- `content/portal/thumbs/`, `content/portal/zips/`
- `content/analytics/`               uploaded LinkedIn/TikTok exports (CSV/XLS), one per post

## Features
LinkedIn / TikTok / Instagram menu - grid previews - single or one-click carousel zip download
(suggestive filename) - caption / ALT / first-comment copy boxes - mark posted - analytics upload
- cross-post (copy to TikTok/LinkedIn) - filters (posted, carousels, needs-revision, ...).
