#!/usr/bin/env python3
# Push adaptari IG Scraped: 2 randuri noi per material (TikTok tag ["TikTok"], IG tag ["IG Scraped"]),
# caption kit per canal (S15.6 + S30 TikTok mechanic), apoi STERGE randul-sursa "Scraped ·"
# (operator: "raman doar cele adaptate"). Usage: python3 push_adapted.py <slug> ...
import os, sys, json, time, glob, uuid, ssl, urllib.request
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; BUCKET="ultron-reels"
ME="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; CA="/root/.ccr/ca-bundle.crt"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method)
    r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    with urllib.request.urlopen(r,context=ctx,timeout=120) as resp: return resp.read()
def r2put(key,path):
    for att in range(5):
        try:
            req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",open(path,"rb").read(),"image/png"); return
        except Exception:
            if att==4: raise
            time.sleep(2**att)
def d1(sql,params=None):
    body={"sql":sql}
    if params: body["params"]=params
    out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps(body).encode(),"application/json"))
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

H="#claude #ai #founder #startup #buildinpublic"

# slug -> (TITLE, keyword(pastila), resurse DM, src_prefix de sters, tiktok_body, ig_body, first_comment_ig)
KITS={
 "aios":("THE AI OPERATING SYSTEM","OPERATOR","the AI OS setup map","263c2cda",
  "Most founders rent tabs that forget them at midnight.\n\nOperators run an OS: one memory, one command center, agents on triggers.\n\nNow I type one sentence and 200 accounts are briefed before coffee.\n\nEvery correction becomes a rule. The system compounds while the tabs reset.\n\nStop running your company from a chat window that has amnesia.",
  "Your AI forgets you the second the tab closes. That is the bottleneck, not the model.\n\nThe fix is an operating system: one permanent memory, agents that run on triggers, a command center that is yours, not rented.\n\nThis morning it read 1,284 leads and briefed 200 accounts from one typed sentence.\n\nNothing external fires without my tap. Power, gated.",
  "Rented tabs forget. Owned systems compound.\n\nDrop OPERATOR below and I will DM you the AI OS setup map, plus where the memory layer lives.\n\nSave this if your AI still asks who you are."),
 "loops":("PROMPTS ARE DEAD, LOOPS RUN","BUILDER","the loop playbook","6bf71ba3",
  "You are still typing prompts. The top operators set goals with exits.\n\nA loop runs on a trigger, checks its own work and reports when done.\n\nLast week: 212 cycles. I typed three sentences.\n\nOne trap: a loop without a checker burns budget in silence. Ultron caps every flow.\n\nScale past your hours, not into them.",
  "Prompt after prompt is working backwards: you are the cron job.\n\nAn Ultron flow takes one goal in plain English, runs on a trigger, verifies each cycle and reports when done.\n\n212 cycles ran last week from three typed sentences.\n\nEverything external still parks on HOLD for my tap. Loops run free, sends do not.",
  "The whole setup is one sentence: follow up every lead quiet for 3 days.\n\nDrop BUILDER below and I will DM you the loop playbook with the checker and exit rules.\n\nSave this before you type your next prompt."),
 "aibody":("THE COMPLETE AI BODY","FOUNDER","the full operator stack map","0a3c53ce",
  "Most founders rent one mouth: a chatbot that answers.\n\nOperators wire the whole body. The router thinks, CORTEX reads the market, PULSE speaks in your voice, SENTINEL ships product, one memory keeps it alive.\n\nEvery external move still waits for your tap.\n\nAugmented, not replaced. That is the difference.",
  "A chatbot answers questions. A body does work.\n\nInside Ultron: the router is the brain, CORTEX the eyes on 1,284 companies, PULSE the voice sampled from your posts, SENTINEL the hands that ship, one memory as the heart.\n\nYou hold the reins: nothing external fires without your tap.",
  "Brain, eyes, voice, hands, heart. One login.\n\nDrop FOUNDER below and I will DM you the full operator stack map, organ by organ.\n\nSave this if you are still typing into one mouth."),
 "fivesigns":("5 SIGNS YOU NEED AI NOW","FOUNDER","the 5-signs checklist + first-flow guide","fa7eedb6",
  "Same questions answered daily. Data moved by hand. Everything waiting on you. Leads waiting hours. Reports taking days.\n\nEvery yes is a leak. Five yes answers is not a staffing problem, it is missing systems.\n\nStart with the worst leak. One sentence sets up the flow. The gate keeps your tap on everything.\n\nScore yourself before you hire again.",
  "Most businesses do not need more employees. They need fewer repetitive tasks.\n\nThe five signs: repeat questions, copy-paste bridges between apps, approval bottlenecks, slow first replies, month-end reports that take days.\n\nUltron fixes them one flow at a time, and every customer-facing step still parks for your tap.",
  "Count your yes answers. Every one is a leak that a flow can plug this week.\n\nDrop FOUNDER below and I will DM you the 5-signs checklist plus the first-flow setup guide.\n\nSave this and score your own business tonight."),
 "contentdesk":("THE 500K CONTENT DESK","OPERATOR","the 5-skill content desk setup","5af9c9ec",
  "A content team used to mean five salaries and a Monday meeting.\n\nMine is five skills in one chat: the calendar plans itself, hooks rotate from my bank, drafts land in my voice, one brief becomes five formats, newsletters hit 99.2% inbox.\n\nNothing posts without my tap.\n\nThe desk is metered in cents, not salaries.",
  "Five skills run my whole content desk from one chat.\n\nThe calendar plans 14 slots from one line. Hooks come in three angles, I pick the winner. Drafts arrive in my voice, ranked. One brief becomes five native formats. Newsletters land at 99.2%.\n\nEvery draft parks for my tap before it posts.",
  "Planner, writer, designer, distributor: one subscription, no meetings.\n\nDrop OPERATOR below and I will DM you the 5-skill content desk setup.\n\nSave the desk and steal the pipeline."),
}

