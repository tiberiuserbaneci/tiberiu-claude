#!/usr/bin/env python3
# TikTok 2D coded (Model A) - HUMAN GATE. Coded approval-card UIs at 1080x1920.
import os
from playwright.sync_api import sync_playwright
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
OUT=f"{TE}/roll3/maps_docs"; os.makedirs(OUT,exist_ok=True)
F=f"file://{TE}"; ACCENT=f"file://{TE}/claude_official.png"; ULOGO="file:///home/user/tiberiu-claude/content/ultron-logo.png"
CSS=f"""
@font-face{{font-family:'DMSans';src:url('{F}/DMSans-VF.ttf');font-weight:100 900;}}
@font-face{{font-family:'DMMono';src:url('{F}/DMMono-Medium.ttf');font-weight:500;}}
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{background:#0f0f0f;}}
#artifact{{width:1080px;height:1920px;background:#161514;position:relative;overflow:hidden;font-family:'DMSans',sans-serif;padding:300px 78px 470px;display:flex;flex-direction:column;justify-content:center;}}
#artifact::before{{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(204,120,92,.05) 1.1px,transparent 1.2px);background-size:32px 32px;opacity:.5;}}
.ghost{{position:absolute;top:308px;right:150px;font-family:'DMSans';font-weight:900;font-size:250px;color:#201e1c;line-height:1;z-index:0;}}
.mark{{width:66px;height:66px;margin-bottom:12px;position:relative;z-index:2;filter:drop-shadow(0 12px 22px rgba(0,0,0,.4));}}
.eyebrow{{position:relative;z-index:2;font-family:'DMMono';font-weight:500;font-size:26px;letter-spacing:.34em;text-transform:uppercase;color:#C8643F;}}
.head{{position:relative;z-index:2;font-weight:900;font-size:96px;line-height:1.02;letter-spacing:-2px;color:#FAFAF7;margin-top:20px;}}
.head.mid{{font-size:76px;letter-spacing:-1.5px;}}
.head .o{{color:#C8643F;}}
.desc{{position:relative;z-index:2;margin-top:30px;font-weight:400;font-size:31px;line-height:1.46;color:#9a988f;max-width:910px;}}
.desc b{{color:#FAFAF7;font-weight:700;}}
.desc .fl{{display:block;color:#FAFAF7;font-weight:700;margin-top:10px;}}
.card{{position:relative;z-index:2;margin-top:34px;background:#1d1c1a;border:1px solid rgba(250,250,247,.09);border-radius:22px;padding:22px 24px;box-shadow:0 30px 70px rgba(0,0,0,.45);}}
.chead{{display:flex;align-items:center;justify-content:space-between;padding:2px 4px 13px;margin-bottom:6px;border-bottom:1px solid rgba(250,250,247,.07);}}
.chead .t{{display:flex;align-items:center;gap:13px;font-family:'DMSans';font-weight:700;font-size:27px;color:#FAFAF7;}}
.cdot{{width:12px;height:12px;border-radius:50%;background:#C8643F;flex:none;box-shadow:0 0 14px #C8643F;}}
.chead .m{{font-family:'DMMono';font-size:20px;color:#83817b;letter-spacing:.04em;}}
.tag{{font-family:'DMMono';font-weight:500;font-size:16px;letter-spacing:.12em;text-transform:uppercase;color:#94918a;background:rgba(250,250,247,.07);border-radius:6px;padding:6px 11px;}}
.tag.o{{color:#1a0f0a;background:#C8643F;}}
.row{{display:flex;align-items:center;justify-content:space-between;padding:12px 8px;}}
.row+.row{{border-top:1px solid rgba(250,250,247,.05);}}
.row .l{{display:flex;align-items:center;gap:15px;min-width:0;}}
.ic{{width:37px;height:37px;border-radius:9px;background:rgba(200,100,63,.12);border:1px solid rgba(200,100,63,.3);display:flex;align-items:center;justify-content:center;flex:none;}}
.ic svg{{width:19px;height:19px;stroke:#C8643F;stroke-width:2;fill:none;stroke-linecap:round;stroke-linejoin:round;}}
.nm{{font-weight:700;font-size:25px;color:#eceae4;}}
.sub{{font-family:'DMSans';font-weight:400;font-size:21px;color:#83817b;margin-top:2px;}}
.apa{{font-weight:800;font-size:38px;color:#FAFAF7;letter-spacing:-.5px;line-height:1.12;margin-top:6px;}}
.apm{{margin-top:12px;font-size:23px;color:#9a988f;}}.apm b{{color:#D4A27F;font-weight:700;}}
.apb{{margin-top:24px;display:flex;gap:14px;}}
.btn{{flex:1;text-align:center;border-radius:12px;padding:18px 0;font-weight:800;font-size:26px;}}
.bo{{background:#C8643F;color:#1a0f0a;box-shadow:0 0 30px rgba(200,100,63,.35);}}
.bn{{background:transparent;color:#9a988f;border:1px solid rgba(250,250,247,.14);}}
.be{{background:transparent;color:#D4A27F;border:1px solid rgba(212,162,127,.3);flex:.6;}}
.inp{{margin-top:6px;background:#26241f;border:1px solid rgba(200,100,63,.4);border-radius:14px;padding:18px 20px;font-family:'DMMono';font-size:27px;color:#FAFAF7;display:flex;align-items:center;}}
.inp .cur{{display:inline-block;width:2px;height:30px;background:#C8643F;margin-left:3px;transform:translateY(4px);}}
.fl{{display:flex;align-items:center;justify-content:space-between;gap:10px;}}
.node{{flex:1;text-align:center;background:#26241f;border:1px solid rgba(250,250,247,.1);border-radius:14px;padding:22px 8px;font-weight:800;font-size:26px;color:#cfcdc7;}}
.node.on{{background:rgba(200,100,63,.16);border-color:#C8643F;color:#FAFAF7;box-shadow:inset 0 0 0 1px rgba(200,100,63,.4);}}
.arr{{color:#C8643F;font-size:30px;font-weight:700;flex:none;}}
.ck{{color:#C8643F;font-size:24px;flex:none;width:26px;}}
.av{{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,#3a3733,#2a2825);flex:none;}}
.foot{{position:absolute;left:90px;right:150px;bottom:476px;z-index:2;display:flex;align-items:center;gap:20px;}}
.bar{{flex:1;height:7px;border-radius:4px;background:#322f2b;overflow:hidden;}}.bar i{{display:block;height:100%;background:#C8643F;border-radius:4px;}}
.pg{{font-family:'DMMono';font-size:26px;color:#83817b;letter-spacing:.06em;}}
.ulogo{{width:50px;height:50px;border-radius:50%;object-fit:cover;flex:none;}}
.url{{font-family:'DMMono';font-weight:500;font-size:30px;color:#C8643F;}}
.cover-burst{{width:330px;height:330px;align-self:center;margin:64px 0 0;position:relative;z-index:2;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5));}}
.swipe{{position:absolute;left:0;right:0;bottom:472px;display:flex;justify-content:center;z-index:3;}}
.swipe span{{display:inline-flex;align-items:center;gap:14px;background:#C8643F;color:#fff;font-weight:800;font-size:34px;padding:18px 42px;border-radius:42px;box-shadow:0 0 40px rgba(200,100,63,.4);}}
"""
def ic(p): return f'<span class="ic"><svg viewBox="0 0 24 24">{p}</svg></span>'
SENT='<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>'; CARD='<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>'
PUB='<path d="M4 4h16v12H4z"/><path d="M8 20h8"/>'; DEL='<path d="M3 6h18"/><path d="M8 6V4h8v2"/><path d="M6 6l1 14h10l1-14"/>'
CAL='<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/>'; SIGN='<path d="M5 21V5a2 2 0 0 1 2-2h7l5 5v13z"/><path d="M9 13l2 2 4-4"/>'
PLUG='<path d="M8 12a4 4 0 0 1 4-4h3a4 4 0 0 1 0 8h-1"/><path d="M16 12a4 4 0 0 1-4 4H9a4 4 0 0 1 0-8h1"/>'
def card(title,meta,body): return f'<div class="card"><div class="chead"><div class="t"><span class="cdot"></span>{title}</div><span class="m">{meta}</span></div>{body}</div>'

