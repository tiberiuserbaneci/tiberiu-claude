#!/usr/bin/env python3
# MONEY IN YOUR SLEEP - 2.5D (coded mockups, big, fill the canvas). Same spine as the Vertex version,
# to compare 3D vs 2.5D. Reuses build_team_3d chrome + cover; bigger object zone (fills the central canvas).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
ZONE=(56,768,1024,1342)   # big landscape zone, clears the 2-line headline, sits above the progress bar

T2.COVER=dict(head=[[wo("I slept 8 hours.")],[co("It worked all 8.")]])
CONTENT=[
 ("APOLLO",   [[wo("It sourced")],[co("200 leads.")]],          f"{M}/apollo.png",     0.99),
 ("GMAIL",    [[wo("It sent")],[co("every email.")]],           f"{M}/gmail_sent.png", 0.99),
 ("REPLIES",  [[wo("18 replies")],[co("by 6am.")]],             f"{M}/gmail.png",      0.99),
 ("CALENDLY", [[wo("6 calls")],[co("booked.")]],                f"{M}/calendly.png",   0.99),
 ("HUBSPOT",  [[wo("2 deals")],[co("Closed Won.")]],            f"{M}/hubspot.png",    0.99),
 ("STRIPE",   [[wo("$8,400")],[co("collected.")]],              f"{M}/stripe.png",     0.99),
 ("THE GATE", [[wo("Nothing ran")],[co("without my yes.")]],    f"{M}/gate.png",       0.99),
 ("ULTRON",   [[wo("One operator.")],[co("The night shift.")]], f"{M}/ultron.png",     0.99),
]
CTA=("WAKE UP TO IT", [[wo("Wake up to it,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.55)

def body25(base, eyebrow, head, objpath, page, n, last, fill):
    from PIL import ImageDraw
    d=ImageDraw.Draw(base); T2.ghost(base, f"{page:02d}")
    T2.ls_text(d,(T2.MX,476),eyebrow,T2.mono(28),T2.CORAL,4)
    s=T2.fit_hook(d,head,T2.W-2*T2.MX,start=84,floor=64); hf=T2.dm(900,s); lh=int(s*1.14); y=540
    for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=lh
    z=ZONE if not last else (300,820,780,1300)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), z, fill=fill)
    if last:
        d.text((T2.MX,1258),"Follow for one AI system for founders every day.",font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
    else: T2.progress(d,page,n)

def deck(outdir, overlay):
    import os; os.makedirs(outdir,exist_ok=True)
    slides=[("cover",)]+[("mid",c) for c in CONTENT]+[("last",CTA)]; n=len(slides)
    for i,sl in enumerate(slides,1):
        if sl[0]=="cover":
            if overlay: T2.cover_ig(f"{outdir}/s{i}.png"); continue
            base=Image.new("RGBA",(T2.W,T2.H),T2.BG+(255,)); T2.cover_tt(base,n); base.convert("RGB").save(f"{outdir}/s{i}.png"); continue
        eb,head,objp,fill=sl[1]; base=Image.new("RGBA",(T2.W,T2.H),T2.BG+(255,))
        body25(base,eb,head,objp,i,n,sl[0]=="last",fill); base.convert("RGB").save(f"{outdir}/s{i}.png")
    return n

if __name__=="__main__":
    a=deck(f"{T2.OUTBASE}/s25_tt",False); b=deck(f"{T2.OUTBASE}/s25_ig",True)
    T2.montage(f"{T2.OUTBASE}/s25_tt","s25_tt",a); T2.montage(f"{T2.OUTBASE}/s25_ig","s25_ig",b)
    print("tt",a,"ig",b)
