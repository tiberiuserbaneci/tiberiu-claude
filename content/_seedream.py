#!/usr/bin/env python3
"""Generate one picture with BytePlus Seedream (ModelArk) and save it.

The reveal format (CLAUDE.md 32) needs a titleless square picture; this is the step that makes
one. It was done inline the first time and lost, so it lives here now (operator: "salveaza tot
ce am facut ca regula sa iti fie usor pentru urmatoarele").

    python3 content/_seedream.py "<prompt>" --out content/ig/<slug>/picture.jpg

The key is ARK_API_KEY in the environment. The base URL is overridable with ARK_BASE_URL; the
default list is tried in order because a key is provisioned for one region and the other answers
404, which tells us which one without a guess. watermark is OFF: the visible BytePlus corner mark
is the thing that reads as AI slop, and the band gets composited over the top of the frame anyway.
"""
import argparse, base64, json, os, pathlib, sys, urllib.request, urllib.error

REPO = pathlib.Path(__file__).resolve().parent.parent
BASES = [os.environ.get("ARK_BASE_URL")] if os.environ.get("ARK_BASE_URL") else [
    "https://ark.ap-southeast.bytepluses.com/api/v3",
    "https://ark.cn-beijing.volces.com/api/v3",
]
MODEL = os.environ.get("ARK_IMAGE_MODEL", "dola-seedream-5-0-pro-260628")


def generate(prompt: str, size: str, model: str) -> bytes:
    key = os.environ.get("ARK_API_KEY")
    if not key:
        sys.exit("ARK_API_KEY is not set")
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "size": size,
        "response_format": "b64_json",
        "watermark": False,
    }).encode()
    last = None
    for base in BASES:
        url = f"{base}/images/generations"
        req = urllib.request.Request(url, data=body, method="POST", headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                payload = json.loads(r.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:500]
            last = f"{url} -> HTTP {e.code}: {detail}"
            # auth/model errors are not fixed by trying another region
            if e.code in (401, 403):
                sys.exit(last)
            print(f"  {last}", file=sys.stderr)
            continue
        except Exception as e:                       # noqa: BLE001
            last = f"{url} -> {e}"
            print(f"  {last}", file=sys.stderr)
            continue
        item = payload["data"][0]
        if item.get("b64_json"):
            print(f"  ok  {url}")
            return base64.b64decode(item["b64_json"])
        if item.get("url"):                          # some endpoints only return a url
            print(f"  ok  {url}  (fetching returned url)")
            with urllib.request.urlopen(item["url"], timeout=180) as r:
                return r.read()
        last = f"{url} -> no image in response: {json.dumps(payload)[:300]}"
    sys.exit(f"generation failed. last: {last}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="2048x2048",
                    help="square, downscaled into the 1093px picture band")
    ap.add_argument("--model", default=MODEL)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    data = generate(a.prompt, a.size, a.model)
    out.write_bytes(data)
    print(f"saved  {out}  ({len(data) // 1024} KB)")