PIN='<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>'
def c_ask():
    def fld(k,v): return f'<div class="row"><div class="l"><span class="sub" style="font-size:22px">{k}</span></div><span class="nm" style="font-size:26px">{v}</span></div>'
    b=fld("Category","dentist")+fld("Location","Austin, TX")+fld("Max results","500")+'<div class="apb" style="margin-top:20px"><span class="btn bo">Run scrape</span></div>'
    return card("New scrape","one input",b)
def c_results():
    def place(name,rating): return f'<div class="row"><div class="l">{ic(PIN)}<span class="nm">{name}</span></div><span class="tag o">{rating}</span></div>'
    b=place("Joe Coffee","4.7")+place("Bright Dental","4.9")+place("Austin Plumbing","4.5")+place("Green Yoga","4.8")
    return card("Places found","247 total",b)
def c_fields():
    def f(k,v,acc=False): return f'<div class="row"><div class="l"><span class="nm">{k}</span></div><span class="tag{" o" if acc else ""}">{v}</span></div>'
    b=(f("Name and address","who")+f("Phone","call",True)+f("Website","visit",True)+f("Categories","what")
       +f("Rating","4.7")+f("Review count","312")+f("Opening hours","open")+f("Photo count","28")+f("Place id","key"))
    return card("Per place","9 fields",b)
