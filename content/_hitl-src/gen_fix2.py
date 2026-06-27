import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
# SEED-INDEPENDENT: no reference image -> Vertex follows the text, stops copying the dashboard seed.
# Prompts are DENSER (more rows / real labels) per operator: panels need real context, not one word.
MBASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D quality, physically-based rendering) of a premium UI panel, "
 "viewed STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW - upright, symmetric, no perspective tilt. A soft-touch MATTE charcoal panel "
 "with subtly BEVELED rounded edges and visible THICKNESS, three-point softbox lighting, ambient occlusion, a soft contact "
 "shadow. NOT a flat screenshot, NOT a sticker. On a COMPLETELY FLAT #191919 dark charcoal background, vertical 4:5, the panel "
 "about 3:2 in the MIDDLE at ~70% width with a GENEROUS EMPTY charcoal margin on ALL FOUR sides. CRITICAL: the panel is WHOLE "
 "and COMPLETE - all four rounded corners and the full left/right/top/bottom edges visible inside the frame, nothing cropped. "
 "The panel BODY is dark charcoal (NOT a light/cream/white dashboard). ALL accents, chips, icons, dots are ONE warm terracotta "
 "orange (muted burnt-sienna). NO green, NO blue, NO purple, NO light dashboards. Real legible text, EXACT words, no garbled "
 "text, no hex codes, no raw code, no prices. Make it DENSE and information-rich - real rows and labels, not one or two words. "
 "NO title/eyebrow/footer/page-number outside the panel. The panel shows ")
MTAIL=" Centred, front-on, dense and complete. One panel only."
# Only the objects that collapsed to the seed dashboard or were too thin / contained 'GTM'. Each distinct + on-topic + dense.
J={
 "projects/pain":"a chat window titled 'Every new chat' showing a long user message bubble that is visibly re-pasting business context, with three greyed repeated lines inside it: 'our ICP is US/UK founders...', 'our pricing is...', 'our brand voice is...', and a small tired note at the bottom 'you type this every single time'.",
 "projects/setonce":"a project workspace panel titled 'Services Co-pilot' with a 'Custom instructions' block of two readable lines ('US/UK founders, 2 to 50 staff' and 'blunt, specific, end with the next action'), a small warm-orange 'Saved' chip, and a faint row of file chips beneath.",
 "projects/name":"a project settings panel with a highlighted title field reading 'Services Co-pilot', a small caption 'name it after the job, not the tool', and two greyed example rows beneath: 'Outbound Engine', 'Content Studio'.",
 "skills/striker":"a roster card for a deals agent: a circular agent node icon, the name 'STRIKER', a command chip '/striker', and four skill rows each with a small warm-orange dot and a short label: 'Objection handler', 'Pre-call research', 'Discovery script', 'Post-meeting follow-up'.",
 "skills/pulse":"a roster card for a content agent: a circular agent node icon, the name 'PULSE', a command chip '/pulse', and four skill rows each with a small warm-orange dot: 'LinkedIn post', 'Content hooks', 'Newsletter', 'Repurpose to 5 posts'.",
 "skills/amplify":"a roster card for a paid-media agent: a circular agent node icon, the name 'AMPLIFY', a command chip '/amplify', and four skill rows each with a small warm-orange dot: 'Campaign setup', 'Audience builder', 'Ad copy', 'Spend report'.",
 "chat/onebox":"a single dark chat composer panel titled with a greeting, a wide 'Ask anything, or slash an agent' input bar, a row of four suggestion chips ('Research an account', 'Draft outbound', 'Score leads', 'Write a post'), and a small tier toggle (Lite / Smart / Deep) in the corner.",
 "chat/tier":"a dark settings panel titled 'Model tier' with a segmented control (Lite / Smart / Deep, the 'Deep' segment filled warm orange) and three explanatory rows beneath: 'Lite - quick lookups', 'Smart - the real work', 'Deep - hard judgement'.",
 "chat/files":"a dark file panel titled 'Working context' with four rows, each a file icon, a name, a size and a small warm-orange 'cached' check: 'pitch-deck  2.4 MB', 'icp-list  880 KB', 'sales-call  14 MB', 'pricing  640 KB', and a faint 'read by every new chat' note.",
 "chat/share":"a dark panel titled 'Share session' with a rounded 'Read-only link' pill at the top showing a short url, a small caption 'carries every turn, source and artifact', and a 3x3 grid of small proof tiles beneath with one tile highlighted warm orange.",
}
def gen(prompt,out):
    body={"contents":[{"role":"user","parts":[{"text":prompt}]}],   # NO seed image
          "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for a in range(7):
        try: r=requests.post(URL,headers={"authorization":f"Bearer {tok}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        except Exception as e: print(" exc",str(e)[:40]); time.sleep(10); continue
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print(" no image",j.get("candidates",[{}])[0].get("finishReason"))
        else: print(" HTTP",r.status_code,r.text[:90])
        time.sleep(20*(a+1) if r.status_code==429 else 6)
    return False
keys=sys.argv[1:] if len(sys.argv)>1 else list(J)
for k in keys:
    m,name=k.split("/"); OUT=f"{TE}/roll3/models_{m}"; os.makedirs(OUT,exist_ok=True); o=f"{OUT}/{name}.png"
    print(k,"OK" if gen(MBASE+J[k]+MTAIL,o) else "FAIL"); time.sleep(6)
print("FIX2 DONE")
