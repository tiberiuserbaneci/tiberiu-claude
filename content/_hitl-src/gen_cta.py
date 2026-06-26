import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
SEED=b64(f"{TE}/roll3/models/m4.png")
# Reusable 3D CTA pills, charcoal, front-on, brand orange C8643F. Generated ONCE, rotated across materials.
BASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D quality, physically-based rendering) of a SINGLE premium "
 "PILL-SHAPED BUTTON, viewed STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW - upright and perfectly symmetric, no perspective tilt. "
 "It IS a real 3D object: a glossy soft-touch button with subtly BEVELED rounded edges and clear visible THICKNESS, lit by a "
 "three-point SOFTBOX studio setup with ambient occlusion and a SOFT CONTACT SHADOW beneath it. NOT a flat 2D screenshot, NOT "
 "a sticker, NOT an illustration. On a COMPLETELY FLAT #191919 dark charcoal background, vertical 4:5, the pill WIDE and centred "
 "with even margins. The pill body is solid warm orange hex C8643F. On the left edge a small clean white speech-bubble comment "
 "icon, then bold WHITE sans-serif text that reads: %s . Show those two words only, correctly spelled, with NO quotation marks "
 "and NO other words, labels or symbols. NO eyebrow/title/footer/page number anywhere - ONLY the one orange pill button on charcoal.")
CTAS={"operator":"Comment OPERATOR","founder":"Comment FOUNDER","builder":"Comment BUILDER"}
def gen(prompt,out):
    body={"contents":[{"role":"user","parts":[{"inlineData":{"mimeType":"image/png","data":SEED}},{"text":prompt}]}],
          "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for a in range(6):
        try: r=requests.post(URL,headers={"authorization":f"Bearer {tok}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        except Exception as e: print(" exc",str(e)[:40]); time.sleep(10); continue
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print(" no image",j.get("candidates",[{}])[0].get("finishReason"))
        else: print(" HTTP",r.status_code,r.text[:120])
        time.sleep(20*(a+1) if r.status_code==429 else 6)
    return False
OUT=f"{TE}/roll3/cta3d"; os.makedirs(OUT,exist_ok=True)
keys=sys.argv[1:] if len(sys.argv)>1 else list(CTAS)
for k in keys:
    o=f"{OUT}/cta-{k}.png"
    if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",k); continue
    print(k,"OK" if gen(BASE%CTAS[k],o) else "FAIL"); time.sleep(8)
print("CTA DONE")
