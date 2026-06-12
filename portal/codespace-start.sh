#!/usr/bin/env bash
# Starts the Ultron content portal in a GitHub Codespace on a Private forwarded port.
# Runs on container start (wake) AND on attach.
#
# SERVER-FIRST (fixes "white screen after wake"): bind port 8753 immediately from the committed
# manifest on disk, BEFORE any slow network/scan work. The old order ran git fetch + reset --hard
# + scan.py FIRST, so when the Codespace woke and the forwarded port opened, the server was not
# listening yet for 20-40s (or forever if a git step stalled) -> the auto-opened preview showed a
# blank white screen and never recovered. Now the server binds in ~2s; its own sync worker pulls
# origin immediately on boot, so the newest material still lands without blocking first paint.
cd "$(dirname "$0")/.." || exit 1
BRANCH="${PORTAL_BRANCH:-claude/epic-davinci-eGOGS}"
LOG=/tmp/portal.log

# 1) self-recover git: bail out of any stuck merge/rebase left by an earlier crash (fast, local)
git merge --abort 2>/dev/null
git rebase --abort 2>/dev/null

# 2) get on the work branch (fast, local). Only touch the network if the branch is not here yet
#    (first creation); every later wake is an instant local checkout. A Codespace left on main
#    would otherwise serve main with none of the new posters.
git checkout "$BRANCH" 2>/dev/null || { echo "portal: fetching $BRANCH ..."; git fetch origin "$BRANCH" 2>&1 | tail -1; git checkout -b "$BRANCH" "origin/$BRANCH" 2>/dev/null; }
echo "portal: on branch $(git branch --show-current)"

# 3) START THE SERVER NOW under the watchdog, before any network work. It serves the committed
#    manifest instantly and, on boot, server.py's sync worker pulls origin right away (no 15s
#    wait) so anything pushed while the Codespace was idle lands within a couple of seconds. A
#    restart is a ~1.5s blip; the page self-recovers (retries the manifest fetch every 1.5s,
#    re-renders every 8s). The watchdog restarts the server within ~10s if it ever dies.
pkill -f "[p]ortal/server.py" 2>/dev/null
pkill -f "[p]ortal/keepalive.sh" 2>/dev/null
sleep 1
nohup bash portal/keepalive.sh > /dev/null 2>&1 &

# 4) confirm it bound the port (give the watchdog a moment to spawn python)
sleep 2.5
if pgrep -f "[p]ortal/server.py" >/dev/null 2>&1; then
  TOTAL=$(python3 -c "import json;print(json.load(open('content/portal/manifest.json'))['counts']['total'])" 2>/dev/null)
  echo "portal: UP on 8753 (Private, watchdog on) - ${TOTAL:-?} materials. Newest content syncs in the background."
else
  echo "portal: FAILED to bind 8753 - last log lines:"; tail -20 "$LOG" 2>/dev/null
fi
echo "Open the PORTS tab -> 'Ultron Content Portal' (8753). Private: only your GitHub login can open it."
