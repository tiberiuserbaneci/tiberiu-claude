#!/bin/bash
# finish_material.sh <slug> <NAME substring>
# Build the eyes-bar deck for a rebuilt {slug}_t3.py and push IG (1920) + TikTok (1350) to the vault.
SLUG="$1"; NAME="$2"
HS=/home/user/tiberiu-claude/content/_hitl-src
SC=/home/user/tiberiu-claude/scratchpad
cd "$HS" || exit 1
timeout 140 python3 adapt_build.py "$SLUG" || { echo "BUILD FAIL $SLUG"; exit 1; }
timeout 80 python3 to916.py "$SC/${SLUG}_ig" || { echo "TO916 FAIL $SLUG"; exit 1; }
cd /home/user/tiberiu-claude || exit 1
source scratchpad/cfenv
python3 monolith/push_dense_ig.py "$SLUG" "$NAME" || echo "IG PUSH FAIL $SLUG"
sleep 5
python3 monolith/push_dense_tt.py "$SLUG" "$NAME" || echo "TT PUSH FAIL $SLUG"
echo "FINISHED $SLUG"
