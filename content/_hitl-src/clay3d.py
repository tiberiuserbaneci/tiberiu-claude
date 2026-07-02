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

/* ---- v3 FORM VARIANTS (structura, nu doar culoare) ---- */
.wrap{{position:relative;width:640px}}
.sheet{{position:absolute;inset:0;border-radius:26px;background:linear-gradient(162deg,#2b2b29,#1d1d1b);
  border:1px solid rgba(255,255,255,.05);box-shadow:0 30px 60px rgba(0,0,0,.5)}}
.dial{{width:470px;height:470px;border-radius:50%;padding:26px;margin:0 auto;position:relative;
  background:conic-gradient(from -90deg, rgb({acc}) 0% 99.2%, rgba(250,250,247,.12) 99.2% 100%);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 120px rgba({acc},.18), inset 0 3px 4px rgba(255,255,255,.25)}}
.dial .core{{width:100%;height:100%;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;
  background:linear-gradient(160deg,#2a2a28,#191917);
  box-shadow:inset 0 4px 10px rgba(0,0,0,.6), inset 0 -3px 6px rgba(255,255,255,.05), 0 6px 16px rgba(0,0,0,.4)}}
.paper{{width:560px;background:linear-gradient(160deg,#fdfbf5,#efe6d4);border-radius:8px 34px 8px 8px;padding:34px;position:relative;
  box-shadow:0 42px 80px rgba(0,0,0,.45),0 14px 30px rgba(0,0,0,.3), inset 0 2px 3px rgba(255,255,255,.9)}}
.paper::before{{content:'';position:absolute;top:0;right:0;width:64px;height:64px;border-radius:0 34px 0 12px;
  background:linear-gradient(225deg,#b9a582 0%,#d9c8a8 50%,#efe6d4 52%);
  box-shadow:-4px 4px 10px rgba(120,95,60,.3)}}
.receipt{{width:520px;background:linear-gradient(170deg,#fdfbf5,#f0e8d8);padding:32px 34px 46px;position:relative;
  font-family:'DM Mono',monospace;
  clip-path:polygon(0 0,100% 0,100% calc(100% - 18px),95% 100%,90% calc(100% - 18px),85% 100%,80% calc(100% - 18px),75% 100%,70% calc(100% - 18px),65% 100%,60% calc(100% - 18px),55% 100%,50% calc(100% - 18px),45% 100%,40% calc(100% - 18px),35% 100%,30% calc(100% - 18px),25% 100%,20% calc(100% - 18px),15% 100%,10% calc(100% - 18px),5% 100%,0 calc(100% - 18px));
  filter:drop-shadow(0 34px 50px rgba(0,0,0,.45)) drop-shadow(0 10px 20px rgba(0,0,0,.3))}}
.rrow{{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1.5px dashed rgba(23,21,15,.18);
  font-size:17px;font-weight:500;color:#17150F}}
.rrow .rp{{color:#8a7a5e}}
.pillrow{{display:flex;align-items:center;gap:14px;background:linear-gradient(160deg,#2e2e2b,#232321);
  border-radius:999px;padding:16px 26px;margin-bottom:16px;border:1px solid rgba(255,255,255,.05);
  box-shadow:0 18px 36px rgba(0,0,0,.45), inset 0 2px 2.5px rgba(255,255,255,.1), inset 0 -8px 16px rgba(0,0,0,.3)}}
.pillrow:nth-child(2){{margin-left:44px}} .pillrow:nth-child(3){{margin-left:88px}}
.tickwrap{{filter:drop-shadow(0 34px 55px rgba(0,0,0,.45)) drop-shadow(0 12px 22px rgba(0,0,0,.3))}}
.ticket{{width:600px;background:linear-gradient(158deg,#e0b98f,#c99a6d 48%,#a97a52);padding:30px 34px;
  -webkit-mask:radial-gradient(circle 22px at 0 62%,transparent 21px,#000 22px) left/51% 100% no-repeat,
               radial-gradient(circle 22px at 100% 62%,transparent 21px,#000 22px) right/51% 100% no-repeat;
  border-radius:30px}}
.tdash{{border-top:2.5px dashed rgba(42,28,16,.35);margin:16px 0 14px}}
.console{{width:620px;background:linear-gradient(165deg,#34342f,#1f1f1d 70%);border-radius:40px;padding:34px;
  border:1px solid rgba(255,255,255,.08);
  box-shadow:0 46px 85px rgba(0,0,0,.6),0 0 120px rgba({acc},.12), inset 0 3px 4px rgba(255,255,255,.12), inset 0 -16px 34px rgba(0,0,0,.5)}}
.switchrow{{display:flex;align-items:center;justify-content:space-between;padding:15px 6px}}
.sw{{width:96px;height:50px;border-radius:999px;position:relative;flex-shrink:0;
  background:linear-gradient(180deg,#141412,#242421);box-shadow:inset 0 4px 8px rgba(0,0,0,.7), inset 0 -1.5px 2px rgba(255,255,255,.08)}}
.sw i{{position:absolute;top:5px;width:40px;height:40px;border-radius:50%;
  background:linear-gradient(160deg,#efe6d4,#cbbfa4);box-shadow:0 4px 9px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.8)}}
.sw.on{{background:linear-gradient(180deg,rgba({acc},.7),rgb({acc}));box-shadow:inset 0 4px 8px rgba(0,0,0,.35),0 0 24px rgba({acc},.35)}}
.sw.on i{{right:5px}} .sw:not(.on) i{{left:5px}}
.keycap{{display:inline-block;border-radius:20px;padding:16px 40px;font-weight:900;font-size:19px;color:#fff;
  background:linear-gradient(180deg,#e08a5e,#b2603e);
  box-shadow:0 12px 0 #7c3e26, 0 22px 34px rgba(0,0,0,.5), inset 0 2.5px 3px rgba(255,255,255,.5)}}
.keycap.ghost{{background:linear-gradient(180deg,#3a3a36,#262624);color:rgba(250,250,247,.85);
  box-shadow:0 12px 0 #121210, 0 22px 34px rgba(0,0,0,.5), inset 0 2px 2.5px rgba(255,255,255,.14)}}
.bubble{{width:600px;background:linear-gradient(162deg,#2c2c2a,#1e1e1c);border-radius:38px;padding:30px;position:relative;
  border:1px solid rgba(255,255,255,.06);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 110px rgba({acc},.12), inset 0 2.5px 3px rgba(255,255,255,.1), inset 0 -12px 26px rgba(0,0,0,.4)}}
.bubble::after{{content:'';position:absolute;left:64px;bottom:-26px;width:54px;height:54px;
  background:linear-gradient(162deg,#232321,#1d1d1b);border-radius:0 0 60px 0;
  clip-path:polygon(0 0,100% 0,22% 100%);box-shadow:inset 0 -3px 4px rgba(0,0,0,.3)}}
.minibubble{{background:linear-gradient(160deg,rgb({acc}),rgba({acc},.8));border-radius:26px 26px 26px 8px;padding:16px 22px;margin-bottom:18px;
  width:fit-content;box-shadow:0 12px 26px rgba({acc},.35), inset 0 2px 2.5px rgba(255,255,255,.4)}}
.fan{{position:relative;width:620px;height:auto}}
.fan .b1,.fan .b2{{position:absolute;inset:0;border-radius:30px;background:linear-gradient(162deg,#262624,#1b1b19)}}
.fan .b1{{transform:rotate(-3.2deg) translateY(10px);box-shadow:0 24px 46px rgba(0,0,0,.4)}}
.fan .b2{{transform:rotate(2.4deg) translateY(6px);box-shadow:0 24px 46px rgba(0,0,0,.35)}}
.fan .top{{position:relative;background:linear-gradient(162deg,#2b2b29,#1d1d1b);border-radius:30px;padding:30px;
  border:1px solid rgba(255,255,255,.06);
  box-shadow:0 34px 65px rgba(0,0,0,.5), inset 0 2.5px 3px rgba(255,255,255,.1), inset 0 -12px 26px rgba(0,0,0,.4)}}

"""

# accent per set: stopsoftware = kraft (212,162,127)

PANELS_BODIES={
 # FORM: sheet fan (foi suprapuse rotite, cardul de plan deasupra)
 "scheduler":("",f"""
  <div class="fan"><div class="b1"></div><div class="b2"></div><div class="top">
  <div class="hd"><span class="t">This week</span><span class="tag">QUEUED</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Launch post</div><div class="rs">LinkedIn + X</div></div><span class="chip">Mon 10:00</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Case study</div><div class="rs">carousel, 10 pages</div></div><span class="chip">Wed 10:00</span></div>
  <div class="row"><span class="dot"></span><div><div class="rn">Teardown reel</div><div class="rs">TikTok + IG</div></div><span class="chip">Fri 10:00</span></div>
  </div></div>
 """),
 # FORM: dial circular cu inel de progres conic
 "warmup":("",f"""
  <div class="dial"><div class="core">
    <span style="font-family:'DM Mono',monospace;font-size:15px;letter-spacing:.16em;color:rgb({{acc}})">DELIVERABILITY</span>
    <span style="font-weight:900;font-size:92px;color:#FAFAF7;line-height:1">99.2%</span>
    <span style="font-weight:700;font-size:18px;color:#8f8f85">inbox placement</span>
    <span style="font-weight:500;font-size:14.5px;color:#8f8f85">4 domains warm &middot; spam 0.3%</span>
  </div></div>
 """),
 # FORM: foaie de hartie cu colt indoit
 "seowriter":("",f"""
  <div class="paper">
  <div class="hd" style="margin-bottom:16px"><span class="t" style="color:#17150F">Draft</span><span class="tag" style="color:#a5602f;margin-right:56px">RANKED 92</span></div>
  <div style="font-weight:800;font-size:22px;color:#17150F;margin-bottom:14px">Why founders replace the stack</div>
  <div class="skel" style="background:rgba(23,21,15,.16);margin-bottom:8px"></div>
  <div class="skel" style="background:rgba(23,21,15,.16);margin-bottom:8px;width:92%"></div>
  <div class="skel" style="background:rgba(23,21,15,.10);margin-bottom:8px;width:78%"></div>
  <div class="skel" style="background:rgba(23,21,15,.10);margin-bottom:22px;width:60%"></div>
  <div style="display:flex;align-items:center;gap:12px"><span class="dot"></span>
    <div><div class="rn" style="color:#17150F">On brand</div><div class="rs" style="color:#8a7a5e">your voice, your no-list</div></div>
    <span class="chip">Publish</span></div>
  </div>
 """),
 # FORM: bilet kraft cu crestaturi laterale + linie perforata
 "calendly":("",f"""
  <div class="tickwrap"><div class="ticket">
  <div class="hd" style="margin-bottom:12px"><span class="t" style="color:#2a1c10">Booked</span><span class="tag" style="color:#6e4a28">6 CALLS THIS WEEK</span></div>
  <div style="display:flex;gap:12px"><div style="flex:1;text-align:center"><div style="font-family:'DM Mono',monospace;font-size:12px;color:#6e4a28;margin-bottom:8px">MON</div><div style="border-radius:12px;padding:12px 4px;font-weight:800;font-size:14px;background:linear-gradient(160deg,#b2603e,#8a4630);color:#fff;box-shadow:0 7px 14px rgba(110,50,25,.4), inset 0 1.5px 2px rgba(255,255,255,.35)">Call</div></div><div style="flex:1;text-align:center"><div style="font-family:'DM Mono',monospace;font-size:12px;color:#6e4a28;margin-bottom:8px">TUE</div><div style="border-radius:12px;padding:12px 4px;font-weight:800;font-size:14px;background:rgba(255,255,255,.4);color:#b09877;box-shadow:inset 0 1.5px 2px rgba(255,255,255,.55)">&nbsp;</div></div><div style="flex:1;text-align:center"><div style="font-family:'DM Mono',monospace;font-size:12px;color:#6e4a28;margin-bottom:8px">WED</div><div style="border-radius:12px;padding:12px 4px;font-weight:800;font-size:14px;background:linear-gradient(160deg,#b2603e,#8a4630);color:#fff;box-shadow:0 7px 14px rgba(110,50,25,.4), inset 0 1.5px 2px rgba(255,255,255,.35)">Call</div></div><div style="flex:1;text-align:center"><div style="font-family:'DM Mono',monospace;font-size:12px;color:#6e4a28;margin-bottom:8px">THU</div><div style="border-radius:12px;padding:12px 4px;font-weight:800;font-size:14px;background:linear-gradient(160deg,#b2603e,#8a4630);color:#fff;box-shadow:0 7px 14px rgba(110,50,25,.4), inset 0 1.5px 2px rgba(255,255,255,.35)">Call</div></div><div style="flex:1;text-align:center"><div style="font-family:'DM Mono',monospace;font-size:12px;color:#6e4a28;margin-bottom:8px">FRI</div><div style="border-radius:12px;padding:12px 4px;font-weight:800;font-size:14px;background:linear-gradient(160deg,#b2603e,#8a4630);color:#fff;box-shadow:0 7px 14px rgba(110,50,25,.4), inset 0 1.5px 2px rgba(255,255,255,.35)">Call</div></div></div>
  <div class="tdash"></div>
  <div style="display:flex;justify-content:space-between;font-family:'DM Mono',monospace;font-size:14px;color:#6e4a28">
    <span>ADMIT ONE FOUNDER</span><span>NO BOOKING APP</span></div>
  </div></div>
 """),
 # FORM: stack de capsule libere, in trepte, fara panou-mama
 "gmail_sent":("",f"""
  <div style="width:640px">
  <div class="pillrow"><span class="dot"></span><div><div class="rn">Acme &middot; partnership</div><div class="rs">one trigger &middot; 62 words</div></div><span class="chip">Sent 10:00</span></div>
  <div class="pillrow"><span class="dot"></span><div><div class="rn">Globex &middot; pricing</div><div class="rs">one trigger &middot; 62 words</div></div><span class="chip">Sent 10:00</span></div>
  <div class="pillrow"><span class="dot"></span><div><div class="rn">Northwind &middot; intro</div><div class="rs">one trigger &middot; 62 words</div></div><span class="chip">Sent 10:01</span></div>
  </div>
 """),
 # FORM: bon de casa cu margine zimtata + separatoare perforate
 "softwarebill":("",f"""
  <div class="receipt">
  <div style="text-align:center;font-size:15px;letter-spacing:.22em;color:#8a7a5e;margin-bottom:6px">YOUR SOFTWARE BILL</div>
  <div style="text-align:center;font-size:12.5px;letter-spacing:.14em;color:#b0a284;margin-bottom:16px">MONTHLY &middot; AUTO-RENEW</div>
  <div class="rrow"><span style="text-decoration:line-through;text-decoration-color:rgba(178,96,62,.9);text-decoration-thickness:2.5px">Buffer</span><span class="rp" style="text-decoration:line-through">$15</span></div>
  <div class="rrow"><span style="text-decoration:line-through;text-decoration-color:rgba(178,96,62,.9);text-decoration-thickness:2.5px">Instantly</span><span class="rp" style="text-decoration:line-through">$97</span></div>
  <div class="rrow"><span style="text-decoration:line-through;text-decoration-color:rgba(178,96,62,.9);text-decoration-thickness:2.5px">Jasper</span><span class="rp" style="text-decoration:line-through">$49</span></div>
  <div class="rrow"><span style="text-decoration:line-through;text-decoration-color:rgba(178,96,62,.9);text-decoration-thickness:2.5px">Calendly + sender</span><span class="rp" style="text-decoration:line-through">$41</span></div>
  <div class="rrow" style="border-bottom:none;padding-top:14px"><span style="font-weight:800">One chat</span><span style="font-weight:800;color:#b2603e">cents</span></div>
  </div>
 """),
 # FORM: consola fizica - switch-uri + keycap cu perete de extrudare
 "gate":("",f"""
  <div class="console">
  <div class="hd"><span class="t">The gate</span><span class="tag">YOUR TAP</span></div>
  <div class="switchrow"><div><div class="rn">Send 240 outreach emails</div><div class="rs">parked on HOLD</div></div><div class="sw"><i></i></div></div>
  <div class="switchrow"><div><div class="rn">Publish 3 posts</div><div class="rs">drafted in your voice</div></div><div class="sw"><i></i></div></div>
  <div class="switchrow"><div><div class="rn">Move Globex to Proposal</div><div class="rs">from this morning's reply</div></div><div class="sw on"><i></i></div></div>
  <div style="display:flex;gap:22px;margin-top:22px;padding-bottom:12px;justify-content:center">
    <span class="keycap">Approve all</span><span class="keycap ghost">Hold</span></div>
  </div>
 """),
 # FORM: bula de chat cu coada + mini-bula de raspuns
 "ultron_real":("",f"""
  <div style="width:640px;padding-bottom:30px">
  <div class="minibubble"><span style="font-weight:700;font-size:16px;color:#fff">Stack replaced. Five tools, one chat.</span></div>
  <div class="bubble">
  <div class="hd" style="margin-bottom:16px"><span class="t">One chat</span><span class="tag">THE WHOLE STACK</span></div>
  <div class="row" style="border-radius:999px;padding:14px 18px">
    <img src="data:image/png;base64,{ORB}" style="width:32px;height:32px;border-radius:50%;flex-shrink:0;box-shadow:0 4px 9px rgba(0,0,0,.45)">
    <div class="rs" style="font-size:16.5px;color:rgba(250,250,247,.6)">cancel the rest</div>
    <span style="margin-left:auto;width:46px;height:46px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,rgb({{acc}}),rgba({{acc}},.8));box-shadow:0 8px 18px rgba({{acc}},.42), inset 0 2px 2.5px rgba(255,255,255,.45);color:#fff;font-weight:900;font-size:20px">&#8594;</span></div>
  </div></div>
 """),
}

def panels(acc):
    out={}
    for k,(v,h) in PANELS_BODIES.items():
        out[k]=(v, h.replace("{acc}",acc))
    return out

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
