# Ultron Content Portal

Maps every material produced in this repo into one dashboard.

## Run
```
python3 portal/server.py
# open http://127.0.0.1:8753
```
The server is autonomous: marking a post as posted, uploading analytics, or cross-posting
writes `content/portal/manifest.json` and auto-commits (and pushes to the work branch).
Disable push with `PORTAL_PUSH=0`, change port with `PORTAL_PORT=xxxx`.

## Rebuild the index (after adding materials)
```
python3 portal/scan.py        # or the "Rescan" button in the UI
```
Scans `content/`, groups materials by channel/type, parses caption files, zips carousels,
renders thumbnails for the 72 reference materials (tagged `needs-revision`), and merges with
the existing manifest so posted/analytics state is preserved.

## Layout
- `portal/scan.py`        builds the manifest
- `portal/server.py`      serves + autonomous API (save / analytics / rescan)
- `content/portal/index.html`   the dashboard
- `content/portal/manifest.json` the database
- `content/portal/thumbs/`, `content/portal/zips/`
- `content/analytics/`    uploaded LinkedIn/TikTok exports (CSV/XLS), one per post

## Features
LinkedIn / TikTok / Instagram menu - grid previews - single or one-click carousel zip download
(suggestive filename) - caption / ALT / first-comment copy boxes - mark posted - analytics upload
- cross-post (copy to TikTok/LinkedIn) - filters (posted, carousels, needs-revision, ...).
