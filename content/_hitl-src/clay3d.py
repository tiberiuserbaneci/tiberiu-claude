#!/usr/bin/env python3
# CLAY3D - coded-3D panel engine (operator 2026-07-02: "design 3D executat din cod").
# Dark-clay recipe (claymorphism adapted to Dark Ultron): layered tinted drop shadows,
# inset top-left highlight, inset bottom pooling, hue-tinted rim glow. Rendered via
# headless Chromium with omit_background -> REAL-ALPHA RGBA panels, exact DM Sans text
# (zero garble), pixel-exact density, zero generation cost. Same front-on view on every
# panel by construction. Usage: python3 clay3d.py <set> [stems...]
import sys, os, base64
from playwright.sync_api import sync_playwright

ROOT="/home/user/tiberiu-claude"; ASSETS=f"{ROOT}/content/assets"
def b64f(p): return base64.b64encode(open(p,"rb").read()).decode()
ORB=b64f(f"{ROOT}/content/ultron-logo.png")

def css(acc):
    return f"""
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-500.ttf');font-weight:500}}
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-700.ttf');font-weight:700}}
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-800.ttf');font-weight:800}}
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-900.ttf');font-weight:900}}
@font-face{{font-family:'DM Mono';src:url('file://{ASSETS}/DMMono-500.ttf');font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'DM Sans',sans-serif}}
body{{background:transparent;padding:90px}}
.panel{{
  width:620px;background:linear-gradient(162deg,#282826 0%,#1e1e1c 58%,#191917 100%);
  border-radius:34px;padding:30px;position:relative;
  border:1px solid rgba(255,255,255,.055);
  box-shadow:
    0 42px 80px rgba(0,0,0,.58),
    0 16px 34px rgba(0,0,0,.44),
    0 0 110px rgba({acc},.11),
    inset 0 2px 3px rgba(255,255,255,.10),
    inset 3px 3px 14px rgba(255,255,255,.035),
    inset 0 -12px 26px rgba(0,0,0,.42);
}}
.hd{{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}}
.hd .t{{font-weight:800;font-size:24px;color:#FAFAF7;letter-spacing:-.2px}}
.hd .tag{{font-family:'DM Mono',monospace;font-size:12.5px;letter-spacing:.14em;color:rgb({acc})}}
.row{{
  background:linear-gradient(160deg,#2e2e2b,#242422);border-radius:18px;padding:15px 18px;
  display:flex;align-items:center;gap:13px;margin-bottom:12px;
  border:1px solid rgba(255,255,255,.045);
  box-shadow:0 8px 18px rgba(0,0,0,.35), inset 0 1.5px 2px rgba(255,255,255,.08), inset 0 -6px 14px rgba(0,0,0,.28);
}}
.row:last-child{{margin-bottom:0}}
.dot{{width:26px;height:26px;border-radius:50%;flex-shrink:0;
  background:radial-gradient(circle at 34% 30%, rgb({acc}), rgba({acc},.55));
  box-shadow:0 4px 9px rgba(0,0,0,.4), inset 0 1.5px 2px rgba(255,255,255,.35)}}
.rn{{font-weight:700;font-size:18.5px;color:#FAFAF7}}
.rs{{font-weight:500;font-size:13.5px;color:#8f8f85;margin-top:2px}}
.chip{{
  margin-left:auto;flex-shrink:0;background:linear-gradient(160deg,rgb({acc}),rgba({acc},.82));
  color:#fff;font-weight:800;font-size:14.5px;border-radius:999px;padding:8px 17px;
  box-shadow:0 6px 14px rgba({acc},.35), inset 0 1.5px 2px rgba(255,255,255,.4), inset 0 -4px 8px rgba(0,0,0,.22)}}
.ghostchip{{margin-left:auto;flex-shrink:0;border:1.6px solid rgba(250,250,247,.3);color:rgba(250,250,247,.72);
  font-weight:700;font-size:14px;border-radius:999px;padding:7px 16px}}
.skel{{height:9px;border-radius:5px;background:rgba(250,250,247,.14)}}
.skel.s2{{width:62%;background:rgba(250,250,247,.09)}}
.bar{{height:13px;border-radius:7px;background:rgba(250,250,247,.10);overflow:hidden;position:relative}}
.bar i{{position:absolute;inset:0;width:var(--w);border-radius:7px;
  background:linear-gradient(90deg,rgba({acc},.85),rgb({acc}));
  box-shadow:inset 0 1.5px 2px rgba(255,255,255,.35)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;font-weight:800;font-size:17px;
  border-radius:999px;padding:13px 30px;
  background:linear-gradient(160deg,rgb({acc}),rgba({acc},.8));color:#fff;
  box-shadow:0 10px 22px rgba({acc},.4), 0 3px 8px rgba(0,0,0,.35), inset 0 2px 2.5px rgba(255,255,255,.45), inset 0 -6px 12px rgba(0,0,0,.25)}}
.btn.ghost{{background:transparent;color:rgba(250,250,247,.8);border:2px solid rgba(250,250,247,.3);
  box-shadow:inset 0 1.5px 2px rgba(255,255,255,.06)}}
.cols{{display:flex;gap:14px}}
.col{{flex:1;background:linear-gradient(160deg,#2c2c2a,#232321);border-radius:18px;padding:14px;
  border:1px solid rgba(255,255,255,.04);
  box-shadow:0 8px 18px rgba(0,0,0,.32), inset 0 1.5px 2px rgba(255,255,255,.07), inset 0 -6px 14px rgba(0,0,0,.26)}}
.col .cl{{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.1em;color:#8f8f85;margin-bottom:10px}}
.mini{{background:linear-gradient(160deg,#353532,#2a2a27);border-radius:12px;padding:11px;margin-bottom:9px;
  box-shadow:0 5px 11px rgba(0,0,0,.3), inset 0 1px 1.5px rgba(255,255,255,.08)}}
.mini.on{{background:linear-gradient(160deg,rgb({acc}),rgba({acc},.78));
  box-shadow:0 7px 16px rgba({acc},.4), inset 0 1.5px 2px rgba(255,255,255,.4), inset 0 -5px 10px rgba(0,0,0,.22)}}
.mini .mt{{font-weight:700;font-size:14px;color:#FAFAF7}}
.mini .ms{{font-weight:500;font-size:11.5px;color:rgba(250,250,247,.55);margin-top:2px}}
.mini.on .ms{{color:rgba(255,255,255,.8)}}
.strike{{text-decoration:line-through;text-decoration-color:rgba(178,96,62,.9);text-decoration-thickness:2.5px}}
.price{{margin-left:auto;font-weight:800;font-size:17px;color:#8f8f85}}
.panel.terra{{background:linear-gradient(158deg,#d98a63 0%,#b2603e 46%,#8a4630 100%);
  border:1px solid rgba(255,255,255,.16);
  box-shadow:0 42px 80px rgba(0,0,0,.5),0 16px 34px rgba(0,0,0,.38),0 0 120px rgba({acc},.2),
   inset 0 2.5px 3px rgba(255,255,255,.35), inset 4px 4px 16px rgba(255,255,255,.12), inset 0 -14px 30px rgba(90,35,18,.5)}}
.panel.terra .hd .t{{color:#fff}} .panel.terra .hd .tag{{color:rgba(255,240,232,.85)}}
.panel.terra .row{{background:linear-gradient(160deg,rgba(255,255,255,.16),rgba(255,255,255,.06));border-color:rgba(255,255,255,.14);
  box-shadow:0 8px 18px rgba(90,35,18,.35), inset 0 1.5px 2px rgba(255,255,255,.22)}}
.panel.terra .rn{{color:#fff}} .panel.terra .rs{{color:rgba(255,236,226,.75)}}
.panel.kraft{{background:linear-gradient(158deg,#e0b98f 0%,#c99a6d 48%,#a97a52 100%);
  border:1px solid rgba(255,255,255,.2);border-radius:52px;
  box-shadow:0 42px 80px rgba(0,0,0,.44),0 16px 34px rgba(0,0,0,.32),0 0 120px rgba({acc},.18),
   inset 0 2.5px 3px rgba(255,255,255,.4), inset 4px 4px 18px rgba(255,255,255,.14), inset 0 -14px 30px rgba(110,70,35,.42)}}
.panel.kraft .hd .t{{color:#2a1c10}} .panel.kraft .hd .tag{{color:#6e4a28}}
.panel.kraft .col{{background:linear-gradient(160deg,rgba(255,255,255,.34),rgba(255,255,255,.14));border-color:rgba(255,255,255,.25);
  box-shadow:0 8px 18px rgba(110,70,35,.3), inset 0 1.5px 2px rgba(255,255,255,.4)}}
.panel.kraft .col .cl{{color:#6e4a28}}
.panel.kraft .mini{{background:linear-gradient(160deg,rgba(255,255,255,.5),rgba(255,255,255,.28));box-shadow:0 5px 11px rgba(110,70,35,.25), inset 0 1px 1.5px rgba(255,255,255,.5)}}
.panel.kraft .mini .mt{{color:#2a1c10}} .panel.kraft .mini .ms{{color:#6e4a28}}
.panel.kraft .mini.on{{background:linear-gradient(160deg,#b2603e,#8a4630)}}
.panel.kraft .mini.on .mt{{color:#fff}} .panel.kraft .mini.on .ms{{color:rgba(255,236,226,.8)}}
.panel.ivory{{background:linear-gradient(160deg,#fdfbf5 0%,#f1e9da 55%,#e2d6c0 100%);
  border:1px solid rgba(120,95,60,.18);border-radius:26px;
  box-shadow:0 42px 80px rgba(0,0,0,.4),0 16px 34px rgba(0,0,0,.28),0 0 110px rgba({acc},.14),
   inset 0 2.5px 3px rgba(255,255,255,.9), inset 4px 4px 16px rgba(255,255,255,.55), inset 0 -12px 26px rgba(150,120,80,.22)}}
.panel.ivory .hd .t{{color:#17150F}} .panel.ivory .hd .tag{{color:#a5602f}}
.panel.ivory .row{{background:linear-gradient(160deg,#fff,#f3ecdd);border-color:rgba(120,95,60,.14);
  box-shadow:0 8px 18px rgba(150,120,80,.22), inset 0 1.5px 2px rgba(255,255,255,.9)}}
.panel.ivory .rn{{color:#17150F}} .panel.ivory .rs{{color:#8a7a5e}}
.panel.ivory .skel{{background:rgba(23,21,15,.16)}} .panel.ivory .skel.s2{{background:rgba(23,21,15,.09)}}
"""

