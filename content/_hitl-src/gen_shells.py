import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
# BLANK reusable 3D shells - the rich embossed CONTAINER only; text gets injected from code later.
SBASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D, physically-based) of ONE premium UI container, viewed "
 "STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW, upright and perfectly symmetric, NO perspective tilt. Soft-touch MATTE dark "
 "charcoal, subtly BEVELED rounded edges, visible THICKNESS, three-point softbox lighting, gentle ambient occlusion, a "
 "soft contact shadow beneath. On a COMPLETELY FLAT #191919 charcoal background, vertical 4:5, the object ~72% width in the "
 "MIDDLE with a GENEROUS empty charcoal margin on ALL four sides; rendered WHOLE, all corners and edges inside the frame. "
 "Warm terracotta-orange (muted burnt-sienna) is the ONLY accent colour; otherwise charcoal, near-black, muted grey. "
 "CRITICAL: the container is COMPLETELY BLANK - absolutely NO text, NO letters, NO numbers, NO labels, NO icons, NO logos, "
 "NO charts - ONLY the empty 3D container structure with clean flat empty zones ready to receive text. NO green/blue/purple. "
 "The container is ")
STAIL=" Front-on, centred, complete, and totally blank inside. One container only."
S={
 "panel":"a single wide empty rounded-rectangle panel - one large clean flat blank face, beveled raised edges, a subtle inner emboss groove around the rim, nothing on it.",
 "list":"a tall rounded panel split into SIX equal empty horizontal rows by thin recessed separator lines, with a small empty circular icon well at the left of each row - every row totally blank.",
 "stat":"a wide rounded panel whose left two-thirds is one big clean blank recessed area (for a large number) and whose right third holds two small empty rounded raised chips stacked vertically - all blank.",
 "donut":"a wide rounded panel with, on the left, a thick terracotta-orange 3D progress RING about 70 percent filled with a hollow blank centre, and on the right three empty horizontal rows each with a tiny raised dot at the left - no text.",
 "pill":"a single horizontal rounded-capsule 3D button, glossy terracotta-orange, smooth and raised with a soft inner highlight - completely blank, no text.",
 "chatbox":"a rounded chat panel: a slim header bar across the top, then two empty message rows each with a small circular avatar well and a blank line beside it, and at the bottom a recessed input field with a small raised orange square button on its right - all blank.",
}
def gen(prompt,out):
    body={"contents":[{"role":"user","parts":[{"text":prompt}]}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
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
OUT=f"{TE}/shells"; os.makedirs(OUT,exist_ok=True)
for k in (sys.argv[1:] or list(S)):
    o=f"{OUT}/{k}.png"
    if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",k); continue
    print(k,"OK" if gen(SBASE+S[k]+STAIL,o) else "FAIL"); time.sleep(6)
print("SHELLS DONE")
