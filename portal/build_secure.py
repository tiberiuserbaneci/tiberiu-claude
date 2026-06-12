#!/usr/bin/env python3
"""Build the INNER (decrypted) portal viewer as one self-contained HTML string.

Read-only snapshot of the manifest: every material with an inlined thumbnail, caption / ALT /
first-comment (with copy buttons) and a download link that points at the PRIVATE repo (a second
GitHub-login gate). Output goes to a temp file; portal/encrypt_gate.js then AES-encrypts it so
nothing is readable on the host without the user + password.

Usage: python3 portal/build_secure.py /tmp/inner.html
"""
import json, sys, base64, io, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
MANIFEST = CONTENT / "portal" / "manifest.json"
REPO = "NexityNetwork/tiberiu-claude"
DL_BRANCH = "main"          # download links resolve on main (login-gated by the private repo)
THUMB_W = 300

def thumb_data_uri(preview):
    if not preview:
        return ""
    p = ROOT / preview
    if not p.is_file():
        return ""
    try:
        im = Image.open(p).convert("RGB")
        w, h = im.size
        if w > THUMB_W:
            im = im.resize((THUMB_W, round(h * THUMB_W / w)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=72, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return ""

def build():
    m = json.loads(MANIFEST.read_text())
    out = []
    for x in m.get("materials", []):
        out.append({
            "id": x["id"], "title": x.get("title", x["id"]),
            "channel": x.get("channel", ""), "type": x.get("type", "single"),
            "slides": x.get("slides", 1), "dims": x.get("dims", ""),
            "posted": bool(x.get("posted")), "date": x.get("generated_date", ""),
            "added": x.get("added", 0), "source": x.get("source", "generated"),
            "status": x.get("status", "ready"),
            "cap": x.get("caption", ""), "alt": x.get("alt", ""), "fc": x.get("first_comment", ""),
            "thumb": thumb_data_uri(x.get("preview")),
            "dl": f"https://github.com/{REPO}/raw/{DL_BRANCH}/{x.get('download','')}" if x.get("download") else "",
        })
    out.sort(key=lambda d: d.get("added", 0), reverse=True)
    counts = m.get("counts", {})
    data = {"materials": out, "counts": counts, "generated_at": m.get("generated_at", "")}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.replace("__DATA__", payload)

TEMPLATE = r"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ultron Content Portal</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{--slate:#191919;--slate2:#222221;--card:#1e1e1d;--ivory:#FAFAF7;--ink70:rgba(250,250,247,.72);--ink46:rgba(250,250,247,.46);--ink30:rgba(250,250,247,.3);--rule:rgba(250,250,247,.1);--book:#CC785C;--book-d:#C84623;--kraft:#D4A27F;--green:#7fae6b;--red:#d9685a;}
*{box-sizing:border-box;margin:0;padding:0;font-family:'DM Sans',sans-serif;}
body{background:#121211;color:var(--ivory);padding:0 0 80px;}
header{position:sticky;top:0;z-index:20;background:rgba(18,18,17,.96);backdrop-filter:blur(8px);border-bottom:1px solid var(--rule);padding:18px 30px;}
.htop{display:flex;align-items:center;gap:16px;flex-wrap:wrap;}
.logo{font-weight:900;font-size:22px;letter-spacing:-.5px;}.logo em{color:var(--book);font-style:normal;}
.sub{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink46);}
.spacer{flex:1;}
.count{font-family:'DM Mono',monospace;font-size:12px;color:var(--ink46);}
.lock{font-family:'DM Mono',monospace;font-size:11px;color:var(--book);border:1px solid var(--rule);border-radius:8px;padding:7px 12px;cursor:pointer;}
.tabs{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap;}
.tab{font-weight:700;font-size:14px;color:var(--ink46);background:transparent;border:1px solid var(--rule);border-radius:24px;padding:9px 20px;cursor:pointer;}
.tab.on{color:#1a0f0a;background:var(--book);border-color:var(--book);}
.filters{display:flex;gap:7px;margin-top:12px;flex-wrap:wrap;}
.fl{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink46);background:var(--slate2);border:1px solid var(--rule);border-radius:20px;padding:7px 14px;cursor:pointer;}
.fl.on{color:var(--book);border-color:var(--book);background:rgba(204,120,92,.1);}
main{padding:26px 30px;}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:22px;}
.card{background:var(--card);border:1px solid var(--rule);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;}
.card.posted{border-color:rgba(127,174,107,.4);}
.pv{position:relative;background:#0e0e0d;display:flex;align-items:center;justify-content:center;min-height:150px;border-bottom:1px solid var(--rule);cursor:pointer;}
.pv img{width:100%;display:block;max-height:360px;object-fit:cover;object-position:top;}
.pv .ph{color:var(--ink30);font-family:'DM Mono',monospace;font-size:11px;padding:50px;}
.badges{position:absolute;top:10px;left:10px;display:flex;gap:6px;flex-wrap:wrap;}
.bg{font-family:'DM Mono',monospace;font-size:9.5px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:5px 9px;border-radius:6px;background:rgba(0,0,0,.6);color:var(--ivory);border:1px solid var(--rule);}
.bg.ch{color:var(--book);}.bg.car{color:var(--kraft);}.bg.rev{color:var(--book-d);background:rgba(200,70,35,.18);}
.bg.post{position:absolute;top:10px;right:10px;left:auto;color:#0e1a0c;background:var(--green);}
.dimchip{position:absolute;bottom:8px;right:8px;font-family:'DM Mono',monospace;font-size:9px;color:var(--ink70);background:rgba(0,0,0,.62);border:1px solid var(--rule);border-radius:6px;padding:3px 7px;}
.body{padding:15px 16px;display:flex;flex-direction:column;gap:11px;}
.tt{font-weight:800;font-size:17px;letter-spacing:-.3px;}
.meta{font-family:'DM Mono',monospace;font-size:10.5px;color:var(--ink46);display:flex;gap:10px;flex-wrap:wrap;}
.empty{color:var(--ink46);text-align:center;padding:80px;font-family:'DM Mono',monospace;}
.lb{position:fixed;inset:0;z-index:100;background:rgba(8,8,8,.94);backdrop-filter:blur(7px);display:none;}
.lb.on{display:flex;}
.lb-inner{flex:1;display:flex;min-height:0;min-width:0;}
.lb-stage{flex:1;position:relative;display:flex;align-items:center;justify-content:center;padding:30px;min-width:0;}
.lb-stage img{max-width:100%;max-height:calc(100vh - 60px);object-fit:contain;border-radius:8px;box-shadow:0 14px 60px rgba(0,0,0,.6);}
.lb-side{width:440px;flex-shrink:0;border-left:1px solid var(--rule);background:#121211;overflow-y:auto;padding:24px;display:flex;flex-direction:column;gap:15px;}
.lb-title{font-weight:900;font-size:24px;letter-spacing:-.5px;line-height:1.15;}
.lb-id{font-family:'DM Mono',monospace;font-size:11px;color:var(--ink46);word-break:break-all;}
.lb-chips{display:flex;gap:6px;flex-wrap:wrap;}
.lb-chips .bg{position:static;}
.cbox{border:1px solid var(--rule);border-radius:10px;overflow:hidden;}
.cbox .ch{display:flex;align-items:center;justify-content:space-between;padding:7px 11px;background:var(--slate2);}
.cbox .ch span{font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink46);}
.cprev{white-space:pre-wrap;word-break:break-word;color:var(--ink70);font-size:13px;line-height:1.5;padding:12px;max-height:300px;overflow:auto;}
.cprev .muted{color:var(--ink30);font-style:italic;}
.copy{font-family:'DM Mono',monospace;font-size:10px;color:var(--book);background:none;border:1px solid var(--book);border-radius:6px;padding:4px 10px;cursor:pointer;}
.copy.ok{color:#0e1a0c;background:var(--green);border-color:var(--green);}
.dl{display:inline-flex;align-items:center;gap:7px;font-family:'DM Mono',monospace;font-size:12px;font-weight:500;color:#1a0f0a;background:var(--book);border-radius:9px;padding:11px 16px;text-decoration:none;}
.lb-close{position:absolute;top:14px;right:16px;z-index:6;font-family:'DM Mono',monospace;font-size:12px;color:var(--ivory);background:rgba(0,0,0,.5);border:1px solid var(--rule);border-radius:8px;padding:9px 14px;cursor:pointer;}
.lb-close:hover{border-color:var(--book);color:var(--book);}
@media(max-width:820px){.lb-inner{flex-direction:column;}.lb-side{width:100%;border-left:none;border-top:1px solid var(--rule);}.lb-stage{min-height:46vh;}}
#toast{position:fixed;left:50%;bottom:28px;transform:translateX(-50%) translateY(20px);z-index:200;background:var(--slate2);border:1px solid var(--book);color:var(--ivory);font-family:'DM Mono',monospace;font-size:12.5px;padding:12px 18px;border-radius:10px;opacity:0;pointer-events:none;transition:.2s;}
#toast.on{opacity:1;transform:translateX(-50%) translateY(0);}
</style></head><body>
<header>
 <div class="htop">
  <div class="logo">ULTRON<em>.</em></div>
  <div class="sub">Content Portal &middot; secure</div>
  <div class="spacer"></div>
  <div class="count" id="count"></div>
  <div class="lock" onclick="location.reload()">LOCK</div>
 </div>
 <div class="tabs" id="tabs"></div>
 <div class="filters" id="filters"></div>
</header>
<main><div class="grid" id="grid"></div></main>
<div class="lb" id="lb"><div class="lb-inner">
  <div class="lb-stage"><button class="lb-close" onclick="closeLb()">CLOSE</button><img id="lbimg" src=""></div>
  <div class="lb-side" id="lbside"></div>
</div></div>
<div id="toast"></div>
<script>
const DATA = __DATA__;
let chan="all", src="all";
const esc=s=>(s||"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
function toast(t){const e=document.getElementById('toast');e.textContent=t;e.classList.add('on');setTimeout(()=>e.classList.remove('on'),1400);}
function copy(txt,btn){navigator.clipboard.writeText(txt).then(()=>{btn.classList.add('ok');btn.textContent="COPIED";setTimeout(()=>{btn.classList.remove('ok');btn.textContent="COPY";},1200);});}
function shown(){return DATA.materials.filter(m=>(chan==="all"||m.channel===chan)&&(src==="all"||m.source===src));}
function tabs(){
  const T=[["all","All"],["linkedin","LinkedIn"],["tiktok","TikTok"],["instagram","Instagram"]];
  document.getElementById('tabs').innerHTML=T.map(([k,l])=>`<button class="tab ${chan===k?'on':''}" onclick="chan='${k}';render()">${l}</button>`).join('');
  const S=[["all","All"],["generated","Generated"],["reference","Reference"]];
  document.getElementById('filters').innerHTML=S.map(([k,l])=>`<button class="fl ${src===k?'on':''}" onclick="src='${k}';render()">${l}</button>`).join('');
}
function card(m){
  const pv=m.thumb?`<img src="${m.thumb}">`:`<div class="ph">no preview</div>`;
  const post=m.posted?`<div class="bg post">posted</div>`:``;
  const rev=m.source==="reference"?`<div class="bg rev">needs-revision</div>`:``;
  const car=m.type==="carousel"?`<div class="bg car">${m.slides} slides</div>`:``;
  const dim=m.dims?`<div class="dimchip">${m.dims}</div>`:``;
  return `<div class="card ${m.posted?'posted':''}">
   <div class="pv" onclick="openLb('${m.id}')">${pv}<div class="badges"><div class="bg ch">${m.channel||'?'}</div>${car}${rev}</div>${post}${dim}</div>
   <div class="body"><div class="tt">${esc(m.title)}</div>
   <div class="meta"><span>${m.id}</span><span>${m.date||''}</span></div></div></div>`;
}
function render(){
  tabs();
  const list=shown();
  document.getElementById('count').textContent=`${list.length} shown / ${DATA.materials.length} total`;
  document.getElementById('grid').innerHTML=list.length?list.map(card).join(''):`<div class="empty">nothing here</div>`;
}
function field(label,val){
  if(!val)return `<div class="cbox"><div class="ch"><span>${label}</span></div><div class="cprev"><span class="muted">empty</span></div></div>`;
  return `<div class="cbox"><div class="ch"><span>${label}</span><button class="copy" onclick='copy(this.dataset.t,this)' data-t="${esc(val).replace(/"/g,'&quot;')}">COPY</button></div><div class="cprev">${esc(val)}</div></div>`;
}
function openLb(id){
  const m=DATA.materials.find(x=>x.id===id);if(!m)return;
  document.getElementById('lbimg').src=m.thumb||"";
  const chips=`<div class="bg ch">${m.channel}</div>`+(m.type==="carousel"?`<div class="bg car">${m.slides} slides</div>`:``)+(m.dims?`<div class="bg">${m.dims}</div>`:``)+(m.posted?`<div class="bg post" style="position:static">posted</div>`:``);
  document.getElementById('lbside').innerHTML=
   `<div class="lb-title">${esc(m.title)}</div><div class="lb-id">${m.id}</div>
    <div class="lb-chips">${chips}</div>
    ${field('Caption',m.cap)}${field('ALT text',m.alt)}${field('First comment',m.fc)}
    ${m.dl?`<a class="dl" href="${m.dl}" target="_blank" rel="noopener">Download (GitHub login)</a>`:''}`;
  document.getElementById('lb').classList.add('on');
}
function closeLb(){document.getElementById('lb').classList.remove('on');}
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeLb();});
render();
</script>
</body></html>"""

if __name__ == "__main__":
    dest = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/inner.html")
    html = build()
    dest.write_text(html, encoding="utf-8")
    print(f"inner viewer: {dest} ({len(html)/1024:.0f} KB, {len(json.loads(MANIFEST.read_text()).get('materials',[]))} materials)")
