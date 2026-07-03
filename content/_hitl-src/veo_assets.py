#!/usr/bin/env python3
# Generate the 3D assets to INJECT into the Veo seed (operator: inject Claude 3D logo + Fable 5 logo
# from Vertex; I inject code + output; Veo only animates). Vertex gemini image, cream bg to composite.
import os,json,base64,time,requests
SP="/home/user/tiberiu-claude/scratchpad"; CA="/root/.ccr/ca-bundle.crt"
P="project-c28b1276-8b53-430a-a7a"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
def token(): return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]

JOBS={
 "claude3d":("A premium 3D render of the Claude logo: a radial starburst / sunburst mark made of "
   "rounded tapered rays bursting from a centre, sculpted in soft matte-and-glossy COPPER-CORAL "
   "(#D97757) with subtle warm studio lighting and soft shadow. Centred, floating, on a PLAIN FLAT "
   "warm cream background (#F5F3EE). Clean, elegant, no text, no other objects. Square 1:1."),
 "fable5":("A premium 3D render of the wordmark 'Fable 5' in bold elegant sans-serif 3D lettering, "
   "sculpted in charcoal ink with a soft coral (#D97757) edge light, subtle depth and soft shadow, "
   "centred on a PLAIN FLAT warm cream background (#F5F3EE). Crisp, correctly spelled 'Fable 5', "
   "premium, nothing else. Wide 16:9."),
}
def gen(name,prompt,ar):
    body={"contents":[{"role":"user","parts":[{"text":prompt}]}],
      "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":ar,"imageSize":"2K"}}}
    for att in range(6):
        try:
            r=requests.post(URL,headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json=body,verify=CA,timeout=300)
            if r.status_code==429: print("429",name,att); time.sleep(20*(att+1)); continue
            r.raise_for_status(); c=(r.json().get("candidates") or [])
            for p2 in ((c[0].get("content") or {}).get("parts") or []):
                if "inlineData" in p2:
                    open(f"{SP}/covers/{name}.png","wb").write(base64.b64decode(p2["inlineData"]["data"])); print("OK",name); return True
            print("empty",name,att); time.sleep(6)
        except Exception as e: print("err",name,att,str(e)[:120]); time.sleep(6)
    return False
if __name__=="__main__":
    gen("claude3d",JOBS["claude3d"],"1:1"); gen("fable5",JOBS["fable5"],"16:9")
