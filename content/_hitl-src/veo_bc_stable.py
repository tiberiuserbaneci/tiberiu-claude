#!/usr/bin/env python3
# Regenerate veoB (code) + veoC (DONE) with TEXT-STABLE camera (slow push-in / gentle hold).
# Root cause of earlier drift: camera MOVED and revealed new areas -> Veo hallucinated garbled text.
# A near-static push-in keeps text put. Resilient polling.
import json, base64, time, requests, sys
SP="/home/user/tiberiu-claude/scratchpad"; CA="/root/.ccr/ca-bundle.crt"
P="project-c28b1276-8b53-430a-a7a"; LOC="us-central1"; MODEL="veo-3.0-fast-generate-001"
BASE=f"https://{LOC}-aiplatform.googleapis.com/v1/projects/{P}/locations/{LOC}/publishers/google/models/{MODEL}"
info=json.load(open(f"{SP}/adc.json"))
def token(): return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
SHOTS={
 "veoB":("shotB.png","Extreme slow dolly-in on a light code editor window (that's where the camera is). "
   "The Python code stays perfectly still and fully readable, nothing scrolls; a single soft cursor "
   "blinks at the end of the last line; a gentle warm side window light drifts. Cream Claude palette, "
   "shallow depth, premium film grain, calm, quiet room tone no music. "
   "Negative: no scrolling, no new lines, no changing or duplicated or warped text, no watermark, no subtitles."),
 "veoC":("shotC.png","Extreme slow push-in, centered, on a completion screen (that's where the camera is). "
   "The coral circular check mark gently pulses with a soft glow; the word DONE holds perfectly still; "
   "nothing else moves. Cream Claude palette, soft even top light, premium film grain, calm, quiet a soft "
   "single confirmation tone no music. "
   "Negative: no changing or duplicated or warped text, no new objects, no watermark, no subtitles."),
}
def post(url,body):
    for a in range(6):
        try: return requests.post(url,headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json=body,verify=CA,timeout=120)
        except Exception as e: print("net retry",a,str(e)[:70]); time.sleep(4*(a+1))
    raise RuntimeError("net dead")
def gen(name,seed,prompt):
    img=base64.b64encode(open(f"{SP}/covers/{seed}","rb").read()).decode()
    body={"instances":[{"prompt":prompt,"image":{"bytesBase64Encoded":img,"mimeType":"image/png"}}],
      "parameters":{"aspectRatio":"9:16","durationSeconds":8,"sampleCount":1}}
    r=post(f"{BASE}:predictLongRunning",body); print("start",name,r.status_code); r.raise_for_status(); op=r.json()["name"]
    for i in range(100):
        time.sleep(12)
        try: j=post(f"{BASE}:fetchPredictOperation",{"operationName":op}).json()
        except Exception as e: print("poll err continue",str(e)[:60]); continue
        if j.get("done"):
            resp=j.get("response",{}); vids=resp.get("videos") or resp.get("generatedVideos") or []
            if not vids: print("no vids",name,json.dumps(resp)[:200]); return
            v=vids[0]; data=v.get("bytesBase64Encoded") or (v.get("video") or {}).get("bytesBase64Encoded")
            if data: open(f"{SP}/covers/{name}.mp4","wb").write(base64.b64decode(data)); print("saved",name); return
            print("keys",name,list(v.keys())); return
        print("...",name,(i+1)*12,"s")
if __name__=="__main__":
    for nm,(seed,pr) in SHOTS.items(): gen(nm,seed,pr)
    print("BC DONE")
