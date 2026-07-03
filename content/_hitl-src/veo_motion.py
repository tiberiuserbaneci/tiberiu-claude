#!/usr/bin/env python3
# Veo 3 Fast test: animate the Vertex eye (image-to-video) -> IG reel intro motion.
import json, base64, time, requests
SP="/home/user/tiberiu-claude/scratchpad"; CA="/root/.ccr/ca-bundle.crt"
P="project-c28b1276-8b53-430a-a7a"; LOC="us-central1"; MODEL="veo-3.0-generate-001"
BASE=f"https://{LOC}-aiplatform.googleapis.com/v1/projects/{P}/locations/{LOC}/publishers/google/models/{MODEL}"
info=json.load(open(f"{SP}/adc.json"))
def token(): return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]

PROMPT=("The amber eye-orb slowly comes alive inside its dark glass sphere: the iris subtly "
 "contracts and dilates, a single thin horizontal scan-line of warm light sweeps across it once, "
 "faint concentric energy rings pulse gently outward, soft volumetric glow breathing. "
 "Cinematic photoreal, very slow subtle motion, camera holds perfectly still, background stays "
 "deep black, warm copper-and-charcoal palette. No text, no logos.")

def main():
    tok=token()
    img=base64.b64encode(open(f"{SP}/covers/vertex_raw.png","rb").read()).decode()
    body={"instances":[{"prompt":PROMPT,"image":{"bytesBase64Encoded":img,"mimeType":"image/png"}}],
          "parameters":{"aspectRatio":"9:16","durationSeconds":8,"sampleCount":1}}
    r=requests.post(f"{BASE}:predictLongRunning",headers={"Authorization":f"Bearer {tok}","Content-Type":"application/json"},json=body,verify=CA,timeout=120)
    print("start",r.status_code, r.text[:300])
    r.raise_for_status()
    op=r.json()["name"]; print("op",op)
    for i in range(60):
        time.sleep(12)
        tok=token()
        pr=requests.post(f"{BASE}:fetchPredictOperation",headers={"Authorization":f"Bearer {tok}","Content-Type":"application/json"},json={"operationName":op},verify=CA,timeout=120)
        j=pr.json()
        if j.get("done"):
            print("DONE after",(i+1)*12,"s")
            resp=j.get("response",{})
            vids=resp.get("videos") or resp.get("generatedVideos") or []
            if not vids:
                print("no videos in response:", json.dumps(resp)[:600]); return
            v=vids[0]
            data=v.get("bytesBase64Encoded") or (v.get("video") or {}).get("bytesBase64Encoded")
            if data:
                open(f"{SP}/covers/eye_motion_v3.mp4","wb").write(base64.b64decode(data)); print("saved eye_motion.mp4")
            else:
                print("video keys:", list(v.keys()), "gcs?", v.get("gcsUri"))
            return
        print("...polling",(i+1)*12,"s", j.get("metadata",{}).get("state",""))
    print("timed out")

if __name__=="__main__": main()
