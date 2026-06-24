import os,json,base64,time,requests,sys
TOK=open("gcp_token.txt").read().strip(); P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
styleref=base64.b64encode(open("out/creative-A.png","rb").read()).decode()
prompt=("Use the reference image ONLY for the premium cream 3D editorial STYLE, palette, lighting and typography "
 "(warm cream hex f3ebdf background, glossy Cinema-4D 3D objects with soft shadows, deep near-black bold DM Sans headline with selected words in vivid orange hex e8542b). "
 "IMPORTANT: do NOT put the Ultron orb anywhere on this slide. Vertical 4:5, generous clean negative space, no watermark text. "
 "Scene: a dynamic premium arrangement of large glossy 3D APP-ICON tiles - a green accounting app icon, a red-and-white Gmail envelope icon, a blue-and-white calendar icon, an orange CRM contact icon, a multicolor Slack icon, and a blue payment card - floating and connected by glowing warm-orange flow lines, with a couple of invoice papers and gold coins travelling along the lines, showing the apps working together to collect money. "
 "Headline near the top: 'Ultron chases every overdue invoice.' with the words 'chases every overdue invoice' in vivid orange. "
 "Include one small glossy pill chip that reads 'Waits for a YES before the late fee' with a small orange YES button and a question-mark button. Premium, dynamic, clean, scroll-stopping.")
def gen(out):
    parts=[{"inlineData":{"mimeType":"image/png","data":styleref}},{"text":prompt}]
    body={"contents":[{"role":"user","parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for a in range(5):
        r=requests.post(URL,headers={"authorization":f"Bearer {TOK}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print("  no image",j.get("candidates",[{}])[0].get("finishReason"))
        else: print("  HTTP",r.status_code,r.text[:140]); sys.exit(2) if r.status_code==401 else None
        time.sleep(8*(a+1))
    return False
print("collections-apps:","OK" if gen("out/apps-collections.png") else "FAIL")
