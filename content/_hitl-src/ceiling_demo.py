#!/usr/bin/env python3
# CEILING DEMO - cele mai complexe clase de forme din cod (HTML/CSS 3D + SVG), alpha real.
# Proof pentru operator: cat de departe pot duce panourile fata de shapes simple.
import importlib.util, os
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="204,120,92"

# ---- CLASS A: ISOMETRIC 2.5D STACK (CSS 3D transforms - real perspective, top+side faces) ----
def iso_stack():
    layers=[("DISTRIBUTION","10:00 local, daily",4),("CONTENT","your voice, ranked",3),
            ("PIPELINE","gated at every send",2),("MEMORY","icp / voice / rules",1)]
    slabs=""
    for i,(t,s,lvl) in enumerate(layers):
        z=i*70
        tone=["#3a3a36","#332f2b","#2c2824","#262220"][i]
        slabs+=f'''<div class="slab" style="transform:translateZ({z}px);background:linear-gradient(135deg,{tone},#1a1816)">
          <div class="face-r"></div><div class="face-f"></div>
          <div class="cap"><b>{t}</b><span>{s}</span></div></div>'''
    return f'''<div class="isowrap"><div class="iso">{slabs}</div></div>
    <style>
    .isowrap{{width:900px;height:760px;display:flex;align-items:center;justify-content:center;perspective:1600px}}
    .iso{{transform-style:preserve-3d;transform:rotateX(58deg) rotateZ(-42deg)}}
    .slab{{position:absolute;width:420px;height:420px;left:-210px;top:-210px;border-radius:30px;
      transform-style:preserve-3d;border:1px solid rgba(255,255,255,.08);
      box-shadow:0 0 0 1px rgba(0,0,0,.4);}}
    .slab .face-f{{position:absolute;left:0;bottom:-46px;width:100%;height:46px;border-radius:0 0 30px 30px;
      background:linear-gradient(180deg,#181614,#0e0d0c);transform-origin:top;transform:rotateX(-90deg);}}
    .slab .face-r{{position:absolute;right:-46px;top:0;width:46px;height:100%;border-radius:0 30px 30px 0;
      background:linear-gradient(90deg,#0e0d0c,#181614);transform-origin:left;transform:rotateY(90deg);}}
    .slab .cap{{position:absolute;left:34px;top:30px;transform:rotate(0deg)}}
    .slab .cap b{{display:block;font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7;letter-spacing:-.5px}}
    .slab .cap span{{font-family:'DM Mono';font-size:15px;color:#c9a583;letter-spacing:.04em}}
    </style>'''

# ---- CLASS B: NODE / FLOW GRAPH (SVG bezier connectors + glowing nodes) ----
def node_graph():
    import math
    cx,cy=450,340; R=230
    sat=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
         ("PULSE","content"),("SENTINEL","code"),("COUNSEL","legal")]
    edges=""; nodes=""
    for i,(nm,role) in enumerate(sat):
        ang=math.radians(-90+i*(360/len(sat)))
        x=cx+R*math.cos(ang); y=cy+R*math.sin(ang)
        mx=(cx+x)/2 + (y-cy)*0.18; my=(cy+y)/2 - (x-cx)*0.18
        edges+=f'<path d="M{cx} {cy} Q{mx:.0f} {my:.0f} {x:.0f} {y:.0f}" stroke="rgba(204,120,92,.55)" stroke-width="2.5" fill="none"/>'
        nodes+=f'''<g filter="url(#g)"><circle cx="{x:.0f}" cy="{y:.0f}" r="52" fill="url(#nd)"/>
          <circle cx="{x:.0f}" cy="{y:.0f}" r="52" fill="none" stroke="rgba(255,255,255,.1)"/></g>
          <text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{nm}</text>
          <text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#9a9488">{role}</text>'''
    return f'''<div style="width:900px;height:700px">
    <svg width="900" height="700" viewBox="0 0 900 680">
      <defs>
        <radialGradient id="nd" cx="35%" cy="30%"><stop offset="0%" stop-color="#34302c"/><stop offset="100%" stop-color="#1a1816"/></radialGradient>
        <radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a30"/></radialGradient>
        <filter id="g" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.55"/></filter>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter>
      </defs>
      {edges}
      {nodes}
      <g filter="url(#gh)"><circle cx="{cx}" cy="{cy}" r="86" fill="url(#hub)"/>
        <circle cx="{cx}" cy="{cy}" r="86" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="1.5"/></g>
      <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">ONE</text>
      <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">FOUNDER</text>
    </svg></div>'''

# ---- CLASS C: REAL DATA-VIZ (SVG area chart, gradient fill, gridlines, plotted points, axis) ----
def area_chart():
    pts=[18,26,22,40,52,48,70,88,82,100]
    W,H=820,440; pad=40
    xs=[pad+i*(W-2*pad)/(len(pts)-1) for i in range(len(pts))]
    ys=[H-pad-(v/100)*(H-2*pad) for v in pts]
    line=" ".join(f"{'M' if i==0 else 'L'}{xs[i]:.0f} {ys[i]:.0f}" for i in range(len(pts)))
    area=line+f" L{xs[-1]:.0f} {H-pad} L{xs[0]:.0f} {H-pad} Z"
    dots="".join(f'<circle cx="{xs[i]:.0f}" cy="{ys[i]:.0f}" r="5" fill="#1a1816" stroke="rgb({ACC})" stroke-width="3"/>' for i in range(len(pts)))
    grid="".join(f'<line x1="{pad}" y1="{H-pad-(g/100)*(H-2*pad):.0f}" x2="{W-pad}" y2="{H-pad-(g/100)*(H-2*pad):.0f}" stroke="rgba(250,250,247,.07)"/>' for g in (0,25,50,75,100))
    return f'''<div class="chcard"><div class="hd" style="margin-bottom:6px"><span class="t">Usefulness</span><span class="tag">EVERY SESSION</span></div>
    <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
      <defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="rgba(204,120,92,.42)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></linearGradient></defs>
      {grid}
      <path d="{area}" fill="url(#fill)"/>
      <path d="{line}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      {dots}
      <circle cx="{xs[-1]:.0f}" cy="{ys[-1]:.0f}" r="9" fill="rgb({ACC})"/>
    </svg>
    <div style="font-weight:500;font-size:15px;color:#8f8f85;margin-top:6px">corrections become rules: month three runs sharper than month one alone</div>
    </div>
    <style>.chcard{{width:900px;background:linear-gradient(165deg,#2b2b28,#1d1d1b);border-radius:34px;padding:34px;
      border:1px solid rgba(255,255,255,.07);box-shadow:0 42px 80px rgba(0,0,0,.55), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)}}
      .chcard .hd .t{{font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7}}
      .chcard .hd .tag{{font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#a5602f}}</style>'''

DEMOS={"iso_stack":iso_stack(),"node_graph":node_graph(),"area_chart":area_chart()}

if __name__=="__main__":
    outd=f"{ROOT}/scratchpad/ceiling"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":960,"height":820},device_scale_factor=2)
        for name,html in DEMOS.items():
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{Lm.css(ACC)}</style></head><body style='padding:30px'>{html}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{outd}/{name}.png",omit_background=True,full_page=True)
            print("rendered",name)
        b.close()
    print("done")
