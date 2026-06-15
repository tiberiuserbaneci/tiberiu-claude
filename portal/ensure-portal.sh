#!/usr/bin/env bash
# Idempotent portal launcher. Wired as a SessionStart hook in .claude/settings.json so the
# DYNAMIC management portal (mark-posted / analytics / cross-post - the things Pages cannot do)
# auto-(re)starts every time the session wakes from idle. Nothing can run while the container is
# suspended; this brings the portal back the instant we are live again, so there is no more manual
# "reporneste portalul". If the server is already listening, it does nothing.
cd "$(dirname "$0")/.." 2>/dev/null || exit 0
pgrep -f "[p]ortal/server.py" >/dev/null 2>&1 && exit 0     # already up -> no-op
# fully detached (setsid + closed stdin) so it survives the hook's process group and keeps serving
setsid bash -c 'PORTAL_HOST=0.0.0.0 PORTAL_PORT=8753 exec python3 portal/server.py' >>/tmp/portal.log 2>&1 < /dev/null &
exit 0