# accent per set: stopsoftware = kraft (212,162,127)
def panels(acc):
    A=f"rgb({acc})"
    return {
 "scheduler":("",f"""
  <div class="hd"><span class="t">This week</span><span class="tag">QUEUED</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Launch post</div><div class="rs">LinkedIn + X</div></div><span class="chip">Mon 10:00</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Case study</div><div class="rs">carousel, 10 pages</div></div><span class="chip">Wed 10:00</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Teardown reel</div><div class="rs">TikTok + IG</div></div><span class="chip">Fri 10:00</span></div>
  <div class="row"><span class="dot" style="opacity:.35"></span><div><div class="rn" style="color:#8f8f85">Newsletter</div><div class="rs">drafting now</div></div><span class="ghostchip">queued</span></div>
 """),
 "warmup":("terra",f"""
  <div class="hd"><span class="t">Deliverability</span><span class="tag">4 DOMAINS WARM</span></div>
  <div style="display:flex;align-items:baseline;gap:12px;margin-bottom:18px">
    <span style="font-weight:900;font-size:64px;color:#fff;text-shadow:0 6px 18px rgba(60,20,8,.4)">99.2%</span>
    <span style="font-weight:700;font-size:16px;color:rgba(255,236,226,.85)">inbox placement</span></div>
  <div style="display:grid;gap:13px">
    <div><div style="display:flex;justify-content:space-between;margin-bottom:6px"><span class="rn" style="font-size:14.5px">Inbox</span><span class="rs" style="color:rgba(255,236,226,.85)">99.2%</span></div><div class="bar"><i style="--w:99%"></i></div></div>
    <div><div style="display:flex;justify-content:space-between;margin-bottom:6px"><span class="rn" style="font-size:14.5px">Spam</span><span class="rs" style="color:rgba(255,236,226,.85)">0.3%</span></div><div class="bar"><i style="--w:3%"></i></div></div>
    <div><div style="display:flex;justify-content:space-between;margin-bottom:6px"><span class="rn" style="font-size:14.5px">Bounce</span><span class="rs" style="color:rgba(255,236,226,.85)">0.3%</span></div><div class="bar"><i style="--w:3%"></i></div></div>
  </div>
 """),
 "seowriter":("ivory",f"""
  <div class="hd"><span class="t">Draft</span><span class="tag">RANKED 92 / 100</span></div>
  <div class="row" style="display:block">
    <div class="rn" style="font-size:19px;margin-bottom:10px">Why founders replace the stack</div>
    <div class="skel" style="margin-bottom:7px"></div>
    <div class="skel" style="margin-bottom:7px;width:88%"></div>
    <div class="skel s2"></div>
  </div>
  <div class="row"><span class="dot"></span><div><div class="rn">On brand</div><div class="rs">your voice, your no-list</div></div><span class="chip">Publish</span></div>
 """),
 "calendly":("kraft",f"""
  <div class="hd"><span class="t">Booked</span><span class="tag">6 CALLS THIS WEEK</span></div>
  <div class="cols">
    <div class="col"><div class="cl">MON</div><div class="mini on"><div class="mt">Call</div><div class="ms">30m</div></div><div class="mini"><div class="mt">&nbsp;</div><div class="ms">&nbsp;</div></div></div>
    <div class="col"><div class="cl">TUE</div><div class="mini"><div class="mt">&nbsp;</div><div class="ms">&nbsp;</div></div><div class="mini on"><div class="mt">Call</div><div class="ms">30m</div></div></div>
    <div class="col"><div class="cl">WED</div><div class="mini on"><div class="mt">Call</div><div class="ms">30m</div></div><div class="mini"><div class="mt">&nbsp;</div><div class="ms">&nbsp;</div></div></div>
    <div class="col"><div class="cl">THU</div><div class="mini"><div class="mt">&nbsp;</div><div class="ms">&nbsp;</div></div><div class="mini on"><div class="mt">Call</div><div class="ms">30m</div></div></div>
    <div class="col"><div class="cl">FRI</div><div class="mini on"><div class="mt">Call</div><div class="ms">30m</div></div><div class="mini on"><div class="mt">Call</div><div class="ms">30m</div></div></div>
  </div>
 """),
 "gmail_sent":("",f"""
  <div class="hd"><span class="t">Outbox</span><span class="tag">GATED &middot; YOUR TAP</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Acme &middot; partnership</div><div class="rs">one trigger &middot; 62 words</div></div><span class="chip">Sent 10:00</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Globex &middot; pricing</div><div class="rs">one trigger &middot; 62 words</div></div><span class="chip">Sent 10:00</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Northwind &middot; intro</div><div class="rs">one trigger &middot; 62 words</div></div><span class="chip">Sent 10:01</span></div>
 """),
 "softwarebill":("ivory",f"""
  <div class="hd"><span class="t">The bill</span><span class="tag">CANCELLED</span></div>
  <div class="row" style="padding:12px 18px"><div class="rn strike" style="font-size:16.5px">Buffer</div><span class="price strike">$15</span></div>
  <div class="row" style="padding:12px 18px"><div class="rn strike" style="font-size:16.5px">Instantly</div><span class="price strike">$97</span></div>
  <div class="row" style="padding:12px 18px"><div class="rn strike" style="font-size:16.5px">Jasper</div><span class="price strike">$49</span></div>
  <div class="row" style="padding:12px 18px"><div class="rn strike" style="font-size:16.5px">Calendly + sender</div><span class="price strike">$41</span></div>
  <div class="row" style="background:linear-gradient(160deg,rgb({acc}),rgba({acc},.8));border:none;
    box-shadow:0 10px 22px rgba({acc},.42), inset 0 2px 2.5px rgba(255,255,255,.45), inset 0 -6px 12px rgba(0,0,0,.25)">
    <div class="rn" style="color:#fff">One chat</div><span class="price" style="color:#fff">cents</span></div>
 """),
 "gate":("terra",f"""
  <div class="hd"><span class="t">The gate</span><span class="tag">YOUR TAP</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Send 240 outreach emails</div><div class="rs">parked on HOLD &middot; waiting for you</div></div><span class="ghostchip">HOLD</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Publish 3 posts</div><div class="rs">drafted in your voice</div></div><span class="ghostchip">HOLD</span></div>
  <div style="display:flex;gap:14px;margin-top:19px">
    <span class="btn">Approve all</span><span class="btn ghost">Hold</span></div>
 """),
 "ultron_real":("",f"""
  <div class="hd"><span class="t">One chat</span><span class="tag">THE WHOLE STACK</span></div>
  <div class="row" style="align-items:flex-start">
    <img src="data:image/png;base64,{ORB}" style="width:30px;height:30px;border-radius:50%;flex-shrink:0;box-shadow:0 4px 9px rgba(0,0,0,.45)">
    <div><div class="rn">Stack replaced.</div><div class="rs">scheduler, warmup, writer, booking, outreach: running</div></div></div>
  <div class="row" style="padding:14px 16px">
    <div class="rs" style="font-size:16px;color:rgba(250,250,247,.55)">cancel the rest</div>
    <span style="margin-left:auto;width:44px;height:44px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;
      background:linear-gradient(160deg,rgb({acc}),rgba({acc},.8));
      box-shadow:0 8px 18px rgba({acc},.42), inset 0 2px 2.5px rgba(255,255,255,.45);color:#fff;font-weight:900;font-size:20px">&#8594;</span></div>
 """),
}

SETS={
 "stopsoftware": ("212,162,127", panels("212,162,127")),
}

if __name__=="__main__":
    setname=sys.argv[1]; acc,P=SETS[setname]
    stems=sys.argv[2:] or list(P)
    outd=f"{ROOT}/content/_hitl-src/models_clay/{setname}"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":900,"height":1000},device_scale_factor=2)
        for s in stems:
            variant,body_html=P[s]
            html=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css(acc)}</style></head><body><div class='panel {variant}' id='panel'>{body_html}</div></body></html>"
            pg.set_content(html); pg.wait_for_timeout(350)
            pg.locator("#panel").screenshot(path=f"{outd}/{s}.png",omit_background=False)
            # omit_background on element screenshots keeps the shadow zone; capture body region w/ alpha:
            pg.screenshot(path=f"{outd}/{s}.png",omit_background=True,full_page=True)
            print("clay OK",s)
        b.close()
    print("done")
