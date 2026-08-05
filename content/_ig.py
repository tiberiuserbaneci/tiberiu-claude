#!/usr/bin/env python3
"""Sync the rendered decks into content/ig/, the folder the operator posts from.

The portal was retired: the delivery surface is now one folder per post, holding the files
to upload and the caption to paste. The PNGs in there are copies of what `_carousel.py`
rendered, so a re-render has to be pushed through or the operator posts a stale slide. This
does that, and refuses to do it silently if a deck is missing a render.

Captions are hand written and are never touched. Only the numbered PNGs are replaced.

Usage:
  python3 content/_ig.py            # sync every deck
  python3 content/_ig.py --check    # report drift, write nothing
"""
import filecmp, functools, hashlib, pathlib, shutil, sys

print = functools.partial(print, flush=True)  # noqa: A001

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLAY = ROOT / "content" / "clay"
IG = ROOT / "content" / "ig"

# post folder -> deck stem
DECKS = {
    "01-ceo": "clay-01-ceo",
    "02-launch": "clay-02-launch",
    "03-48h": "clay-03-48h",
    "04-night": "clay-04-night",
    "05-posts": "clay-05-posts",
    "06-72h": "clay-06-72h",
    "07-ten": "clay-07-ten",
    "08-investors": "clay-08-investors",
    "09-engineer": "clay-09-engineer",
    "10-setup": "clay-10-setup",
}


def sync(check=False):
    changed = missing = 0
    for folder, stem in DECKS.items():
        src = sorted(CLAY.glob(f"{stem}-*.png"))
        if not src:
            print(f"  MISSING  {stem}: no render in content/clay")
            missing += 1
            continue
        dest_dir = IG / folder
        dest_dir.mkdir(parents=True, exist_ok=True)
        moved = []
        for i, s in enumerate(src, 1):
            d = dest_dir / f"{i:02d}.png"
            if d.exists() and filecmp.cmp(s, d, shallow=False):
                continue
            moved.append(d.name)
            if not check:
                shutil.copy2(s, d)
        # a deck that shrank leaves orphans behind, and the operator would upload them
        for extra in sorted(dest_dir.glob("*.png")):
            if int(extra.stem) > len(src):
                moved.append(f"-{extra.name}")
                if not check:
                    extra.unlink()
        if moved:
            changed += 1
            print(f"  {folder:14} {len(src)} slides  updated: {', '.join(moved)}")
        else:
            print(f"  {folder:14} {len(src)} slides  up to date")
    if missing:
        sys.exit(f"{missing} deck(s) not rendered; run content/_carousel.py first")
    verb = "would change" if check else "synced"
    print(f"{len(DECKS)} posts, {changed} {verb}")
    return changed


def fingerprint():
    """One line per post, so drift is visible in a diff even when file names do not move."""
    for folder in DECKS:
        h = hashlib.sha256()
        for p in sorted((IG / folder).glob("*.png")):
            h.update(p.read_bytes())
        print(f"  {folder:14} {h.hexdigest()[:12]}")


if __name__ == "__main__":
    sync(check="--check" in sys.argv)
    if "--fingerprint" in sys.argv:
        fingerprint()
