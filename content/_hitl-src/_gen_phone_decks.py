# regenerate the 4 phone-format build files (all phone-shaped, no orange-glow screen)
HEADER='''#!/usr/bin/env python3
# {title}
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{{T2.OBJ}}/models_phone"; LIB=T2.LIB; UL=f"{{T2.OBJ}}/models_rival2/ultron_login.png"
T2.COVER=dict(head={cover})
T2.CONTENT=[
{content}
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{{LIB}}/cta3d-operator.png", 0.92)
from PIL import Image as _I
from PIL import ImageDraw as _ID
def _u():
    d=_ID.Draw(_I.new("RGB",(10,10))); heads=[h for _,h,_,_ in T2.CONTENT]+[T2.CTA[1]]; s=84
    while s>50:
        hf=T2.dm(900,s)
        if all(max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=T2.W-2*T2.MX for head in heads): break
        s-=2
    return s
_USZ=_u(); _of=T2.fit_hook
T2.fit_hook=lambda d,head,maxw,start=84,floor=58:(_of(d,head,maxw,start=start,floor=floor) if head is T2.COVER["head"] else _USZ)
if __name__=="__main__":
    a=T2.deck(f"{{T2.OUTBASE}}/{tt}",False); b=T2.deck(f"{{T2.OUTBASE}}/{ig}",True)
    T2.montage(f"{{T2.OUTBASE}}/{tt}","{tt}",a); T2.montage(f"{{T2.OUTBASE}}/{ig}","{ig}",b)
    print("tt",a,"ig",b)
'''
def row(eb,l1,l2,obj,fill="1.0"): return f'  ("{eb}", [[wo("{l1}")],[co("{l2}")]], f"{{PH}}/{obj}.png", {fill}),'
def rowul(l1,l2): return f'  ("ULTRON", [[wo("{l1}")],[co("{l2}")]], UL, 0.98),'

decks={
"build_phone_3d.py":dict(title="I RUN IT FROM MY PHONE - v1 (phone)",tt="phone_tt",ig="phone_ig",
  cover='[[wo("My company runs")],[co("from my phone.")]]',
  content="\n".join([
    row("LIVE","A whole team's work,","running live.","p_jobs"),
    row("DEALS","Agents work","the deals.","p_deals"),
    row("UNITS","Seven units.","One operator.","p_skills"),
    row("MEMORY","It remembers","everything.","p_brain"),
    row("PROJECTS","Every project,","one place.","p_projects"),
    row("STACK","One subscription.","My whole stack.","p_stack"),
    row("PLAYBOOKS","Proven playbooks,","built in.","p_playbooks"),
    rowul("One chat.","In my pocket."),
  ])),
"build_phone_v2.py":dict(title="I RUN IT FROM MY PHONE - v2 (phone, 2nd account; different cover/order/hooks)",tt="phv2_tt",ig="phv2_ig",
  cover='[[wo("One chat.")],[co("One operator.")]]',
  content="\n".join([
    row("UNITS","A team of seven,","on tap.","p_skills"),
    row("MEMORY","It never","forgets.","p_brain"),
    row("DEALS","It works","every deal.","p_deals"),
    row("LIVE","The work runs","while I sleep.","p_jobs"),
    row("STACK","Ten tools,","one bill.","p_stack"),
    row("PROJECTS","All my work,","one place.","p_projects"),
    row("PLAYBOOKS","Battle-tested","playbooks.","p_playbooks"),
    rowul("One chat.","Runs it all."),
  ])),
"build_zero.py":dict(title="FROM ZERO TO COMPANY (phone, build-arc)",tt="zero_tt",ig="zero_ig",
  cover='[[wo("From zero to a company.")],[co("One command.")]]',
  content="\n".join([
    row("WORKSPACE","It opens","the workspace.","p_projects"),
    row("UNITS","It staffs","every unit.","p_skills"),
    row("PLAYBOOKS","It loads","the playbooks.","p_playbooks"),
    row("OUTBOUND","It runs","the outbound.","p_jobs"),
    row("DEALS","It works","the deals.","p_deals"),
    row("MEMORY","It builds","the memory.","p_brain"),
    row("STACK","It connects","your tools.","p_stack"),
    rowul("From zero to a company.","One chat."),
  ])),
"build_justme.py":dict(title="IT'S JUST ME (phone, solo flex)",tt="justme_tt",ig="justme_ig",
  cover='''[[wo("It's just me.")],[co("And one chat.")]]''',
  content="\n".join([
    row("THE TEAM","This looks like","a whole team.","p_jobs"),
    row("DEALS","Three agents,","one deal.","p_deals"),
    row("UNITS","Seven units.","One person.","p_skills"),
    row("MEMORY","One shared","memory.","p_brain"),
    row("PROJECTS","Every project.","One owner. Me.","p_projects"),
    row("PLAYBOOKS","My playbooks,","on tap.","p_playbooks"),
    row("STACK","One bill,","not ten salaries.","p_stack"),
    rowul("It's just me.","And one chat."),
  ])),
}
for fn,cfg in decks.items():
    open(fn,"w").write(HEADER.format(**cfg))
    print("wrote",fn)
