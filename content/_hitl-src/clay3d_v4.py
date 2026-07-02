#!/usr/bin/env python3
# CLAY3D v4 - form library + per-deck contextual specs (operator OK 2026-07-02 on the
# STOP PAYING test: "e corect, poti trece la executia celorlalte in aceeasi maniera").
# 9 decks x 8 panels, each deck its OWN mix of 3D forms + accent; content from the deck copy.
# Forms: rows-panel (charcoal/terra/kraft/ivory), sheet fan, dial, paper+fold, receipt+zigzag,
# ticket+notches, free pill cascade, physical console (switches+keycaps), speech bubble,
# podium staircase, browser window, stat card.
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
.panel{{width:620px;background:linear-gradient(162deg,#282826 0%,#1e1e1c 58%,#191917 100%);
  border-radius:34px;padding:30px;position:relative;border:1px solid rgba(255,255,255,.055);
  box-shadow:0 42px 80px rgba(0,0,0,.58),0 16px 34px rgba(0,0,0,.44),0 0 110px rgba({acc},.11),
    inset 0 2px 3px rgba(255,255,255,.10), inset 3px 3px 14px rgba(255,255,255,.035), inset 0 -12px 26px rgba(0,0,0,.42)}}
.panel.terra{{background:linear-gradient(158deg,#d98a63 0%,#b2603e 46%,#8a4630 100%);border:1px solid rgba(255,255,255,.16);
  box-shadow:0 42px 80px rgba(0,0,0,.5),0 16px 34px rgba(0,0,0,.38),0 0 120px rgba({acc},.2),
   inset 0 2.5px 3px rgba(255,255,255,.35), inset 4px 4px 16px rgba(255,255,255,.12), inset 0 -14px 30px rgba(90,35,18,.5)}}
.panel.kraft{{background:linear-gradient(158deg,#e0b98f 0%,#c99a6d 48%,#a97a52 100%);border:1px solid rgba(255,255,255,.2);border-radius:52px;
  box-shadow:0 42px 80px rgba(0,0,0,.44),0 16px 34px rgba(0,0,0,.32),0 0 120px rgba({acc},.18),
   inset 0 2.5px 3px rgba(255,255,255,.4), inset 4px 4px 18px rgba(255,255,255,.14), inset 0 -14px 30px rgba(110,70,35,.42)}}
.panel.ivory{{background:linear-gradient(160deg,#fdfbf5 0%,#f1e9da 55%,#e2d6c0 100%);border:1px solid rgba(120,95,60,.18);border-radius:26px;
  box-shadow:0 42px 80px rgba(0,0,0,.4),0 16px 34px rgba(0,0,0,.28),0 0 110px rgba({acc},.14),
   inset 0 2.5px 3px rgba(255,255,255,.9), inset 4px 4px 16px rgba(255,255,255,.55), inset 0 -12px 26px rgba(150,120,80,.22)}}
.hd{{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}}
.hd .t{{font-weight:800;font-size:24px;color:#FAFAF7;letter-spacing:-.2px}}
.hd .tag{{font-family:'DM Mono',monospace;font-size:12.5px;letter-spacing:.14em;color:rgb({acc})}}
.panel.terra .hd .t,.bubble .hd .t{{color:#fff}} .panel.terra .hd .tag{{color:rgba(255,240,232,.85)}}
.panel.kraft .hd .t{{color:#2a1c10}} .panel.kraft .hd .tag{{color:#6e4a28}}
.panel.ivory .hd .t{{color:#17150F}} .panel.ivory .hd .tag{{color:#a5602f}}
.row{{background:linear-gradient(160deg,#2e2e2b,#242422);border-radius:18px;padding:15px 18px;
  display:flex;align-items:center;gap:13px;margin-bottom:12px;border:1px solid rgba(255,255,255,.045);
  box-shadow:0 8px 18px rgba(0,0,0,.35), inset 0 1.5px 2px rgba(255,255,255,.08), inset 0 -6px 14px rgba(0,0,0,.28)}}
.row:last-child{{margin-bottom:0}}
.panel.terra .row{{background:linear-gradient(160deg,rgba(255,255,255,.16),rgba(255,255,255,.06));border-color:rgba(255,255,255,.14);
  box-shadow:0 8px 18px rgba(90,35,18,.35), inset 0 1.5px 2px rgba(255,255,255,.22)}}
.panel.kraft .row{{background:linear-gradient(160deg,rgba(255,255,255,.42),rgba(255,255,255,.2));border-color:rgba(255,255,255,.3);
  box-shadow:0 8px 18px rgba(110,70,35,.28), inset 0 1.5px 2px rgba(255,255,255,.5)}}
.panel.ivory .row{{background:linear-gradient(160deg,#fff,#f3ecdd);border-color:rgba(120,95,60,.14);
  box-shadow:0 8px 18px rgba(150,120,80,.22), inset 0 1.5px 2px rgba(255,255,255,.9)}}
.dot{{width:26px;height:26px;border-radius:50%;flex-shrink:0;background:radial-gradient(circle at 34% 30%, rgb({acc}), rgba({acc},.55));
  box-shadow:0 4px 9px rgba(0,0,0,.4), inset 0 1.5px 2px rgba(255,255,255,.35)}}
.rn{{font-weight:700;font-size:18.5px;color:#FAFAF7}} .rs{{font-weight:500;font-size:13.5px;color:#8f8f85;margin-top:2px}}
.panel.terra .rn{{color:#fff}} .panel.terra .rs{{color:rgba(255,236,226,.75)}}
.panel.kraft .rn{{color:#2a1c10}} .panel.kraft .rs{{color:#6e4a28}}
.panel.ivory .rn{{color:#17150F}} .panel.ivory .rs{{color:#8a7a5e}}
.chip{{margin-left:auto;flex-shrink:0;background:linear-gradient(160deg,rgb({acc}),rgba({acc},.82));color:#fff;font-weight:800;font-size:14.5px;
  border-radius:999px;padding:8px 17px;box-shadow:0 6px 14px rgba({acc},.35), inset 0 1.5px 2px rgba(255,255,255,.4), inset 0 -4px 8px rgba(0,0,0,.22)}}
.ghostchip{{margin-left:auto;flex-shrink:0;border:1.6px solid rgba(250,250,247,.3);color:rgba(250,250,247,.72);font-weight:700;font-size:14px;border-radius:999px;padding:7px 16px}}
.panel.ivory .ghostchip,.panel.kraft .ghostchip{{border-color:rgba(23,21,15,.3);color:rgba(23,21,15,.6)}}
.strikei{{text-decoration:line-through;text-decoration-color:rgba(178,96,62,.9);text-decoration-thickness:2.5px}}
.skel{{height:9px;border-radius:5px;background:rgba(250,250,247,.14)}}
.fan{{position:relative;width:620px}}
.fan .b1,.fan .b2{{position:absolute;inset:0;border-radius:30px;background:linear-gradient(162deg,#262624,#1b1b19)}}
.fan .b1{{transform:rotate(-3.2deg) translateY(10px);box-shadow:0 24px 46px rgba(0,0,0,.4)}}
.fan .b2{{transform:rotate(2.4deg) translateY(6px);box-shadow:0 24px 46px rgba(0,0,0,.35)}}
.fan .top{{position:relative;background:linear-gradient(162deg,#2b2b29,#1d1d1b);border-radius:30px;padding:30px;border:1px solid rgba(255,255,255,.06);
  box-shadow:0 34px 65px rgba(0,0,0,.5), inset 0 2.5px 3px rgba(255,255,255,.1), inset 0 -12px 26px rgba(0,0,0,.4)}}
.dial{{width:470px;height:470px;border-radius:50%;padding:26px;margin:0 auto;position:relative;
  background:conic-gradient(from -90deg, rgb({acc}) 0% var(--p), rgba(250,250,247,.12) var(--p) 100%);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 120px rgba({acc},.18), inset 0 3px 4px rgba(255,255,255,.25)}}
.dial .core{{width:100%;height:100%;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;
  background:linear-gradient(160deg,#2a2a28,#191917);
  box-shadow:inset 0 4px 10px rgba(0,0,0,.6), inset 0 -3px 6px rgba(255,255,255,.05), 0 6px 16px rgba(0,0,0,.4)}}
.paper{{width:560px;background:linear-gradient(160deg,#fdfbf5,#efe6d4);border-radius:8px 34px 8px 8px;padding:34px;position:relative;
  box-shadow:0 42px 80px rgba(0,0,0,.45),0 14px 30px rgba(0,0,0,.3), inset 0 2px 3px rgba(255,255,255,.9)}}
.paper::before{{content:'';position:absolute;top:0;right:0;width:64px;height:64px;border-radius:0 34px 0 12px;
  background:linear-gradient(225deg,#b9a582 0%,#d9c8a8 50%,#efe6d4 52%);box-shadow:-4px 4px 10px rgba(120,95,60,.3)}}
.receipt{{width:520px;background:linear-gradient(170deg,#fdfbf5,#f0e8d8);padding:32px 34px 46px;position:relative;font-family:'DM Mono',monospace;
  clip-path:polygon(0 0,100% 0,100% calc(100% - 18px),95% 100%,90% calc(100% - 18px),85% 100%,80% calc(100% - 18px),75% 100%,70% calc(100% - 18px),65% 100%,60% calc(100% - 18px),55% 100%,50% calc(100% - 18px),45% 100%,40% calc(100% - 18px),35% 100%,30% calc(100% - 18px),25% 100%,20% calc(100% - 18px),15% 100%,10% calc(100% - 18px),5% 100%,0 calc(100% - 18px));
  filter:drop-shadow(0 34px 50px rgba(0,0,0,.45)) drop-shadow(0 10px 20px rgba(0,0,0,.3))}}
.rrow{{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1.5px dashed rgba(23,21,15,.18);font-size:17px;font-weight:500;color:#17150F}}
.rrow .rp{{color:#8a7a5e}}
.tickwrap{{filter:drop-shadow(0 34px 55px rgba(0,0,0,.45)) drop-shadow(0 12px 22px rgba(0,0,0,.3))}}
.ticket{{width:600px;background:linear-gradient(158deg,#e0b98f,#c99a6d 48%,#a97a52);padding:30px 34px;border-radius:30px;
  -webkit-mask:radial-gradient(circle 22px at 0 62%,transparent 21px,#000 22px) left/51% 100% no-repeat,
               radial-gradient(circle 22px at 100% 62%,transparent 21px,#000 22px) right/51% 100% no-repeat}}
.tdash{{border-top:2.5px dashed rgba(42,28,16,.35);margin:16px 0 14px}}
.pillrow{{display:flex;align-items:center;gap:14px;background:linear-gradient(160deg,#2e2e2b,#232321);border-radius:999px;padding:16px 26px;margin-bottom:16px;
  border:1px solid rgba(255,255,255,.05);box-shadow:0 18px 36px rgba(0,0,0,.45), inset 0 2px 2.5px rgba(255,255,255,.1), inset 0 -8px 16px rgba(0,0,0,.3)}}
.pills .pillrow:nth-child(2){{margin-left:44px}} .pills .pillrow:nth-child(3){{margin-left:88px}} .pills .pillrow:nth-child(4){{margin-left:132px}}
.console{{width:620px;background:linear-gradient(165deg,#34342f,#1f1f1d 70%);border-radius:40px;padding:34px;border:1px solid rgba(255,255,255,.08);
  box-shadow:0 46px 85px rgba(0,0,0,.6),0 0 120px rgba({acc},.12), inset 0 3px 4px rgba(255,255,255,.12), inset 0 -16px 34px rgba(0,0,0,.5)}}
.switchrow{{display:flex;align-items:center;justify-content:space-between;padding:15px 6px}}
.sw{{width:96px;height:50px;border-radius:999px;position:relative;flex-shrink:0;background:linear-gradient(180deg,#141412,#242421);
  box-shadow:inset 0 4px 8px rgba(0,0,0,.7), inset 0 -1.5px 2px rgba(255,255,255,.08)}}
.sw i{{position:absolute;top:5px;width:40px;height:40px;border-radius:50%;background:linear-gradient(160deg,#efe6d4,#cbbfa4);
  box-shadow:0 4px 9px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.8)}}
.sw.on{{background:linear-gradient(180deg,rgba({acc},.7),rgb({acc}));box-shadow:inset 0 4px 8px rgba(0,0,0,.35),0 0 24px rgba({acc},.35)}}
.sw.on i{{right:5px}} .sw:not(.on) i{{left:5px}}
.keycap{{display:inline-block;border-radius:20px;padding:16px 40px;font-weight:900;font-size:19px;color:#fff;
  background:linear-gradient(180deg,#e08a5e,#b2603e);box-shadow:0 12px 0 #7c3e26, 0 22px 34px rgba(0,0,0,.5), inset 0 2.5px 3px rgba(255,255,255,.5)}}
.keycap.ghost{{background:linear-gradient(180deg,#3a3a36,#262624);color:rgba(250,250,247,.85);
  box-shadow:0 12px 0 #121210, 0 22px 34px rgba(0,0,0,.5), inset 0 2px 2.5px rgba(255,255,255,.14)}}
.bubble{{width:600px;background:linear-gradient(162deg,#2c2c2a,#1e1e1c);border-radius:38px;padding:30px;position:relative;border:1px solid rgba(255,255,255,.06);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 110px rgba({acc},.12), inset 0 2.5px 3px rgba(255,255,255,.1), inset 0 -12px 26px rgba(0,0,0,.4)}}
.bubble::after{{content:'';position:absolute;left:64px;bottom:-26px;width:54px;height:54px;background:linear-gradient(162deg,#232321,#1d1d1b);
  border-radius:0 0 60px 0;clip-path:polygon(0 0,100% 0,22% 100%)}}
.minibubble{{background:linear-gradient(160deg,rgb({acc}),rgba({acc},.8));border-radius:26px 26px 26px 8px;padding:16px 22px;margin-bottom:18px;width:fit-content;
  box-shadow:0 12px 26px rgba({acc},.35), inset 0 2px 2.5px rgba(255,255,255,.4)}}
.podium{{width:640px;display:flex;align-items:flex-end;gap:14px;padding-bottom:8px}}
.step{{flex:1;border-radius:14px 14px 8px 8px;background:linear-gradient(180deg,#33332f,#232321);position:relative;text-align:center;
  box-shadow:0 14px 0 #141412, 0 26px 40px rgba(0,0,0,.5), inset 0 2px 2.5px rgba(255,255,255,.12)}}
.step.on{{background:linear-gradient(180deg,#e08a5e,#b2603e);box-shadow:0 14px 0 #7c3e26, 0 26px 44px rgba(0,0,0,.5),0 0 34px rgba({acc},.3), inset 0 2.5px 3px rgba(255,255,255,.45)}}
.step .sl{{font-weight:900;font-size:20px;color:#FAFAF7;padding-top:12px;display:block}}
.step .sm{{font-weight:500;font-size:11.5px;color:#8f8f85;display:block;padding-bottom:8px}}
.step.on .sm{{color:rgba(255,236,226,.85)}}
.browser{{width:640px;border-radius:26px;overflow:hidden;background:linear-gradient(162deg,#2b2b29,#1d1d1b);border:1px solid rgba(255,255,255,.06);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 110px rgba({acc},.12), inset 0 -12px 26px rgba(0,0,0,.35)}}
.bbar{{display:flex;align-items:center;gap:9px;background:linear-gradient(180deg,#3a3a36,#2c2c29);padding:14px 20px;border-bottom:1px solid rgba(0,0,0,.4)}}
.bdot{{width:14px;height:14px;border-radius:50%;box-shadow:inset 0 1.5px 2px rgba(255,255,255,.35),0 2px 4px rgba(0,0,0,.4)}}
.burl{{margin-left:12px;flex:1;background:rgba(0,0,0,.35);border-radius:999px;padding:7px 18px;font-family:'DM Mono',monospace;font-size:13.5px;color:#a8a89e;
  box-shadow:inset 0 2px 5px rgba(0,0,0,.5)}}
.bbody{{padding:26px 30px 30px}}
.stat{{width:620px;background:linear-gradient(158deg,#d98a63 0%,#b2603e 46%,#8a4630 100%);border-radius:34px;padding:34px;border:1px solid rgba(255,255,255,.16);
  box-shadow:0 42px 80px rgba(0,0,0,.5),0 0 120px rgba({acc},.2), inset 0 2.5px 3px rgba(255,255,255,.35), inset 0 -14px 30px rgba(90,35,18,.5)}}
.stat .big{{font-weight:900;font-size:88px;color:#fff;line-height:1;text-shadow:0 6px 18px rgba(60,20,8,.4)}}
.stat .lbl{{font-weight:700;font-size:18px;color:rgba(255,236,226,.85);margin:6px 0 20px}}
.bars{{display:flex;align-items:flex-end;gap:12px;height:150px}}
.bars i{{flex:1;border-radius:9px 9px 4px 4px;background:linear-gradient(180deg,rgba(255,255,255,.5),rgba(255,255,255,.22));
  box-shadow:inset 0 2px 2.5px rgba(255,255,255,.5)}}
.bars i.hot{{background:linear-gradient(180deg,#fff,#f0d9c8);box-shadow:0 0 22px rgba(255,255,255,.35), inset 0 2px 2.5px #fff}}

/* ---- v5 UTILITY FORMS (alta utilitate, nu liste re-vopsite) ---- */
.envwrap{{filter:drop-shadow(0 36px 55px rgba(0,0,0,.5)) drop-shadow(0 12px 22px rgba(0,0,0,.32))}}
.env{{width:600px;height:360px;position:relative;background:linear-gradient(165deg,#2e2e2b,#201f1d);border-radius:22px;overflow:hidden}}
.env .flap{{position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,#3a3a36,#2a2a27);
  clip-path:polygon(0 0,100% 0,50% 100%);box-shadow:inset 0 3px 4px rgba(255,255,255,.12)}}
.env .letter{{position:absolute;left:34px;right:34px;top:120px;bottom:-8px;background:linear-gradient(170deg,#fdfbf5,#efe6d4);
  border-radius:14px 14px 0 0;padding:24px 26px;box-shadow:0 -8px 24px rgba(0,0,0,.3)}}
.badgewrap{{position:relative;width:340px;margin:0 auto;padding:26px 26px 0}}
.badgetile{{width:290px;height:290px;border-radius:64px;background:linear-gradient(160deg,#34342f,#1f1f1d);
  display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,.08);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 110px rgba({acc},.14), inset 0 3px 4px rgba(255,255,255,.14), inset 0 -14px 30px rgba(0,0,0,.5)}}
.badge{{position:absolute;top:0;right:0;min-width:96px;height:96px;border-radius:999px;padding:0 20px;
  background:linear-gradient(160deg,#e0684f,#b2432e);display:flex;align-items:center;justify-content:center;
  font-weight:900;font-size:38px;color:#fff;box-shadow:0 14px 30px rgba(178,67,46,.5), inset 0 3px 3px rgba(255,255,255,.4)}}
.metro{{width:660px;padding:30px 10px}}
.mline{{position:relative;height:10px;border-radius:6px;background:rgba(250,250,247,.14);margin:56px 24px 70px;
  box-shadow:inset 0 2px 4px rgba(0,0,0,.5)}}
.mfill{{position:absolute;left:0;top:0;bottom:0;width:72%;border-radius:6px;background:linear-gradient(90deg,rgba({acc},.8),rgb({acc}));
  box-shadow:0 0 24px rgba({acc},.4), inset 0 2px 2px rgba(255,255,255,.4)}}
.mst{{position:absolute;top:50%;transform:translate(-50%,-50%);width:34px;height:34px;border-radius:50%;
  background:linear-gradient(160deg,#efe6d4,#cbbfa4);box-shadow:0 6px 14px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.8)}}
.mst.on{{background:linear-gradient(160deg,rgb({acc}),rgba({acc},.75));box-shadow:0 0 26px rgba({acc},.5), inset 0 2px 2px rgba(255,255,255,.45)}}
.mlab{{position:absolute;top:44px;transform:translateX(-50%);font-weight:700;font-size:15px;color:#FAFAF7;white-space:nowrap}}
.msub{{position:absolute;top:68px;transform:translateX(-50%);font-family:'DM Mono',monospace;font-size:11.5px;color:#8f8f85;white-space:nowrap}}
.split{{width:640px;display:flex;border-radius:30px;overflow:hidden;
  box-shadow:0 42px 80px rgba(0,0,0,.55), inset 0 2px 3px rgba(255,255,255,.1)}}
.split .lft{{flex:1;background:linear-gradient(165deg,#31312d,#232320);padding:28px 24px;position:relative}}
.split .rgt{{flex:1;background:linear-gradient(165deg,#d98a63,#8a4630);padding:28px 24px}}
.split .cap{{font-family:'DM Mono',monospace;font-size:12.5px;letter-spacing:.14em;margin-bottom:16px;display:block}}
.gaugewrap{{width:560px;margin:0 auto;text-align:center}}
.gauge{{width:460px;height:230px;margin:0 auto;border-radius:460px 460px 0 0;position:relative;overflow:hidden;
  background:conic-gradient(from -90deg at 50% 100%, rgb({acc}) 0% var(--g), rgba(250,250,247,.13) var(--g) 50%);
  box-shadow:0 30px 60px rgba(0,0,0,.5), inset 0 3px 4px rgba(255,255,255,.2)}}
.gauge::after{{content:'';position:absolute;left:50%;bottom:-120px;transform:translateX(-50%);width:340px;height:340px;border-radius:50%;
  background:linear-gradient(160deg,#262624,#191917);box-shadow:inset 0 4px 10px rgba(0,0,0,.6)}}
.odow{{width:640px;background:linear-gradient(165deg,#2b2b28,#1d1d1b);border-radius:34px;padding:34px;text-align:center;
  border:1px solid rgba(255,255,255,.07);box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 110px rgba({acc},.12), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)}}
.odo{{display:inline-flex;gap:10px;margin:14px 0 8px}}
.odo b{{width:82px;height:118px;border-radius:16px;background:linear-gradient(180deg,#141412,#232320 45%,#141412);
  display:flex;align-items:center;justify-content:center;font-weight:900;font-size:64px;color:#FAFAF7;
  box-shadow:inset 0 6px 12px rgba(0,0,0,.7), inset 0 -2px 3px rgba(255,255,255,.07), 0 6px 14px rgba(0,0,0,.4);position:relative}}
.odo b::after{{content:'';position:absolute;left:0;right:0;top:50%;height:2px;background:rgba(0,0,0,.55)}}
.odo b.hot{{color:rgb({acc});text-shadow:0 0 18px rgba({acc},.5)}}
.batw{{width:660px;margin-top:60px;background:linear-gradient(165deg,#2b2b28,#1d1d1b);border-radius:34px;padding:36px;text-align:center;
  border:1px solid rgba(255,255,255,.07);box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)}}
.bat{{position:relative;width:480px;height:196px;margin:12px auto 20px;border-radius:40px;background:linear-gradient(180deg,#141412,#232320);
  box-shadow:inset 0 5px 12px rgba(0,0,0,.68), inset 0 -2px 3px rgba(255,255,255,.07), 0 2px 3px rgba(255,255,255,.06)}}
.bat .nub{{position:absolute;right:-28px;top:60px;width:28px;height:76px;border-radius:0 15px 15px 0;
  background:linear-gradient(180deg,#3a3a36,#232320);box-shadow:inset 0 2px 3px rgba(255,255,255,.14)}}
.bat .fill{{position:absolute;left:14px;top:14px;bottom:14px;border-radius:28px;
  background:linear-gradient(180deg,rgb({acc}),rgba({acc},.72));box-shadow:0 0 46px rgba({acc},.5), inset 0 3px 4px rgba(255,255,255,.4)}}
.bat .pct{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:66px;color:#FAFAF7;text-shadow:0 4px 18px rgba(0,0,0,.6)}}
.calw{{width:660px;border-radius:24px;background:linear-gradient(170deg,#f7f1e4,#e9dfc9);padding:32px 32px 28px;
  box-shadow:0 42px 80px rgba(0,0,0,.5),0 14px 30px rgba(0,0,0,.3), inset 0 2px 2px rgba(255,255,255,.85)}}
.cal{{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;margin-top:20px}}
.cal b{{height:66px;border-radius:12px;background:#efe6d2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;
  font-weight:700;font-size:17px;color:#8a7a5e;box-shadow:inset 0 1.5px 2px rgba(255,255,255,.85), inset 0 -3px 6px rgba(0,0,0,.09)}}
.cal b.hot{{background:linear-gradient(180deg,rgb({acc}),rgba({acc},.8));color:#fff;box-shadow:0 8px 18px rgba({acc},.35), inset 0 2px 2.5px rgba(255,255,255,.45)}}
.cal b small{{font-size:10px;font-weight:800;letter-spacing:.05em}}
.calfoot{{margin-top:18px;font-weight:700;font-size:17px;color:#6e5f45;text-align:center}}
.ringsw{{width:660px;text-align:center}}
.rings{{position:relative;width:430px;height:430px;margin:0 auto;filter:drop-shadow(0 40px 60px rgba(0,0,0,.55))}}
.rings i{{position:absolute;border-radius:50%}}
.rings .r1{{inset:0;background:radial-gradient(circle at 32% 26%,#33332f,#1c1c1a 74%);box-shadow:inset 0 5px 9px rgba(255,255,255,.09), inset 0 -14px 30px rgba(0,0,0,.5)}}
.rings .r2{{inset:64px;background:radial-gradient(circle at 32% 26%,#2a2a27,#181816 74%);box-shadow:inset 0 4px 8px rgba(0,0,0,.55), 0 2px 3px rgba(255,255,255,.07)}}
.rings .r3{{inset:128px;background:radial-gradient(circle at 32% 26%,#343430,#1d1d1b 74%);box-shadow:inset 0 4px 7px rgba(255,255,255,.08), inset 0 -8px 18px rgba(0,0,0,.5)}}
.rings .core{{position:absolute;inset:158px;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;padding:12px;
  background:linear-gradient(160deg,rgb({acc}),rgba({acc},.74));font-weight:900;font-size:26px;color:#fff;line-height:1.05;
  box-shadow:0 14px 34px rgba({acc},.45), inset 0 3px 4px rgba(255,255,255,.45)}}
.rings-tags{{display:flex;gap:12px;justify-content:center;margin-top:30px;flex-wrap:wrap}}
.rings-tags b{{display:flex;align-items:center;gap:9px;padding:13px 18px;border-radius:999px;background:linear-gradient(165deg,#2c2c29,#1d1d1b);
  font-weight:700;font-size:16.5px;color:#d9d9d0;box-shadow:0 14px 26px rgba(0,0,0,.45), inset 0 2px 2.5px rgba(255,255,255,.1)}}
.rings-tags b i{{width:11px;height:11px;border-radius:50%;background:rgb({acc});box-shadow:0 0 12px rgba({acc},.7)}}
.shelfw{{width:640px;display:flex;flex-direction:column;gap:24px}}
.tray{{position:relative;border-radius:18px;background:linear-gradient(165deg,#2e2e2b,#1f1f1d);padding:20px 24px 24px;
  box-shadow:0 26px 44px rgba(0,0,0,.5), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -12px 22px rgba(0,0,0,.4)}}
.tray::after{{content:'';position:absolute;left:9px;right:9px;bottom:-11px;height:15px;border-radius:0 0 15px 15px;
  background:linear-gradient(180deg,#191917,#0e0e0d);box-shadow:0 12px 20px rgba(0,0,0,.55)}}
.tray .tn{{font-weight:800;font-size:22px;color:#FAFAF7}}
.tray .ts{{font-weight:500;font-size:16.5px;color:#8f8f85;margin-top:4px}}
.tray .tchip{{position:absolute;right:22px;top:24px;padding:7px 14px;border-radius:999px;background:rgba({acc},.16);
  font-family:'DM Mono',monospace;font-size:12.5px;letter-spacing:.1em;color:rgb({acc});box-shadow:inset 0 0 0 1.5px rgba({acc},.4)}}
.vaultw{{width:560px;margin:0 auto;text-align:center}}
.vault{{width:400px;height:400px;margin:0 auto;border-radius:50%;position:relative;
  background:
   repeating-conic-gradient(rgba(250,250,247,.16) 0deg 2deg, transparent 2deg 30deg),
   radial-gradient(circle at 34% 30%, #3a3a36, #1d1d1b 70%);
  box-shadow:0 42px 80px rgba(0,0,0,.6),0 0 110px rgba({acc},.12), inset 0 4px 6px rgba(255,255,255,.14), inset 0 -12px 26px rgba(0,0,0,.55)}}
.vault .knob{{position:absolute;inset:90px;border-radius:50%;background:linear-gradient(160deg,#2e2e2b,#191917);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;
  box-shadow:0 10px 24px rgba(0,0,0,.5), inset 0 3px 4px rgba(255,255,255,.12)}}
.vault .handle{{position:absolute;left:50%;top:-16px;transform:translateX(-50%);width:16px;height:64px;border-radius:9px;
  background:linear-gradient(180deg,rgb({acc}),rgba({acc},.7));box-shadow:0 8px 18px rgba({acc},.4), inset 0 2px 2.5px rgba(255,255,255,.5)}}
.folderw{{filter:drop-shadow(0 36px 55px rgba(0,0,0,.5)) drop-shadow(0 12px 22px rgba(0,0,0,.32));width:620px}}
.folder{{position:relative;background:linear-gradient(165deg,#e0b98f,#c99a6d 55%,#a97a52);border-radius:0 26px 26px 26px;padding:80px 30px 28px}}
.folder::before{{content:'';position:absolute;top:-34px;left:0;width:240px;height:44px;border-radius:18px 26px 0 0;
  background:linear-gradient(180deg,#e6c29b,#d5a97e);box-shadow:inset 0 2px 3px rgba(255,255,255,.5)}}
.stampw{{position:relative;width:580px}}
.stamp{{position:absolute;right:16px;top:14px;transform:rotate(-11deg);border:6px solid #3f7d5c;border-radius:14px;padding:10px 22px;
  font-family:'DM Mono',monospace;font-weight:500;font-size:30px;letter-spacing:.2em;color:#3f7d5c;opacity:.92;
  text-shadow:0 1px 0 rgba(255,255,255,.4)}}
.chartp{{width:640px;background:linear-gradient(162deg,#2b2b29,#1d1d1b);border-radius:34px;padding:32px;border:1px solid rgba(255,255,255,.06);
  box-shadow:0 42px 80px rgba(0,0,0,.55),0 0 110px rgba({acc},.12), inset 0 2.5px 3px rgba(255,255,255,.1), inset 0 -12px 26px rgba(0,0,0,.4)}}
.keysrow{{display:flex;gap:26px;justify-content:center;align-items:flex-end;width:660px;padding:20px 0 26px}}
.bigkey{{border-radius:26px;padding:30px 44px;font-weight:900;font-size:26px;color:#fff;text-align:center;
  background:linear-gradient(180deg,#e08a5e,#b2603e);box-shadow:0 16px 0 #7c3e26, 0 30px 44px rgba(0,0,0,.55), inset 0 3px 4px rgba(255,255,255,.5)}}
.bigkey.dim{{background:linear-gradient(180deg,#3a3a36,#262624);color:rgba(250,250,247,.8);box-shadow:0 16px 0 #121210, 0 30px 44px rgba(0,0,0,.55), inset 0 2.5px 3px rgba(255,255,255,.14)}}
.bigkey small{{display:block;font-family:'DM Mono',monospace;font-weight:500;font-size:12.5px;letter-spacing:.14em;margin-top:6px;color:rgba(255,255,255,.75)}}

"""

# ---------- builders ----------
def hd(t,tag): return f'<div class="hd"><span class="t">{t}</span><span class="tag">{tag}</span></div>'
def row(n,s,chip=None,ghost=None,strike=False,dot=True):
    nm=f'<span class="strikei">{n}</span>' if strike else n
    right=f'<span class="chip">{chip}</span>' if chip else (f'<span class="ghostchip">{ghost}</span>' if ghost else "")
    dd='<span class="dot"></span>' if dot else ""
    return f'<div class="row">{dd}<div><div class="rn">{nm}</div><div class="rs">{s}</div></div>{right}</div>'
def f_rows(cls,t,tag,rows): return f'<div class="panel {cls}">{hd(t,tag)}{"".join(rows)}</div>'
def f_fan(t,tag,rows): return f'<div class="fan"><div class="b1"></div><div class="b2"></div><div class="top">{hd(t,tag)}{"".join(rows)}</div></div>'
def f_pills(rows):
    inner="".join(r.replace('class="row"','class="pillrow"') for r in rows)
    return '<div class="pills" style="width:660px">'+inner+'</div>'
def f_dial(pct,tag,big,lbl,sub):
    return (f'<div class="dial" style="--p:{pct}%"><div class="core">'
            f'<span style="font-family:\'DM Mono\',monospace;font-size:15px;letter-spacing:.16em;color:inherit" class="tag">{tag}</span>'
            f'<span style="font-weight:900;font-size:84px;color:#FAFAF7;line-height:1">{big}</span>'
            f'<span style="font-weight:700;font-size:18px;color:#8f8f85">{lbl}</span>'
            f'<span style="font-weight:500;font-size:14.5px;color:#8f8f85">{sub}</span></div></div>')
def f_paper(t,tag,head,extra):
    return (f'<div class="paper"><div class="hd" style="margin-bottom:16px"><span class="t" style="color:#17150F">{t}</span>'
            f'<span class="tag" style="color:#a5602f;margin-right:56px">{tag}</span></div>'
            f'<div style="font-weight:800;font-size:22px;color:#17150F;margin-bottom:14px">{head}</div>'
            f'<div class="skel" style="background:rgba(23,21,15,.16);margin-bottom:8px"></div>'
            f'<div class="skel" style="background:rgba(23,21,15,.16);margin-bottom:8px;width:92%"></div>'
            f'<div class="skel" style="background:rgba(23,21,15,.10);margin-bottom:8px;width:78%"></div>'
            f'<div class="skel" style="background:rgba(23,21,15,.10);margin-bottom:22px;width:60%"></div>{extra}</div>')
def f_receipt(t,sub,items,total_l,total_r):
    rows_="".join(f'<div class="rrow"><span class="strikei">{a}</span><span class="rp strikei">{b}</span></div>' for a,b in items)
    return (f'<div class="receipt"><div style="text-align:center;font-size:15px;letter-spacing:.22em;color:#8a7a5e;margin-bottom:6px">{t}</div>'
            f'<div style="text-align:center;font-size:12.5px;letter-spacing:.14em;color:#b0a284;margin-bottom:16px">{sub}</div>{rows_}'
            f'<div class="rrow" style="border-bottom:none;padding-top:14px"><span style="font-weight:800">{total_l}</span>'
            f'<span style="font-weight:800;color:#b2603e">{total_r}</span></div></div>')
def f_ticket(t,tag,inner,fl,fr):
    return (f'<div class="tickwrap"><div class="ticket"><div class="hd" style="margin-bottom:12px">'
            f'<span class="t" style="color:#2a1c10">{t}</span><span class="tag" style="color:#6e4a28">{tag}</span></div>{inner}'
            f'<div class="tdash"></div><div style="display:flex;justify-content:space-between;font-family:\'DM Mono\',monospace;font-size:14px;color:#6e4a28">'
            f'<span>{fl}</span><span>{fr}</span></div></div></div>')
def tick_cells(cells):
    out=""
    for dn,lab,on in cells:
        st=("background:linear-gradient(160deg,#b2603e,#8a4630);color:#fff;box-shadow:0 7px 14px rgba(110,50,25,.4), inset 0 1.5px 2px rgba(255,255,255,.35)"
            if on else "background:rgba(255,255,255,.4);color:#b09877;box-shadow:inset 0 1.5px 2px rgba(255,255,255,.55)")
        out+=(f'<div style="flex:1;text-align:center"><div style="font-family:\'DM Mono\',monospace;font-size:12px;color:#6e4a28;margin-bottom:8px">{dn}</div>'
              f'<div style="border-radius:12px;padding:12px 4px;font-weight:800;font-size:14px;{st}">{lab if on else "&nbsp;"}</div></div>')
    return f'<div style="display:flex;gap:12px">{out}</div>'
def f_console(t,tag,switches,buttons=True,btn1="Approve all",btn2="Hold"):
    sw="".join(f'<div class="switchrow"><div><div class="rn">{a}</div><div class="rs">{b}</div></div><div class="sw{" on" if on else ""}"><i></i></div></div>' for a,b,on in switches)
    bt=f'<div style="display:flex;gap:22px;margin-top:22px;padding-bottom:12px;justify-content:center"><span class="keycap">{btn1}</span><span class="keycap ghost">{btn2}</span></div>' if buttons else ""
    return f'<div class="console">{hd(t,tag)}{sw}{bt}</div>'
def f_bubble(mini,t,tag,line,acc):
    return (f'<div style="width:640px;padding-bottom:30px"><div class="minibubble"><span style="font-weight:700;font-size:16px;color:#fff">{mini}</span></div>'
            f'<div class="bubble">{hd(t,tag)}'
            f'<div class="row" style="border-radius:999px;padding:14px 18px">'
            f'<img src="data:image/png;base64,{ORB}" style="width:32px;height:32px;border-radius:50%;flex-shrink:0;box-shadow:0 4px 9px rgba(0,0,0,.45)">'
            f'<div class="rs" style="font-size:16.5px;color:rgba(250,250,247,.6)">{line}</div>'
            f'<span style="margin-left:auto;width:46px;height:46px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;'
            f'background:linear-gradient(160deg,rgb({acc}),rgba({acc},.8));box-shadow:0 8px 18px rgba({acc},.42), inset 0 2px 2.5px rgba(255,255,255,.45);color:#fff;font-weight:900;font-size:20px">&#8594;</span></div></div></div>')
def f_podium(steps):
    out=""
    for i,(lb,sm,on) in enumerate(steps):
        h=70+i*36
        out+=f'<div class="step{" on" if on else ""}" style="height:{h}px"><span class="sl">{lb}</span><span class="sm">{sm}</span></div>'
    return f'<div class="podium">{out}</div>'
def f_browser(url,inner):
    return (f'<div class="browser"><div class="bbar"><span class="bdot" style="background:#e0684f"></span>'
            f'<span class="bdot" style="background:#e8b34c"></span><span class="bdot" style="background:#9fb377"></span>'
            f'<span class="burl">{url}</span></div><div class="bbody">{inner}</div></div>')
def f_stat(big,lbl,bars_hot):
    bars="".join(f'<i style="height:{h}%" class="{"hot" if i==len(bars_hot)-1 else ""}"></i>' for i,h in enumerate(bars_hot))
    return f'<div class="stat"><span class="big">{big}</span><div class="lbl">{lbl}</div><div class="bars">{bars}</div></div>'


PLANE='<svg width="120" height="120" viewBox="0 0 24 24" fill="none" stroke="rgb({acc})" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13"/><path d="M22 2 15 22 11 13 2 9z"/></svg>'
LOCK='<svg width="110" height="110" viewBox="0 0 24 24" fill="none" stroke="rgb({acc})" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
# ---- v5 utility builders ----
def f_env(title,frm,sub,chip):
    return ('<div class="envwrap"><div class="env"><div class="flap"></div><div class="letter">'
            +'<div style="font-family:\'DM Mono\',monospace;font-size:13px;letter-spacing:.16em;color:#a5602f;margin-bottom:10px">'+title+'</div>'
            +'<div style="font-weight:800;font-size:22px;color:#17150F;margin-bottom:6px">'+frm+'</div>'
            +'<div style="font-weight:500;font-size:15px;color:#8a7a5e;margin-bottom:14px">'+sub+'</div>'
            +'<span class="chip" style="margin-left:0">'+chip+'</span></div></div></div>')
def f_badge(iconhtml,badge,cap1,cap2):
    return ('<div style="width:640px;text-align:center"><div class="badgewrap"><div class="badgetile">'+iconhtml+'</div>'
            +'<span class="badge">'+badge+'</span></div>'
            +'<div style="display:inline-block;background:linear-gradient(160deg,#2b2b28,#1d1d1b);border-radius:999px;padding:14px 30px;margin-top:24px;box-shadow:0 14px 30px rgba(0,0,0,.4), inset 0 2px 2.5px rgba(255,255,255,.1)">'
            +'<span style="font-weight:800;font-size:21px;color:#FAFAF7">'+cap1+'</span>'
            +'<span style="font-weight:500;font-size:15px;color:#8f8f85;margin-left:12px">'+cap2+'</span></div></div>')
def f_metro(title,tag,stops):
    n=len(stops); html=''
    for i,(lb,sub,on) in enumerate(stops):
        x=int(100*i/(n-1))
        html+=('<span class="mst'+(' on' if on else '')+'" style="left:'+str(x)+'%"></span>'
               +'<span class="mlab" style="left:'+str(x)+'%">'+lb+'</span>'
               +'<span class="msub" style="left:'+str(x)+'%">'+sub+'</span>')
    return ('<div class="metro">'+hd(title,tag)+'<div class="mline"><div class="mfill"></div>'+html+'</div></div>')
def f_split(lcap,lrows,rcap,rrows):
    l='<span class="cap" style="color:#8f8f85">'+lcap+'</span>'
    for a in lrows: l+='<div style="font-weight:700;font-size:16.5px;color:rgba(250,250,247,.55);padding:7px 0"><span style="color:#7a5348;margin-right:9px">&#10005;</span><span class="strikei">'+a+'</span></div>'
    r='<span class="cap" style="color:rgba(255,240,232,.9)">'+rcap+'</span>'
    for a in rrows: r+='<div style="font-weight:700;font-size:16.5px;color:#fff;padding:7px 0"><span style="margin-right:9px">&#10003;</span>'+a+'</div>'
    return '<div class="split"><div class="lft">'+l+'</div><div class="rgt">'+r+'</div></div>'
def f_gauge(pct,big,lbl,sub):
    g=50 if pct>=99 else int(pct/2)
    return ('<div class="gaugewrap"><div class="gauge" style="--g:'+str(g)+'%"></div>'
            +'<div style="margin-top:-176px;position:relative;z-index:2"><div style="font-weight:900;font-size:62px;color:#FAFAF7">'+big+'</div>'
            +'<div style="font-weight:700;font-size:16px;color:#b9b9ae;margin:2px auto 0;max-width:300px">'+lbl+'</div>'
            +'<div style="font-weight:500;font-size:13.5px;line-height:1.35;color:#8f8f85;margin:3px auto 0;max-width:300px">'+sub+'</div></div></div>')
def f_odo(digits,hot_from,cap1,cap2):
    cells=''.join('<b class="'+('hot' if i>=hot_from else '')+'">'+c+'</b>' for i,c in enumerate(digits))
    return ('<div class="odow"><div style="font-family:\'DM Mono\',monospace;font-size:14px;letter-spacing:.18em;color:#8f8f85">'+cap1+'</div>'
            +'<div class="odo">'+cells+'</div>'
            +'<div style="font-weight:700;font-size:17px;color:#FAFAF7">'+cap2+'</div></div>')
def f_vault(big,lbl):
    return ('<div class="vaultw"><div class="vault"><div class="handle"></div><div class="knob">'
            +'<span style="font-weight:900;font-size:52px;color:#FAFAF7">'+big+'</span>'
            +'<span style="font-family:\'DM Mono\',monospace;font-size:13px;letter-spacing:.16em;color:#8f8f85">'+lbl+'</span></div></div></div>')
def f_folder(title,tag,rows):
    return ('<div class="folderw"><div class="folder"><div class="hd" style="margin-bottom:14px">'
            +'<span class="t" style="color:#2a1c10">'+title+'</span><span class="tag" style="color:#6e4a28">'+tag+'</span></div>'
            +''.join(rows)+'</div></div>')
def f_stamp(title,tag,head,lines,stamp):
    body=''.join('<div class="rrow"><span>'+a+'</span><span class="rp">'+b+'</span></div>' for a,b in lines)
    return ('<div class="stampw"><div class="paper" style="width:580px;border-radius:10px">'
            +'<div class="hd" style="margin-bottom:14px"><span class="t" style="color:#17150F">'+title+'</span>'
            +'<span class="tag" style="color:#a5602f;margin-right:56px">'+tag+'</span></div>'
            +'<div style="font-weight:800;font-size:21px;color:#17150F;margin-bottom:12px">'+head+'</div>'
            +'<div style="font-family:\'DM Mono\',monospace">'+body+'</div></div>'
            +'<div class="stamp">'+stamp+'</div></div>')
def f_chartline(title,tag,pts,cap):
    # pts: list of 0..100, draw svg polyline
    W2,H2=560,220
    coords=' '.join(str(int(20+i*(W2-40)/(len(pts)-1)))+','+str(int(H2-20-(H2-50)*v/100)) for i,v in enumerate(pts))
    last=coords.split()[-1].split(',')
    svg=('<svg width="'+str(W2)+'" height="'+str(H2)+'">'
         +'<polyline points="'+coords+'" fill="none" stroke="rgb({acc})" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
         +'<circle cx="'+last[0]+'" cy="'+last[1]+'" r="12" fill="#fff"/></svg>')
    return '<div class="chartp">'+hd(title,tag)+svg+'<div style="font-weight:600;font-size:15px;color:#8f8f85;margin-top:8px">'+cap+'</div></div>'
def f_keys(keys):
    html=''.join('<span class="bigkey'+('' if on else ' dim')+'">'+a+'<small>'+b+'</small></span>' for a,b,on in keys)
    return '<div class="keysrow">'+html+'</div>'
def f_battery(pct,cap1,cap2):
    fw=int(452*pct/100)
    return ('<div class="batw"><div style="font-family:\'DM Mono\',monospace;font-size:14px;letter-spacing:.18em;color:#8f8f85">'+cap1+'</div>'
            +'<div class="bat"><span class="fill" style="width:'+str(fw)+'px"></span><span class="nub"></span><span class="pct">'+str(pct)+'%</span></div>'
            +'<div style="font-weight:700;font-size:17px;color:#FAFAF7">'+cap2+'</div></div>')
def f_calendar(title,tag,cells,foot):
    body=''.join('<b'+(' class="hot"' if hot else '')+'>'+dn+('<small>'+hot+'</small>' if hot else '')+'</b>' for dn,hot in cells)
    return ('<div class="calw"><div class="hd" style="margin-bottom:2px"><span class="t" style="color:#17150F">'+title+'</span>'
            +'<span class="tag" style="color:#a5602f">'+tag+'</span></div>'
            +'<div class="cal">'+body+'</div><div class="calfoot">'+foot+'</div></div>')
def f_rings(core,items,cap):
    tags=''.join('<b><i></i>'+a+'&nbsp;&middot;&nbsp;<span style="color:#8f8f85;font-weight:500">'+b+'</span></b>' for a,b in items)
    return ('<div class="ringsw"><div class="rings"><i class="r1"></i><i class="r2"></i><i class="r3"></i><div class="core">'+core+'</div></div>'
            +'<div class="rings-tags">'+tags+'</div>'
            +'<div style="margin-top:18px;font-weight:500;font-size:15px;color:#8f8f85">'+cap+'</div></div>')
def f_shelf(title,tag,trays):
    body=''.join('<div class="tray"><div class="tn">'+a+'</div><div class="ts">'+b+'</div><span class="tchip">'+c+'</span></div>' for a,b,c in trays)
    return '<div class="shelfw">'+hd(title,tag)+body+'</div>'

# ---------- per-deck specs ----------
def specs(acc):
    A=acc
    return {
 "solostack":{
  "apollo": f_odo(["1",",","2","8","4"],3,"LEADS FOUND THIS MORNING","typed one sentence at 09:14 &middot; 200 exported with briefs"),
  "gmail_sent": f_env("FROM: YOUR SDR DESK","240 drafts, ready.","One company trigger in each. Zero templates.","Queued 10:00 local"),
  "hubspot": f_metro("Deal flow","HANDS OFF",[("Lead","auto-sourced",1),("Qualified","reply landed",1),("Proposal","drafted for you",1),("Won","$120k",0)]),
  "designer": f_folder("Brand files","OPENED BY THE CHAT",[row("launch-hero.png","in your tokens",chip="done"),row("pricing-page.fig","assembled from the pack",chip="done"),row("9 more assets","no brief, no revision loop",ghost="ready")]),
  "developer": f_stamp("Release note","TONIGHT 23:40","launch funnel &middot; live",[("Build from plain English","19:04"),("Tests: 42 passed","23:12"),("Deployed to your domain","23:40")],"SHIPPED"),
  "bill": f_receipt("YOUR OLD PAYROLL","FIVE ROLES &middot; MONTHLY",[("Researcher","$4k"),("SDR","$4k"),("Ops lead","$3k"),("Designer + dev","$4k")],"One chat, all five","cents"),
  "gate": f_vault("240","ON HOLD FOR YOU"),
  "ultron_real": f_bubble("Five roles walked into one chat.","One operator","NO HEADCOUNT","run it solo",A),
 },
 "systems":{
  "orgchart": f_split("THE HIRING PLAN",["Ops manager, $3k/mo","SDR, $4k/mo","Coordinator, $2.5k/mo"],"THE SYSTEM",["Flows fire on triggers","The gate holds sends","You approve, once"]),
  "workflows": f_console("Always on","NO REMINDERS",[("Inbound triage","every message, instantly",True),("Follow-up cadence","daily 09:00",True),("Churn watch","pings before it hurts",True),("Weekly digest","Friday 17:00",True)],buttons=False),
  "hubspot": f_chartline("Pipeline value","WHILE YOU SELL",[22,30,28,44,52,66,78,92],"$235k open &middot; every stage moved by a reply, not a meeting"),
  "scheduler": f_ticket("Publishing","NOBODY SCHEDULES",tick_cells([("MON","Post",1),("TUE","",0),("WED","Reel",1),("THU","Post",1),("FRI","News",1)]),"42 IN THE QUEUE","10:00 LOCAL EACH"),
  "leadscore": f_gauge(63,"63","accounts worth a call","out of 1,284 scanned overnight"),
  "agents": f_pills([row("CORTEX","reads companies all night",chip="on"),row("SPECTER","writes, then waits for you",chip="on"),row("STRIKER","answers every objection",chip="on"),row("PULSE","posts in your voice",chip="on")]),
  "gate": f_keys([("HOLD","PARKS THE BATCH",False),("APPROVE","RELEASES 240",True)]),
  "ultron_real": f_bubble("Zero employees. A company running.","One chat","THE SYSTEM","set it once",A),
 },
 "leadmachine":{
  "apollo": f_browser("app.51ultron.com/leads", hd("Fresh pipe","09:14 THIS MORNING")+row("Sarah Lin","Northwind &middot; hiring SDRs now",chip="94")+row("Marco Diaz","Globex &middot; raised $4M in May",chip="88")+row("Priya Rao","Initech &middot; CMO started Monday",chip="81")),
  "leadscore": f_dial(37,"THE FILTER","471","pass your ICP","the other 813 never waste a send"),
  "gmail_sent": f_badge(''''''+PLANE+'''''',"240","Ready to fly.","every one waits at the gate first"),
  "warmup": f_gauge(99,"99.2%","land in the inbox","4 warm domains &middot; ramped, never blasted"),
  "calendly": f_metro("Reply to call","NO BACK-AND-FORTH",[("Reply","comes in",1),("Slot","found for both",1),("Confirmed","calendar holds",1),("Briefed","1 page, fresh",0)]),
  "hubspot": f_split("MOST THREADS",["Die after touch one","68% never followed up","Meetings lost silently"],"THIS DESK",["Touch 2 drafted from the thread","Spaced by behaviour","58% of meetings live here"]),
  "gate": f_console("Release control","YOURS",[("240 drafts parked","read 12, spot-check the rest",False),("One tap","releases the week",True)]),
  "ultron_real": f_bubble("An SDR desk that never sleeps.","One chat","THE MACHINE","fill the pipe",A),
 },
 "agency":{
  "skills": f_browser("app.51ultron.com/techniques", hd("The roster","INSTALLED IN ONE DAY")+row("Research desk","briefs any account in minutes",chip="on")+row("Copy desk","ranked drafts, your voice",chip="on")+row("Studio","builds from 822 parts",chip="on")+row("Account exec","replies in seconds, always",chip="on")),
  "apollo": f_folder("Client folder","REFRESHED 07:00",[row("northwind-brief.pdf","champion + angle + next step",chip="today"),row("globex-brief.pdf","fresh signals overnight",chip="today"),row("call-notes.md","auto-filed after every call",ghost="synced")]),
  "seowriter": f_paper("Draft 14","SCORED 92/100","Why founders replace the stack",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Reads like you wrote it</div><div class="rs" style="color:#8a7a5e">because it learned from what you wrote</div></div><span class="chip">Publish</span></div>'),
  "designer": f_split("THE OLD LOOP",["Brief, wait 4 days","Round 1, notes","Round 2, more notes"],"NOW",["Described it once","On-brand, first try","9 assets same day"]),
  "content": f_ticket("Content retainer","CANCELLED",tick_cells([("MON","Post",1),("TUE","Reel",1),("WED","",0),("THU","Deck",1),("FRI","News",1)]),"14 SLOTS, ONE LINE","WORTH $2k/MO, COSTS CENTS"),
  "hubspot": f_pills([row("Acme","qualified while you slept",chip="$25k"),row("Globex","proposal waits for your tap",chip="$90k"),row("Northwind","closed, case study drafting",chip="$120k")]),
  "gate": f_stamp("Work order","EVERY DELIVERABLE","nothing ships unsigned",[("240 outreach emails","HOLD"),("3 posts + newsletter","HOLD"),("Launch page deploy","HOLD")],"YOUR CALL"),
  "ultron_real": f_bubble("The agency, minus the retainer.","One chat","TEN HIRES","run the roster",A),
 },
 "agentnotchatbot":{
  "agents": f_fan("Right now","WHILE YOU READ THIS",[row("Briefing Northwind","started 2 min ago",chip="running"),row("Drafting 4-step sequence","from the brief, not vibes",chip="running"),row("Updating the pipeline","reply landed at 11:02",chip="done")]),
  "workflows": f_console("It already ran","BEFORE YOUR COFFEE",[("Overnight triage","14 messages sorted",True),("Morning digest","hot threads first",True),("Cadence fired","09:00 sharp, no prompt",True)],buttons=False),
  "apollo": f_browser("live sources &middot; not memory", hd("It went and looked","JUST NOW")+row("Northwind hiring page","3 new ops roles this week",chip="live")+row("Globex funding news","$4M seed, May 28",chip="live")+row("Initech tech stack","no AI layer yet",chip="live")),
  "hubspot": f_metro("Your CRM","IT TYPES, CORRECTLY",[("Reply in","11:02",1),("Parsed","intent: pricing",1),("Stage moved","Proposal",1),("Task set","call Thursday",0)]),
  "revenue": f_stat("$48,200","MRR &middot; it did the reps, you did the calls",[30,42,52,63,75,90,100]),
  "gmail_sent": f_badge(''''''+PLANE+'''''',"SENT","Not suggested. Sent.","after your tap, never before"),
  "gate": f_split("AUTONOMOUS",["Writes alone","Researches alone","Drafts alone"],"NOT UNSUPERVISED",["Sends: your tap","Ships: your merge","Signs: never"]),
  "ultron_real": f_bubble("Chatbots reply. Operators deliver.","One chat","IT WORKS","clock it in",A),
 },
 "levels":{
  "levels": f_podium([("L1","ask",0),("L2","draft",0),("L3","chain",0),("L4","team",0),("L5","auto",0),("L6","gate",0),("L7","run",1)]),
  "apollo": f_metro("One line, five jobs","LEVEL 3",[("Source","1,284 found",1),("Filter","471 pass",1),("Brief","1 page each",1),("Draft","240 ready",0)]),
  "agents": f_pills([row("Researcher agent","works the list",chip="L4"),row("Writer agent","works the drafts",chip="L4"),row("Deals agent","works the replies",chip="L4"),row("All at once","you read one digest",ghost="parallel")]),
  "workflows": f_console("No prompts at all","LEVEL 5",[("Triggers","replace your typing",True),("Cadences","replace your memory",True),("Watchers","replace your worry",True)],buttons=False),
  "hubspot": f_vault("L6","SPEED, GATED"),
  "revenue": f_odo(["4","8",",","2","0","0"],0,"MRR AT LEVEL 7","$ &middot; one operator &middot; the machine compounds"),
  "gate": f_keys([("AUTO","EVERYTHING INTERNAL",False),("YOUR TAP","EVERYTHING EXTERNAL",True)]),
  "ultron_real": f_bubble("Level 7 is quiet. It just runs.","One chat","THE CLIMB","climb one level",A),
 },
 "onepersonrev":{
  "revenue": f_stat("$48,200","MRR &middot; up 32% &middot; payroll: $0",[30,42,52,63,75,90,100]),
  "stripe": f_receipt("COLLECTED","NOBODY CHASED",[("Acme &middot; net 30","on time"),("Globex &middot; nudge 2","paid"),("Initech &middot; renewal","auto")],"This month","$41k"),
  "leadscore": f_odo(["6","3"],0,"HOT ACCOUNTS MONDAY 07:00","the pipe refilled itself over the weekend"),
  "hubspot": f_browser("crm &middot; while you were on calls", hd("Deals moved","TODAY")+row("Acme &#8594; Qualified","reply parsed at 09:40",chip="auto")+row("Globex &#8594; Proposal","draft parked for your tap",ghost="HOLD")+row("Northwind &#8594; Won","$120k &middot; invoice queued",chip="&#10003;")),
  "calendly": f_ticket("This week","BOOKED ITSELF",tick_cells([("MON","Call",1),("TUE","",0),("WED","Call",1),("THU","Call",1),("FRI","2x",1)]),"6 CALLS FROM REPLIES","EACH WITH A BRIEF"),
  "scheduler": f_fan("Marketing","RUNS AT 10:00",[row("Launch post","went out Monday",chip="&#10003;"),row("Case study","went out Wednesday",chip="&#10003;"),row("Teardown reel","queued Friday",ghost="queued")]),
  "gate": f_vault("$","EVERY MOVE, YOUR TAP"),
  "ultron_real": f_bubble("$48k MRR. Company of one.","One chat","THE STACK","show me the money",A),
 },
 "contentteam":{
  "content": f_metro("The week","PLANNED FROM ONE LINE",[("Mon","launch post",1),("Wed","carousel",1),("Thu","teardown",1),("Fri","newsletter",0)]),
  "designer": f_folder("Asset folder","FILLED OVERNIGHT",[row("14 visuals","your tokens, every one",chip="done"),row("3 formats each","feed, story, carousel",chip="done"),row("Banned words","zero slipped through",ghost="clean")]),
  "seowriter": f_env("DRAFT 14 &middot; RANKED 92","In your voice.","Sampled from 60 of your real posts.","Publish"),
  "agents": f_fan("Pick the winner","3 HOOKS PER POST",[row("Hook A","the confession angle",chip="A"),row("Hook B","the number angle",chip="B"),row("Hook C","the enemy angle",chip="C")]),
  "warmup": f_gauge(99,"99.2%","newsletters landing","not in promotions, in the inbox"),
  "skills": f_console("The desk","12 SKILLS, NO MEETINGS",[("Calendar","plans itself",True),("Hooks","rotate, never repeat",True),("Repurpose","one post, five channels",True),("Queue","10:00 local, daily",True)],buttons=False),
  "gate": f_badge(''''''+LOCK+'''''',"3","Three drafts wait for you.","nothing posts without your tap"),
  "ultron_real": f_bubble("The feed got better after the layoff.","One chat","THE DESK","plan the week",A),
 },
 "onepersonco":{
  "orgchart": f_split("THE ORG CHART",["Head of Sales","Head of Ops","Head of Product"],"THE REALITY",["One chat, briefed once","Every role, on demand","You, approving"]),
  "apollo": f_chartline("Sales pipe","SELF-FILLING",[15,28,26,40,55,68,84,100],"19 minutes from one sentence to 200 briefed accounts"),
  "workflows": f_pills([row("Ops flow 1","triage, every message",chip="on"),row("Ops flow 2","follow-up, daily 09:00",chip="on"),row("Ops flow 3","churn watch, always",chip="on"),row("Meetings held","this quarter",ghost="zero")]),
  "developer": f_browser("app.51ultron.com/launch", hd("Product","SHIPPED FROM A SENTENCE")+row("Launch page","built + tested overnight",chip="live")+row("Changelog","wrote itself from commits",chip="live")+row("Cost past the plan","$0.00",ghost="$0")),
  "content": f_fan("Marketing","ONE LINE A WEEK",[row("Mon &middot; launch post","out at 10:00",chip="&#10003;"),row("Wed &middot; case study","out at 10:00",chip="&#10003;"),row("Fri &middot; newsletter","99.2% inboxed",chip="&#10003;")]),
  "revenue": f_dial(82,"FINANCE","$48k","MRR, adding up","invoiced, chased and booked alone"),
  "gate": f_stamp("Department orders","ALL OF THEM","today, waiting for one person",[("Sales: release 240 sends","HOLD"),("Marketing: publish 3","HOLD"),("Product: merge the PR","HOLD")],"THE CEO"),
  "ultron_real": f_bubble("CEO, staff and board. All me.","One chat","THE COMPANY","run every role",A),
 },
}

ACCENTS={
 "solostack":"204,120,92","systems":"200,70,35","leadmachine":"204,120,92","agency":"212,162,127",
 "agentnotchatbot":"200,70,35","levels":"204,120,92","onepersonrev":"212,162,127",
 "contentteam":"200,70,35","onepersonco":"204,120,92",
}

if __name__=="__main__":
    decks=sys.argv[1:] or list(ACCENTS)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":900,"height":1100},device_scale_factor=2)
        for dk in decks:
            acc=ACCENTS[dk]; sp=specs(acc)[dk]
            outd=f"{ROOT}/content/_hitl-src/models_clay/{dk}"; os.makedirs(outd,exist_ok=True)
            for stem,bodyhtml in sp.items():
                bodyhtml=bodyhtml.replace("{acc}",acc)
                html=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css(acc)}</style></head><body>{bodyhtml}</body></html>"
                pg.set_content(html); pg.wait_for_timeout(300)
                pg.screenshot(path=f"{outd}/{stem}.png",omit_background=True,full_page=True)
            print("deck OK",dk)
        b.close()
    print("done")