def c_modes():
    def m(k,v): return f'<div class="row"><div class="l"><span class="nm">{k}</span></div><span class="sub">{v}</span></div>'
    b=m("Fast","names, ratings, reviews")+m("Full","plus phone, website, hours")+m("Reviews","a sample per place")+m("Any language","any country")
    return card("Two modes","your call",b)
def c_scale():
    chips='<div style="display:flex;gap:12px;justify-content:center;margin-top:10px"><span class="tag" style="font-size:19px;padding:11px 16px">residential proxy</span><span class="tag" style="font-size:19px;padding:11px 16px">one row per place</span></div>'
    b=f'<div style="text-align:center;padding:6px 0"><div style="font-weight:900;font-size:130px;color:#C8643F;line-height:.95">500</div><div style="font-size:26px;color:#9a988f;margin-top:8px">places per search</div></div>{chips}'
    return card("At scale","up to 500",b)
def c_pipeline():
    b='<div class="fl"><span class="node">Scrape</span><span class="arr">&rarr;</span><span class="node">Enrich</span><span class="arr">&rarr;</span><span class="node on">Outbound</span></div>'
    return card("Lead to outbound","end to end",b)
def c_comment():
    b=('<div class="row"><div class="l"><span class="av"></span><div><div class="nm" style="font-size:24px">founder_mode</div><div class="sub">send me this</div></div></div></div>'
       '<div class="row"><div class="l"><span class="av"></span><div><div class="nm" style="font-size:24px">gtm_sam</div><div class="sub">need it</div></div></div></div>'
       '<div class="inp" style="margin-top:14px;justify-content:space-between"><span>FOUNDER<span class="cur"></span></span><span class="tag o" style="padding:10px 20px;font-size:19px">Post</span></div>')
    return card("Comments","2.3k",b)

