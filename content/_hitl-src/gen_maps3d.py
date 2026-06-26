import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
SEED=b64(f"{TE}/roll3/models/m4.png")
# Charcoal front-on panel formula + anti-crop rule (objects rendered whole, full margins).
MBASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D quality, physically-based rendering) of a premium UI panel, "
 "viewed STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW - upright and perfectly symmetric, no perspective tilt. It IS a real 3D "
 "object: a soft-touch MATTE panel with subtly BEVELED rounded edges and visible THICKNESS, lit by a three-point SOFTBOX "
 "studio setup with ambient occlusion and a SOFT CONTACT SHADOW beneath it. NOT a flat 2D screenshot, NOT a sticker, NOT "
 "an illustration. On a COMPLETELY FLAT #191919 dark charcoal background, vertical 4:5, a panel about 3:2 sitting in the "
 "MIDDLE at roughly 70% width so there is a GENEROUS EMPTY CHARCOAL MARGIN on ALL FOUR sides. CRITICAL: the panel is rendered "
 "WHOLE and COMPLETE - every one of its four rounded corners and its full LEFT, RIGHT, TOP and BOTTOM edges are clearly visible "
 "inside the frame; NOTHING is cropped, cut off, or running past the frame edge; the object is not a fragment. "
 "ALL accent colours, buttons, chips, icons use the EXACT warm orange hex C8643F and nothing "
 "else orange or red. NO green, NO blue, NO purple - only charcoal, white, muted grey and that orange. Real legible text, "
 "numbers EXACT, no garbled words. NO eyebrow/headline/title/footer/page number anywhere - ONLY the panel. The panel shows ")
MTAIL=" The whole panel is exactly this, centred, front-on. No other panels."
J={
 "ask":"a New scrape input form with three labelled fields stacked: 'Category: dentist', 'Location: Austin, TX', 'Max results: 500', and an orange 'Run' button at the bottom.",
 "results":"a results list titled 'Places found' with four rows, each a small pin icon, a business name and a rating number: 'Joe Coffee   4.7', 'Bright Dental   4.9', 'Austin Plumbing   4.5', 'Green Yoga   4.8'.",
 "fields":"a single place detail card titled 'Joe Coffee' with stacked labelled fields: 'Phone   +1 512 555 1234', 'Website   joecoffee.com', 'Rating   4.7 / 312 reviews', 'Hours   Mon-Sun 7 to 7', 'Category   Coffee shop'.",
 "coverage":"a checklist card titled 'Per place you get' with six rows, each a small orange check mark and a label: 'Name and address', 'Phone and website', 'Rating and reviews', 'Opening hours', 'Categories', 'Photo count'.",
 "modes":"a two-column comparison card: left column under a grey header 'Fast' lists 'name', 'rating', 'reviews'; right column under an ORANGE header chip 'Full' lists 'phone', 'website', 'hours', 'place id'.",
 "scale":"a stat panel with a very large orange number '500' and a smaller label under it 'per search', and to the right two small rounded chips reading 'residential proxy' and 'one row per place'.",
 "accuracy":"a small card titled 'No half-empty rows' with a body line 'it waits for phone and website to load before reading' and one orange check mark, plus a small sub-line 'one clean row per place'.",
 "pipeline":"a horizontal flow of three rounded cards joined by thin orange arrows: a card 'Scrape', an arrow, a card 'Enrich', an arrow, and a highlighted orange card 'Outbound'.",
}
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
OUT=f"{TE}/roll3/models_maps"; os.makedirs(OUT,exist_ok=True)
keys=sys.argv[1:] if len(sys.argv)>1 else list(J)
for k in keys:
    o=f"{OUT}/{k}.png"
    if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",k); continue
    print(k,"OK" if gen(MBASE+J[k]+MTAIL,o) else "FAIL"); time.sleep(8)
print("MAPS3D DONE")
