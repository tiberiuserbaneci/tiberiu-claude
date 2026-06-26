import os,json,base64,time,requests
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
SEED=b64(f"{TE}/roll3/models/m4.png")
# Same charcoal front-on formula, but the colour is DESCRIBED (warm terracotta orange) and the hex is
# explicitly forbidden as visible text - the previous tiers render printed 'C8643F' as a chip and
# hallucinated prices. No money anywhere.
MBASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D quality, physically-based rendering) of a premium UI panel, "
 "viewed STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW - upright and perfectly symmetric, no perspective tilt. It IS a real 3D "
 "object: a soft-touch MATTE panel with subtly BEVELED rounded edges and visible THICKNESS, lit by a three-point SOFTBOX "
 "studio setup with ambient occlusion and a SOFT CONTACT SHADOW beneath it. NOT a flat 2D screenshot, NOT a sticker, NOT "
 "an illustration. On a COMPLETELY FLAT #191919 dark charcoal background, vertical 4:5, a panel about 3:2 sitting in the "
 "MIDDLE at roughly 70% width so there is a GENEROUS EMPTY CHARCOAL MARGIN on ALL FOUR sides. CRITICAL: the panel is rendered "
 "WHOLE and COMPLETE - every one of its four rounded corners and its full LEFT, RIGHT, TOP and BOTTOM edges are clearly visible "
 "inside the frame; NOTHING is cropped, cut off, or running past the frame edge. "
 "ALL accent colours, buttons, chips, icons are the SAME warm terracotta orange (a muted burnt-sienna). NO green, NO blue, "
 "NO purple - only charcoal, white, muted grey and that one warm orange. Real legible text, EXACT words, no garbled text. "
 "CRITICAL: do NOT render any hex code or colour code (such as 'C8643F') as visible text; colours are colours, never labels. "
 "NO prices, NO dollar amounts, NO money, NO percentages, NO stray numbers. "
 "NO eyebrow/headline/title/footer/page number anywhere - ONLY the panel. The panel shows ")
MTAIL=" The whole panel is exactly this, centred, front-on. No other panels. Remember: no hex text, no prices, no money."
TIERS=("three tier cards side by side, each card a vertical stack of three short text lines - a tier name on top, "
 "a model name in the middle, and a short use case at the bottom: the LEFT card reads 'Lite' then 'Haiku' then 'quick lookups'; "
 "the CENTRE card reads 'Smart' then 'Sonnet' then 'the default'; the RIGHT card reads 'Deep' then 'Opus' then 'hard judgment'. "
 "The centre 'Smart' card is highlighted with a warm-orange border and a small warm-orange pill reading 'Most used' at its very top; "
 "the left and right cards are plain charcoal with a thin grey outline. Each card has only those three text lines and nothing else.")
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
        else: print(" HTTP",r.status_code,r.text[:160])
        time.sleep(20*(a+1) if r.status_code==429 else 6)
    return False
out=f"{TE}/roll3/models_routing/tiers.png"
print("tiers regen:", "OK" if gen(MBASE+TIERS+MTAIL,out) else "FAIL")
