#!/usr/bin/env bash
# Portal watchdog. Keeps portal/server.py actually SERVING on 8753 (health-check, not just a
# process check) and restarts it within ~10s if it dies or hangs.
cd "$(dirname "$0")/.." || exit 1
LOG=/tmp/portal.log
PORT="${PORTAL_PORT:-8753}"
# only one watchdog at a time
for pid in $(pgrep -f "[p]ortal/keepalive.sh" 2>/dev/null); do
  [ "$pid" != "$$" ] && kill "$pid" 2>/dev/null
done
have_curl=0; command -v curl >/dev/null 2>&1 && have_curl=1
serving() {
  if [ "$have_curl" = 1 ]; then
    curl -fsS -o /dev/null --max-time 4 "http://127.0.0.1:${PORT}/" 2>/dev/null
  else
    pgrep -f "[p]ortal/server.py" >/dev/null 2>&1
  fi
}
while true; do
  if ! serving; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) keepalive: not serving, (re)starting" >> "$LOG"
    pkill -f "[p]ortal/server.py" 2>/dev/null; sleep 1
    PORTAL_HOST=0.0.0.0 nohup python3 portal/server.py >> "$LOG" 2>&1 &
    sleep 4
  fi
  sleep 10
done
