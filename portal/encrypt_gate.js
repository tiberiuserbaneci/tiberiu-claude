// Encrypt the inner portal HTML into a password-gated single file.
// Real crypto: PBKDF2-SHA256 (250k) -> AES-256-GCM, identical params on both sides so the
// browser's window.crypto.subtle decrypts exactly what Node's webcrypto encrypts.
// Nothing on the host is readable without the user + password.
//
//   PUSER=<user> PPASS=<pass> node portal/encrypt_gate.js /tmp/inner.html docs/index.html
const fs = require('fs');
const { webcrypto: wc } = require('crypto');
const ITER = 250000;

const GATE = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Ultron Content Portal</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:'DM Sans',sans-serif;}
body{background:radial-gradient(120% 80% at 50% -10%,#222221 0%,#121211 60%);color:#FAFAF7;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;}
.card{width:100%;max-width:392px;background:#1e1e1d;border:1px solid rgba(250,250,247,.1);border-radius:18px;padding:34px 30px;box-shadow:0 30px 90px rgba(0,0,0,.5);}
.logo{font-weight:900;font-size:26px;letter-spacing:-.6px;}.logo em{color:#CC785C;font-style:normal;}
.sub{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:rgba(250,250,247,.46);margin-top:6px;}
.lab{font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:rgba(250,250,247,.46);margin:20px 0 7px;}
input{width:100%;background:#161615;border:1px solid rgba(250,250,247,.14);border-radius:10px;padding:13px 14px;color:#FAFAF7;font-size:15px;}
input:focus{outline:none;border-color:#CC785C;}
button{width:100%;margin-top:22px;background:linear-gradient(165deg,#CC785C,#C84623);color:#1a0f0a;font-weight:800;font-size:15px;letter-spacing:.02em;border:none;border-radius:11px;padding:14px;cursor:pointer;}
button:disabled{opacity:.6;cursor:default;}
.err{color:#d9685a;font-family:'DM Mono',monospace;font-size:12px;margin-top:14px;min-height:16px;text-align:center;}
.foot{font-family:'DM Mono',monospace;font-size:10px;color:rgba(250,250,247,.3);text-align:center;margin-top:18px;}
</style></head><body>
<form class="card" id="f" onsubmit="return unlock(event)">
  <div class="logo">ULTRON<em>.</em></div>
  <div class="sub">Content Portal</div>
  <div class="lab">User</div><input id="u" autocomplete="username" autofocus>
  <div class="lab">Password</div><input id="p" type="password" autocomplete="current-password">
  <button id="b" type="submit">Unlock</button>
  <div class="err" id="e"></div>
  <div class="foot">private &middot; encrypted in your browser</div>
</form>
<script>
const SALT="__SALT__",IV="__IV__",CT="__CT__",ITER=__ITER__;
const b64=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
async function unlock(ev){
  ev.preventDefault();
  const b=document.getElementById('b'),e=document.getElementById('e');
  const u=document.getElementById('u').value.trim(),p=document.getElementById('p').value;
  b.disabled=true;b.textContent="Unlocking...";e.textContent="";
  try{
    const base=await crypto.subtle.importKey('raw',new TextEncoder().encode(u+':'+p),'PBKDF2',false,['deriveKey']);
    const key=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64(SALT),iterations:ITER,hash:'SHA-256'},base,{name:'AES-GCM',length:256},false,['decrypt']);
    const pt=await crypto.subtle.decrypt({name:'AES-GCM',iv:b64(IV)},key,b64(CT));
    const html=new TextDecoder().decode(pt);
    document.open();document.write(html);document.close();
  }catch(err){
    e.textContent="Wrong user or password.";b.disabled=false;b.textContent="Unlock";
  }
  return false;
}
</script></body></html>`;

(async () => {
  const src = process.argv[2] || "/tmp/inner.html";
  const dst = process.argv[3] || "docs/index.html";
  const user = process.env.PUSER, pass = process.env.PPASS;
  if (!user || !pass) { console.error("set PUSER and PPASS"); process.exit(1); }
  const inner = fs.readFileSync(src);
  const salt = wc.getRandomValues(new Uint8Array(16));
  const iv = wc.getRandomValues(new Uint8Array(12));
  const base = await wc.subtle.importKey('raw', new TextEncoder().encode(user + ':' + pass), 'PBKDF2', false, ['deriveKey']);
  const key = await wc.subtle.deriveKey({ name: 'PBKDF2', salt, iterations: ITER, hash: 'SHA-256' }, base, { name: 'AES-GCM', length: 256 }, false, ['encrypt']);
  const ct = await wc.subtle.encrypt({ name: 'AES-GCM', iv }, key, inner);
  const b = x => Buffer.from(x).toString('base64');
  const gate = GATE.replace('__SALT__', b(salt)).replace('__IV__', b(iv))
                   .replace('__CT__', b(new Uint8Array(ct))).replace('__ITER__', String(ITER));
  fs.mkdirSync(require('path').dirname(dst), { recursive: true });
  fs.writeFileSync(dst, gate);
  console.log(`gate: ${dst} (${(gate.length/1024/1024).toFixed(2)} MB, inner ${(inner.length/1024).toFixed(0)} KB encrypted)`);
})();
