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
 "ALL accent colours, buttons, chips, icons, checks, dots use the SAME warm terracotta orange (a muted burnt-sienna). "
 "NO green, NO blue, NO purple - only charcoal, white, muted grey and that one warm orange. Real legible text, EXACT words, "
 "no garbled text. CRITICAL: do NOT render any hex code or colour code as visible text; no raw code, no snake_case, no prices. "
 "NO eyebrow/headline/title/footer/page number outside the panel - ONLY the panel. The panel shows ")
MTAIL=" The whole panel is exactly this, centred, front-on. No other panels. No code, no hex text."
MATS={
 "code":{
  "start":"a clean dark terminal window mockup with a top label 'Claude Code' and a single prompt line reading 'add rate limiting and test it' with a blinking cursor, and a small status line below 'ready'. No code, just the one plain-English prompt.",
  "init":"a step card pairing a rounded command chip reading '/init' on the left with, on the right, a small document icon labelled 'CLAUDE.md' and a one-line caption 'reads your repo, remembers your rules'.",
  "plan":"a panel titled 'Plan' listing three short proposed steps, each a row with a small empty checkbox and a few plain words, and a filled warm-orange 'Approve' button at the bottom - it plans before it edits.",
  "run":"a terminal run panel with three stacked status rows each led by a small warm-orange dot: 'Editing 4 files', 'Running tests', and a bold final row '6 passed', conveying it runs and fixes itself.",
  "resume":"a card titled 'Resume' showing a short list of three past session rows with the top one highlighted warm orange and labelled 'restored', plus a caption 'pick up with full context'.",
  "proof":"a clean result card titled 'One ask' with a top line 'add rate limiting and test it', then three outcome rows each with a small warm-orange check: 'built', 'tested', 'opened a pull request'. No code.",
  "why":"three small rounded value cards in a horizontal row, each an icon and a short label: 'Remembers your repo', 'Plans before it codes', 'Fixes its own errors'.",
  "loop":"a recap card titled 'The loop' with three short numbered steps in warm-orange chips: 'start', 'describe it', 'review'.",
  "cta":"a chat comments panel titled 'Comments' with two faint placeholder comment rows near the top, then a highlighted input row containing the single word 'CODE' with a filled warm-orange 'Post' button to its right.",
 },
 "projects":{
  "pain":"a chat panel titled 'Every new chat' showing three faint grey repeated lines 'pasting your ICP', 'pasting your pricing', 'pasting your voice', conveying tedious re-explaining.",
  "setonce":"a project panel titled 'GTM Co-pilot' with a 'Custom instructions' block of two short lines and a small warm-orange 'saved' chip in the corner.",
  "knowledge":"a project panel titled 'Knowledge' with four file chips in a grid, each a small document icon and a name: 'brand voice', 'ICP', 'pricing', 'past wins'.",
  "activity":"a panel titled 'Recent activity' with three rows, each a task on the left and a timestamp on the right: 'Cold email   now', 'Pricing rewrite   yesterday', 'Q3 sequence   2h ago'.",
  "three":"three stacked rounded cards, each an icon plus a label: 'Your rules', 'Your docs', 'Your context', with a small warm-orange dot on each.",
  "beforeafter":"a two-column split panel: the LEFT column header 'Plain chat' with a grey speech bubble 'who is this for?'; the RIGHT column header 'In the Project' with a warm-orange speech bubble 'on-brand, first try' and a small check.",
  "name":"a single highlighted project-title input field reading 'GTM Co-pilot' with a small caption beneath 'name it after the job, not the tool'.",
  "everywhere":"a panel titled 'Same context, every output' with three rounded output chips in a row, each with a small warm-orange check: 'Posts', 'Pricing page', 'Teardown'.",
  "cta":"a chat comments panel titled 'Comments' with two faint placeholder comment rows near the top, then a highlighted input row containing the single word 'PROJECTS' with a filled warm-orange 'Post' button to its right.",
 },
 "skills":{
  "stats":"a stat strip with four cells in a row, each a big warm-orange number over a small label: '71 skills', '8 categories', '7 agents', '3 tiers'.",
  "cortex":"a roster card with a circular agent node icon and the name 'CORTEX', a small command chip '/cortex', and three skill rows each with a warm-orange dot: 'Competitive analysis', 'Company deep dive', 'Funding signals'.",
  "specter":"a roster card with a circular agent node icon and the name 'SPECTER', a command chip '/specter', and three skill rows: 'Find buyers', 'Cold email', 'Lead scoring'.",
  "striker":"a roster card with a circular agent node icon and the name 'STRIKER', a command chip '/striker', and three skill rows: 'Objection handler', 'Pre-call research', 'Follow-up'.",
  "pulse":"a roster card with a circular agent node icon and the name 'PULSE', a command chip '/pulse', and three skill rows: 'LinkedIn post', 'Content hooks', 'Repurpose'.",
  "sentinel":"a roster card with a circular agent node icon and the name 'SENTINEL', a command chip '/sentinel', and three skill rows: 'Build a web app', 'Clone a site', 'Website audit'.",
  "amplify":"two stacked roster cards: the top one named 'AMPLIFY' with chip '/amplify' and rows 'Campaigns', 'Audiences', 'Ad copy'; the bottom one named 'COUNSEL' with chip '/counsel' and rows 'Contract draft', 'Review', 'Clauses'.",
  "how":"a four-step vertical flow spine, each step a small rounded node with a warm-orange connector: 'Ask', 'Router picks the skill', 'Runs it', 'You approve', and a small three-card tier row at the bottom 'Lite', 'Smart', 'Deep' (Smart highlighted).",
  "cta":"a chat comments panel titled 'Comments' with two faint placeholder comment rows near the top, then a highlighted input row containing the single word 'SKILLS' with a filled warm-orange 'Post' button to its right.",
 },
 "chat":{
  "onebox":"a chat composer mockup with a greeting line, an 'ask anything' input bar, three small suggestion chips, and a small tier toggle on the right, conveying one box for everything.",
  "slash":"a chat composer with a slash-command autocomplete menu of four rows '/cortex', '/specter', '/striker', '/pulse' (the second highlighted warm orange) above an input.",
  "tier":"a segmented control tier picker with three segments 'Lite', 'Smart', 'Deep' (the 'Deep' segment filled warm orange) and a small three-column legend of model names beneath.",
  "memory":"a stack of five memory-layer rows, each a small warm-orange dot and a label: 'instructions', 'business profile', 'integrations', 'top memories', 'today', with the fourth row highlighted.",
  "upload":"a file panel titled 'Files' with three rows, each a file icon, a name and a small warm-orange 'cached' check: 'pitch deck', 'ICP list', 'sales call', and an 'Upload' button.",
  "background":"a job card with a warm-orange progress donut showing '71%' on the left and three status rows on the right: 'scrape sites  done', 'score the list  running', 'waiting  your approval'.",
  "fork":"a simple branching diagram: one session node on the left connected by warm-orange lines to two cards on the right, 'keep' and 'fork', conveying a thread splitting in two.",
  "share":"a panel with a rounded 'Read-only link' pill at the top and below it a small grid of square proof tiles (one highlighted warm orange), conveying that the link sends the whole session, not one screenshot.",
  "cta":"a chat comments panel titled 'Comments' with two faint placeholder comment rows near the top, then a highlighted input row containing the single word 'CHAT' with a filled warm-orange 'Post' button to its right.",
 },
}
def gen(prompt,out):
    body={"contents":[{"role":"user","parts":[{"inlineData":{"mimeType":"image/png","data":SEED}},{"text":prompt}]}],
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
mats=sys.argv[1:] if len(sys.argv)>1 else list(MATS)
for m in mats:
    OUT=f"{TE}/roll3/models_{m}"; os.makedirs(OUT,exist_ok=True)
    for k,pr in MATS[m].items():
        o=f"{OUT}/{k}.png"
        if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",m,k); continue
        print(m,k,"OK" if gen(MBASE+pr+MTAIL,o) else "FAIL"); time.sleep(6)
print("BATCH DONE")
