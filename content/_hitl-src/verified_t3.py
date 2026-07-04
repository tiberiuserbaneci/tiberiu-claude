#!/usr/bin/env python3
# TIER 3 - I CHECKED THE LISTS. NON-RECTANGULAR silhouettes, dense, TALL (fills the band), mixed dark/ivory.
# stems: flood / test / fakes / keepers / safest / curated / rule / desk
import importlib.util
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM; shape=B.shape; circle=B.circle
ACC="200,70,35"; IV_ACC="190,70,40"
def head(tt,tag,ink="#FAFAF7",mut=MUT,acc=ACC): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:30px;color:{ink}">{tt}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.14em;color:rgb({acc})">{tag}</span></div>')
def foot(items,ink="#FAFAF7",mut=MUT,bg="#191614",bd="rgba(255,255,255,.06)",acc=ACC):
    chips="".join(f'<div style="flex:1;text-align:center;padding:22px 8px;background:{bg};border:1px solid {bd};border-radius:15px"><div style="font-family:DM Sans;font-weight:900;font-size:32px;color:rgb({acc});line-height:1">{b}</div><div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.08em;color:{mut};margin-top:9px">{s}</div></div>' for b,s in items)
    return f'<div style="display:flex;gap:13px;margin-top:24px">{chips}</div>'

W=760   # content flows to its natural height; design each panel dense enough to be ~1.19 aspect (fills the zone)
def box(inner): return f'<div style="width:{W}px">{inner}</div>'

# 1. flood - a WALL of 90 skill chips, mostly unverified, "0 receipts". Shape: slantL
def flood():
    cells=""
    for i in range(90):
        dead=(i%3!=0)
        cells+=(f'<div style="height:38px;border-radius:6px;background:{"#262320" if dead else "rgba(200,70,35,.30)"};'
          f'border:1px solid {"rgba(255,255,255,.05)" if dead else "rgba(200,70,35,.55)"}"></div>')
    inner=(f'{head("Fifty skills a list, no proof","THE FLOOD")}'
      f'<div style="display:flex;align-items:center;gap:18px;margin-bottom:16px">'
      f'<div style="display:flex;align-items:center;gap:8px"><span style="width:14px;height:14px;border-radius:4px;background:rgba(200,70,35,.30);border:1px solid rgba(200,70,35,.55)"></span><span style="font-family:DM Mono;font-size:13px;color:{MUT}">has a receipt</span></div>'
      f'<div style="display:flex;align-items:center;gap:8px"><span style="width:14px;height:14px;border-radius:4px;background:#262320;border:1px solid rgba(255,255,255,.05)"></span><span style="font-family:DM Mono;font-size:13px;color:{MUT}">unverified</span></div></div>'
      f'<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:8px;margin-bottom:20px">{cells}</div>'
      f'<div style="display:flex;align-items:center;gap:14px">'
      f'<div style="font-family:DM Mono;font-size:14px;color:{MUT}">the same recycled lists, reposted daily</div>'
      f'<div style="margin-left:auto;font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:rgb({ACC});border:1.5px solid rgb({ACC});border-radius:8px;padding:8px 15px;transform:rotate(-3deg)">0 RECEIPTS</div></div>'
      f'{foot([("50","PER LIST"),("0","VERIFIED"),("daily","REPOSTED")])}')
    return shape(box(inner),"slantL")

