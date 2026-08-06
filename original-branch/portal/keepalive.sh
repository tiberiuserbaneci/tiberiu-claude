#!/usr/bin/env bash
# Portal watchdog. While the container is up, keep portal/server.py listening on 8753.
# postStart only fires when the container (re)starts; if the server process dies mid-session
# nothing brings it back - that is the "e oprit iar" case. This loop closes that gap: it
# restarts the server within ~10s of it going down. It cannot run while the container itself
# is suspended (nothing can) - that path is covered by the devcontainer postStart/postAttach.
cd "$(dirname "$0")/.." || exit 1
LOG=/tmp/portal.log

# only one watchdog at a time: kill any earlier keepalive (but not this process)
for pid in $(pgrep -f "[p]ortal/keepalive.sh" 2>/dev/null); do
  [ "$pid" != "$$" ] && kill "$pid" 2>/dev/null
done

while true; do
  if ! pgrep -f "[p]ortal/server.py" >/dev/null 2>&1; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) keepalive: server down, restarting" >> "$LOG"
    PORTAL_HOST=0.0.0.0 nohup python3 portal/server.py >> "$LOG" 2>&1 &
  fi
  sleep 10
done
