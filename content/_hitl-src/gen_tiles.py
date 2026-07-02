#!/usr/bin/env python3
# CONGRUENT brand-tile library (operator 2026-07-02: "logo-uri autentice... genereaza-le in
# vertex pentru congruenta sa fie toate egale, la aceeasi forma, context, volum").
# ONE seed tile -> every brand tile identical in shape/volume/lighting. 4:5, 2K.
import os,json,base64,time,requests,sys
SP="/home/user/tiberiu-claude/scratchpad"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
OUT="/home/user/tiberiu-claude/content/_hitl-src/tiles"
os.makedirs(OUT,exist_ok=True)
info=json.load(open(f"{SP}/adc.json"))
def token():
    return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
# seed: the clean 6-tile row (approved look: soft 3D keycap tiles, front-on)
SEED=b64("/home/user/tiberiu-claude/content/_hitl-src/covers/tabsrow_clean.png")

BASE=("A HIGH-FIDELITY 3D PRODUCT RENDER of EXACTLY ONE mobile app icon tile, matching the reference tiles: "
 "a rounded-square soft-plastic 3D keycap with beveled edges and visible thickness, viewed STRAIGHT-ON, "
 "perfectly front-facing and centred, soft studio lighting, a SOFT CONTACT SHADOW directly beneath it. "
 "The tile fills about 55% of the frame width, on a COMPLETELY FLAT #191919 dark charcoal background, "
 "with generous empty margin on all four sides; the tile is WHOLE - all four corners and edges fully visible. "
 "The tile shows ONLY the AUTHENTIC, ACCURATE official logo of ")
TAIL=(" - the real brand mark, correct shape and official brand colours, crisp and exact, nothing else on the tile. "
 "No text anywhere. No second tile. No extra icons. One tile only.")

TILES={
 "linkedin":"LinkedIn (the white 'in' letters on the official blue rounded square)",
 "gmail":"Gmail (the red-blue-green-yellow M envelope on white)",
 "hubspot":"HubSpot (the orange sprocket symbol on white)",
 "figma":"Figma (the five-part multicolour geometric F mark on black)",
 "github":"GitHub (the white Octocat silhouette in a circle on black)",
 "stripe":"Stripe (the white S word-symbol on the official blurple violet)",
 "slack":"Slack (the multicolour pinwheel hash mark on white)",
 "notion":"Notion (the black-and-white N page mark on white)",
 "calendly":"Calendly (the blue C calendar mark on white)",
 "buffer":"Buffer (the stacked black layers mark on white)",
 "jasper":"Jasper (the dark friendly robot-face J mark on khaki)",
 "zapier":"Zapier (the white asterisk on the official orange)",
}

def gen(stem,desc):
    body={"contents":[{"role":"user","parts":[
        {"inlineData":{"mimeType":"image/png","data":SEED}},
        {"text":BASE+desc+TAIL}]}],
      "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"1:1","imageSize":"1K"}}}
    for att in range(7):
        try:
            r=requests.post(URL,headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json=body,verify=CA,timeout=300)
            if r.status_code==429: time.sleep(20*(att+1)); continue
            r.raise_for_status()
            out=r.json(); cands=out.get("candidates") or []
            parts=(cands[0].get("content") or {}).get("parts") if cands else None
            img=None
            for p2 in (parts or []):
                if "inlineData" in p2: img=p2["inlineData"]["data"]
            if not img: print(stem,"empty retry",att); time.sleep(8); continue
            open(f"{OUT}/{stem}.png","wb").write(base64.b64decode(img))
            print("OK",stem); return True
        except Exception as e:
            print(stem,"err",e); time.sleep(10)
    print("FAIL",stem); return False

if __name__=="__main__":
    stems=sys.argv[1:] or list(TILES)
    for s in stems: gen(s,TILES[s])
    print("done")
