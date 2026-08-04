#!/usr/bin/env python3
"""Fetch an image for a material, verify it, and turn it into an inlinable data URI.

Headless Chromium in this sandbox cannot reach the internet: every external image fails
ERR_CONNECTION_RESET, with or without the agent proxy passed explicitly. curl can, so an
image has to be pulled down here and carried into the page as base64 before rendering.
That is a sandbox behaviour, not a house rule (CLAUDE.md 18).

Usage:
  python3 content/_img.py <url> [dest]        # fetch, verify, save, print a summary
  python3 content/_img.py <url> --uri         # print the data: URI to stdout for piping
  python3 content/_img.py <file> --uri        # same, for a file already on disk

Not every host is reachable through the proxy (Unsplash answers, Wikimedia does not), so this
reports the failure plainly rather than retrying, which is what the proxy README asks for.
"""
import base64, mimetypes, pathlib, subprocess, sys

ASSETS = pathlib.Path(__file__).resolve().parent / "assets"
# What a browser will actually decode. A server handing back an HTML error page with a 200 is
# the common failure, so the bytes are sniffed rather than trusting the content-type header.
MAGIC = {b"\xff\xd8\xff": "image/jpeg", b"\x89PNG\r\n\x1a\n": "image/png",
         b"GIF87a": "image/gif", b"GIF89a": "image/gif", b"RIFF": "image/webp"}


def sniff(raw: bytes) -> str | None:
    for sig, mime in MAGIC.items():
        if raw.startswith(sig):
            return mime
    if raw.lstrip()[:5].lower() in (b"<html", b"<!doc", b"<?xml"):
        return None                      # an error page wearing an image's URL
    return None


def fetch(url: str, dest: pathlib.Path) -> tuple[bytes, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-o", str(dest),
                        "-w", "%{http_code}", url], capture_output=True, text=True)
    code = (r.stdout or "").strip()
    if r.returncode != 0 or not dest.exists():
        sys.exit(f"fetch failed ({code or 'no response'}): {r.stderr.strip()[:200]}")
    raw = dest.read_bytes()
    mime = sniff(raw)
    if code != "200" or mime is None:
        dest.unlink(missing_ok=True)
        sys.exit(f"host returned {code} and {len(raw)} bytes that are not an image. "
                 f"Blocked or wrong URL. Report the host, do not retry it.")
    return raw, mime


def data_uri(raw: bytes, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(raw).decode()


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--uri"]
    uri_only = "--uri" in sys.argv
    if not args:
        sys.exit(__doc__)
    src = args[0]

    if "://" in src:
        dest = pathlib.Path(args[1]) if len(args) > 1 else ASSETS / pathlib.Path(src.split("?")[0]).name
        raw, mime = fetch(src, dest)
    else:
        dest = pathlib.Path(src)
        raw = dest.read_bytes()
        mime = sniff(raw) or mimetypes.guess_type(str(dest))[0] or "image/jpeg"

    uri = data_uri(raw, mime)
    if uri_only:
        print(uri)
        return
    try:
        from PIL import Image
        dims = "x".join(str(d) for d in Image.open(dest).size)
    except Exception:
        dims = "unknown"
    print(f"  saved  {dest}")
    print(f"  type   {mime}  {dims}  {len(raw)/1024:.0f} KB")
    print(f"  uri    {len(uri)/1024:.0f} KB of base64 "
          f"(inline it in the HTML; the renderer cannot fetch it)")


if __name__ == "__main__":
    main()
