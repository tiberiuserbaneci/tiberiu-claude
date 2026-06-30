#!/usr/bin/env python3
# FROM 9 TO 5 TO FOUNDER - NORMAL Vertex GTM dashboards (no phone), TikTok+IG (deck_poll)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("From 9 to 5,")],[co("to founder.")]])
T2.CONTENT=[
  ("LIVE", [[wo("It runs")],[co("while you clock in.")]], f"{D}/m3_01.png", 1.0),
  ("OUTREACH", [[wo("Outreach goes out")],[co("on its own.")]], f"{D}/m3_02.png", 1.0),
  ("PIPELINE", [[wo("Deals move")],[co("without you.")]], f"{D}/m3_03.png", 1.0),
  ("PROJECTS", [[wo("Your side company,")],[co("organized.")]], f"{D}/m3_04.png", 1.0),
  ("UNITS", [[wo("Seven units,")],[co("zero hires.")]], f"{D}/m3_05.png", 1.0),
  ("MEMORY", [[wo("It never")],[co("forgets.")]], f"{D}/m3_06.png", 1.0),
  ("STACK", [[wo("One bill,")],[co("your whole stack.")]], f"{D}/m3_07.png", 1.0),
  ("ULTRON", [[wo("Quit when")],[co("it pays you.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
MX=T2.MX
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{page:02d}")
    if last:
        T2.ls_text(d,(MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
        s=T2.fit_hook(d,head,T2.W-2*MX,start=84,floor=58); hf=T2.dm(900,s); y=534
        for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.14)
        T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (130,720,950,1245), fill=fill)
        _ft=(T2.save_foot() if getattr(T2,"_TT",False) else "Follow for one AI system for founders every day.")
        d.text((MX,1262),_ft,font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
        return
    T2.ls_text(d,(MX,300),eyebrow,T2.mono(26),T2.CORAL,4)
    s=min(T2.fit_hook(d,head,T2.W-2*MX,start=64,floor=44),56); hf=T2.dm(900,s); y=340
    for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.12)
    # NORMAL dashboard: native aspect, uniform scale (no distortion, sphere stays circular)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (130,492,950,1560), fill=1.0)
    x0,x1=90,928; yb=1576; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck_poll(f"{T2.OUTBASE}/mat3_tt",False); b=T2.deck_poll(f"{T2.OUTBASE}/mat3_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat3_tt",f"mat3_tt",a); T2.montage(f"{T2.OUTBASE}/mat3_ig",f"mat3_ig",b)
    print("tt",a,"ig",b)
