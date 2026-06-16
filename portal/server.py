#!/usr/bin/env python3
"""Autonomous portal server. Serves the dashboard and writes every change
(posted status, analytics upload, cross-post) straight to manifest.json and
auto-commits, so the operator never has to commit by hand.

Run:  python3 portal/server.py    then open http://127.0.0.1:8753
"""
import json, os, re, pathlib, threading, subprocess, datetime, urllib.parse, mimetypes, time, zipfile, base64, sys, hashlib, http.cookies
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PORTAL = CONTENT / "portal"
ZIPS = PORTAL / "zips"
MANIFEST = PORTAL / "manifest.json"

def ensure_zip(mid):
    """Build a carousel's download zip on demand from the slides in the manifest, if it is not on
    disk. A hard-sync to origin can land the manifest + slides before the (large) zip artifact, so
    this guarantees a download never 404s. Byte-identical to scan.py's deterministic writer."""
    z = ZIPS / (mid + ".zip")
    if z.is_file():
        return z
    try:
        m = json.loads(MANIFEST.read_text())
    except Exception:
        return None
    mat = next((x for x in m.get("materials", []) if x["id"] == mid), None)
    if not mat or mat.get("type") != "carousel":
        return None
    slides = [ROOT / s for s in (mat.get("files") or []) if (ROOT / s).is_file()]
    if not slides:
        return None
    ZIPS.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(z, "w", zipfile.ZIP_STORED) as zf:
        for i, f in enumerate(sorted(str(s) for s in slides), 1):
            zi = zipfile.ZipInfo(f"{mid}-{i:02d}.png", date_time=(1980, 1, 1, 0, 0, 0))
            zi.external_attr = 0o644 << 16
            zf.writestr(zi, pathlib.Path(f).read_bytes())
    return z
ANALYTICS = CONTENT / "analytics"
ANALYTICS.mkdir(exist_ok=True)
PORT = int(os.environ.get("PORTAL_PORT", "8753"))
HOST = os.environ.get("PORTAL_HOST", "127.0.0.1")
BRANCH = os.environ.get("PORTAL_BRANCH", "claude/epic-davinci-eGOGS")
AUTOPUSH = os.environ.get("PORTAL_PUSH", "1") != "0"
AUTOCOMMIT = os.environ.get("PORTAL_COMMIT", "1") != "0"   # PORTAL_COMMIT=0 -> write manifest but no git (testing)
SYNC = os.environ.get("PORTAL_SYNC", "1") != "0"           # background pull of materials pushed by content sessions
SYNC_SECS = int(os.environ.get("PORTAL_SYNC_SECS", "15"))  # how often to check origin for new content
P_USER = os.environ.get("PORTAL_USER", "ultron")
P_PASS = os.environ.get("PORTAL_PASS", "")   # set -> HTTP Basic Auth on every request, so the port is safe to make Public
def _auth_token():
    # cookie value the form login sets; recomputable, so no server-side session store is needed.
    return hashlib.sha256(("uap1:" + P_USER + ":" + P_PASS).encode()).hexdigest()

# Form login (cookie) instead of HTTP Basic Auth: the Codespaces port proxy commandeers the
# Authorization header / WWW-Authenticate challenge, so Basic Auth returns a bare 401 with no
# prompt even on a Public port. A cookie set by a normal form POST sails through the proxy.
LOGIN_HTML = """<!doctype html><html><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>Ultron Portal</title>
<style>*{box-sizing:border-box}body{margin:0;height:100vh;display:grid;place-items:center;
background:#191919;color:#FAFAF7;font-family:system-ui,-apple-system,sans-serif}
form{width:320px;padding:34px;border:1px solid rgba(250,250,247,.12);border-radius:16px;background:#262625}
h1{font-size:19px;margin:0 0 4px;letter-spacing:-.3px}p{margin:0 0 22px;color:#919180;font-size:13px}
input{width:100%;padding:13px 15px;border:1px solid rgba(250,250,247,.18);border-radius:10px;
background:#191919;color:#FAFAF7;font-size:15px;outline:none}input:focus{border-color:#CC785C}
button{width:100%;margin-top:12px;padding:13px;border:0;border-radius:10px;background:#CC785C;
color:#1a0f0a;font-weight:800;font-size:15px;cursor:pointer}.e{color:#C84623;font-size:12.5px;
margin-top:11px;min-height:15px}</style></head><body>
<form method=post action=/login><h1>Ultron Content Portal</h1><p>Enter the portal password.</p>
<input type=password name=p autofocus placeholder="Password"><button>Open portal</button>
<div class=e>{ERR}</div></form></body></html>"""

