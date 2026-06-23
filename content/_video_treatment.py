#!/usr/bin/env python3
"""Ultron video TREATMENT pipeline. One command turns a source clip into the standard
recolor variants for cross-account posting.

Each variant = grade (built from a clean B&W base) + a burned-in viral hook (first 3s,
DM Sans Bold on a dark pill) + an audio pitch/tempo shift (different per variant, moves the
audio fingerprint) + an optional zoom (bw) + a discreet 'follow @tiberiu.ai' watermark
(no box, bottom-left safe zone, the whole duration) + stripped metadata.

Usage:
  python3 content/_video_treatment.py SOURCE SLUG --hooks "h_cream|h_bw|h_book|h_duo"
          [--variants cream,bw,bookcloth,duotone] [--outdir content]
  (line breaks inside a hook: write \\n ; variants/hooks line up in order)

Notes:
- Source should already be vertical (720x1280). Letterbox a landscape clip to vertical first.
- Grades desaturate first, so they work on any source colour. On near-black content the warm
  variants barely differ - that is expected (the dodge then leans on audio + hook + watermark).
"""
import sys, os, re, base64, tempfile, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
FONT = CONTENT / "assets" / "DMSans-Bold.ttf"
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

# --- the standard 4 grades (all start from B&W: hue=s=0) ---
GRADES = {
 "claude-theme": "hue=s=0,eq=contrast=1.05,curves=r='0/0.05 0.5/0.56 1/1':g='0/0.03 1/0.92':b='0/0.0 1/0.83'",
 "bw":           "hue=s=0,eq=contrast=1.08:brightness=0.004",
 "bookcloth":    "hue=s=0,eq=contrast=1.05,curves=r='0/0.10 0.5/0.64 1/1':g='0/0.06 0.5/0.46 1/0.90':b='0/0.07 0.5/0.40 1/0.84'",
 "duotone":      "hue=s=0,eq=contrast=1.06,curves=r='0/0.08 0.5/0.66 1/1':g='0/0.02 0.5/0.38 1/0.88':b='0/0.06 0.5/0.30 1/0.80'",
}
AUDIO_F = {"claude-theme": 1.04, "bw": 1.03, "bookcloth": 1.05, "duotone": 1.045}
ZOOM    = {"bw": 1.025}   # subtle framing change on one variant; others none

def dims(path):
    out = subprocess.run([FF, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    m = re.search(r"(\d{2,5})x(\d{2,5})", out)
    return (int(m.group(1)), int(m.group(2))) if m else (720, 1280)

def hook_png(text, out, W, H):
    text = text.replace("\\n", "\n")
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    fs = 60 if max(len(l) for l in text.split("\n")) <= 15 else 54
    font = ImageFont.truetype(str(FONT), fs)
    lines = text.split("\n"); ls = 12
    ws = [d.textbbox((0, 0), l, font=font)[2] for l in lines]
    hs = [d.textbbox((0, 0), l, font=font)[3] - d.textbbox((0, 0), l, font=font)[1] for l in lines]
    lh = max(hs) + ls; tw = max(ws); th = lh * len(lines) - ls; padx, pady = 36, 28
    bw, bh = tw + 2 * padx, th + 2 * pady; bx = (W - bw) // 2; by = int(H * 0.13)
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=26, fill=(18, 16, 14, 175))
    y = by + pady
    for l in lines:
        b = d.textbbox((0, 0), l, font=font); lw = b[2] - b[0]
        d.text(((W - lw) // 2, y - b[1]), l, font=font, fill=(250, 250, 247, 255)); y += lh
    img.save(out)

def watermark_png(out, W, H):
    """Discreet 'follow @tiberiu.ai' - no box, white + thin dark outline, bottom-left safe zone."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(FONT), 28); text = "follow @tiberiu.ai"
    b = d.textbbox((0, 0), text, font=font, stroke_width=2)
    x = int(W * 0.061); y = H - int(H * 0.178) - (b[3] - b[1])
    d.text((x - b[0], y - b[1]), text, font=font, fill=(252, 252, 250, 238),
           stroke_width=2, stroke_fill=(8, 6, 5, 155))
    img.save(out)

def main():
    a = sys.argv[1:]
    src, slug = a[0], a[1]
    hooks = []; variants = ["claude-theme", "bw", "bookcloth", "duotone"]; outdir = CONTENT
    i = 2
    while i < len(a):
        if a[i] == "--hooks": hooks = a[i + 1].split("|"); i += 2
        elif a[i] == "--variants": variants = a[i + 1].split(","); i += 2
        elif a[i] == "--outdir": outdir = pathlib.Path(a[i + 1]); i += 2
        else: i += 1
    outdir.mkdir(parents=True, exist_ok=True)
    W, H = dims(src)
    tmp = pathlib.Path(tempfile.mkdtemp())
    wm = tmp / "wm.png"; watermark_png(wm, W, H)
    for vi, v in enumerate(variants):
        grade = GRADES[v]; f = AUDIO_F[v]
        zf = f"crop=iw/{ZOOM[v]}:ih/{ZOOM[v]},scale={W}:{H}," if v in ZOOM else ""
        hk = tmp / f"hook_{v}.png"; hook_png(hooks[vi], hk, W, H)
        out = outdir / f"{slug}-{v}.mp4"
        fc = (f"[0:v]{grade},{zf}setpts=PTS/{f}[g];"
              f"[g][1:v]overlay=0:0:enable='lt(t,3)'[h];"
              f"[h][2:v]overlay=0:0[vo];"
              f"[0:a]asetrate=44100*{f},aresample=44100[ao]")
        subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                        "-i", str(hk), "-i", str(wm), "-filter_complex", fc,
                        "-map", "[vo]", "-map", "[ao]", "-c:v", "libx264", "-preset", "fast",
                        "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "135k",
                        "-map_metadata", "-1", "-movflags", "+faststart", str(out)], check=True)
        print(f"  {out.name}")
    print(f"done: {slug} -> {len(variants)} variants in {outdir}")

if __name__ == "__main__":
    main()
