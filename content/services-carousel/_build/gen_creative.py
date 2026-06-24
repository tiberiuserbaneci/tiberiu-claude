import os,json,base64,time,requests
TOK=open("gcp_token.txt").read().strip(); P="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
logo=base64.b64encode(open("ultron-logo.png","rb").read()).decode()
BRAND=("Brand: Ultron, an AI operator that runs a founder's services for them. Premium Cinema-4D 3D editorial style. "
 "Warm cream background hex f3ebdf, vivid orange hex e8542b accents, deep near-black bold DM Sans headlines, soft studio lighting, shallow depth of field, glossy 3D objects. "
 "The LAST reference image is the Ultron orb: render it exactly, a glossy dark 3D sphere with a vivid electric-blue glow on one edge and a warm orange glow on the opposite edge. "
 "Vertical 4:5 social poster, generous clean negative space, no watermark text. ")
FREEDOM=("You have FULL creative freedom over the layout and graphics. Do NOT use a plain table, list, or rows of cards. "
 "Design a striking, dynamic, scroll-stopping composition that could later be animated. Make every element intentional and premium. ")
OPTS={
 "A":(BRAND+FREEDOM+"Concept: Ultron automatically chases every overdue invoice and collects the money for the founder, but waits for a yes before charging any late fee. "
      "Express this with a bold 3D scene or metaphor of invoices or payments being pulled in and resolved by Ultron. Headline: 'Ultron chases every overdue invoice.' Keep it clean and cinematic."),
 "B":(BRAND+FREEDOM+"Concept: the founder asks once and Ultron runs the whole collections service. "
      "Make the Ultron orb the hero with a confident bold-typography editorial layout and a few floating 3D payment or invoice objects. Headline: 'You ask once. Ultron collects.' Premium, minimal, high-contrast."),
}
def gen(prompt,out):
    parts=[{"inlineData":{"mimeType":"image/png","data":logo}},{"text":prompt}]
    body={"contents":[{"role":"user","parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for a in range(5):
        r=requests.post(URL,headers={"authorization":f"Bearer {TOK}","content-type":"application/json"},data=json.dumps(body),verify=CA,timeout=180)
        if r.status_code==200:
            j=r.json();img=next((p for p in j.get("candidates",[{}])[0].get("content",{}).get("parts",[]) if "inlineData" in p),None)
            if img: open(out,"wb").write(base64.b64decode(img["inlineData"]["data"])); return True
            print("  no image",j.get("candidates",[{}])[0].get("finishReason"))
        else: print("  HTTP",r.status_code,r.text[:140])
        time.sleep(8*(a+1))
    return False
for k,p in OPTS.items():
    o=f"out/creative-{k}.png"
    if os.path.exists(o) and os.path.getsize(o)>10000: print("skip",k); continue
    print(k,"OK" if gen(p,o) else "FAIL", os.path.getsize(o) if os.path.exists(o) else 0); time.sleep(4)
print("DONE")
