import os,json,base64,time,requests
TOK=open("gcp_token.txt").read().strip(); P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
COMMON=("Reproduce the reference image's exact design, the same app icons, identical headline text, identical orange '51ultron.com' footer, same palette, lighting and background. "
 "Keep the headline text and footer pixel-identical. Animate the scene PROMINENTLY and boldly for this frame (the movement between frames should be clearly visible, not subtle): the glossy 3D app icons clearly FLOAT and bob with a noticeable warm-orange glow pulse while staying recognizable in their arrangement. ")
SL={
 2:("out/final-2.png","invoice papers and gold coins",
    ["the invoices and coins gathered at the far OUTER ends of the orange flow lines, icons low",
     "the invoices and coins moved a third of the way inward along the lines, icons floating up",
     "the invoices and coins now halfway in, clearly travelling, icons high with a glow",
     "the invoices and coins most of the way to the center, icons bobbing",
     "the invoices and coins arriving and being collected at the center, icons settling"]),
 3:("out/final-3.png","the document pages, the price-quote card and the signature piece",
    ["the proposal pieces scattered wide and far apart around the central document slot, icons low",
     "the pieces clearly moving inward toward the central document, icons floating up",
     "the pieces converging closer, the central document half-assembled, icons high glow",
     "the pieces almost snapped into place, document nearly complete, icons bobbing",
     "all pieces assembled into the finished central proposal document, icons settling"]),
 4:("out/final-4.png","the support-ticket cards and chat-message bubbles",
    ["a tall stack of ticket and chat cards at the TOP of the queue, none cleared yet, icons low",
     "the top cards moving down with the first green checkmarks appearing, icons floating up",
     "about half the cards cleared with green checks, the stack visibly shorter, icons high glow",
     "most cards cleared, only a couple left, inbox tray nearly empty, icons bobbing",
     "all cards cleared with green checks, the inbox tray empty and clean, icons settling"]),
}
def gen(seed_b64,prompt,out):
    parts=[{"inlineData":{"mimeType":"image/png","data":seed_b64}},{"text":prompt}]
    body={"contents":[{"role":"user","parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"1K"}}}
    for a in range(5):
        r=requests.post(URL,headers={"authorization":f"Bearer {TOK}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print("  no image",j.get("candidates",[{}])[0].get("finishReason"))
        else: print("  HTTP",r.status_code,r.text[:120])
        time.sleep(8*(a+1))
    return False
for n,(seedp,obj,arc) in SL.items():
    seed=base64.b64encode(open(seedp,"rb").read()).decode()
    d=f"mf{n}"; os.makedirs(d,exist_ok=True)
    for i,pos in enumerate(arc):
        o=f"{d}/f{i+1}.png"
        if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",n,i+1); continue
        pr=COMMON+f"Also the {obj} travel a LONG, clearly visible distance along their path. In this frame: {pos}."
        print(n,i+1,"OK" if gen(seed,pr,o) else "FAIL"); time.sleep(12)
print("DONE")
