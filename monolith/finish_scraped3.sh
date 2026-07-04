#!/bin/bash
# finish_scraped2.sh <slug> <row_id>
# Build a new IG Scraped 2 deck from build_{slug}.py (+ {slug}_t3.py panels) and push IG+TT to its row.
SLUG="$1"; RID="$2"
HS=/home/user/tiberiu-claude/content/_hitl-src
SC=/home/user/tiberiu-claude/scratchpad
cd "$HS" || exit 1
timeout 130 python3 build_ed45.py "build_${SLUG}.py" "$SLUG" || { echo "BUILD FAIL $SLUG"; exit 1; }
timeout 80 python3 to916.py "$SC/${SLUG}_ig" || { echo "TO916 FAIL $SLUG"; exit 1; }
cd /home/user/tiberiu-claude || exit 1
source scratchpad/cfenv
python3 monolith/push_scraped3.py "$SLUG" "$RID" || echo "PUSH FAIL $SLUG"
echo "FINISHED $SLUG"
