#!/usr/bin/env bash
# Starts the Ultron content portal in a GitHub Codespace on a Private forwarded port.
# Runs on container start (wake) AND on attach. Every run: get on the work branch, pull the
# latest content, REBUILD the manifest from the files on disk, and RESTART the server so the
# newest code and material always take effect. This is what keeps the portal from going stale.
cd "$(dirname "$0")/.." || exit 1
BRANCH="${PORTAL_BRANCH:-claude/epic-davinci-eGOGS}"
LOG=/tmp/portal.log

# 1) self-recover git: bail out of any stuck merge/rebase left by an earlier crash
git merge --abort 2>/dev/null
git rebase --abort 2>/dev/null

# 2) make sure we are ON the work branch. A Codespace created from main would otherwise
#    serve main (no new posters) no matter how many times you Rescan.
git fetch origin "$BRANCH" 2>&1 | tail -1
git checkout "$BRANCH" 2>/dev/null || git checkout -b "$BRANCH" "origin/$BRANCH" 2>/dev/null
echo "portal: on branch $(git branch --show-current)"

# 3) pull the latest. -X ours = local portal edits (posted toggles) win on conflict; brand-new
#    files (new posters) have no local version, so they always land. Show the result, never hide it.
echo "portal: pulling origin/$BRANCH ..."
git pull --no-rebase --no-edit -X ours origin "$BRANCH" 2>&1 | tail -3

# 4) rebuild the manifest from the files actually on disk. This recovers any material the merge
#    did not write into the manifest text; the scanner preserves posted/analytics state.
echo "portal: reindexing ..."
python3 portal/scan.py 2>&1 | tail -1 || git checkout -- content/portal/manifest.json 2>/dev/null

# 5) RESTART the server so the running process is always the latest server.py (an old process
#    means the auto-sync/auto-refresh fixes never load). A restart is a ~1.5s blip; the page
#    auto-recovers because it retries the manifest fetch.
pkill -f "[p]ortal/server.py" 2>/dev/null && sleep 1
PORTAL_HOST=0.0.0.0 nohup python3 portal/server.py > "$LOG" 2>&1 &
sleep 1.5
if pgrep -f "[p]ortal/server.py" >/dev/null 2>&1; then
  TOTAL=$(python3 -c "import json;print(json.load(open('content/portal/manifest.json'))['counts']['total'])" 2>/dev/null)
  echo "portal: started on port 8753 (Private) - ${TOTAL:-?} materials."
else
  echo "portal: FAILED to start - last log lines:"; tail -20 "$LOG" 2>/dev/null
fi
echo "Open the PORTS tab -> 'Ultron Content Portal' (8753). Private: only your GitHub login can open it."
