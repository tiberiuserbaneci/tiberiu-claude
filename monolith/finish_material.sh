#!/bin/bash
# finish_material.sh <slug> <NAME substring>
# Build the eyes-bar deck for a rebuilt {slug}_t3.py and push IG (1920) + TikTok (1350) to the vault.
set -e
SLUG="$1"; NAME="$2"
HS=/home/user/tiberiu-claude/content/_hitl-src
SC=/home/user/tiberiu-claude/scratchpad
cd "$HS"
timeout 130 python3 adapt_build.py "$SLUG"
timeout 70 python3 to916.py "$SC/${SLUG}_ig"
cd /home/user/tiberiu-claude
source scratchpad/cfenv
python3 monolith/push_dense_ig.py "$SLUG" "$NAME"
sleep 4
python3 monolith/push_dense_tt.py "$SLUG" "$NAME"
echo "FINISHED $SLUG"
