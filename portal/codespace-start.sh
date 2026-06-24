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

# 2) get on the work branch (fast, LOCAL ONLY). GitHub link disabled by operator directive
#    (2026-06-24): storage moved to the Monolith account, so the portal no longer fetches or pulls
#    from origin (that GitHub traffic cost money and was unreliable). Local checkout only.
git checkout "$BRANCH" 2>/dev/null || true
echo "portal: on branch $(git branch --show-current) (offline - no origin fetch/pull)"

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
  # Make the forwarded port reachable from ANY browser (desktop + phone). A Private port returns a
  # 404 unless the browser carries the Codespaces auth - that is the daily "page can't be found".
  # Public removes that. It is safe because server.py requires a login when PORTAL_PASS is set
  # (add a PORTAL_PASS Codespaces secret to turn the password on). Best-effort; needs gh codespace scope.
  if [ -n "$CODESPACE_NAME" ]; then
    if gh codespace ports visibility 8753:public -c "$CODESPACE_NAME" >/dev/null 2>&1; then VIS="PUBLIC"; else VIS="set-failed"; fi
    URL="https://$CODESPACE_NAME-8753.app.github.dev"
  fi
  GATE=$([ -n "$PORTAL_PASS" ] && echo "password ON" || echo "no password yet")
  echo "portal: UP - ${TOTAL:-?} materials - port ${VIS:-?} - ${GATE}"
  [ -n "$URL" ] && echo "portal URL (open anywhere): $URL"
  if [ "$VIS" = "set-failed" ]; then
    echo "  auto-set-public needs a gh 'codespace' scope the default Codespace token lacks."
    echo "  FIX ONCE (persists across wakes): PORTS tab -> right-click 8753 -> Port Visibility -> Public, then reload the URL."
    echo "  (CLI alt: gh auth refresh -h github.com -s codespace   then re-run this script)"
  fi
else
  echo "portal: FAILED to bind 8753 - last log lines:"; tail -20 "$LOG" 2>/dev/null
fi
