import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
SEED=b64(f"{TE}/roll3/models/m4.png")
# Same charcoal front-on panel formula as gen_hitl (MBASE) -> reusable by build_3d916.
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
 "trigger":"FOUR task cards in a 2x2 grid, each a small orange square icon and a short label: 'Scrape 200 sites', 'Enrich a lead list', 'Transcribe a call', 'A 9am digest'. Each a small rounded sub-panel.",
 "mission":"a vertical orchestration flow: a top command card reading 'Scrape 200 sites', a thin orange arrow down, then a stacked sequence of five small job chips: 'Crawl the sites', 'Pull the data', 'Enrich the list', 'Build the report', and a final highlighted orange chip 'Human gate'.",
 "dashboard":"a jobs dashboard: on the LEFT a big progress DONUT ring reading '4 of 6 done', on the RIGHT a stacked list of four job rows, each a job name and a small status chip: 'Scrape 200 sites - running', 'Enrich list - done', 'Transcribe call - paused', 'Morning digest - queued', with tiny control labels 'cancel  pause  resume' beneath.",
 "parallel":"THREE small running job cards side by side, each with a job name, a tiny horizontal progress bar at a different fill level and a percent: 'Scrape sites 62%', 'Enrich list 30%', 'Transcribe call 80%'. Shows many jobs running at once.",
 "controls":"a single wide job row card with the job name 'Scrape 200 sites' and a small 'running' chip, and below it a row of FOUR small rounded control buttons labelled 'Cancel', 'Pause', 'Resume', 'Retry'.",
 "gate":"an approval card for a paused background job: a header 'Approval needed' with a small orange dot, a bold line 'Post the Q3 report to the blog', a sub-line 'the job is paused, waiting for you', and two buttons - an orange 'Approve' and an outlined 'Hold'.",
 "notify":"a notification toast card: a small bell icon, a bold line 'Your job is done', a sub-line 'Scrape 200 sites finished - 8,400 rows', and a small orange 'View' button on the right.",
 "scheduled":"a scheduled job card: a clock icon, a bold line 'Morning digest', a sub-line 'every day at 9:00 am', and a small orange ON toggle switch on the right.",
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
OUT=f"{TE}/roll3/models_jobs"; os.makedirs(OUT,exist_ok=True)
keys=sys.argv[1:] if len(sys.argv)>1 else list(J)
for k in keys:
    o=f"{OUT}/{k}.png"
    if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",k); continue
    print(k,"OK" if gen(MBASE+J[k]+MTAIL,o) else "FAIL"); time.sleep(8)
print("JOBS3D DONE")
