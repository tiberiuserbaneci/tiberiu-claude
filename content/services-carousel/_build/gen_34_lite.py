import os,json,base64,time,requests
TOK=open("gcp_token.txt").read().strip(); P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
COMMON=("Reproduce the reference image's exact design, same app icons, identical headline text, identical orange '51ultron.com' footer, same palette, lighting and background. "
 "Keep headline text and footer pixel-identical. Animate the scene PROMINENTLY for this frame (clearly visible movement): the glossy 3D app icons float and bob with a warm-orange glow pulse (stay recognizable). ")
SL={
 3:("out/final-3.png","the document pages, the price-quote card and the signature piece",
    ["the proposal pieces scattered wide and far apart around the empty central document slot, icons low",
     "the pieces clearly converging inward, the central proposal document half-assembled, icons floating high with a glow",
     "all pieces snapped together into the finished central proposal document, icons settling"]),
 4:("out/final-4.png","the support-ticket cards and chat-message bubbles",
    ["a tall full stack of ticket and chat cards at the top, none cleared, inbox tray full, icons low",
     "about half the cards cleared with bright green checkmarks, the stack visibly shorter, icons floating high with a glow",
     "all cards cleared with green checks, the inbox tray empty and clean, icons settling"]),
}
def gen(seed,prompt,out):
    parts=[{"inlineData":{"mimeType":"image/png","data":seed}},{"text":prompt}]
    body={"contents":[{"role":"user","parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"1K"}}}
    for a in range(6):
        r=requests.post(URL,headers={"authorization":f"Bearer {TOK}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print("  no image",j.get("candidates",[{}])[0].get("finishReason"))
        else:
            print("  HTTP",r.status_code);
            if r.status_code==401: return False
        time.sleep(20*(a+1) if r.status_code==429 else 6)
    return False
for n,(seedp,obj,arc) in SL.items():
    seed=base64.b64encode(open(seedp,"rb").read()).decode()
    d=f"mf{n}b"; os.makedirs(d,exist_ok=True)
    for i,pos in enumerate(arc):
        o=f"{d}/f{i+1}.png"
        if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",n,i+1); continue
        pr=COMMON+f"Also the {obj} travel a long, clearly visible distance. In this frame: {pos}."
        print(n,i+1,"OK" if gen(seed,pr,o) else "FAIL"); time.sleep(22)
print("DONE")
