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

# ---------- per-deck specs ----------
def specs(acc):
    A=acc
    return {
 "solostack":{
  "apollo": f_browser("app.51ultron.com/leads", hd("Leads","CORTEX &middot; LIVE")+row("Sarah Lin","Northwind &middot; hiring SDRs",chip="94 hot")+row("Marco Diaz","Globex &middot; raised $4M",chip="88 hot")+row("Priya Rao","Initech &middot; new CMO",chip="81 hot")),
  "gmail_sent": f_fan("Outbox","GATED &middot; YOUR TAP",[row("Acme &middot; partnership","one trigger &middot; 62 words",chip="Sent 10:00"),row("Globex &middot; pricing","one trigger &middot; 62 words",chip="Sent 10:00"),row("Northwind &middot; intro","one trigger &middot; 62 words",chip="Sent 10:01")]),
  "hubspot": f_rows("kraft","Pipeline","UPDATES ITSELF",[row("Acme","Qualified &middot; $25k",ghost="moved"),row("Globex","Proposal &middot; $90k",ghost="drafted"),row("Northwind","Closed won &middot; $120k",chip="WON")]),
  "designer": f_paper("On brand","9 ASSETS","Launch visuals, your tokens",'<div style="display:flex;gap:12px;margin-bottom:8px"><span style="flex:1;height:64px;border-radius:14px;background:linear-gradient(160deg,#c97a54,#a55a38);box-shadow:inset 0 2px 2.5px rgba(255,255,255,.4)"></span><span style="flex:1;height:64px;border-radius:14px;background:linear-gradient(160deg,#e0b98f,#c99a6d);box-shadow:inset 0 2px 2.5px rgba(255,255,255,.5)"></span><span style="flex:1;height:64px;border-radius:14px;background:linear-gradient(160deg,#fdfbf5,#e8ddc6);border:1px solid rgba(120,95,60,.2)"></span></div>'),
  "developer": f_console("Deploy","SENTINEL",[("Build the page","from plain English",True),("Tests","42 passed &middot; 0 failed",True),("Live","$0 beyond the plan",True)],btn1="Ship it",btn2="Preview"),
  "bill": f_receipt("YOUR PAYROLL","FIVE ROLES &middot; MONTHLY",[("Researcher","$4k"),("SDR","$4k"),("Ops","$3k"),("Designer + dev","$4k")],"One chat","cents"),
  "gate": f_rows("terra","The gate","YOUR TAP",[row("Send 240 outreach emails","parked on HOLD &middot; waiting for you",ghost="HOLD"),row("Publish 3 posts","drafted in your voice",ghost="HOLD"),row("Move Globex to Proposal","from this morning's reply",chip="AUTO")])+'<div style="width:620px;display:flex;gap:22px;margin-top:24px;justify-content:center"><span class="keycap">Approve all</span><span class="keycap ghost">Hold</span></div>',
  "ultron_real": f_bubble("Team replaced. Five roles, one chat.","One chat","NO HEADCOUNT","run it solo",A),
 },
 "systems":{
  "orgchart": f_rows("ivory","Org chart","HEADCOUNT: 0",[row("Researcher","CORTEX runs it",strike=True,ghost="system"),row("SDR","SPECTER + the gate",strike=True,ghost="system"),row("Ops lead","flows on triggers",strike=True,ghost="system"),row("Content","PULSE in your voice",strike=True,ghost="system")]),
  "workflows": f_console("Systems","SET ONCE",[("Inbound triage","every message",True),("Follow-up cadence","daily 09:00",True),("Churn watch","on usage drop",True),("Weekly digest","Fri 17:00",True)],buttons=False),
  "hubspot": f_fan("Pipeline","NO DRAGGING",[row("Acme","reply landed &middot; auto-moved",chip="Qualified"),row("Globex","proposal drafted &middot; on HOLD",ghost="your tap"),row("Northwind","$120k &middot; closed won",chip="WON")]),
  "scheduler": f_ticket("This week","42 QUEUED",tick_cells([("MON","Post",1),("TUE","",0),("WED","Reel",1),("THU","Post",1),("FRI","News",1)]),"ONE MESSAGE IN","10:00 LOCAL OUT"),
  "leadscore": f_dial(63,"LEADSCORE","63","accounts flagged hot","1,284 scanned &middot; scored 0-100"),
  "agents": f_pills([row("CORTEX","briefs the account",chip="runs"),row("SPECTER","drafts, the gate holds",chip="runs"),row("STRIKER","moves the pipeline",chip="runs"),row("PULSE","writes in your voice",chip="runs")]),
  "gate": f_console("The gate","YOUR TAP",[("240 outreach emails","parked on HOLD",False),("3 posts + newsletter","drafted, queued",False),("Globex to Proposal","from this morning",True)]),
  "ultron_real": f_bubble("Systems running. Employees: zero.","One chat","EVERY SYSTEM","set it once",A),
 },
 "leadmachine":{
  "apollo": f_pills([row("Sarah Lin","Northwind &middot; hiring SDRs",chip="94"),row("Marco Diaz","Globex &middot; raised $4M",chip="88"),row("Priya Rao","Initech &middot; new CMO",chip="81"),row("Alex Chen","Vandelay &middot; tech switch",chip="79")]),
  "leadscore": f_rows("ivory","Ranked","0-100 &middot; PUBLIC DATA",[row("1,284 scanned","live company + contact data",ghost="in"),row("471 pass the ICP","founder / CEO &middot; 2-50 seats",ghost="scored"),row("63 flagged hot","call-now, briefed",chip="OUT")]),
  "gmail_sent": f_browser("mail &middot; outbox", hd("Sequence","SPECTER")+row("Acme &middot; intro","one trigger &middot; 62 words",chip="Sent")+row("Acme &middot; follow-up 2","from the thread, not a timer",chip="Sent")+row("Acme &middot; case study","books the call",ghost="queued")),
  "warmup": f_rows("terra","Deliverability","4 DOMAINS WARM",[row("Inbox placement","ramped 60 a day",chip="99.2%"),row("Spam rate","watched weekly",chip="0.3%"),row("Bounce","under control",chip="0.3%")]),
  "calendly": f_rows("","Booked","FROM REPLIES",[row("Sarah Lin","Tue 10:00 &middot; 30m &middot; brief attached",chip="Call"),row("Marco Diaz","Wed 14:00 &middot; 30m &middot; brief attached",chip="Call"),row("Priya Rao","Fri 11:00 &middot; 30m &middot; brief attached",chip="Call")]),
  "hubspot": f_fan("Follow-up","NO DEAD THREADS",[row("Touch 2 drafted","58% of meetings live here",ghost="your tap"),row("Stage moves","as replies land",chip="auto"),row("Stale deals","flagged at day 30",chip="2")]),
  "gate": f_console("The gate","YOUR TAP",[("240 sends ready","read 12, spot-check the rest",False),("Release the queue","10:00 local per prospect",True)]),
  "ultron_real": f_bubble("A whole SDR desk. One subscription.","One chat","THE MACHINE","source, write, send, book",A),
 },
 "agency":{
  "skills": f_browser("app.51ultron.com/techniques", hd("The roster","10 SKILLS INSTALLED")+row("Research + briefs","CORTEX",chip="on")+row("Copy + content","PULSE &middot; SPECTER",chip="on")+row("Design + build","SENTINEL &middot; Crescendo",chip="on")+row("Deals + follow-up","STRIKER",chip="on")),
  "apollo": f_rows("ivory","Account briefs","1 PAGE EACH",[row("Northwind","champion &middot; signals &middot; angle",chip="ready"),row("Globex","refreshed this morning",chip="ready"),row("Initech","next step attached",chip="ready")]),
  "seowriter": f_paper("Draft","RANKED 92","Why founders replace the stack",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">On brand</div><div class="rs" style="color:#8a7a5e">your voice, your no-list</div></div><span class="chip">Publish</span></div>'),
  "designer": f_rows("kraft","On brand","FROM THE PACK",[row("Hero + pricing + FAQ","assembled in your tokens",chip="done"),row("9 assets","one brief, no revision loop",chip="done"),row("822 components","Crescendo library",ghost="ready")]),
  "content": f_ticket("The plan","14 SLOTS",tick_cells([("MON","Post",1),("TUE","Reel",1),("WED","",0),("THU","Post",1),("FRI","News",1)]),"PLANNED FROM ONE LINE","QUEUED 10:00"),
  "hubspot": f_pills([row("Acme","qualified from the reply",chip="$25k"),row("Globex","proposal on HOLD",chip="$90k"),row("Northwind","closed won",chip="$120k")]),
  "gate": f_rows("terra","The gate","YOUR TAP",[row("Everything external","parks on HOLD first",ghost="HOLD"),row("You read, you tap","then it moves",chip="1 tap"),row("Every release","stamped with a run ID",ghost="logged")])+'<div style="width:620px;display:flex;gap:22px;margin-top:24px;justify-content:center"><span class="keycap">Approve all</span><span class="keycap ghost">Hold</span></div>',
  "ultron_real": f_bubble("Ten hires. One chat, no retainer.","One chat","THE AGENCY","run the roster",A),
 },
 "agentnotchatbot":{
  "agents": f_fan("Parallel runs","SIX AT ONCE",[row("Brief Northwind","CORTEX &middot; running",chip="2 min"),row("Draft the sequence","SPECTER &middot; running",chip="4 min"),row("Update the pipe","STRIKER &middot; done",chip="&#10003;")]),
  "workflows": f_console("It keeps going","NO PROMPTS",[("Inbound triage","fires on every message",True),("Follow-up cadence","daily 09:00, no reminder",True),("Churn watch","pings before it hurts",True)],buttons=False),
  "apollo": f_browser("live data &middot; not memory", hd("It goes and finds it","CORTEX")+row("1,284 companies","pulled live, not guessed",chip="now")+row("902 net-new","deduped against your CRM",chip="clean")+row("200 exported","ranked, with briefs",chip="19 min")),
  "hubspot": f_ticket("It updates your systems","CRM &middot; LIVE",tick_cells([("QUAL","Acme",1),("PROP","Globex",1),("WON","North",1),("NEXT","",0),("NEXT","",0)]),"REPLIES MOVE STAGES","NO DRAGGING"),
  "revenue": f_stat("$48,200","MRR &middot; up 32% &middot; it acts, you approve",[30,42,52,63,75,90,100]),
  "gmail_sent": f_pills([row("It sends","not suggests &middot; gate first",chip="240"),row("It books","replies become calls",chip="6"),row("It logs","every run stamped",chip="ID")]),
  "gate": f_console("The gate","STILL YOURS",[("Nothing external","fires alone",False),("Your tap","releases the batch",True)]),
  "ultron_real": f_bubble("Not a chatbot. An operator.","One chat","IT WORKS","run the company",A),
 },
 "levels":{
  "levels": f_podium([("L1","ask",0),("L2","draft",0),("L3","flow",0),("L4","desk",0),("L5","team",0),("L6","gate",0),("L7","run",1)]),
  "apollo": f_rows("kraft","Level 3","CHAINED RUNS",[row("Source the list","one line in",chip="done"),row("Brief each account","hands off to the next",chip="auto"),row("Draft the openers","no copy-paste between",chip="auto")]),
  "agents": f_pills([row("Level 4","agents wired, side by side",chip="6"),row("One task each","running in parallel",chip="now"),row("You approve","the only human step",chip="tap")]),
  "workflows": f_console("Level 5","AUTOMATE",[("Triggers, not prompts","fires all day",True),("No reminders","it remembers the cadence",True),("Set it once","runs daily",True)],buttons=False),
  "hubspot": f_fan("Level 6","THE GATE ON",[row("AI speed","240 drafts in minutes",chip="fast"),row("Zero accidents","everything parks first",ghost="HOLD"),row("You stay CEO","one tap a day",chip="1")]),
  "revenue": f_dial(90,"LEVEL 7","$48k","MRR &middot; one operator","the whole business behind a chat"),
  "gate": f_rows("terra","The gate","EVERY LEVEL",[row("Nothing sends alone","at any level",ghost="rule"),row("Undo anytime","hold parks with zero loss",ghost="safe"),row("Audit trail","run ID on every release",chip="log")])+'<div style="width:620px;display:flex;gap:22px;margin-top:24px;justify-content:center"><span class="keycap">Approve all</span><span class="keycap ghost">Hold</span></div>',
  "ultron_real": f_bubble("Most stop at level 2. The map goes to 7.","One chat","THE CLIMB","climb a level",A),
 },
 "onepersonrev":{
  "revenue": f_stat("$48,200","MRR &middot; up 32% &middot; no team on the payroll",[30,42,52,63,75,90,100]),
  "stripe": f_receipt("PAID INVOICES","AUTO-CHASED",[("Acme &middot; net 30","waited"),("Globex &middot; reminder 2","waited")],"Collected on time","$41k"),
  "leadscore": f_dial(63,"THE PIPE","63","accounts flagged hot","sourced, enriched, scored 0-100"),
  "hubspot": f_browser("crm &middot; live", hd("Closing","SELF-UPDATING")+row("Acme","reply in &middot; moved to Qualified",chip="auto")+row("Globex","proposal drafted &middot; on HOLD",ghost="your tap")+row("Northwind","$120k &middot; closed won",chip="WON")),
  "calendly": f_ticket("Booked","6 THIS WEEK",tick_cells([("MON","Call",1),("TUE","",0),("WED","Call",1),("THU","Call",1),("FRI","Call",1)]),"FROM REPLIES","BRIEF ATTACHED"),
  "scheduler": f_fan("Marketing","QUEUED",[row("Launch post","LinkedIn + X",chip="Mon"),row("Case study","carousel, 10 pages",chip="Wed"),row("Teardown reel","TikTok + IG",chip="Fri")]),
  "gate": f_console("The gate","YOUR TAP",[("Every send","parked on HOLD first",False),("Every invoice chase","your tone, your call",False),("Release","one tap",True)]),
  "ultron_real": f_bubble("$48k MRR. Headcount: one.","One chat","THE STACK","show me the money",A),
 },
 "contentteam":{
  "content": f_ticket("The plan","14 SLOTS",tick_cells([("MON","Post",1),("TUE","Reel",1),("WED","",0),("THU","Deck",1),("FRI","News",1)]),"PLANNED FROM ONE LINE","POSTS 10:00 LOCAL"),
  "designer": f_rows("kraft","On brand","NO BRIEFS",[row("9 assets","one message, your tokens",chip="done"),row("Posts + reels + carousels","each channel native",chip="done"),row("Banned words","enforced on every draft",ghost="clean")]),
  "seowriter": f_paper("Draft","RANKED 92","Why founders replace the stack",'<div style="display:flex;align-items:center;gap:12px"><span class="dot"></span><div><div class="rn" style="color:#17150F">Voice locked</div><div class="rs" style="color:#8a7a5e">sampled from your real posts</div></div><span class="chip">Publish</span></div>'),
  "agents": f_fan("Drafts","IN PARALLEL",[row("Hook A / B / C","you approve the best",chip="3"),row("Long-form + caption","from the same brief",chip="2"),row("Repurposed","LinkedIn to TikTok",chip="auto")]),
  "warmup": f_dial(99,"NEWSLETTER","99.2%","landed in the inbox","domains warm &middot; spam 0.3%"),
  "skills": f_console("The desk","12 SKILLS ON",[("Content calendar","plans the week",True),("Hooks + captions","your voice",True),("Repurpose","every channel",True),("Publish queue","10:00 local",True)],buttons=False),
  "gate": f_pills([row("Nothing posts alone","every draft parks first",ghost="HOLD"),row("You approve the best","one tap on the batch",chip="tap"),row("Every post logged","run ID attached",chip="ID")]),
  "ultron_real": f_bubble("A creative team. Price of a chat.","One chat","THE DESK","plan the week",A),
 },
 "onepersonco":{
  "orgchart": f_rows("ivory","The org chart","EVERY BOX = ONE CHAT",[row("Sales","STRIKER + the gate",strike=True,ghost="chat"),row("Operations","flows on triggers",strike=True,ghost="chat"),row("Product","SENTINEL ships it",strike=True,ghost="chat"),row("Marketing + finance","PULSE &middot; the meter",strike=True,ghost="chat")]),
  "apollo": f_fan("Sales","SELF-FILLING",[row("1,284 scanned","200 briefed",chip="19 min"),row("240 drafted","gate holds",ghost="HOLD"),row("6 calls booked","briefs attached",chip="&#10003;")]),
  "workflows": f_console("Operations","NO MEETINGS",[("Inbound triage","every message",True),("Follow-up cadence","daily 09:00",True),("Churn watch","on usage drop",True),("Weekly digest","Fri 17:00",True)],buttons=False),
  "developer": f_browser("app.51ultron.com/launch", hd("Product","SHIPPED FROM CHAT")+row("Build the page","plain English in",chip="built")+row("Tests","42 passed &middot; 0 failed",chip="&#10003;")+row("Live","$0 beyond the plan",chip="live")),
  "content": f_ticket("Marketing","QUEUED",tick_cells([("MON","Post",1),("TUE","",0),("WED","Reel",1),("THU","Post",1),("FRI","News",1)]),"ONE COORDINATOR: NONE","10:00 LOCAL"),
  "revenue": f_stat("$48,200","MRR &middot; up 32% &middot; payroll $0",[30,42,52,63,75,90,100]),
  "gate": f_rows("terra","The gate","EVERY DEPARTMENT",[row("Sales sends","your tap first",ghost="HOLD"),row("Posts publish","your tap first",ghost="HOLD"),row("Code ships","your merge",chip="PR")])+'<div style="width:620px;display:flex;gap:22px;margin-top:24px;justify-content:center"><span class="keycap">Approve all</span><span class="keycap ghost">Hold</span></div>',
  "ultron_real": f_bubble("One person. Every department.","One chat","THE COMPANY","run every role",A),
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
                html=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css(acc)}</style></head><body>{bodyhtml}</body></html>"
                pg.set_content(html); pg.wait_for_timeout(300)
                pg.screenshot(path=f"{outd}/{stem}.png",omit_background=True,full_page=True)
            print("deck OK",dk)
        b.close()
    print("done")
