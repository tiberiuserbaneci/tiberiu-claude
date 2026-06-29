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
# bigger phone zone -> fills the visible band (kills bottom dead space); progress moved lower
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{{page:02d}}")
    T2.ls_text(d,(T2.MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
    s=T2.fit_hook(d,head,T2.W-2*T2.MX,start=84,floor=58); hf=T2.dm(900,s); lh=int(s*1.14); y=534
    for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=lh
    z=(50,720,1030,1250) if last else (50,720,1030,1520)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), z, fill=fill)
    if last:
        d.text((T2.MX,1262),"Follow for one AI system for founders every day.",font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
    else:
        x0,x1=90,928; yb=1556; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
        d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
# uniform hook size across content slides
def _u():
    dd=ImageDraw.Draw(Image.new("RGB",(10,10))); heads=[h for _,h,_,_ in T2.CONTENT]+[T2.CTA[1]]; s=84
    while s>50:
        hf=T2.dm(900,s)
        if all(max(dd.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=T2.W-2*T2.MX for head in heads): break
        s-=2
    return s
_USZ=_u(); _of=T2.fit_hook
T2.fit_hook=lambda d,head,maxw,start=84,floor=58:(_of(d,head,maxw,start=start,floor=floor) if head is T2.COVER["head"] else _USZ)
if __name__=="__main__":
    a=T2.deck(f"{{T2.OUTBASE}}/{tt}",False); b=T2.deck(f"{{T2.OUTBASE}}/{ig}",True)
    T2.montage(f"{{T2.OUTBASE}}/{tt}","{tt}",a); T2.montage(f"{{T2.OUTBASE}}/{ig}","{ig}",b)
    print("tt",a,"ig",b)
'''
def row(eb,l1,l2,obj): return f'  ("{eb}", [[wo("{l1}")],[co("{l2}")]], f"{{PH}}/{obj}.png", 1.0),'
def rowul(l1,l2): return f'  ("ULTRON", [[wo("{l1}")],[co("{l2}")]], UL, 0.98),'
decks={
"build_phone_3d.py":dict(title="FROM MY PHONE v1",tt="phone_tt",ig="phone_ig",
  cover='[[wo("My company runs")],[co("from my phone.")]]', sub='',
  content="\n".join([
    row("LIVE","A whole team's work,","running live.","p_jobs"),
    row("DEALS","Agents work","the deals.","p_pipeline"),
    row("UNITS","Seven units.","One operator.","p_skills"),
    row("MEMORY","It remembers","everything.","p_brain"),
    row("PROJECTS","Every project,","one place.","p_projects"),
    row("STACK","One subscription.","My whole stack.","p_stack"),
    row("PLAYBOOKS","Proven playbooks,","built in.","p_playbooks"),
    rowul("One chat.","In my pocket."),
  ])),
"build_phone_v2.py":dict(title="FROM MY PHONE v2 (2nd account)",tt="phv2_tt",ig="phv2_ig",
  cover='[[wo("One chat.")],[co("One operator.")]]', sub='',
  content="\n".join([
    row("UNITS","A team of seven,","on tap.","p_skills"),
    row("MEMORY","It never","forgets.","p_brain"),
    row("DEALS","It works","every deal.","p_pipeline"),
    row("LIVE","The work runs","while I sleep.","p_jobs"),
    row("STACK","Ten tools,","one bill.","p_stack"),
    row("PROJECTS","All my work,","one place.","p_projects"),
    row("PLAYBOOKS","Battle-tested","playbooks.","p_playbooks"),
    rowul("Always on.","In your pocket."),
  ])),
"build_zero.py":dict(title="FROM ZERO TO COMPANY",tt="zero_tt",ig="zero_ig",
  cover='[[wo("From zero to a company.")],[co("One command.")]]', sub='',
  content="\n".join([
    row("WORKSPACE","It opens","the workspace.","p_projects"),
    row("UNITS","It staffs","every unit.","p_skills"),
    row("PLAYBOOKS","It loads","the playbooks.","p_playbooks"),
    row("OUTBOUND","It runs","the outbound.","p_jobs"),
    row("DEALS","It works","the deals.","p_pipeline"),
    row("MEMORY","It builds","the memory.","p_brain"),
    row("STACK","It connects","your tools.","p_stack"),
    rowul("The whole company.","One chat."),
  ])),
"build_justme.py":dict(title="IT'S JUST ME",tt="justme_tt",ig="justme_ig",
  cover='''[[wo("It's just me.")],[co("And one chat.")]]''', sub=', sub="Everyone thinks I have a team of thirty."',
  content="\n".join([
    row("THE TEAM","This looks like","a whole team.","p_jobs"),
    row("DEALS","Three agents,","one deal.","p_pipeline"),
    row("UNITS","Seven units.","One person.","p_skills"),
    row("MEMORY","One shared","memory.","p_brain"),
    row("PROJECTS","Every project.","One owner. Me.","p_projects"),
    row("PLAYBOOKS","My playbooks,","on tap.","p_playbooks"),
    row("STACK","One bill,","not ten salaries.","p_stack"),
    rowul("No team.","Just me."),
  ])),
}
for fn,cfg in decks.items():
    open(fn,"w").write(HEADER.format(**cfg)); print("wrote",fn)
