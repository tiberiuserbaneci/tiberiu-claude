#!/usr/bin/env python3
# Shared Tier-3 base for the batch rebuild: card styles, embedded-font render harness, coded CTA pill.
# Each <slug>_t3.py imports this, defines 8 bespoke panel functions, and calls render(slug, PANELS).
import importlib.util, os
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
_L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(_L); _L.loader.exec_module(Lm)   # css() = embedded DM Sans/Mono @font-face

# focal dark card (reads on cream AND dark slides). Near-black, no accent tint.
CARD=('background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);'
 'border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44),'
 'inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)')
# ivory card BUILT FROM the cream slide bg (use on light/cream slides when a light object suits the idea)
CARDIV=('background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);'
 'border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14),'
 'inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)')
INK="#eae4d8"; MUT="#8f8f85"; DIM="#5f5b54"; IVINK="#2a2016"; IVMUT="#8a745a"

def render(slug, panels, vw=980, vh=980):
    outd=f"{ROOT}/content/_hitl-src/models_clay/{slug}"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":vw,"height":vh},device_scale_factor=2)
        for name,html in panels.items():
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{Lm.css('212,162,127')}</style></head><body style='padding:30px'>{html}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(360)
            pg.screenshot(path=f"{outd}/{name}.png",omit_background=True,full_page=True)
            print("  rendered",name)
        b.close()

def cta_pill(word, acc):
    # coded Tier-3 CTA pill: dark left (COMMENT + WORD) + accent cap with send arrow. Matches eyes.
    A=",".join(str(x) for x in acc)
    return f'''<div style="width:760px;height:210px;display:flex;align-items:center;justify-content:center">
      <div style="display:flex;align-items:center;border-radius:999px;overflow:hidden;box-shadow:0 24px 46px rgba(0,0,0,.45)">
        <div style="display:flex;flex-direction:column;justify-content:center;padding:26px 34px 26px 44px;
          background:linear-gradient(160deg,#2b2824,#1c1a17);border:1px solid rgba(255,255,255,.08);border-right:none">
          <span style="font-family:'DM Mono';font-weight:500;font-size:25px;letter-spacing:.16em;color:rgb({A})">COMMENT</span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:46px;color:#FAFAF7;line-height:1;margin-top:4px">{word.upper()}</span>
        </div>
        <div style="align-self:stretch;display:flex;align-items:center;padding:0 42px;
          background:linear-gradient(160deg,#e6b48f,rgb({A}) 55%,#9a5a35);box-shadow:inset 0 2px 3px rgba(255,255,255,.4)">
          <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </div>
      </div></div>'''

def render_ctas():
    # render the 3 coded pills once into _templates/cta/cta-<word>.png (keyword aligns to the pill word)
    outd=f"{ROOT}/content/_hitl-src/_templates/cta"; os.makedirs(outd,exist_ok=True)
    pills={"operator":(204,120,92),"founder":(212,162,127),"builder":(200,70,35)}
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":860,"height":320},device_scale_factor=2)
        for w,acc in pills.items():
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{Lm.css('212,162,127')}</style></head><body style='padding:30px'>{cta_pill(w,acc)}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(360)
            pg.screenshot(path=f"{outd}/cta-{w}.png",omit_background=True,full_page=True); print("cta",w)
        b.close()

if __name__=="__main__": render_ctas()
