#!/usr/bin/env bash
# Auto-starts the Ultron content portal inside a GitHub Codespace on a Private forwarded port.
# Runs on every attach. It is self-recovering and always (re)starts so the latest code is live.
cd "$(dirname "$0")/.." || exit 1
BRANCH="${PORTAL_BRANCH:-claude/epic-davinci-eGOGS}"

# 1) stop any server already running, so updated server code is picked up (bracket-trick avoids self-kill)
pkill -f "[p]ortal/server.py" 2>/dev/null && sleep 1

# 2) self-recover git: bail out of any stuck merge/rebase, drop a broken working copy of the manifest
git merge --abort 2>/dev/null
git rebase --abort 2>/dev/null
git checkout -- content/portal/manifest.json 2>/dev/null

# 3) pull the latest (ours wins on conflict, so a pull can never leave the tree broken)
git fetch origin "$BRANCH" 2>/dev/null
git pull --no-rebase --no-edit -X ours origin "$BRANCH" 2>/dev/null || true

# 3b) guarantee a readable manifest before the server starts (so the portal can never hang on LOADING).
#     If the working file is broken, restore the committed one; if HEAD is broken too, rebuild from disk.
if ! python3 -c "import json; json.load(open('content/portal/manifest.json'))" 2>/dev/null; then
  echo "manifest unreadable - restoring / rebuilding..."
  git checkout -- content/portal/manifest.json 2>/dev/null
  python3 -c "import json; json.load(open('content/portal/manifest.json'))" 2>/dev/null || python3 portal/scan.py
fi

# 4) start the server (bind 0.0.0.0 so Codespaces forwards it; the port stays Private)
PORTAL_HOST=0.0.0.0 nohup python3 portal/server.py > /tmp/portal.log 2>&1 &
sleep 1
if pgrep -f "[p]ortal/server.py" >/dev/null 2>&1; then
  echo "Portal running on port 8753 (Private)."
else
  echo "Portal failed to start - last log lines:"; tail -20 /tmp/portal.log 2>/dev/null
fi
echo "Open the PORTS tab -> 'Ultron Content Portal' (8753). Private: only your GitHub login can open it."
