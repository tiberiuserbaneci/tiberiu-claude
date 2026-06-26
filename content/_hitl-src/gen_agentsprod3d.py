import os,json,base64,time,requests,sys
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
tok=requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
SEED=b64(f"{TE}/roll3/models/m4.png")
MBASE=("A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D quality, physically-based rendering) of a premium UI panel, "
 "viewed STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW - upright and perfectly symmetric, no perspective tilt. It IS a real 3D "
 "object: a soft-touch MATTE panel with subtly BEVELED rounded edges and visible THICKNESS, lit by a three-point SOFTBOX "
 "studio setup with ambient occlusion and a SOFT CONTACT SHADOW beneath it. NOT a flat 2D screenshot, NOT a sticker, NOT "
 "an illustration. On a COMPLETELY FLAT #191919 dark charcoal background, vertical 4:5, a panel about 3:2 sitting in the "
 "MIDDLE at roughly 70% width so there is a GENEROUS EMPTY CHARCOAL MARGIN on ALL FOUR sides. CRITICAL: the panel is rendered "
 "WHOLE and COMPLETE - every one of its four rounded corners and its full LEFT, RIGHT, TOP and BOTTOM edges are clearly visible "
 "inside the frame; NOTHING is cropped, cut off, or running past the frame edge; the object is not a fragment. "
 "ALL accent colours, buttons, chips, icons, checks and dots are the SAME warm terracotta orange (a muted burnt-sienna). "
 "NO green, NO blue, NO purple - only charcoal, white, muted grey and that one warm orange. Real legible text, EXACT words, "
 "no garbled text. CRITICAL: do NOT render any hex code or colour code as visible text; no raw code, no snake_case, no prices. "
 "NO eyebrow/headline/title/footer/page number outside the panel - ONLY the panel. The panel shows ")
MTAIL=" The whole panel is exactly this, centred, front-on. No other panels. No code, no hex text."
J={
 "compare":"a two-column comparison panel. The LEFT column has a header 'Demo' and four rows, each with a small muted-grey cross mark: 'Happy path only', 'No retries', 'No memory', 'Crashes on bad input'. The RIGHT column has a header 'Production' and four rows, each with a small warm-orange check mark: 'Handles failures', 'Retries and fallbacks', 'Persistent memory', 'Stays up'.",
 "checklist":"a checklist card titled 'Production-ready' with six rows, each a small warm-orange check and a short label: 'Handles tool failures', 'Every run observable', 'Memory across sessions', 'Guardrails on risky actions', 'Stays within budget', 'Tested before ship'.",
 "model":"a panel titled 'Right model per job' with three small rounded model chips in a horizontal row labelled 'Haiku', 'Sonnet', 'Opus' (only the middle 'Sonnet' chip filled warm orange, the others plain charcoal), and one line of text below reading 'plus a clear system prompt'.",
 "tools":"a status card titled 'Tool call' showing a left-to-right flow of three rounded pills: a muted-grey pill 'timeout', then a warm-orange pill 'retry', then a warm-orange pill 'recovered', and a small sub-line beneath reading 'a dead API never crashes the run'.",
 "memory":"a panel titled 'It remembers' with three stacked rows, each led by a small warm-orange dot: 'Last session', 'Your context', 'Business rules', and a small sub-line at the bottom 'no re-explaining every time'.",
 "trace":"a run-trace log panel titled 'Run trace' with four short rows, each with a tiny warm-orange status dot and plain text: 'search  ok', 'draft  ok', 'send  waiting', 'done', conveying full visibility of what the agent did.",
 "gate":"an approval card titled 'Needs your yes' listing three high-risk actions, each with a small warm-orange lock icon: 'Delete records', 'Send emails', 'Charge a card', and two buttons at the bottom: a filled warm-orange 'Approve' and an outlined 'Hold'.",
 "eval":"an evaluation card titled 'Before ship' with one very large warm-orange score '24/25' and a label beneath 'golden set passed', plus a small sub-row 'every change tested'.",
 "cta":"a chat comments panel titled 'Comments' with two faint placeholder comment rows near the top, then a highlighted input row at the bottom containing the single word 'AGENTS' with a filled warm-orange 'Post' button to its right.",
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
OUT=f"{TE}/roll3/models_agentsprod"; os.makedirs(OUT,exist_ok=True)
keys=sys.argv[1:] if len(sys.argv)>1 else list(J)
for k in keys:
    o=f"{OUT}/{k}.png"
    if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",k); continue
    print(k,"OK" if gen(MBASE+J[k]+MTAIL,o) else "FAIL"); time.sleep(7)
print("AGENTSPROD DONE")