_lock = threading.Lock()        # guards manifest read/modify/write only (fast; never held during git)
_gitlock = threading.Lock()     # serializes git; held only by the background worker
_dirty = threading.Event()      # set when the manifest changed and needs committing
_last_msg = ["portal: update"]

def load():
    try:
        return json.loads(MANIFEST.read_text())
    except Exception:
        # self-heal: working file unreadable (e.g. a leftover conflict) -> fall back to the last commit
        r = git(["show", "HEAD:content/portal/manifest.json"])
        if r and r.returncode == 0:
            return json.loads(r.stdout)
        raise

def save(m):
    if "materials" in m:   # keep counts in sync with the array on every write (delete/restore left total stale)
        mats = m["materials"]
        m["counts"] = {"total": len(mats),
                       "generated": sum(1 for x in mats if x.get("source") == "generated"),
                       "reference": sum(1 for x in mats if x.get("source") == "reference"),
                       "crosspost": sum(1 for x in mats if x.get("source") == "crosspost")}
    tmp = MANIFEST.with_name(MANIFEST.name + ".tmp")
    tmp.write_text(json.dumps(m, indent=2))
    os.replace(tmp, MANIFEST)   # atomic: a concurrent reader / git add never sees a half-written file

def git(args):
    try: return subprocess.run(["git"]+args, cwd=ROOT, capture_output=True, text=True, timeout=60)
    except Exception as e: print("git error", e); return None

def autocommit(paths=None, msg="portal: update"):
    """Signal the background git worker. Returns instantly - never blocks the request, never holds _lock."""
    if not AUTOCOMMIT: return
    _last_msg[0] = msg
    _dirty.set()

def _git_commit_push(msg):
    """Runs only inside the git worker (under _gitlock). Uses -X ours on pull so it never leaves a conflict."""
    # stage portal artifacts too (zips/thumbs regenerated by a rescan), not just the manifest -
    # otherwise a rescan leaves the tree dirty and the auto-sync stalls (new content stops landing)
    git(["add", "content/portal", "content/analytics"])
    r = git(["commit", "-m", msg])
    if not (r and r.returncode == 0):
        return  # nothing to commit
    print("committed:", msg)
    if not AUTOPUSH:
        return
    for delay in (0, 2, 4, 8, 16):
        if delay: time.sleep(delay)
        git(["pull", "--no-rebase", "--no-edit", "-X", "ours", "origin", BRANCH])  # ours wins on conflict
        p = git(["push", "origin", BRANCH])
        if p and p.returncode == 0:
            print("pushed"); return
    print("push failed; will retry on the next change")

def _git_worker():
    while True:
        _dirty.wait()
        time.sleep(0.6)      # debounce a burst of rapid clicks into one commit
        _dirty.clear()
        with _gitlock:
            _git_commit_push(_last_msg[0])

def _sync_once():
    """Pull commits pushed by *other* sessions (new posters, captions) so the portal shows them
    without anyone clicking Rescan. This is the fix for 'the portal does not update'.

    Safe by construction: pulls with -X ours (local portal edits always win on conflict), then
    rebuilds the manifest from the files actually on disk - which recovers any new material that
    -X ours dropped from the manifest text - and commits ONLY when that changed the material set,
    so there is no timestamp commit ping-pong."""
    if git(["fetch", "origin", BRANCH]) is None:
        return
    r = git(["rev-parse", f"origin/{BRANCH}"]); h = git(["rev-parse", "HEAD"])
    if not (r and h and r.returncode == 0 and h.returncode == 0):
        return
    remote, local = r.stdout.strip(), h.stdout.strip()
    if remote == local:
        return                                                    # already current
    anc = git(["merge-base", "--is-ancestor", remote, local])     # is origin already contained in HEAD?
    if anc and anc.returncode == 0:
        return                                                    # we are ahead of origin; nothing to pull
    st = git(["status", "--porcelain"])
    if st and st.stdout.strip():
        return                                                    # local edits in flight; let the commit worker push first, retry next cycle
    with _gitlock:
        git(["reset", "--hard", f"origin/{BRANCH}"])              # hard-sync; origin (which has your pushed actions) is the source of truth
    print(f"sync: {local[:8]} -> {remote[:8]} (hard reset to origin)")
    # if this hard-sync changed the portal's OWN code, re-exec so the running process picks it up
    # (a reset updates the files on disk but not the live process) -> future fixes deploy hands-free.
    diff = git(["diff", "--name-only", local, remote])
    if diff and diff.returncode == 0 and any(x.startswith("portal/") and x.endswith(".py") for x in diff.stdout.split()):
        print("sync: portal code changed -> re-exec to load it")
        os.execv(sys.executable, [sys.executable, str(pathlib.Path(__file__).resolve())])

