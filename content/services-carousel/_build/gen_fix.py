import os,json,base64,time,requests
TOK=open("gcp_token.txt").read().strip(); P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
logo=b64("ultron-logo.png"); creA=b64("out/creative-A.png"); s2=b64("out/apps-2.png")
FONT="Match EXACTLY the headline FONT (bold geometric sans) and the vivid orange hex e8542b accent color and the premium cream 3D editorial style, palette and lighting of the reference image. Vertical 4:5, no watermark. "
JOBS=[
 (1,[creA],
  FONT+"This is the HOOK slide, keep the dynamic energy of the reference: the glossy dark Ultron orb (vivid electric-blue glow one edge, warm-orange the other) as the hero, surrounded by a dynamic swirl of MIXED glossy 3D service objects - a signed contract, an invoice, a calendar, an email envelope and a chat bubble - flying in with warm-orange motion streaks. "
  "Headline: 'You run every service by hand.' in near-black, then 'Ultron runs it for you.' in vivid orange italic."),
 (3,[s2],
  FONT+"Do NOT put the Ultron orb. A DIFFERENT STRUCTURE from a scattered cloud of icons: a clear CENTRAL composition - one large glossy 3D proposal DOCUMENT in the middle being assembled, with proposal app icons (a blue Docs icon, a green Sheets icon, an e-signature pen icon, an orange CRM contact icon) arranged neatly around it and feeding into it along short orange connectors, like building a document. "
  "Headline: 'Ultron writes the proposal.' with 'writes the proposal' in orange. Small glossy pill chip 'Waits for a YES before sending' with an orange YES button and a ? button."),
 (4,[s2],
  FONT+"Do NOT put the Ultron orb. A DIFFERENT STRUCTURE again: a clean VERTICAL QUEUE / STACK - a column of glossy 3D support-ticket and chat-bubble cards stacked top to bottom, each getting a green check and clearing down into an empty inbox tray at the bottom, with small support app icons (Gmail inbox, a headset helpdesk icon, an orders bag, an issue-tracker checklist, Slack) aligned down one side. "
  "Headline: 'Ultron clears the support inbox.' with 'clears the support inbox' in orange. Small glossy pill chip 'Waits for a YES before any refund' with an orange YES button and a ? button."),
 (5,[s2],
  FONT+"Do NOT put the Ultron orb. Clean and minimal CTA slide with lots of negative space. Big bold headline centered: 'One ask.' in near-black and 'Every service runs.' in vivid orange italic. Below, a single bold solid orange 3D pill button reading 'COMMENT SERVICES'. A soft ring of small glossy 3D app icons around the edges. Leave a little clear space at the very bottom."),
]
def gen(refs,prompt,out):
    parts=[{"inlineData":{"mimeType":"image/png","data":r}} for r in refs]+[{"text":prompt}]
    body={"contents":[{"role":"user","parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for a in range(5):
        r=requests.post(URL,headers={"authorization":f"Bearer {TOK}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print("  no image",j.get("candidates",[{}])[0].get("finishReason"))
        else: print("  HTTP",r.status_code,r.text[:140])
        time.sleep(8*(a+1))
    return False
for n,refs,pr in JOBS:
    print(n,"OK" if gen(refs,pr,f"out/fix-{n}.png") else "FAIL"); time.sleep(4)
print("DONE")
