#!/usr/bin/env python3
# SOLO STACK premium Vertex panels (operator 2026-07-02): 8 distinct-structure panels,
# SAME orthographic front view + material system, per analysis/vertex-3d-prompting.md.
import os,json,base64,time,requests,sys
SP="/home/user/tiberiu-claude/scratchpad"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
OUT="/home/user/tiberiu-claude/content/_hitl-src/models_prem/solostack"
os.makedirs(OUT,exist_ok=True)
info=json.load(open(f"{SP}/adc.json"))
def token():
    return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
SEED=b64("/home/user/tiberiu-claude/content/_hitl-src/models_agentsprod/gate.png")

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
 "clean sans-serif labels, no garbled text. CRITICAL: do NOT render any hex code or colour code as visible text; no raw code, "
 "no snake_case, no prices, no dollar amounts. "
 "NO eyebrow/headline/title/footer/page number outside the panel - ONLY the panel. The panel shows ")
MTAIL=" The whole panel is exactly this, centred, front-on. No other panels. No code, no hex text."

PANELS={
 "apollo":"a lead list table: a slim header strip titled 'Leads', then three list rows, each with a small round avatar dot on the left, a name in clean sans-serif ('Sarah Lin', 'Marco Diaz', 'Priya Rao') and a rounded warm-orange score chip on the right reading '94', '88', '81'.",
 "gmail_sent":"an email outbox: a header strip titled 'Outbox' with a small paper-plane icon, then three message rows, each a short subject ('Acme intro', 'Globex pricing', 'Northwind') with a small warm-orange 'Sent' chip carrying a tiny check on the right.",
 "hubspot":"a sales pipeline board: three upright columns side by side labelled 'Qualified', 'Proposal', 'Won', each column holding one rounded deal card with a faint company row; the card in the 'Won' column is filled warm orange with a small white check.",
 "designer":"a brand board titled 'On brand': a row of three large rounded colour swatch tiles (terracotta, warm sand, soft cream), and beneath them a neat row of four small outlined chips labelled 'hero', 'pricing', 'FAQ', 'CTA'.",
 "developer":"a dark deploy console: a title strip reading 'Deploy', three short status rows each led by a small warm-orange dot reading 'building', 'tests passed', 'live', and a large round warm-orange button with a white check in the lower right corner of the panel.",
 "bill":"a cost comparison: two stacked full-width rounded rows inside the panel; the top row muted grey labelled 'Five tools' with a small grey cross icon; the bottom row filled warm orange, slightly taller, labelled 'One chat' with a small white check icon.",
 "gate":"an approvals queue titled 'The gate': one parked task row reading 'Send 240 emails' with a small padlock icon, and beneath it two side-by-side buttons: a filled warm-orange 'Approve' button and an outlined 'Hold' button.",
 "ultron_real":"a chat composer: a short assistant message row with a small round dot avatar near the top, and a large rounded input bar reading 'run it solo' with a circular filled warm-orange send button holding a white arrow on its right end.",
}

def gen(stem,desc):
    body={"contents":[{"role":"user","parts":[
        {"inlineData":{"mimeType":"image/png","data":SEED}},
        {"text":MBASE+desc+MTAIL}]}],
      "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for att in range(7):
        try:
            r=requests.post(URL,headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json=body,verify=CA,timeout=300)
            if r.status_code==429: time.sleep(20*(att+1)); continue
            r.raise_for_status()
            out=r.json()
            cands=out.get("candidates") or []
            parts=(cands[0].get("content") or {}).get("parts") if cands else None
            img=None
            for p2 in (parts or []):
                if "inlineData" in p2: img=p2["inlineData"]["data"]
            if not img:
                print(stem,"empty, retry",att); time.sleep(8); continue
            open(f"{OUT}/{stem}.png","wb").write(base64.b64decode(img))
            print("OK",stem); return True
        except Exception as e:
            print(stem,"err",e); time.sleep(10)
    print("FAIL",stem); return False

if __name__=="__main__":
    stems=sys.argv[1:] or list(PANELS)
    for s in stems: gen(s,PANELS[s])
    print("done")
