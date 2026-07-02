#!/usr/bin/env python3
# Genereaza build_<slug>.py pentru fiecare adaptare si ruleaza build_ed45.
# Usage: python3 adapt_build.py [slugs...]
import sys, os, subprocess, importlib.util
ROOT="/home/user/tiberiu-claude"
def _load(name,p):
    s=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
S=_load("S",f"{ROOT}/content/_hitl-src/adapt_specs.py")

TPL='''#!/usr/bin/env python3
# {title} - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","{root}/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="{root}/content/_hitl-src/models_clay/{slug}"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT={accent}; T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo({cw!r})],[co({ca!r})]])
T2.CONTENT=[
{slides}
]
T2.CTA=("SAVE THIS", [[wo({ctaw!r})],[co({ctaa!r})]], f"{{LIB}}/cta3d-{pill}.png", 0.92)
T2.CLOSE=dict(l1={l1!r},l2={l2!r},q={q!r})
MARK2="{mark}"
'''

def emit(d):
    rows=[]
    for (eb,(hw,ha),sub,foot,stem) in [(s[0],s[1],s[2],s[3],s[4]) for s in d["slides"]]:
        f0=foot[0]
        rows.append(f' ({eb!r}, [[wo({hw!r})],[co({ha!r})]], {sub!r}, [co({f0!r})], f"{{M}}/{stem}.png", 1.0),')
    kw=d["pill"].upper()
    src=TPL.format(title=d["title"],root=ROOT,slug=d["slug"],accent=tuple(d["accent"]),
        cw=d["cover"][0],ca=d["cover"][1],slides="\n".join(rows),
        ctaw="Want the playbook?",ctaa=f"comment {kw}.",pill=d["pill"],
        l1=d["close"][0],l2=d["close"][1],q=d["close"][2],mark=d["mark"])
    p=f"{ROOT}/content/_hitl-src/build_{d['slug']}.py"
    open(p,"w").write(src)
    return p

if __name__=="__main__":
    slugs=sys.argv[1:] or [d["slug"] for d in S.ALL]
    for d in S.ALL:
        if d["slug"] not in slugs: continue
        p=emit(d)
        r=subprocess.run(["python3",f"{ROOT}/content/_hitl-src/build_ed45.py",p,d["slug"]],capture_output=True,text=True)
        print(d["slug"], r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-200:])
