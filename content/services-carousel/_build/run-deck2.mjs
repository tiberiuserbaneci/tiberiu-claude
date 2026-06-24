import fs from 'node:fs';
let TOKEN = fs.readFileSync(process.env.TOKENFILE,'utf8').trim();
const PROJECT = process.env.PROJECT;
const MODEL='gemini-3-pro-image-preview';
const URL=`https://aiplatform.googleapis.com/v1/projects/${PROJECT}/locations/global/publishers/google/models/${MODEL}:generateContent`;
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const LOGOREF='ultron-logo.png';
const STYLE='Premium 3D rendered vertical social slide. Clean warm cream background hex f3ebdf with lots of empty space. Only a few glossy 3D Claude sunburst logos (a clean white many-rayed sunburst on a glossy coral-orange tile), softly out of focus, placed in the corners and along the edges only, never behind the text. The center stays clean and uncluttered so every word is easy to read. Soft studio lighting, shallow depth of field, high-end Cinema 4D editorial style. Near-black bold sans serif typography with selected words in vibrant orange hex e8542b, high contrast and perfectly legible. Calm, minimal, premium, not busy. No clutter behind the text. No watermark text anywhere. ';
const LOGO='The LAST reference image is the real Ultron logo: render every Ultron orb to match it exactly, a glossy three dimensional dark sphere with a vivid electric-blue glow along one edge and a warm orange glow along the opposite edge, deep near-black center, glossy and dimensional, never flat and never orange-only. ';
const FORMATS=[['4:5','45']];
const outDir='out'; fs.mkdirSync(outDir,{recursive:true});
async function gen(content,out,styleRef,ar){
  const parts=[];
  if(styleRef) parts.push({inlineData:{mimeType:'image/png',data:fs.readFileSync(styleRef).toString('base64')}});
  parts.push({inlineData:{mimeType:'image/png',data:fs.readFileSync(LOGOREF).toString('base64')}});
  const match=styleRef?'Match the exact cream premium visual style, palette and lighting of the FIRST reference image (the cover), with new layout and content as described. ':'';
  parts.push({text: match+LOGO+STYLE+content});
  const body={contents:[{role:'user',parts}],generationConfig:{responseModalities:['IMAGE'],imageConfig:{aspectRatio:ar,imageSize:'2K'}}};
  for(let a=1;a<=6;a++){
    const r=await fetch(URL,{method:'POST',headers:{authorization:`Bearer ${TOKEN}`,'content-type':'application/json'},body:JSON.stringify(body)});
    if(r.status===401){console.log('  401 token expired');process.exit(2);}
    const j=await r.json().catch(()=>({}));
    if(r.ok){const img=(j.candidates?.[0]?.content?.parts||[]).find(p=>p.inlineData);if(img){fs.writeFileSync(out,Buffer.from(img.inlineData.data,'base64'));return true;}console.log('  no image',j.candidates?.[0]?.finishReason);}
    else{console.log('  HTTP',r.status,JSON.stringify(j.error?.message||j).slice(0,90));if(r.status===429||r.status>=500)await sleep(15000*a);}
  }
  return false;
}
const deck=JSON.parse(fs.readFileSync(process.env.DECK||'decks/toolengine.json','utf8'));
for(const [ar,suf] of FORMATS){
  const prefix=`${outDir}/${deck.prefix}-${suf}`;
  const cover=`${prefix}-1.png`;
  if(!fs.existsSync(cover)){console.log(`${deck.prefix} ${suf} cover`); await gen(deck.slides[0],cover,null,ar); await sleep(8000);}
  for(let i=1;i<deck.slides.length;i++){const out=`${prefix}-${i+1}.png`;if(fs.existsSync(out))continue;console.log(`${deck.prefix} ${suf} slide ${i+1}`);const ok=await gen(deck.slides[i],out,cover,ar);console.log('   ',ok?'OK':'FAIL',out);await sleep(8000);}
}
console.log('BATCH DONE');
