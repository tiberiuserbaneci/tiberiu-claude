#!/usr/bin/env python3
# Veo image-to-video on the 3 shot-seeds (multi-shot cut). One camera move each + "(that's where the
# camera is)" trick. Veo animates the injected seed (real logo, real code, DONE). Veo 3 Fast (cost).
import json, base64, time, requests, sys
SP="/home/user/tiberiu-claude/scratchpad"; CA="/root/.ccr/ca-bundle.crt"
P="project-c28b1276-8b53-430a-a7a"; LOC="us-central1"; MODEL="veo-3.0-fast-generate-001"
BASE=f"https://{LOC}-aiplatform.googleapis.com/v1/projects/{P}/locations/{LOC}/publishers/google/models/{MODEL}"
info=json.load(open(f"{SP}/adc.json"))
def token(): return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]
SHOTS={
 "veoA":("shotA.png","Slow cinematic dolly-in toward the Claude logo at the centre (that's where the "
   "camera is). The coral 3D Claude starburst gently rotates and blooms while a warm rim light drifts "
   "across it; the 'Fable 5' wordmark settles. Cream Claude palette, soft film grain, premium, calm. "
   "No new objects, do not change the text or logo."),
 "veoB":("shotB.png","Slow smooth pan across the code editor (that's where the camera is). The code "
   "reads in line by line with a soft blinking cursor and a gentle side window light drifting. Cream "
   "Claude palette, film grain, premium. Keep the code and layout exact, no warping, no new text."),
 "veoC":("shotC.png","Slow crane-down over the completion screen (that's where the camera is). The "
   "coral check settles with a soft glow pulse and 'DONE' holds steady. Cream Claude palette, soft top "
   "light, film grain, premium, calm. No new objects, keep the text exact."),
}
def gen(name,seed,prompt):
    img=base64.b64encode(open(f"{SP}/covers/{seed}","rb").read()).decode()
    body={"instances":[{"prompt":prompt,"image":{"bytesBase64Encoded":img,"mimeType":"image/png"}}],
      "parameters":{"aspectRatio":"9:16","durationSeconds":8,"sampleCount":1}}
    r=requests.post(f"{BASE}:predictLongRunning",headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json=body,verify=CA,timeout=120)
    print("start",name,r.status_code,r.text[:120]); r.raise_for_status(); op=r.json()["name"]
    for i in range(90):
        time.sleep(12)
        pr=requests.post(f"{BASE}:fetchPredictOperation",headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json={"operationName":op},verify=CA,timeout=120); j=pr.json()
        if j.get("done"):
            resp=j.get("response",{}); vids=resp.get("videos") or resp.get("generatedVideos") or []
            if not vids: print("no vids",name,json.dumps(resp)[:300]); return False
            v=vids[0]; data=v.get("bytesBase64Encoded") or (v.get("video") or {}).get("bytesBase64Encoded")
            if data: open(f"{SP}/covers/{name}.mp4","wb").write(base64.b64decode(data)); print("saved",name); return True
            print("keys",name,list(v.keys())); return False
        print("...",name,(i+1)*12,"s")
    return False
if __name__=="__main__":
    for nm,(seed,pr) in SHOTS.items(): gen(nm,seed,pr)
    print("ALL DONE")
