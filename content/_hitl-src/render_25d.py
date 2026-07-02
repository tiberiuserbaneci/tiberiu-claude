#!/usr/bin/env python3
# 2.5D coded app-window mockups (PIL) - big, fill the central canvas, depth via layered shadows + bevels.
# A third material category: Vertex=3D, classic=2D, this=2.5D (coded by us). Landscape app windows.
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
A="/home/user/tiberiu-claude/content/assets"
BG=(25,25,25); BODY=(39,39,37); BAR=(31,31,30); CARD=(50,50,47); CARD2=(58,58,55)
CORAL=(204,120,92); CORAL2=(232,150,110); WHITE=(248,248,244); MUT=(150,150,142); LINE=(64,63,60)
SS=2
def F(w,px):
    m={900:"DMSans-900",800:"DMSans-800",700:"DMSans-700",500:"DMSans-500"}; return ImageFont.truetype(f"{A}/{m.get(w,'DMSans-500')}.ttf",px*SS)
def MONO(px): return ImageFont.truetype(f"{A}/DMMono-500.ttf",px*SS)
def rr(d,box,r,fill=None,outline=None,w=1):
    d.rounded_rectangle([box[0]*SS,box[1]*SS,box[2]*SS,box[3]*SS],radius=r*SS,fill=fill,outline=outline,width=w*SS)
def shadow(base,box,r,blur=26,alpha=150,dy=14):
    s=Image.new("RGBA",base.size,(0,0,0,0)); ImageDraw.Draw(s).rounded_rectangle([box[0]*SS,(box[1]+dy)*SS,box[2]*SS,(box[3]+dy)*SS],radius=r*SS,fill=(0,0,0,alpha))
    base.alpha_composite(s.filter(ImageFilter.GaussianBlur(blur*SS)))
def text(d,xy,s,font,fill,ls=0):
    x,y=xy[0]*SS,xy[1]*SS
    if ls==0: d.text((x,y),s,font=font,fill=fill); return
    for ch in s: d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+ls*SS
def card(base,d,box,r=14,fill=CARD,sh=True):
    if sh: shadow(base,box,r,blur=12,alpha=90,dy=7)
    rr(d,box,r,fill=fill); rr(d,box,r,outline=(70,69,66),w=1)

