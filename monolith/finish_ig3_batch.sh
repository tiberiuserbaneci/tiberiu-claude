#!/bin/bash
# finish_ig3_batch.sh <slug> [<slug> ...]
# For each slug: look up row_id from scratchpad/ig3_map.json, then finish_scraped3.sh (build+to916+push).
# Skips a slug whose panels or build file are missing. Prints a compact per-slug status line.
cd /home/user/tiberiu-claude || exit 1
for SLUG in "$@"; do
  RID=$(python3 -c "import json;m=json.load(open('scratchpad/ig3_map.json'));r=[o['row_id'] for o in m if o['slug']=='$SLUG'];print(r[0] if r else '')")
  if [ -z "$RID" ]; then echo "SKIP $SLUG (no row_id)"; continue; fi
  np=$(ls content/_hitl-src/models_clay/$SLUG/*.png 2>/dev/null | wc -l)
  if [ ! -f content/_hitl-src/build_$SLUG.py ] || [ "$np" -lt 8 ]; then echo "SKIP $SLUG (build?=$([ -f content/_hitl-src/build_$SLUG.py ]&&echo y||echo n) panels=$np)"; continue; fi
  bash monolith/finish_scraped3.sh "$SLUG" "$RID" 2>&1 | tail -3
done