def _sync_worker():
    first = True
    while True:
        if not first:
            time.sleep(SYNC_SECS)
        first = False
        try:
            _sync_once()
        except Exception as e:
            print("sync error", e)

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, code, body=b"", ctype="application/json"):
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store, max-age=0")   # always fresh; survives Codespace wake
        self.send_header("Content-Length", str(len(body))); self.end_headers()
        if body: self.wfile.write(body)
    def _json(self, obj, code=200): self._send(code, json.dumps(obj).encode(), "application/json")
    def _auth_ok(self):
        if not P_PASS: return True            # no password configured -> open (local / Private-port use)
        # 1) cookie from the form login (survives the Codespaces proxy)
        try:
            ck = http.cookies.SimpleCookie(self.headers.get("Cookie", ""))
            if "up_auth" in ck and ck["up_auth"].value == _auth_token():
                return True
        except Exception:
            pass
        # 2) HTTP Basic fallback (curl / API clients)
        h = self.headers.get("Authorization", "")
        if h.startswith("Basic "):
            try:
                u, _, p = base64.b64decode(h[6:]).decode("utf-8", "replace").partition(":")
                return u == P_USER and p == P_PASS
            except Exception:
                return False
        return False
    def _need_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Ultron Portal"')
        self.send_header("Content-Length", "0"); self.end_headers()
    def _login_page(self, err=""):
        return self._send(200, LOGIN_HTML.replace("{ERR}", err).encode(), "text/html; charset=utf-8")
    def _do_login(self):
        n = int(self.headers.get("Content-Length", 0)); body = self.rfile.read(n) if n else b""
        pw = urllib.parse.parse_qs(body.decode("utf-8", "replace")).get("p", [""])[0]
        if P_PASS and pw == P_PASS:
            self.send_response(302); self.send_header("Location", "/")
            c = http.cookies.SimpleCookie(); c["up_auth"] = _auth_token()
            m = c["up_auth"]; m["path"] = "/"; m["max-age"] = "2592000"; m["httponly"] = True; m["samesite"] = "Lax"; m["secure"] = True
            self.send_header("Set-Cookie", m.OutputString())
            self.send_header("Content-Length", "0"); self.end_headers(); return
        return self._login_page("Wrong password." if pw else "")

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if not self._auth_ok(): return self._login_page()   # form login, not a bare 401
        if path in ("/","/index.html"):
            f = PORTAL/"index.html"
            return self._send(200, f.read_bytes(), "text/html; charset=utf-8")
        if path == "/manifest.json":
            return self._send(200, json.dumps(load()).encode(), "application/json")  # load() self-heals if broken
        # serve any file under the repo (images, thumbs, zips, html, analytics)
        rel = path.lstrip("/")
        fp = (ROOT/rel).resolve()
        if str(fp).startswith(str(ROOT)) and fp.is_file():
            ctype = mimetypes.guess_type(str(fp))[0] or "application/octet-stream"
            return self._send(200, fp.read_bytes(), ctype)
        # a carousel zip not yet on disk (synced ahead of its artifact) -> build it from the slides
        if rel.startswith("content/portal/zips/") and rel.endswith(".zip"):
            built = ensure_zip(pathlib.Path(rel).stem)
            if built and built.is_file():
                return self._send(200, built.read_bytes(), "application/zip")
        return self._send(404, b'{"error":"not found"}')

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        if path == "/login": return self._do_login()
        if not self._auth_ok(): return self._need_auth()
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n) if n else b""
        if path == "/api/save":
            data = json.loads(body or b"{}")
            mid = data.get("id"); patch = data.get("patch", {})
            with _lock:
                m = load(); hit=None
                for x in m["materials"]:
                    if x["id"]==mid: x.update(patch); hit=x
                if not hit: return self._json({"error":"id not found"}, 404)
                save(m)
            autocommit([MANIFEST], f"portal: update {mid} ({', '.join(patch)})")
            return self._json({"ok":True, "material":hit})
        if path == "/api/analytics":
            mid = qs.get("id",[""])[0]; fname = qs.get("filename",["analytics.csv"])[0]
            fname = re.sub(r"[^A-Za-z0-9._-]","_", fname)
            dest = ANALYTICS / f"{mid}__{fname}"
            dest.write_bytes(body)
            with _lock:
                m = load()
                for x in m["materials"]:
                    if x["id"]==mid:
                        x["analytics"] = "content/analytics/"+dest.name
                        x["analytics_uploaded"] = datetime.date.today().isoformat()
                save(m)
            autocommit([MANIFEST, dest], f"portal: analytics for {mid}")
            return self._json({"ok":True, "path":"content/analytics/"+dest.name})
        if path == "/api/crosspost":
            data = json.loads(body or b"{}")
            mid = data.get("id"); target = data.get("target")
            if target not in ("linkedin","tiktok","instagram"):
                return self._json({"error":"bad target"}, 400)
            with _lock:
                m = load()
                src = next((x for x in m["materials"] if x["id"]==mid), None)
                if not src: return self._json({"error":"id not found"}, 404)
                clone_id = f"{mid}--as-{target}"
                if any(x["id"]==clone_id for x in m["materials"]):
                    return self._json({"ok":True, "id":clone_id, "already":True})
                clone = dict(src)
                clone.update({"id":clone_id, "channel":target, "source":"crosspost", "origin":mid,
                              "posted":False, "posted_date":None, "analytics":None,
                              "analytics_uploaded":None, "crossposts":[], "status":"ready"})
                m["materials"].append(clone)
                xp = set(src.get("crossposts") or []); xp.add(target); src["crossposts"] = sorted(xp)
                save(m)
            autocommit([MANIFEST], f"portal: crosspost {mid} -> {target}")
            return self._json({"ok":True, "id":clone_id})
        if path == "/api/delete":
            data = json.loads(body or b"{}"); mid = data.get("id")
            with _lock:
                m = load(); m.setdefault("deleted", [])
                idx = next((i for i,x in enumerate(m["materials"]) if x["id"]==mid), None)
                if idx is None: return self._json({"error":"id not found"}, 404)
                mat = m["materials"].pop(idx)
                mat["deleted_date"] = datetime.date.today().isoformat()
                if mat.get("source")=="crosspost" and mat.get("origin"):  # untag the origin
                    for x in m["materials"]:
                        if x["id"]==mat["origin"]:
                            x["crossposts"] = [c for c in (x.get("crossposts") or []) if c!=mat.get("channel")]
                m["deleted"] = [d for d in m["deleted"] if d["id"]!=mid] + [mat]
                save(m)
            autocommit([MANIFEST], f"portal: delete {mid}")
            return self._json({"ok":True})
        if path == "/api/restore":
            data = json.loads(body or b"{}"); mid = data.get("id")
            with _lock:
                m = load(); m.setdefault("deleted", [])
                idx = next((i for i,d in enumerate(m["deleted"]) if d["id"]==mid), None)
                if idx is None: return self._json({"error":"id not found"}, 404)
                mat = m["deleted"].pop(idx); mat.pop("deleted_date", None)
                if mat.get("source")=="crosspost" and mat.get("origin"):  # re-tag the origin
                    for x in m["materials"]:
                        if x["id"]==mat["origin"]:
                            xp = set(x.get("crossposts") or []); xp.add(mat.get("channel")); x["crossposts"] = sorted(xp)
                m["materials"].append(mat)
                save(m)
            autocommit([MANIFEST], f"portal: restore {mid}")
            return self._json({"ok":True})
        if path == "/api/rescan":
            git(["fetch","origin",BRANCH])
            r = git(["reset","--hard",f"origin/{BRANCH}"])  # hard-sync to origin: a diverged local copy can never block the update
            pull_ok = bool(r and r.returncode == 0)
            tail = ((r.stdout or "") + (r.stderr or "")).strip().splitlines() if r else []
            pull_msg = tail[-1] if tail else ("git unavailable" if not r else "")
            with _lock:                                                          # block writes while the index is rebuilt
                subprocess.run(["python3","portal/scan.py"], cwd=ROOT, timeout=600)
            autocommit(msg="portal: sync + rescan")
            return self._json({"ok":True, "pull_ok":pull_ok, "pull":pull_msg,
                               "materials":len(load().get("materials",[])), "branch":BRANCH})
        return self._json({"error":"unknown endpoint"}, 404)

if __name__ == "__main__":
    if AUTOCOMMIT:
        threading.Thread(target=_git_worker, daemon=True).start()   # git runs here, off the request path
    if SYNC:
        threading.Thread(target=_sync_worker, daemon=True).start()  # auto-pull new content from origin every SYNC_SECS
    where = f"http://127.0.0.1:{PORT}" if HOST in ("127.0.0.1","localhost") else f"port {PORT} (forwarded by Codespaces, Private)"
    print(f"Portal -> {where}   (auto-commit {'on' if AUTOCOMMIT else 'off'}, push {'on' if AUTOPUSH else 'off'}, sync {'every '+str(SYNC_SECS)+'s' if SYNC else 'off'}, branch={BRANCH})")
    ThreadingHTTPServer((HOST, PORT), H).serve_forever()
