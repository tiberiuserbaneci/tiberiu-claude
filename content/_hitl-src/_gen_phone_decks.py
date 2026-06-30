HEADER='''#!/usr/bin/env python3
# {title}
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{{T2.OBJ}}/models_phone"; LIB=T2.LIB; UL=f"{{T2.OBJ}}/models_rival2/ultron_login.png"
T2.COVER=dict(head={cover}{sub})
T2.CONTENT=[
{content}
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{{LIB}}/cta3d-operator.png", 0.92)
# BIG phone (fills the visible band, screen continuous) + compact hook on top
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{{page:02d}}")
    if last:
        T2.ls_text(d,(T2.MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
        s=T2.fit_hook(d,head,T2.W-2*T2.MX,start=84,floor=58); hf=T2.dm(900,s); y=534
        for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=int(s*1.14)
        T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (50,720,1030,1245), fill=fill)
        _ft=(T2.save_foot() if getattr(T2,"_TT",False) else "Follow for one AI system for founders every day.")
        d.text((T2.MX,1262),_ft,font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
        return
    T2.ls_text(d,(T2.MX,296),eyebrow,T2.mono(26),T2.CORAL,4)
    s=min(T2.fit_hook(d,head,T2.W-2*T2.MX,start=64,floor=44),54); hf=T2.dm(900,s); y=336
    for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=int(s*1.12)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (32,512,1048,1566), fill=1.0)
    x0,x1=90,928; yb=1582; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck_poll(f"{{T2.OUTBASE}}/{tt}",False); b=T2.deck_poll(f"{{T2.OUTBASE}}/{ig}",True)
    T2.montage(f"{{T2.OUTBASE}}/{tt}","{tt}",a); T2.montage(f"{{T2.OUTBASE}}/{ig}","{ig}",b)
    print("tt",a,"ig",b)
'''
def r(eb,l1,l2,obj): return f'  ("{eb}", [[wo("{l1}")],[co("{l2}")]], f"{{PH}}/{obj}.png", 1.0),'
def rul(l1,l2): return f'  ("ULTRON", [[wo("{l1}")],[co("{l2}")]], UL, 0.98),'
decks={
"build_phone_3d.py":dict(title="FROM MY PHONE v1",tt="phone_tt",ig="phone_ig",
  cover='[[wo("My company runs")],[co("from my phone.")]]', sub='',
  content="\n".join([
    r("LIVE","A whole team's work,","running live.","p2_deals"),
    r("BUILD","It builds and","ships itself.","p2_build"),
    r("UNITS","Seven units.","One operator.","p2_units"),
    r("PROJECTS","Every project,","one place.","p2_projects"),
    r("STACK","One subscription.","My whole stack.","p2_stack"),
    r("MEMORY","It never","forgets.","p2_brain"),
    r("AGENTS","Agents run","the missions.","p2_sub"),
    rul("One chat.","In my pocket."),
  ])),
"build_phone_v2.py":dict(title="FROM MY PHONE v2",tt="phv2_tt",ig="phv2_ig",
  cover='[[wo("One chat.")],[co("One operator.")]]', sub='',
  content="\n".join([
    r("MEMORY","It never","forgets.","p2_brain"),
    r("COMPUTER","It runs","its own computer.","p2_build"),
    r("UNITS","A team of seven,","on tap.","p2_units"),
    r("DEALS","It works","every deal.","p2_deals"),
    r("STACK","Ten tools,","one bill.","p2_stack"),
    r("PROJECTS","Every project,","one place.","p2_projects"),
    r("AGENTS","Agents work","in parallel.","p2_sub"),
    rul("Always on.","In your pocket."),
  ])),
"build_zero.py":dict(title="FROM ZERO TO COMPANY",tt="zero_tt",ig="zero_ig",
  cover='[[wo("From zero to a company.")],[co("One command.")]]', sub='',
  content="\n".join([
    r("WORKSPACE","It opens","the workspace.","p2_projects"),
    r("UNITS","It staffs","every unit.","p2_units"),
    r("BUILD","It builds","the product.","p2_build"),
    r("OUTBOUND","It runs","the outbound.","p2_deals"),
    r("STACK","It connects","your tools.","p2_stack"),
    r("MEMORY","It remembers","everything.","p2_brain"),
    r("AGENTS","Agents work","in parallel.","p2_sub"),
    rul("The whole company.","One chat."),
  ])),
"build_justme.py":dict(title="IT'S JUST ME",tt="justme_tt",ig="justme_ig",
  cover='''[[wo("It's just me.")],[co("And one chat.")]]''', sub='',
  content="\n".join([
    r("THE TEAM","This looks like","a whole team.","p2_deals"),
    r("BUILD","One person","ships the product.","p2_build"),
    r("UNITS","Seven units.","One person.","p2_units"),
    r("MEMORY","One shared","memory.","p2_brain"),
    r("PROJECTS","Every project.","One owner. Me.","p2_projects"),
    r("STACK","One bill,","not ten salaries.","p2_stack"),
    r("AGENTS","Agents run","the missions.","p2_sub"),
    rul("No team.","Just me."),
  ])),
}
for fn,cfg in decks.items():
    open(fn,"w").write(HEADER.format(**cfg)); print("wrote",fn)
