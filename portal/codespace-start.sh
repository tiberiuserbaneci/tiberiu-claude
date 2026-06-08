#!/usr/bin/env bash
# Starts the Ultron content portal in a GitHub Codespace on a Private forwarded port.
# Idempotent: runs on container start (wake) AND on attach. Self-recovers git; starts the
# server only if it is not already up, so reconnects never kill a live session.
cd "$(dirname "$0")/.." || exit 1
BRANCH="${PORTAL_BRANCH:-claude/epic-davinci-eGOGS}"

# 1) self-recover git: bail out of any stuck merge/rebase left by an earlier crash
git merge --abort 2>/dev/null
git rebase --abort 2>/dev/null

# 2) pull the latest (ours wins on conflict, so a pull can never leave the tree broken). Non-fatal if offline.
git fetch origin "$BRANCH" 2>/dev/null
git pull --no-rebase --no-edit -X ours origin "$BRANCH" 2>/dev/null || true

# 3) guarantee a readable manifest so the page can never hang on LOADING.
#    If the working copy is broken, restore the committed one; if HEAD is broken too, rebuild from disk.
if ! python3 -c "import json; json.load(open('content/portal/manifest.json'))" 2>/dev/null; then
  echo "manifest unreadable - restoring / rebuilding..."
  git checkout -- content/portal/manifest.json 2>/dev/null
  python3 -c "import json; json.load(open('content/portal/manifest.json'))" 2>/dev/null || python3 portal/scan.py
fi

# 4) start the server if it is not already running (bind 0.0.0.0 so Codespaces forwards it; port stays Private)
if pgrep -f "[p]ortal/server.py" >/dev/null 2>&1; then
  echo "Portal already running on port 8753 (Private)."
else
  PORTAL_HOST=0.0.0.0 nohup python3 portal/server.py > /tmp/portal.log 2>&1 &
  sleep 1
  if pgrep -f "[p]ortal/server.py" >/dev/null 2>&1; then
    echo "Portal started on port 8753 (Private)."
  else
    echo "Portal failed to start - last log lines:"; tail -20 /tmp/portal.log 2>/dev/null
  fi
fi
echo "Open the PORTS tab -> 'Ultron Content Portal' (8753). Private: only your GitHub login can open it."
