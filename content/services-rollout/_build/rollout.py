#!/usr/bin/env python3
# Rollout v2: TikTok REVIEW -> Ultron 5-slide carousels with DESIGN VARIETY (5 layout archetypes),
# small accent orb on the hook, complete in-frame CTA icons, footer space reserved (finalize adds it).
# Permanent ADC token (scratchpad/adc.json). Resumable + paced. Run: python3 rollout.py [--dry]
import os,sys,json,base64,time,glob
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"
P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
DRY="--dry" in sys.argv
MAN=json.load(open(f"{TE}/rollout_manifest.json"))["items"]
import requests as rq
def get_token():
    adc=f"{SP}/adc.json"
    if os.path.exists(adc):
        info=json.load(open(adc))
        r=rq.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30)
        return r.json()["access_token"]
    return open(f"{TE}/gcp_token.txt").read().strip()
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
STYLE=("Match the premium Cinema-4D 3D editorial STYLE, warm cream hex f3ebdf background, glossy 3D objects, soft studio lighting, "
 "and the deep near-black bold DM Sans headline with selected words in vivid orange hex e8542b, of the reference image. "
 "Vertical 4:5, generous clean negative space, no watermark text. Leave clear empty space at the very bottom for a footer. ")
# layout archetype per item (neighbors differ -> design variety)
ARCH={"tool-stack":"flow","one-chat":"flow","jobs":"flow","routing":"flow",
 "tools-catalog":"grid","personas-roster":"grid","team":"grid","skills":"grid","workforce":"grid","chat-habits":"grid",
 "turn-loop":"hero","sessions":"hero","computer":"hero","brain":"hero","builder":"hero","weekend-engine":"hero","claude-code-start":"hero",
 "projects":"split","agents-prod":"split","proof-shared":"split",
 "ai-native-index":"data","realnumbers-stack":"data"}
ARCHC={
 "flow":["the scattered, by-hand reality with app icons and 3D objects strewn messily (the before)",
         "Ultron running it: the same app icons connected by clean glowing warm-orange flow lines, organized and in motion (the mechanism)",
         "one clean unified result gathered in a single workspace (the outcome)"],
 "grid":["a couple of loose disconnected tiles drifting (the before)",
         "a clean structured GRID or MATRIX of labeled glossy 3D tiles showing the full system, evenly arranged (the mechanism)",
         "the grid working as one with a single clear highlighted result (the outcome)"],
 "hero":["a single 3D object that embodies the problem, slightly off-balance (the before)",
         "a bold cinematic 3D HERO scene of Ultron performing the job, one dominant focal object (the mechanism)",
         "the finished result as one clean confident 3D object centered (the outcome)"],
 "split":["a clear SPLIT composition with the messy manual before on the LEFT half",
          "the same split, now the clean Ultron after on the RIGHT half with app icons (the mechanism)",
          "the transformation resolved into one clean outcome filling the frame"],
 "data":["a cluttered scatter of raw numbers and tiny charts (the before)",
         "a clean premium 3D CHART or funnel with the real headline numbers called out (the proof)",
         "the single big headline number, bold and dominant, with a short label (the outcome)"]}
def prompts(it):
    h=it["hook"].split("/"); l1=h[0].strip(); l2=(h[1].strip() if len(h)>1 else ""); th=it["theme"]; kw=it["kw"]; arch=ARCH.get(it["slug"],"flow")
    cover=(STYLE+"This is the HOOK slide. The BOLD HEADLINE is the hero and fills the upper area. The glossy dark Ultron orb (vivid electric-blue glow one edge, warm-orange the other) appears SMALL as an accent, about one fifth of the frame, tucked in a lower corner - it must NOT dominate. A few small themed 3D objects drift nearby. "
           f"Headline: '{l1}' in near-black, then '{l2}' in vivid orange italic.")
    base="Do NOT put the Ultron orb on this slide. Use glossy 3D app-icon tiles and 3D objects. "
    cs=[STYLE+base+f"CONTENT slide {i+1} of 3, {arch.upper()} layout, a DISTINCT composition. Theme: {th}. Show {ARCHC[arch][i]}. A short bold headline." for i in range(3)]
    cta=(STYLE+"Do NOT put the orb. CTA slide, clean and balanced. A short bold near-black line with one word in vivid orange. A single bold solid orange 3D pill button reading "
         f"'COMMENT {kw}'. A COMPLETE, evenly spaced ring of small glossy 3D app icons fully INSIDE the frame with clear margin - nothing cut off at the edges.")
    return [("final-1.png",cover),("final-2.png",cs[0]),("final-2.png",cs[1]),("final-2.png",cs[2]),("final-5.png",cta)]
def gen(tok,refpng,prompt,out):
    parts=[{"inlineData":{"mimeType":"image/png","data":b64(f"{TE}/out/{refpng}")}},{"text":prompt}]
    body={"contents":[{"role":"user","parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for a in range(6):
        try:
            r=rq.post(URL,headers={"authorization":f"Bearer {tok}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        except Exception as e:
            print("   EXC",str(e)[:50]); time.sleep(10); continue
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print("   no image",j.get("candidates",[{}])[0].get("finishReason"))
        elif r.status_code in (401,403): return "AUTH"
        else: print("   HTTP",r.status_code)
        time.sleep(20*(a+1) if r.status_code==429 else 6)
    return False
if __name__=="__main__":
    if DRY:
        from collections import Counter
        print("archetype spread:",dict(Counter(ARCH.values())))
        for it in MAN[:3]:
            for i,(ref,pr) in enumerate(prompts(it)): print(it["slug"],f"s{i+1}",ARCH[it["slug"]],pr[len(STYLE):len(STYLE)+70])
        print("DRY OK"); sys.exit()
    tok=get_token(); done=0
    for it in MAN:
        d=f"{TE}/roll/{it['slug']}"; os.makedirs(d,exist_ok=True)
        if len(glob.glob(f"{d}/s*.png"))>=5: print("skip",it["slug"]); done+=1; continue
        print("ITEM",it["slug"],ARCH.get(it["slug"]))
        for i,(ref,pr) in enumerate(prompts(it)):
            o=f"{d}/s{i+1}.png"
            if os.path.exists(o) and os.path.getsize(o)>10000: continue
            r=gen(tok,ref,pr,o)
            if r=="AUTH": tok=get_token(); r=gen(tok,ref,pr,o)
            print("  ",it["slug"],f"s{i+1}",("OK" if r else "FAIL")); time.sleep(13)
        done+=1; print(f"  [{done}/{len(MAN)}] done")
    print("ROLLOUT V2 GEN DONE")