def cap_tt(kit):
    t,kw,res,_,tt,_,_=kit
    return (f"Comment {kw} for {res} and I reply to the first 20. Save this so you do not lose it.\n\n"
            f"{tt}\n\n{H}\n\nFIRST COMMENT (pinned):\n{res.capitalize()} is in my bio right now, so no waiting on a DM. "
            f"Drop {kw} below and I will send it too, I read every comment. Save the video so you can set it up later.")
def cap_ig(kit):
    t,kw,res,_,_,ig,fc=kit
    return (f"Comment {kw} and I will send you {res}.\n\n{ig}\n\n{H}\n\nFIRST COMMENT:\n{fc}")

if __name__=="__main__":
    slugs=sys.argv[1:]
    ts=time.strftime("%Y-%m-%d %H:%M"); dirid=str(int(time.time()))
    mx=d1(f"SELECT MAX(created_at) m FROM vault_items WHERE owner='{ME}'")[0]["m"] or 0
    base=int(mx)+600000; k=0
    for slug in slugs:
        kit=KITS[slug]; title=kit[0]; srcpref=kit[3]
        for suffix,chan,tags,cap in [("(TikTok 3D)","tt",'["TikTok"]',cap_tt(kit)),("(Instagram)","ig",'["IG Scraped"]',cap_ig(kit))]:
            ddir=f"scratchpad/{slug}_{chan}"
            pngs=sorted(glob.glob(f"{ddir}/s*.png"), key=lambda f:int(''.join(c for c in os.path.basename(f) if c.isdigit())))
            keys=[]
            for i,f in enumerate(pngs,1):
                key=f"imports/pm/{slug}-{chan}-{dirid}/{i:02d}.png"; r2put(key,f); keys.append(key)
            media=json.dumps([{"key":x,"type":"image","ext":"png","contentType":"image/png"} for x in keys])
            nid=str(uuid.uuid4()); k+=1
            d1("INSERT INTO vault_items (id,owner,kind,name,source,thumb_key,media,tags,created_at,caption) VALUES (?,?,?,?,?,?,?,?,?,?)",
               [nid,ME,"carousel",f"Review · {title} {suffix} · {ts}","studio",keys[0],media,tags,base+k*1000,cap])
            print("OK",title,suffix,len(keys))
        # sterge sursa adaptata
        d1(f"DELETE FROM vault_items WHERE owner='{ME}' AND id LIKE '%' AND name LIKE 'Scraped %' AND id IN (SELECT id FROM vault_items WHERE owner='{ME}' AND name LIKE 'Scraped %' AND created_at IN (SELECT created_at FROM vault_items WHERE owner='{ME}' AND name LIKE 'Scraped %'))" if False else "SELECT 1")
        # match sursa dupa numele copiat (prefixul numelui original)
        src=d1(f"SELECT id,name FROM vault_items WHERE owner='{ME}' AND name LIKE 'Scraped %'")
        FIRST={"263c2cda":"Comment “OS”","6bf71ba3":"Comment “LOOP”","0a3c53ce":"AI didn’t take your job","fa7eedb6":"5 Signs Your Business","5af9c9ec":"Comment “SKILLS”"}
        frag=FIRST[srcpref]
        for r in src:
            if frag in r["name"]:
                d1("DELETE FROM vault_items WHERE id=?",[r["id"]]); print("DEL sursa:",r["name"][:60])
    print("DONE")