# 2. test - a full week log: bars + per-day run counts + job checklist. Shape: bevel
def test():
    runs=[7,8,6,9,7,8,5]
    days="".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:100%;height:{40+n*14}px;background:linear-gradient(180deg,rgb({ACC}),rgba(200,70,35,.35));border-radius:7px 7px 0 0"></div><div style="font-family:DM Sans;font-weight:800;font-size:16px;color:#e9e3d7">{n}</div><div style="font-family:DM Mono;font-size:11px;color:{MUT}">D{i+1}</div></div>' for i,n in enumerate(runs))
    jobs="".join(f'<div style="display:flex;align-items:center;gap:11px;background:#211e1b;border:1px solid rgba(255,255,255,.06);border-radius:12px;padding:15px 18px"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.6"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-weight:600;font-size:17px;color:#d7d1c6">{j}</span></div>' for j in ["briefs","drafts","builds","audits"])
    logs=[("MON 08:14","voice-draft","wrote 6 replies in my tone"),("WED 11:40","account-brief","one page, every source cited"),("FRI 16:05","carousel","10 slides, on brand tokens")]
    log="".join(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:DM Mono;font-size:12px;color:{MUT};width:100px">{ts}</span><span style="font-family:DM Sans;font-weight:700;font-size:16px;color:rgb({ACC});width:130px">{sk}</span><span style="flex:1;font-family:DM Sans;font-size:15px;color:#cfc9bd">{r}</span></div>' for ts,sk,r in logs)
    inner=(f'{head("One week on real work","THE TEST")}'
      f'<div style="display:flex;align-items:flex-end;gap:12px;height:180px;margin-bottom:20px">{days}</div>'
      f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:20px">{jobs}</div>'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:6px">SAMPLE RUNS</div>{log}'
      f'{foot([("7","DAYS"),("50","SKILLS RUN"),("0","DEMOS")])}')
    return shape(box(inner),"bevel")

# 3. fakes - strikethrough list + a big kept/cut split bar. Shape: arrow
def fakes():
    rows=""
    for lbl,ex in [("dead links","the repo is gone"),("renamed duplicates","same skill, new name"),("answers, never executes","a chatbot in a trench coat")]:
        rows+=(f'<div style="display:flex;align-items:center;gap:15px;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><path d="M18 6 6 18M6 6l12 12"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-size:19px;color:#9a9488;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">{lbl}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:{DIM};margin-top:3px">{ex}</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;color:{DIM}">cut</span></div>')
    bar=('<div style="display:flex;height:52px;border-radius:11px;overflow:hidden;margin-top:22px">'
      f'<div style="flex:33;background:repeating-linear-gradient(45deg,#2a2420,#2a2420 8px,#211d19 8px,#211d19 16px);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:18px;color:#9a9488">17 fake</div>'
      f'<div style="flex:66;background:linear-gradient(160deg,rgb({ACC}),rgba(200,70,35,.55));display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:18px;color:#1a0f0a">33 real</div></div>')
    topband=(f'<div style="display:flex;align-items:center;gap:14px;background:#211e1b;border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:16px 20px;margin-bottom:18px">'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7">50 installed</span>'
      f'<span style="font-family:DM Sans;font-size:16px;color:#cfc9bd">then run once each. three ways a skill turned out fake:</span></div>')
    inner=(f'{head("A third were made up","THE FAKES")}{topband}{rows}'
      f'<div style="display:flex;align-items:center;gap:16px;margin-top:22px">'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:56px;color:rgb({ACC});line-height:1">17<span style="font-size:26px;color:{MUT}"> / 50</span></div>'
      f'<div style="font-family:DM Mono;font-size:14px;color:{MUT}">removed without mercy before anything shipped</div></div>{bar}'
      f'{foot([("17","FAKE"),("34%","OF THE LIST"),("0","MERCY")])}')
    return shape(box(inner),"arrow")

# 4. keepers - 4 job groups, each a card with the named skills inside. Shape: tag
def keepers():
    grp=[("WRITING",["voice drafts","reply triage","captions"]),("RESEARCH",["account briefs","market scans","citations"]),
         ("DESIGN",["carousels","brand tokens"]),("BUILD",["landing pages","data pulls","fixes","tests"])]
    cards=""
    for nm,items in grp:
        lis="".join(f'<div style="display:flex;align-items:center;gap:8px;margin-top:8px"><span style="width:5px;height:5px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:15px;color:#cfc9bd">{x}</span></div>' for x in items)
        cards+=(f'<div style="background:#211e1b;border:1px solid rgba(200,70,35,.22);border-radius:16px;padding:18px 20px">'
          f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">{nm}</span><span style="font-family:DM Sans;font-weight:900;font-size:28px;color:#FAFAF7;line-height:1">{len(items)}</span></div>{lis}</div>')
    inner=(f'{head("What survived earns its slot","THE KEEPERS")}'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:14px">TWELVE SKILLS, GROUPED BY THE JOB THEY FINISH</div>'
      f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px">{cards}</div>'
      f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(160deg,rgba(200,70,35,.14),rgba(200,70,35,.04));border:1px solid rgba(200,70,35,.34);border-radius:15px;padding:18px 22px;margin-top:16px">'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:28px;color:#FAFAF7">38 tried</span>'
      f'<svg width="46" height="24" viewBox="0 0 46 24" style="flex-shrink:0"><path d="M2 12 H36 M28 5 L44 12 L28 19" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:28px;color:rgb({ACC})">12 kept</span>'
      f'<span style="margin-left:auto;font-family:DM Mono;font-size:13px;color:{MUT}">the rest were advice, not tools</span></div>'
      f'{foot([("12","KEPT"),("4","JOB GROUPS"),("100%","EXECUTE")])}')
    return shape(box(inner),"tag",pad="34px 48px")

# 5. safest - install-order dial (round element, fills naturally). circle
def safest():
    steps=[("1","First-party","the two built by Anthropic"),("2","Verified layer","community, but tested"),("3","Your desk","only what survives")]
    rows="".join(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:16px;width:440px"><div style="flex-shrink:0;width:46px;height:46px;border-radius:50%;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:22px;display:flex;align-items:center;justify-content:center">{n}</div><div><div style="font-family:DM Sans;font-weight:800;font-size:21px;color:#FAFAF7">{a}</div><div style="font-family:DM Mono;font-size:13px;color:{MUT}">{b}</div></div></div>' for n,a,b in steps)
    inner=(f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.16em;color:rgb({ACC});margin-bottom:8px;text-align:center">THE ORDER</div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;margin-bottom:26px;text-align:center;line-height:1.12">The safe<br>install order</div>{rows}')
    return circle(inner,size=760)

# 6. curated - Ultron techniques library, IVORY panel, 6 tested items + badge. Shape: notch2
def curated():
    ivink="#2a2016"; ivmut="#8a745a"
    items="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:16px 0;border-bottom:1px solid rgba(120,95,60,.16)"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({IV_ACC})" stroke-width="2.6"><path d="M20 6 9 17l-5-5"/></svg><span style="flex:1;font-family:DM Sans;font-weight:600;font-size:18px;color:{ivink}">{a}</span><span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:rgb({IV_ACC})">v{v} · TESTED</span></div>' for a,v in [("research briefs","2.1"),("outbound sequences","3.0"),("proposal decks","1.4"),("content carousels","2.2"),("legal redlines","1.1"),("deal scorecards","1.0")])
    badge=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,rgba(190,70,40,.12),rgba(190,70,40,.03));border:1px solid rgba(190,70,40,.3);border-radius:16px;padding:18px 22px;margin-bottom:16px">'
      f'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="rgb({IV_ACC})" stroke-width="1.8"><path d="M12 2 4 5v6c0 5 3.5 8 8 11 4.5-3 8-6 8-11V5z"/><path d="M9 12l2 2 4-4"/></svg>'
      f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:900;font-size:22px;color:{ivink}">Every skill has a receipt</div><div style="font-family:DM Mono;font-size:13px;color:{ivmut}">version-pinned, run on real work, before your desk sees it</div></div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:rgb({IV_ACC})">6/6</div></div>')
    inner=(f'{head("Ultron ships them pre-verified","CURATED",ink=ivink,mut=ivmut,acc=IV_ACC)}{badge}'
      f'<div style="background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-radius:16px;padding:8px 22px">{items}</div>'
      f'<div style="font-family:DM Mono;font-size:14px;color:{ivmut};margin-top:16px">the techniques library, curated and tested before it reaches your desk</div>'
      f'{foot([("100%","PRE-TESTED"),("0","DEAD LINKS"),("1","LIBRARY")],ink=ivink,mut=ivmut,bg="rgba(255,255,255,.6)",bd="rgba(120,95,60,.16)",acc=IV_ACC)}')
    return shape(box(inner),"notch2",iv=True)

# 7. rule - execute vs advice split, each column with bullets. Shape: slantR
def rule():
    def col(lbl,big,sub,items,on):
        bg="linear-gradient(160deg,rgba(200,70,35,.16),rgba(200,70,35,.05))" if on else "#211d19"
        bd="rgba(200,70,35,.4)" if on else "rgba(255,255,255,.14)"
        lc=f"rgb({ACC})" if on else MUT; big_c="#FAFAF7"
        lis="".join(f'<div style="display:flex;align-items:center;gap:10px;margin-top:15px"><span style="flex-shrink:0;width:7px;height:7px;border-radius:50%;background:{lc}"></span><span style="font-family:DM Sans;font-size:16px;color:{"#d7d1c6" if on else DIM}">{x}</span></div>' for x in items)
        sh="box-shadow:0 0 40px rgba(200,70,35,.12)" if on else ""
        return (f'<div style="flex:1;background:{bg};border:1px {"solid" if on else "dashed"} {bd};border-radius:18px;padding:26px 24px">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{lc};margin-bottom:12px">{lbl}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:{big_c}">{big}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:{lc};margin-top:6px;padding-bottom:16px;border-bottom:1px solid {bd}">{sub}</div>{lis}</div>')
    band=(f'<div style="display:flex;align-items:center;gap:14px;background:#211e1b;border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:16px 20px;margin-bottom:16px">'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({ACC})">1 test</span>'
      f'<span style="font-family:DM Sans;font-size:16px;color:#cfc9bd">did the skill hand back a finished artifact, or just talk about one?</span></div>')
    inner=(f'{head("Execute, or it does not count","THE RULE")}{band}'
      f'<div style="display:flex;gap:16px;margin-top:2px">'
      f'{col("ADVICE","a bookmark","returns words, finishes nothing",["saved, never opened","no file, no draft","you still do the work","looks smart, ships zero","another tab to forget"],False)}'
      f'{col("EXECUTION","a finished job","hands back the artifact",["the draft, written","the deck, built","the audit, delivered","the email, queued","the PR, opened"],True)}</div>'
      f'<div style="display:flex;align-items:center;gap:12px;margin-top:16px;background:linear-gradient(160deg,rgba(200,70,35,.14),rgba(200,70,35,.04));border:1px solid rgba(200,70,35,.34);border-radius:14px;padding:16px 22px">'
      f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><path d="M20 6 9 17l-5-5"/></svg>'
      f'<span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">Keep the right column. Delete the left.</span></div>'
      f'{foot([("execute","OR NOTHING"),("0","BOOKMARKS"),("1","RULE")])}')
    return shape(box(inner),"slantR")

# 8. desk - 12 survivor skills grid + a daily-uptime strip. Shape: notch
def desk():
    names=["voice","triage","briefs","scans","carousel","tokens","pages","pulls","fixes","tests","redlines","scores"]
    tiles="".join(f'<div style="height:140px;border-radius:16px;background:linear-gradient(160deg,#302c27,#211d19);border:1px solid rgba(200,70,35,.2);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px"><div style="width:12px;height:12px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 14px rgba(200,70,35,.7)"></div><div style="font-family:DM Sans;font-weight:700;font-size:16px;color:#e9e3d7">{n}</div><div style="font-family:DM Mono;font-size:10px;color:{MUT}">live</div></div>' for n in names)
    strip="".join(f'<div style="flex:1;height:16px;border-radius:4px;background:rgb({ACC});opacity:{0.4+0.05*(i%4)}"></div>' for i in range(14))
    inner=(f'{head("My desk runs on survivors","THE DESK")}'
      f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:13px">{tiles}</div>'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin:22px 0 12px">TWO WEEKS OF DAILY RUNS, EACH TESTED ON MY OWN PIPELINE</div>'
      f'<div style="display:flex;gap:6px">{strip}</div>'
      f'{foot([("12","SURVIVORS"),("daily","RUNNING"),("quality","OVER COUNT")])}')
    return shape(box(inner),"notch")

PANELS={"flood":flood(),"test":test(),"fakes":fakes(),"keepers":keepers(),
        "safest":safest(),"curated":curated(),"rule":rule(),"desk":desk()}
if __name__=="__main__":
    print("verified t3:"); B.render("verified",PANELS)
