import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
MBASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D) of ONE premium UI panel, STRAIGHT-ON ORTHOGRAPHIC FRONT VIEW, "
 "soft-touch MATTE DARK CHARCOAL panel, beveled rounded edges, visible thickness, softbox lighting, soft contact shadow. "
 "On a COMPLETELY FLAT #191919 dark charcoal background, vertical 4:5, the panel ~70% width centred with generous charcoal "
 "margin on all four sides, rendered WHOLE - all corners and edges visible, nothing cropped. The panel body is DARK charcoal. "
 "Accents/chips/dots/icons are ONE warm terracotta orange. ABSOLUTELY NOT a dashboard: NO bar charts, NO line graphs, NO grid "
 "of stat numbers, NO light/cream/white dashboard. NO green/blue/purple. Real legible EXACT text, no garbled text, no hex, no "
 "code, no prices. Dense and information-rich. NO title/eyebrow/footer/page-number outside the panel. The panel shows ")
MTAIL=" Centred, front-on, complete. One dark panel only. Definitely NOT a dashboard."
J={
 "skills/specter":"a roster card for an outbound agent: a circular agent node icon on the left, the name 'SPECTER' in bold, a small command chip '/specter', and four skill rows beneath, each a small warm-orange dot and a short label: 'Find decision-makers', 'Cold email', 'Follow-up sequence', 'Lead scoring'.",
 "skills/cta":"a simple chat comments box titled 'Comments' with two faint placeholder comment rows near the top, then a highlighted input row at the bottom containing the single word 'SKILLS' and a filled warm-orange 'Post' button to its right. Just a comments box.",
 "chat/share":"a single share card titled 'Share session': at the top a rounded 'Read-only link' pill showing a short url, a one-line caption 'carries every turn and source', and beneath it a horizontal row of three small document thumbnail tiles with one tile highlighted warm orange.",
}
def gen(prompt,out):
    body={"contents":[{"role":"user","parts":[{"text":prompt}]}],
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
for k in (sys.argv[1:] or list(J)):
    m,name=k.split("/"); OUT=f"{TE}/roll3/models_{m}"; os.makedirs(OUT,exist_ok=True)
    print(k,"OK" if gen(MBASE+J[k]+MTAIL,f"{OUT}/{name}.png") else "FAIL"); time.sleep(6)
print("FIX3 DONE")
