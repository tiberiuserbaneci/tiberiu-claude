#!/usr/bin/env bash
# Auto-starts the content portal inside a GitHub Codespace, on a Private forwarded port.
# Runs on every attach (idempotent): pulls the latest materials, then (re)starts the server.
set -e
cd "$(dirname "$0")/.."
BRANCH="${PORTAL_BRANCH:-claude/epic-davinci-eGOGS}"
git pull --no-rebase --no-edit origin "$BRANCH" 2>/dev/null || true
if pgrep -f "portal/server.py" >/dev/null 2>&1; then
  echo "Portal already running on port 8753."
else
  PORTAL_HOST=0.0.0.0 nohup python3 portal/server.py > /tmp/portal.log 2>&1 &
  sleep 1
  echo "Portal started on port 8753 (Private)."
fi
echo "Open the PORTS tab -> 'Ultron Content Portal' (8753). It is Private: only your GitHub login can open it."