S=[
 dict(n=1,role="cover",eb=None,head='One ask.<br><span class="o">Five hundred local leads.</span>',sub="Name a category and a city. Get a clean lead list back, with phone and website.",burst=True),
 dict(n=2,role="mid",eb="The ask",head='Name a category<br><span class="o">and a city.</span>',card=c_ask(),desc='One input. Category, location, how many. <b>That is the whole brief.</b>'),
 dict(n=3,role="mid",eb="The pull",head='It walks the map<br><span class="o">for you.</span>',card=c_results(),desc='It scrolls the results, opens each place, and reads the details, patiently.'),
 dict(n=4,role="mid",eb="What you get",head='Phone, site, rating,<br><span class="o">hours. Per place.</span>',card=c_fields(),desc='Nine fields per business, the ones you need to actually reach them.'),
 dict(n=5,role="mid",eb="Fast or full",head='Names fast,<br><span class="o">or the full file.</span>',card=c_modes(),desc='Fast for a quick map, full for the phone, website and hours.'),
 dict(n=6,role="mid",eb="At scale",head='Five hundred<br><span class="o">per search.</span>',card=c_scale(),desc='Residential proxy on by default, one clean row per place.'),
 dict(n=7,role="mid",eb="To outbound",head='Straight into<br><span class="o">your outbound.</span>',card=c_pipeline(),desc='The leads flow on to enrich and contact, end to end, no copy and paste.'),
 dict(n=8,role="last",eb="Get the setup",head='Comment <span class="o">FOUNDER</span>.<br>I will send it.',card=c_comment(),desc='The local-lead scraper setup I run my company on.<span class="fl">Follow for one AI system for founders every day.</span>'),
]
N=len(S)
def html(s):
    body='' if s["role"]=="cover" else f'<div class="ghost">{s["n"]:02d}</div>'   # no number on the cover (it collides with the big hook)
    # Claude logo only on the cover (big burst). Slides 2-8 carry no mark (operator).
    if s.get("eb"): body+=f'<div class="eyebrow">{s["eb"]}</div>'
    body+=f'<div class="head{"" if s.get("burst") else " mid"}">{s["head"]}</div>'
    if s.get("sub"): body+=f'<div class="desc" style="margin-top:30px">{s["sub"]}</div>'
    if s.get("burst"): body+=f'<img class="cover-burst" src="{ACCENT}">'
    if s.get("card"): body+=s["card"]
    if s.get("desc"): body+=f'<div class="desc">{s["desc"]}</div>'
    if s["role"]=="cover": body+='<div class="swipe"><span>Swipe &#8594;</span></div>'
    elif s["role"]=="last": body+=f'<div class="foot"><img class="ulogo" src="{ULOGO}"><span class="url" style="margin-left:4px">51ultron.com</span></div>'
    else: body+=f'<div class="foot"><div class="bar"><i style="width:{int(s["n"]/N*100)}%"></i></div></div>'
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="artifact">{body}</div></body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920},device_scale_factor=2)
    for s in S:
        fp=f"{OUT}/s{s['n']}.html"; open(fp,"w").write(html(s)); pg.goto(f"file://{fp}"); pg.wait_for_timeout(450)
        m=pg.evaluate("""()=>{const a=document.getElementById('artifact');let t=1e9,b=-1e9;for(const c of a.children){if(getComputedStyle(c).position==='absolute')continue;const r=c.getBoundingClientRect();if(r.height<2)continue;t=Math.min(t,r.top);b=Math.max(b,r.bottom);}return {t:Math.round(t),b:Math.round(b)};}""")
        flag="" if (m["t"]>=300 and m["b"]<=1450) else "  <-- OUT"
        print(f"s{s['n']} [{m['t']},{m['b']}] h={m['b']-m['t']}{flag}")
        pg.locator("#artifact").screenshot(path=f"{OUT}/s{s['n']}.png")
    b.close()
from PIL import Image
ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1)]
cols=4;rows=2;sc=300;sh=int(sc*1920/1080)
st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
st.save(f"{TE}/hitl_docs_montage.png"); print("montage saved")
