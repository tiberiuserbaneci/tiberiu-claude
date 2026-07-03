#!/usr/bin/env python3
# 3 cover variants for slide 1 (eyes) + IG overlay proposal. Rendered via Chromium.
# A = coded hero (glowing abstract eye), C = massive type, IG = transparent overlay (rich top zone).
# (B = Vertex photoreal, generated separately.)
import importlib.util, os
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py"); Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
GRID='background:#191919;background-image:linear-gradient(rgba(250,250,247,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(250,250,247,.05) 1px,transparent 1px);background-size:54px 54px'
W,H=1080,1350

# claude spark + ultron orb marks (simplified inline)
MARKS=f'''<div style="display:flex;align-items:center;gap:22px;justify-content:center">
  <svg width="60" height="60" viewBox="0 0 24 24"><g stroke="rgb({ACC})" stroke-width="1.6" stroke-linecap="round">
    <line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></g></svg>
  <span style="color:#4a463f;font-size:30px">+</span>
  <div style="width:56px;height:56px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#4aa0ff,#0b1c3a 60%),radial-gradient(circle at 70% 74%,rgba(204,120,92,.9),transparent 50%)"></div>
</div>'''

# A - coded hero: glowing abstract EYE (sight metaphor)
def variantA():
    return f'''<div style="width:{W}px;height:{H}px;{GRID};position:relative;font-family:'DM Sans'">
      <div style="position:absolute;top:150px;left:0;right:0;text-align:center;padding:0 90px">
        <div style="font-weight:900;font-size:76px;color:#FAFAF7;line-height:1.05">Your AI is blind<br><span style="color:rgb({ACC})">by default.</span></div>
      </div>
      <div style="position:absolute;top:470px;left:0;right:0;display:flex;justify-content:center">
        <svg width="620" height="440" viewBox="0 0 620 440">
          <defs>
            <radialGradient id="iris" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="45%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#6a3a22"/></radialGradient>
            <radialGradient id="gl" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.5)"/><stop offset="60%" stop-color="rgba(204,120,92,.12)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
            <filter id="nd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
          </defs>
          <circle cx="310" cy="220" r="200" fill="url(#gl)"/>
          <path d="M70 220 Q310 40 550 220 Q310 400 70 220 Z" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="4"/>
          <path d="M120 220 Q310 90 500 220 Q310 350 120 220 Z" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>
          <circle cx="310" cy="220" r="118" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>
          <circle cx="310" cy="220" r="150" fill="none" stroke="rgba(212,162,127,.2)" stroke-width="2"/>
          <circle cx="310" cy="220" r="82" fill="url(#iris)"/>
          <ellipse cx="288" cy="196" rx="24" ry="15" fill="rgba(255,255,255,.5)" transform="rotate(-28 288 196)"/>
          <line x1="70" y1="220" x2="550" y2="220" stroke="rgba(212,162,127,.35)" stroke-width="2" stroke-dasharray="3 10"/>
          <circle cx="470" cy="150" r="7" fill="rgb({ACC})" filter="url(#nd)"/>
          <circle cx="160" cy="270" r="6" fill="rgb({ACC})" filter="url(#nd)"/>
        </svg>
      </div>
      <div style="position:absolute;bottom:190px;left:0;right:0">{MARKS}
        <div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#FAFAF7;text-align:center;margin-top:26px">Wire its eyes.</div></div>
      <div style="position:absolute;bottom:80px;left:0;right:0;display:flex;justify-content:center">
        <div style="display:flex;align-items:center;gap:12px;background:#FAFAF7;border-radius:999px;padding:16px 34px;font-weight:800;font-size:24px;color:#191919">Swipe
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#191919" stroke-width="2.6" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div></div>
    </div>'''

# C - massive typography
def variantC():
    return f'''<div style="width:{W}px;height:{H}px;{GRID};position:relative;font-family:'DM Sans'">
      <div style="position:absolute;top:44px;left:70px;border:2px solid rgb({ACC});border-radius:12px;padding:12px 20px;font-family:'DM Mono';font-size:22px;letter-spacing:.14em;color:rgb({ACC})">WIRE ITS EYES</div>
      <div style="position:absolute;top:300px;left:70px;right:70px">
        <div style="font-weight:900;font-size:168px;line-height:.92;color:#FAFAF7;letter-spacing:-4px">YOUR<br>AI IS<br><span style="color:rgb({ACC})">BLIND.</span></div>
      </div>
      <div style="position:absolute;bottom:230px;left:70px;right:70px;font-weight:500;font-size:40px;color:#a8a296">Out of the box it cannot see your market, your inbox, or this morning's news.</div>
      <div style="position:absolute;bottom:96px;left:70px;display:flex;align-items:center;gap:20px">
        <svg width="52" height="52" viewBox="0 0 24 24"><g stroke="rgb({ACC})" stroke-width="1.6" stroke-linecap="round"><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></g></svg>
        <div style="width:48px;height:48px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#4aa0ff,#0b1c3a 60%),radial-gradient(circle at 70% 74%,rgba(204,120,92,.9),transparent 50%)"></div>
        <span style="font-family:'DM Mono';font-size:22px;color:#8f8f85;margin-left:6px">swipe →</span></div>
    </div>'''

# IG overlay - transparent, rich TOP zone only (rest open for the video)
def ig_overlay():
    return f'''<div style="width:{W}px;height:{H}px;background:transparent;position:relative;font-family:'DM Sans'">
      <div style="position:absolute;top:96px;left:70px;right:70px">
        <div style="display:inline-block;border:2px solid rgb({ACC});border-radius:12px;padding:9px 18px;font-family:'DM Mono';font-size:20px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:26px">WIRE ITS EYES</div>
        <div style="position:relative">
          <div style="position:absolute;inset:-16px -24px;background:radial-gradient(ellipse at 30% 50%,rgba(12,10,9,.72),rgba(12,10,9,0) 72%);filter:blur(10px)"></div>
          <div style="position:relative;font-weight:900;font-size:82px;line-height:1.02;color:#FAFAF7">Your AI is blind<br><span style="color:rgb({ACC})">by default.</span></div>
        </div>
        <div style="display:flex;align-items:center;gap:18px;margin-top:30px">
          <svg width="50" height="50" viewBox="0 0 24 24"><g stroke="rgb({ACC})" stroke-width="1.6" stroke-linecap="round"><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></g></svg>
          <div style="width:46px;height:46px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#4aa0ff,#0b1c3a 60%),radial-gradient(circle at 70% 74%,rgba(204,120,92,.9),transparent 50%)"></div>
          <span style="font-family:'DM Mono';font-size:20px;letter-spacing:.1em;color:#d9d5cc;margin-left:4px">wire its eyes</span>
        </div>
      </div>
    </div>'''

if __name__=="__main__":
    outd=f"{ROOT}/scratchpad/covers"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        for name,html,transp in [("A",variantA(),False),("C",variantC(),False),("ig",ig_overlay(),True)]:
            pg=b.new_page(viewport={"width":W,"height":H},device_scale_factor=2)
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{Lm.css(ACC)}*{{box-sizing:border-box}}body{{margin:0;padding:0}}</style></head><body>{html}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{outd}/cover_{name}.png",omit_background=transp)
            pg.close(); print("rendered",name)
        b.close()
