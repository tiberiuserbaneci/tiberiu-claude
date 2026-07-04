#!/bin/bash
# finish_batch.sh — process a list of "slug|NAME substring" lines sequentially through finish_material.sh
# Usage: bash finish_batch.sh < pairs.txt   (or pass a file: bash finish_batch.sh pairs.txt)
IN="${1:-/dev/stdin}"
while IFS='|' read -r slug name; do
  [ -z "$slug" ] && continue
  echo "===== $slug ====="
  bash /home/user/tiberiu-claude/monolith/finish_material.sh "$slug" "$name"
  sleep 3
done < "$IN"
echo "BATCH DONE"