def window(W,H, draw_content, title="", accent=CORAL):
    cw,ch=int(W*1.18),int(H*1.18)                     # margin for shadow
    base=Image.new("RGBA",(cw*SS,ch*SS),BG+(255,)); d=ImageDraw.Draw(base)
    mx,my=(cw-W)//2,(ch-H)//2
    body=(mx,my,mx+W,my+H)
    shadow(base,body,22,blur=34,alpha=170,dy=22)
    # body with vertical gradient
    grad=Image.new("RGBA",(W*SS,H*SS),(0,0,0,0)); gd=ImageDraw.Draw(grad)
    for i in range(H*SS):
        t=i/(H*SS); c=tuple(int(BODY[k]*(1-0.12*t)+(20,20,19)[k]*0.12*t) for k in range(3)); gd.line([(0,i),(W*SS,i)],fill=c+(255,))
    m=Image.new("L",(W*SS,H*SS),0); ImageDraw.Draw(m).rounded_rectangle([0,0,W*SS-1,H*SS-1],radius=22*SS,fill=255)
    base.paste(grad,(mx*SS,my*SS),m)
    rr(d,body,22,outline=(96,94,90),w=1); d.line([((mx+22)*SS,(my+2)*SS),((mx+W-22)*SS,(my+2)*SS)],fill=(96,94,90,255),width=2*SS)
    # top bar
    tb=(mx,my,mx+W,my+58);
    for i,c in enumerate([(232,93,68),(232,176,86),(120,190,120)]):
        d.ellipse([(mx+22+i*26)*SS,(my+24)*SS,(mx+22+i*26+13)*SS,(my+24+13)*SS],fill=(90,89,85))
    if title: text(d,(mx+W//2-len(title)*5,my+20),title,MONO(15),MUT,2)
    d.line([(mx*SS,(my+58)*SS),((mx+W)*SS,(my+58)*SS)],fill=LINE+(255,),width=1*SS)
    draw_content(base,d,(mx,my+58,mx+W,my+H), accent)
    return base.resize((cw,ch),Image.LANCZOS)

def sidebar(d,reg,items,active=0):
    x0,y0,x1,y1=reg; w=150
    d.rectangle([x0*SS,y0*SS,(x0+w)*SS,y1*SS],fill=BAR+(255,)); d.line([((x0+w)*SS,y0*SS),((x0+w)*SS,y1*SS)],fill=LINE+(255,),width=1*SS)
    for i,it in enumerate(items):
        yy=y0+24+i*46
        if i==active: rr(d,(x0+12,yy-6,x0+w-12,yy+30),8,fill=(204,120,92,60))
        d.ellipse([(x0+22)*SS,(yy+2)*SS,(x0+38)*SS,(yy+18)*SS],outline=(CORAL if i==active else MUT),width=2*SS)
        text(d,(x0+50,yy),it,F(700,15),(WHITE if i==active else MUT))
    return x0+w

# ---------- app contents ----------
def c_stripe(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Home","Payments","Balance","Reports"],1)+30
    text(d,(cx,y0+30),"stripe",F(800,30),WHITE); text(d,(x1-180,y0+34),"Net volume today",MONO(13),MUT)
    text(d,(cx,y0+70),"$8,400",F(900,84),CORAL)
    text(d,(cx,y0+170),"+18% vs yesterday",F(700,18),CORAL2)
    cbx=cx; cby=y0+216; cbw=x1-cx-40; cbh=170
    card(base,d,(cbx,cby,cbx+cbw,cby+cbh))
    pts=[0.15,0.28,0.22,0.4,0.52,0.48,0.66,0.8,0.74,0.95]
    for i in range(len(pts)-1):
        x_a=cbx+20+i*(cbw-40)/(len(pts)-1); x_b=cbx+20+(i+1)*(cbw-40)/(len(pts)-1)
        ya=cby+cbh-20-pts[i]*(cbh-40); yb=cby+cbh-20-pts[i+1]*(cbh-40)
        d.line([(x_a*SS,ya*SS),(x_b*SS,yb*SS)],fill=CORAL,width=4*SS)
    ry=cby+cbh+24; text(d,(cx,ry),"Recent payments",F(700,17),MUT); ry+=34
    for nm,amt in [("Acme Corp","$1,200"),("Globex","$2,400"),("Initech","$1,800"),("Umbrella","$3,000"),("Hooli","$950"),("Stark","$2,100")]:
        card(base,d,(cx,ry,x1-40,ry+54),10,fill=CARD,sh=False)
        text(d,(cx+18,ry+15),nm,F(500,18),WHITE); text(d,(x1-40-120,ry+13),amt,F(800,21),CORAL2); ry+=64
def c_apollo(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["People","Saved","Lists","Settings"],0)+24
    text(d,(cx,y0+24),"Apollo",F(800,24),WHITE); rr(d,(cx,y0+62,x1-40,y0+100),10,fill=BAR); text(d,(cx+16,y0+72),"Search prospects",F(500,16),MUT)
    ry=y0+120
    rows=[("John Smith","VP Sales","Acme","94"),("Sarah Davis","CEO","Globex","91"),("Mark Lin","Head of Growth","Initech","89"),
          ("Ana Ruiz","Director","Umbrella","87"),("Tom Reed","Founder","Hooli","85"),("Lia Park","VP Eng","Pied","82"),
          ("Omar Haddad","COO","Vandelay","80"),("Eva Brandt","CMO","Stark","78"),("Ken Watts","Partner","Wayne","76")]
    for nm,ti,co,sc in rows:
        card(base,d,(cx,ry,x1-40,ry+66),10,fill=CARD,sh=False)
        d.ellipse([(cx+16)*SS,(ry+18)*SS,(cx+48)*SS,(ry+50)*SS],fill=(70,69,66))
        text(d,(cx+62,ry+12),nm,F(700,18),WHITE); text(d,(cx+62,ry+38),ti+"  ·  "+co,F(500,14),MUT)
        rr(d,(x1-40-74,ry+18,x1-40-16,ry+48),14,fill=(204,120,92,200)); text(d,(x1-40-60,ry+22),sc,F(800,16),(26,15,10))
        ry+=78
def c_gmail(base,d,reg,accent,sent=False):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Inbox","Sent","Drafts","Spam"],1 if sent else 0)+24
    text(d,(cx,y0+24),"Gmail · "+("Sent" if sent else "Inbox"),F(800,22),WHITE)
    if not sent: rr(d,(cx+240,y0+22,cx+310,y0+52),14,fill=(204,120,92,200)); text(d,(cx+258,y0+27),"18",F(800,18),(26,15,10))
    ry=y0+72
    pre="To: " if sent else "Re: "
    rows=["Acme Corp - Partnership","Globex - Pricing","Initech - Proposal","Umbrella - Demo","Hooli - Intro",
          "Pied - Follow up","Vandelay - Call","Stark - Scope","Wayne - Contract","Oscorp - Renewal","Dunder - Pilot"]
    for r in rows:
        card(base,d,(cx,ry,x1-40,ry+58),10,fill=CARD,sh=False)
        d.ellipse([(cx+16)*SS,(ry+17)*SS,(cx+42)*SS,(ry+43)*SS],fill=(204,120,92) if not sent else (70,69,66))
        text(d,(cx+56,ry+16),pre+r,F(500,18),WHITE)
        if sent: text(d,(x1-40-80,ry+18),"Sent",F(700,14),CORAL2)
        ry+=70
def c_calendly(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+30; text(d,(cx,y0+22),"Calendly",F(800,24),WHITE); text(d,(x1-170,y0+26),"Booked  14",MONO(14),CORAL2)
    gy=y0+66; gx=cx; days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]; cw=(x1-40-cx)/7
    for i,dn in enumerate(days): text(d,(gx+i*cw+10,gy),dn,F(700,14),MUT)
    gy+=30
    booked={(0,0),(0,2),(1,1),(2,0),(2,2),(3,1),(4,0),(1,3),(3,3),(4,2),(0,5),(2,4),(4,5),(1,6)}
    for row in range(7):
        for col in range(7):
            bx=gx+col*cw+6; by=gy+row*106
            if (col,row) in booked:
                card(base,d,(bx,by,bx+cw-12,by+94),8,fill=(204,120,92,210),sh=False)
                text(d,(bx+10,by+12),"Call",F(700,15),(26,15,10)); text(d,(bx+10,by+40),"30m",F(500,13),(60,30,18))
                text(d,(bx+10,by+64),"conf",F(500,11),(60,30,18))
            else: rr(d,(bx,by,bx+cw-12,by+94),8,fill=(40,40,38))
def c_hubspot(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+30; text(d,(cx,y0+22),"HubSpot · Deals",F(800,22),WHITE); text(d,(x1-170,y0+28),"$310k open",MONO(13),CORAL2)
    cols=["Qualified","Meeting","Proposal","Closed Won"]; cw=(x1-40-cx)/4; gy=y0+64
    names=["Acme","Globex","Initech","Umbrella","Hooli","Stark","Wayne","Pied"]
    vals=["$25k","$50k","$90k","$120k","$18k","$36k","$64k","$45k"]
    for i,cn in enumerate(cols):
        bx=cx+i*cw; won=(i==3)
        text(d,(bx+8,gy),cn,F(700,15),(CORAL2 if won else MUT))
        nrows=5 if not won else 4
        for j in range(nrows):
            cy=gy+34+j*150; col=(204,120,92,200) if won else CARD
            card(base,d,(bx+4,cy,bx+cw-12,cy+134),10,fill=col,sh=False)
            text(d,(bx+18,cy+16),names[(i+j)%8],F(700,17),(26,15,10) if won else WHITE)
            text(d,(bx+18,cy+50),vals[(i+j)%8],F(800,21),(26,15,10) if won else CORAL2)
            text(d,(bx+18,cy+92),["Call set","Sent","In review","Signed"][i],F(500,13),(60,32,20) if won else MUT)
def c_gate(base,d,reg,accent):
    x0,y0,x1,y1=reg; W=x1-x0; H=y1-y0
    cw_,ch_=int(W*0.62),int(H*0.62); bx=x0+(W-cw_)//2; by=y0+(H-ch_)//2
    card(base,d,(bx,by,bx+cw_,by+ch_),18,fill=(40,40,38))
    text(d,(bx+30,by+26),"Approval required",F(700,20),MUT)
    text(d,(bx+30,by+70),"Send 240",F(900,46),WHITE); text(d,(bx+30,by+122),"outreach emails",F(900,46),CORAL)
    text(d,(bx+30,by+190),"Campaign  ·  Q3 outbound",F(500,16),MUT)
    bw=(cw_-90)//2; byy=by+ch_-78
    rr(d,(bx+30,byy,bx+30+bw,byy+52),26,fill=CORAL); text(d,(bx+30+bw//2-40,byy+14),"Approve",F(800,18),(26,15,10))
    rr(d,(bx+60+bw,byy,bx+60+2*bw,byy+52),26,outline=MUT,w=2); text(d,(bx+60+bw+bw//2-22,byy+14),"Hold",F(800,18),MUT)

def c_ultron(base,d,reg,accent):
    x0,y0,x1,y1=reg; W=x1-x0; H=y1-y0
    # sphere centered
    orb=Image.open("/home/user/tiberiu-claude/content/ultron-logo.png").convert("RGB"); lum=np.asarray(orb).astype(int).sum(2); oy,ox=np.where(lum>36)
    orb=orb.crop((int(ox.min()),int(oy.min()),int(ox.max())+1,int(oy.max())+1)).convert("RGBA")
    s=max(orb.size); sq=Image.new("RGBA",(s,s),(0,0,0,0)); sq.alpha_composite(orb,((s-orb.width)//2,(s-orb.height)//2))
    m=Image.new("L",(s,s),0); ImageDraw.Draw(m).ellipse([0,0,s,s],fill=255); sq.putalpha(m)
    dia=int(W*0.34*SS); sq=sq.resize((dia,dia),Image.LANCZOS)
    ccx=(x0+W//2)*SS; ccy=(y0+int(H*0.40))*SS
    gl=Image.new("RGBA",base.size,(0,0,0,0)); ImageDraw.Draw(gl).ellipse([ccx-dia//2-40*SS,ccy-dia//2-40*SS,ccx+dia//2+40*SS,ccy+dia//2+40*SS],fill=(204,120,92,90))
    base.alpha_composite(gl.filter(ImageFilter.GaussianBlur(46*SS))); base.alpha_composite(sq,(ccx-dia//2,ccy-dia//2))
    # chat bar
    bx0,by0,bx1,by1=x0+80,y1-130,x1-80,y1-66
    rr(d,(bx0,by0,bx1,by1),(by1-by0)//2,fill=BAR); rr(d,(bx0,by0,bx1,by1),(by1-by0)//2,outline=LINE,w=1)
    text(d,(bx0+30,by0+(by1-by0)//2-13),"Ask anything",F(500,20),MUT)
    sbd=by1-by0-16; scx=bx1-30-sbd
    d.ellipse([scx*SS,(by0+8)*SS,(scx+sbd)*SS,(by0+8+sbd)*SS],fill=CORAL)

def c_designer(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Designs","Brand","Uploads","Apps"],0)+24
    text(d,(cx,y0+24),"Content Studio",F(800,24),WHITE); text(d,(x1-170,y0+30),"On brand",MONO(13),CORAL2)
    ry=y0+70; cols=3; cw=(x1-40-cx-2*16)/cols
    pal=[(196,120,92),(212,162,127),(168,132,108),(150,126,112),(204,120,92),(180,146,120),(158,118,96),(214,150,110),(172,140,124)]
    labels=["Launch post","Carousel","Story","Ad set","Reel cover","Newsletter","Case study","Deck","One-pager"]
    for i in range(9):
        r=i//cols; c=i%cols; bx=cx+c*(cw+16); by=ry+r*266
        card(base,d,(bx,by,bx+cw,by+250),12,fill=CARD,sh=False)
        rr(d,(bx+12,by+12,bx+cw-12,by+196),8,fill=pal[i]+(190,)); text(d,(bx+14,by+210),labels[i],F(700,16),WHITE)
def c_developer(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Project","Deploy","Logs","Domains"],1)+24
    text(d,(cx,y0+24),"Deployments",F(800,24),WHITE); text(d,(x1-150,y0+30),"Live",MONO(13),CORAL2)
    card(base,d,(cx,y0+64,x1-40,y0+284),12,fill=CARD)
    rr(d,(cx+16,y0+80,x1-56,y0+268),8,fill=(40,40,38)); text(d,(cx+30,y0+98),"yoursite.com",F(700,18),MUT)
    rr(d,(cx+30,y0+134,cx+290,y0+152),4,fill=(70,69,66)); rr(d,(cx+30,y0+164,cx+210,y0+180),4,fill=(60,59,56))
    rr(d,(cx+30,y0+196,cx+250,y0+212),4,fill=(60,59,56)); rr(d,(cx+30,y0+228,cx+180,y0+244),4,fill=(70,69,66))
    ry=y0+304
    for nm,st in [("main  ·  production","Ready"),("landing  ·  preview","Ready"),("pricing  ·  preview","Building"),
                  ("docs  ·  preview","Ready"),("api  ·  production","Ready"),("blog  ·  preview","Queued")]:
        card(base,d,(cx,ry,x1-40,ry+66),10,fill=CARD,sh=False); text(d,(cx+18,ry+20),nm,F(500,18),WHITE)
        ok=st=="Ready"; rr(d,(x1-40-130,ry+18,x1-40-16,ry+48),15,fill=(204,120,92,205) if ok else (60,59,56))
        text(d,(x1-40-116,ry+22),st,F(700,15),(26,15,10) if ok else MUT); ry+=78
def c_bill(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+48
    text(d,(cx,y0+34),"What a team costs",F(800,30),WHITE); text(d,(x1-190,y0+42),"per month",MONO(15),MUT)
    ry=y0+108
    for nm,amt in [("Researcher","$4,000"),("SDR","$5,000"),("Ops lead","$6,000"),("Designer","$4,500"),("Developer","$7,500")]:
        text(d,(cx,ry+14),nm,F(500,26),MUT); text(d,(x1-48-180,ry+8),amt,F(700,28),WHITE)
        d.line([(cx*SS,(ry+62)*SS),((x1-48)*SS,(ry+62)*SS)],fill=LINE+(255,),width=1*SS); ry+=76
    ry+=10; d.line([(cx*SS,ry*SS),((x1-48)*SS,ry*SS)],fill=(96,94,90,255),width=2*SS); ry+=24
    text(d,(cx,ry+8),"Team total",F(800,28),WHITE); text(d,(x1-48-280,ry+2),"$15,000/mo",F(900,40),WHITE); ry+=90
    rr(d,(cx,ry,x1-48,ry+88),14,fill=CORAL)
    text(d,(cx+26,ry+24),"One chat",F(800,28),(26,15,10)); text(d,(x1-48-150,ry+16),"cents",F(900,44),(26,15,10))

def c_scheduler(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Queue","Calendar","Analytics","Channels"],1)+22
    text(d,(cx,y0+22),"Post Scheduler",F(800,24),WHITE); text(d,(x1-170,y0+28),"42 queued",MONO(13),CORAL2)
    days=["Mon","Tue","Wed","Thu","Fri"]; cw=(x1-40-cx)/5; gy=y0+62
    for i,dn in enumerate(days): text(d,(cx+i*cw+8,gy),dn,F(700,14),MUT)
    gy+=28; pal=[(196,120,92),(212,162,127),(168,132,108),(180,146,120),(158,118,96)]
    sched={(0,0),(0,2),(0,3),(1,1),(1,3),(2,0),(2,2),(3,1),(3,3),(4,0),(4,2),(1,0),(3,0),(2,3)}
    for row in range(4):
        for col in range(5):
            bx=cx+col*cw+6; by=gy+row*166
            if (col,row) in sched:
                card(base,d,(bx,by,bx+cw-12,by+152),10,fill=CARD,sh=False)
                rr(d,(bx+10,by+10,bx+cw-22,by+88),6,fill=pal[col]+(180,))
                text(d,(bx+10,by+100),["LinkedIn","X","IG","TikTok","Blog"][col],F(700,14),MUT)
                text(d,(bx+10,by+124),"10:00",F(500,12),(120,119,114))
            else: rr(d,(bx,by,bx+cw-12,by+152),10,fill=(40,40,38))
def c_warmup(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+40; text(d,(cx,y0+24),"Deliverability",F(800,26),WHITE); text(d,(x1-180,y0+30),"all inboxing",MONO(13),CORAL2)
    text(d,(cx,y0+70),"99.2%",F(900,88),CORAL); text(d,(cx,y0+172),"inbox placement, 6 domains warm",F(700,18),CORAL2)
    cbx,cby,cbw,cbh=cx,y0+220,x1-40-cx,180; card(base,d,(cbx,cby,cbx+cbw,cby+cbh))
    pts=[0.2,0.3,0.45,0.5,0.62,0.7,0.82,0.9,0.94,0.99]
    for i in range(len(pts)-1):
        xa=cbx+20+i*(cbw-40)/(len(pts)-1); xb=cbx+20+(i+1)*(cbw-40)/(len(pts)-1)
        ya=cby+cbh-20-pts[i]*(cbh-40); yb=cby+cbh-20-pts[i+1]*(cbh-40)
        d.line([(xa*SS,ya*SS),(xb*SS,yb*SS)],fill=CORAL,width=4*SS)
    ry=cby+cbh+22
    for nm in ["hello@acme.co","mail.acme.io","team.acme.dev","out.acme.app","go.acme.co","hq.acme.io"]:
        card(base,d,(cx,ry,x1-40,ry+56),10,fill=CARD,sh=False); text(d,(cx+16,ry+16),nm,F(500,18),WHITE)
        rr(d,(x1-40-104,ry+15,x1-40-16,ry+43),14,fill=(204,120,92,200)); text(d,(x1-40-90,ry+19),"warm",F(700,15),(26,15,10)); ry+=68
def c_seowriter(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+40; text(d,(cx,y0+24),"SEO Writer",F(800,26),WHITE)
    rr(d,(x1-40-130,y0+22,x1-40,y0+58),16,fill=(204,120,92,200)); text(d,(x1-40-112,y0+29),"92 score",F(800,17),(26,15,10))
    text(d,(cx,y0+80),"How founders rank in 2026",F(900,32),WHITE)
    ry=y0+136
    for w in [1.0,0.94,0.72,0.98,0.66,0.9,0.5,0.96,0.7,0.88,0.62,0.84]:
        d.rounded_rectangle([cx*SS,ry*SS,int((cx+(x1-40-cx)*w))*SS,(ry+18)*SS],radius=4*SS,fill=(76,75,72)); ry+=36
    ry+=10; text(d,(cx,ry),"Target keywords",F(700,16),MUT); ry+=36
    x=cx
    for kw in ["ai services","founder tools","cold email","icp","one chat"]:
        w2=len(kw)*12+36; rr(d,(x,ry,x+w2,ry+40),19,fill=(204,120,92,60)); rr(d,(x,ry,x+w2,ry+40),19,outline=CORAL,w=1); text(d,(x+18,ry+9),kw,F(500,17),CORAL2); x+=w2+12
    ry+=60
    for nm,st in [("Internal links","12 added"),("Meta + schema","done"),("Readability","grade 7")]:
        card(base,d,(cx,ry,x1-40,ry+54),10,fill=CARD,sh=False); text(d,(cx+16,ry+14),nm,F(500,17),WHITE); text(d,(x1-40-150,ry+14),st,F(700,16),CORAL2); ry+=64
def c_softwarebill(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+46
    text(d,(cx,y0+30),"Software subscriptions",F(800,26),WHITE); text(d,(x1-180,y0+36),"per month",MONO(14),MUT)
    ry=y0+92
    for nm,amt in [("Buffer","$15"),("Instantly","$97"),("Jasper","$49"),("Typeform","$25"),("Calendly","$16")]:
        text(d,(cx,ry+12),nm,F(500,24),MUT); text(d,(x1-46-140,ry+8),amt,F(700,26),WHITE)
        d.line([(cx*SS,(ry+58)*SS),((x1-46)*SS,(ry+58)*SS)],fill=LINE+(255,),width=1*SS); ry+=72
    ry+=10; d.line([(cx*SS,ry*SS),((x1-46)*SS,ry*SS)],fill=(96,94,90,255),width=2*SS); ry+=22
    text(d,(cx,ry+8),"Every month",F(800,26),WHITE); text(d,(x1-46-200,ry+2),"$202/mo",F(900,38),WHITE); ry+=86
    rr(d,(cx,ry,x1-46,ry+84),14,fill=CORAL); text(d,(cx+26,ry+24),"Ultron",F(800,28),(26,15,10)); text(d,(x1-46-150,ry+18),"cents",F(900,42),(26,15,10))

def c_orgchart(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+40; text(d,(cx,y0+26),"Your org chart",F(800,26),WHITE); text(d,(x1-200,y0+32),"headcount 0",MONO(14),CORAL2)
    roles=[("Research","$4k/mo"),("Sales","$5k/mo"),("Ops","$6k/mo"),("Design","$4.5k/mo"),("Dev","$7.5k/mo")]
    n=len(roles); cw=(x1-40-cx)/n; ty=y0+92
    for i,(rname,sal) in enumerate(roles):
        bx=cx+i*cw+6
        card(base,d,(bx,ty,bx+cw-14,ty+150),10,fill=(40,40,38),sh=False)
        text(d,(bx+16,ty+18),rname,F(700,19),MUT); text(d,(bx+16,ty+52),"1 seat",F(500,14),(120,119,114))
        text(d,(bx+16,ty+96),sal,F(800,18),(150,150,142))
        mid=bx+(cw-14)/2
        d.line([(mid*SS,(ty+150)*SS),(mid*SS,(ty+196)*SS)],fill=LINE+(255,),width=2*SS)
    hub=x0+(x1-x0)//2
    d.line([((cx+cw/2)*SS,(ty+196)*SS),((x1-40-cw/2)*SS,(ty+196)*SS)],fill=LINE+(255,),width=2*SS)
    d.line([(hub*SS,(ty+196)*SS),(hub*SS,(ty+240)*SS)],fill=CORAL+(255,),width=3*SS)
    bw=440; by=ty+240; bx=hub-bw//2
    card(base,d,(bx,by,bx+bw,by+150),14,fill=CORAL); text(d,(bx+30,by+28),"One chat",F(900,40),(26,15,10)); text(d,(bx+30,by+88),"runs every role",F(700,21),(60,32,20))
    ry=by+186
    for txt2 in ["No payroll to run","No briefs to write","No seats to fill"]:
        card(base,d,(cx,ry,x1-40,ry+58),10,fill=CARD,sh=False)
        d.ellipse([(cx+20)*SS,(ry+21)*SS,(cx+36)*SS,(ry+37)*SS],fill=CORAL)
        text(d,(cx+52,ry+15),txt2,F(700,19),WHITE); text(d,(x1-40-120,ry+17),"24/7",MONO(15),CORAL2); ry+=68
def c_workflows(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Workflows","Runs","Triggers","Logs"],0)+22
    text(d,(cx,y0+22),"Active workflows",F(800,24),WHITE); text(d,(x1-160,y0+28),"9 running",MONO(13),CORAL2)
    ry=y0+66
    for nm,tg,on in [("Inbound triage","every message",True),("Lead enrichment","on new lead",True),("Follow-up cadence","daily 9am",True),
                     ("Deal updates","on reply",True),("Weekly report","mondays",False),("Churn watch","on usage drop",True),
                     ("Invoice chase","on due date",True),("Meeting briefs","before each call",True),("CRM hygiene","nightly",True)]:
        card(base,d,(cx,ry,x1-40,ry+70),10,fill=CARD,sh=False)
        text(d,(cx+18,ry+13),nm,F(700,19),WHITE); text(d,(cx+18,ry+42),tg,F(500,15),MUT)
        tw=64; tx=x1-40-tw-18; ty=ry+21
        rr(d,(tx,ty,tx+tw,ty+28),14,fill=(204,120,92,205) if on else (60,59,56))
        kx=tx+tw-24 if on else tx+2; d.ellipse([(kx+2)*SS,(ty+2)*SS,(kx+24)*SS,(ty+24)*SS],fill=(250,248,244))
        ry+=82
def c_leadscore(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+40; text(d,(cx,y0+22),"Lead machine",F(800,24),WHITE); text(d,(x1-180,y0+28),"1,284 in pipe",MONO(13),CORAL2)
    stages=[("Sourced","1,284"),("Enriched","902"),("Scored","471"),("Booked","63")]; sw=(x1-40-cx)/4; gy=y0+62
    for i,(nm,v) in enumerate(stages):
        bx=cx+i*sw; h=[120,96,68,42][i]
        rr(d,(bx+8,gy+126-h,bx+sw-18,gy+126),8,fill=(204,120,92,120+i*30))
        text(d,(bx+8,gy+136),nm,F(700,15),MUT); text(d,(bx+8,gy+158),v,F(900,26),WHITE)
    ry=y0+266
    for nm,co,sc in [("Sarah Lin","Northwind","94"),("Marco Diaz","Globex","88"),("Priya Rao","Initech","81"),
                     ("Tom Fisher","Umbrella","76"),("Nina Petrova","Stark","73"),("Raj Mehta","Wayne","71"),("Amy Chen","Oscorp","68")]:
        card(base,d,(cx,ry,x1-40,ry+64),10,fill=CARD,sh=False)
        text(d,(cx+18,ry+10),nm,F(700,18),WHITE); text(d,(cx+18,ry+37),co,F(500,15),MUT)
        rr(d,(x1-40-104,ry+17,x1-40-16,ry+47),15,fill=(204,120,92,205)); text(d,(x1-40-92,ry+21),sc+" hot",F(700,15),(26,15,10)); ry+=76
def c_skills(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Skills","Installed","Store","Runs"],1)+22
    text(d,(cx,y0+22),"Ultron Skills",F(800,24),WHITE); text(d,(x1-170,y0+28),"12 installed",MONO(13),CORAL2)
    names=["Cold outreach","Lead research","Deal desk","Content studio","Deliverability","Meeting booker",
           "Proposal writer","Weekly report","Data cleanup","Follow-up cadence","Churn watch","Invoice chase"]
    cols=3; cw=(x1-40-cx-2*14)/cols; ry=y0+64
    for i,nm in enumerate(names):
        r=i//cols; c=i%cols; bx=cx+c*(cw+14); by=ry+r*190
        card(base,d,(bx,by,bx+cw,by+176),11,fill=CARD,sh=False)
        rr(d,(bx+16,by+16,bx+68,by+68),10,fill=(204,120,92,70)); rr(d,(bx+16,by+16,bx+68,by+68),10,outline=CORAL,w=1)
        text(d,(bx+16,by+84),nm,F(700,16),WHITE); text(d,(bx+16,by+116),"runs daily",F(500,13),MUT)
        rr(d,(bx+cw-74,by+18,bx+cw-16,by+44),13,fill=(204,120,92,205)); text(d,(bx+cw-64,by+22),"on",F(700,14),(26,15,10))
def c_revenue(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+40; text(d,(cx,y0+22),"Revenue",F(800,24),WHITE); text(d,(x1-150,y0+28),"MRR",MONO(13),CORAL2)
    text(d,(cx,y0+58),"$48,200",F(900,84),CORAL); text(d,(cx,y0+156),"up 32% this month, one operator",F(700,18),CORAL2)
    cbx,cby,cbw,cbh=cx,y0+206,x1-40-cx,240; card(base,d,(cbx,cby,cbx+cbw,cby+cbh))
    bars=[0.28,0.34,0.4,0.38,0.5,0.58,0.64,0.72,0.8,0.86,0.92,1.0]; bw=(cbw-40)/len(bars)
    for i,h in enumerate(bars):
        bh=(cbh-40)*h; bx=cbx+20+i*bw
        rr(d,(bx,cby+cbh-20-bh,bx+bw-8,cby+cbh-20),4,fill=(204,120,92,150+int(90*h)))
    ry=cby+cbh+22
    for nm,v in [("New customers","+38"),("Churn","0.9%"),("Expansion","+$6.2k"),("Payback","2.1 mo")]:
        card(base,d,(cx,ry,x1-40,ry+62),10,fill=CARD,sh=False); text(d,(cx+16,ry+18),nm,F(500,18),MUT); text(d,(x1-40-150,ry+14),v,F(800,22),WHITE); ry+=72
def c_agents(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Agents","Runs","Memory","Tools"],1)+22
    text(d,(cx,y0+22),"Agent runs",F(800,24),WHITE); text(d,(x1-160,y0+28),"live now",MONO(13),CORAL2)
    ry=y0+66
    for nm,act,st in [("Research","profiling 40 accounts","running"),("Outreach","writing sequence 3/8","running"),
                      ("Deals","scoring 12 replies","running"),("Ops","syncing pipeline","done"),
                      ("Content","drafting 5 posts","running"),("Report","building weekly","queued"),
                      ("Invoices","chasing 3 overdue","queued"),("Briefs","prepping tomorrow","running"),("Hygiene","cleaning CRM","done")]:
        card(base,d,(cx,ry,x1-40,ry+70),10,fill=CARD,sh=False)
        dot=CORAL if st=="running" else ((120,190,120) if st=="done" else MUT)
        d.ellipse([(cx+18)*SS,(ry+29)*SS,(cx+32)*SS,(ry+43)*SS],fill=dot+(255,))
        text(d,(cx+46,ry+13),nm,F(700,19),WHITE); text(d,(cx+46,ry+42),act,F(500,15),MUT)
        text(d,(x1-40-140,ry+25),st,MONO(15),(CORAL2 if st=="running" else MUT)); ry+=82
def c_levels(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=x0+40; text(d,(cx,y0+22),"7 levels of Ultron",F(800,24),WHITE); text(d,(x1-160,y0+28),"you: L5",MONO(13),CORAL2)
    lv=[("L1","Ask one question"),("L2","Chain a few steps"),("L3","Run a named agent"),("L4","Wire agents together"),
        ("L5","Automate a workflow"),("L6","Approve, do not do"),("L7","Run the whole company")]
    ry=y0+66; here=4
    for i,(lb,tx) in enumerate(lv):
        on=i<=here
        card(base,d,(cx,ry,x1-40,ry+92),10,fill=(204,120,92,45) if i==here else CARD,sh=False)
        rr(d,(cx+16,ry+20,cx+72,ry+70),9,fill=CORAL if on else (60,59,56)); text(d,(cx+26,ry+30),lb,F(800,22),(26,15,10) if on else MUT)
        text(d,(cx+94,ry+18),tx,F(700,23),WHITE if on else MUT)
        text(d,(cx+94,ry+56),["one prompt","copy paste","hand a job","they hand off","fires on triggers","yes or no","one operator"][i],F(500,15),MUT)
        ry+=104
def c_content(base,d,reg,accent):
    x0,y0,x1,y1=reg; cx=sidebar(d,reg,["Calendar","Drafts","Assets","Analytics"],0)+22
    text(d,(cx,y0+22),"Content calendar",F(800,24),WHITE); text(d,(x1-160,y0+28),"14 scheduled",MONO(13),CORAL2)
    days=["Mon","Tue","Wed","Thu"]; cw=(x1-40-cx)/4; gy=y0+62; pal=[(196,120,92),(212,162,127),(168,132,108),(180,146,120)]
    for i,dn in enumerate(days): text(d,(cx+i*cw+6,gy),dn,F(700,15),MUT)
    gy+=30
    plan={0:[0,2,4],1:[1,3],2:[0,2,4],3:[1,3]}
    for col in range(4):
        for r in range(5):
            bx=cx+col*cw+4; by=gy+r*150
            if r in plan.get(col,[]):
                card(base,d,(bx,by,bx+cw-12,by+136),10,fill=CARD,sh=False)
                rr(d,(bx+10,by+10,bx+cw-22,by+78),6,fill=pal[col]+(180,))
                text(d,(bx+10,by+90),["Post","Carousel","Reel","Story"][(col+r)%4],F(700,15),WHITE)
                text(d,(bx+10,by+112),"10:00",F(500,12),MUT)
            else: rr(d,(bx,by,bx+cw-12,by+136),10,fill=(40,40,38))

MOCK={
 "stripe":lambda:window(1380,940,c_stripe,"stripe.com"),
 "orgchart":lambda:window(1380,940,c_orgchart,"team.51ultron.com"),
 "workflows":lambda:window(1380,940,c_workflows,"flows.51ultron.com"),
 "leadscore":lambda:window(1380,940,c_leadscore,"leads.51ultron.com"),
 "skills":lambda:window(1380,940,c_skills,"skills.51ultron.com"),
 "revenue":lambda:window(1380,940,c_revenue,"app.51ultron.com"),
 "agents":lambda:window(1380,940,c_agents,"app.51ultron.com"),
 "levels":lambda:window(1380,940,c_levels,"app.51ultron.com"),
 "content":lambda:window(1380,940,c_content,"studio.51ultron.com"),
 "scheduler":lambda:window(1380,940,c_scheduler,"schedule.51ultron.com"),
 "warmup":lambda:window(1380,940,c_warmup,"deliver.51ultron.com"),
 "seowriter":lambda:window(1380,940,c_seowriter,"write.51ultron.com"),
 "softwarebill":lambda:window(1380,940,c_softwarebill,"ultron"),
 "designer":lambda:window(1380,940,c_designer,"studio.51ultron.com"),
 "developer":lambda:window(1380,940,c_developer,"deploy.51ultron.com"),
 "bill":lambda:window(1380,940,c_bill,"ultron"),
 "apollo":lambda:window(1380,940,c_apollo,"apollo.io"),
 "gmail":lambda:window(1380,940,lambda b,d,r,a:c_gmail(b,d,r,a,sent=False),"mail.google.com"),
 "gmail_sent":lambda:window(1380,940,lambda b,d,r,a:c_gmail(b,d,r,a,sent=True),"mail.google.com"),
 "calendly":lambda:window(1380,940,c_calendly,"calendly.com"),
 "hubspot":lambda:window(1380,940,c_hubspot,"hubspot.com"),
 "gate":lambda:window(1380,940,c_gate,"ultron"),
 "ultron":lambda:window(1380,940,c_ultron,"ultron"),
}
if __name__=="__main__":
    import sys,os; os.makedirs("/home/user/tiberiu-claude/content/_hitl-src/models_25d",exist_ok=True)
    ks=sys.argv[1:] or list(MOCK)
    for k in ks:
        MOCK[k]().convert("RGB").save(f"/home/user/tiberiu-claude/content/_hitl-src/models_25d/{k}.png"); print("built",k)
