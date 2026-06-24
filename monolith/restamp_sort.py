#!/usr/bin/env python3
"""On-demand sort re-stamp for the Monolith vault (owner = Tiberiu).

Browse sorts `ORDER BY created_at DESC`, and created_at is static, so renaming
an item Review -> Posted in the UI does NOT move it. Run this after marking
items posted: it reads the LIVE vault (name prefix "Posted " = posted) and
re-stamps created_at so Browse shows:

    non-posted (newest first)  ->  top
    posted                     ->  bottom

A just-posted item lands at the top of the posted block, i.e. right below the
review list - exactly the requested behaviour.

Env (source scratchpad/cfenv first):
    CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID
Usage:
    python3 monolith/restamp_sort.py            # dry-run, prints the plan
    python3 monolith/restamp_sort.py --apply    # writes to the DB
"""
import os, sys, json, subprocess, time

OWNER = "x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"   # tiberiu@nexitynetwork.org
DB    = "opencut-vault"
TAGS  = "(tags LIKE '%LinkedIn%' OR tags LIKE '%TikTok%' OR tags LIKE '%Instagram%')"
SP    = 60000   # 1 min spacing between items, enough for a stable distinct order

def wr_query(cmd):
    r = subprocess.run(["npx","--yes","wrangler@latest","d1","execute",DB,
                        "--remote","--json","--command",cmd],
                       capture_output=True, text=True)
    return json.loads(r.stdout)[0]["results"]   # stdout = clean JSON, warnings on stderr

def wr_file(path):
    subprocess.run(["npx","--yes","wrangler@latest","d1","execute",DB,
                    "--remote","--file",path], capture_output=True, text=True)

def main():
    rows = wr_query(f"SELECT id,name,created_at FROM vault_items "
                    f"WHERE owner='{OWNER}' AND {TAGS} ORDER BY created_at DESC")
    nonposted = [r for r in rows if not r["name"].startswith("Posted")]
    posted    = [r for r in rows if r["name"].startswith("Posted")]
    seq = nonposted + posted            # non-posted on top, posted at the bottom
    base = 1_780_000_000_000            # fixed base so dates stay realistic + stable
    T = base + len(seq) * SP
    sql = [f"UPDATE vault_items SET created_at={T - i*SP} "
           f"WHERE id='{r['id']}' AND owner='{OWNER}';" for i, r in enumerate(seq)]
    print(f"non-posted: {len(nonposted)}   posted: {len(posted)}   total: {len(seq)}")
    print("TOP 3:", [r["name"][:34] for r in seq[:3]])
    print("BOT 3:", [r["name"][:34] for r in seq[-3:]])
    if "--apply" in sys.argv:
        tmp = "/tmp/restamp.sql"
        open(tmp, "w").write("\n".join(sql) + "\n")
        wr_file(tmp)
        print(f"applied {len(sql)} updates.")
    else:
        print("(dry-run; pass --apply to write)")

if __name__ == "__main__":
    main()
