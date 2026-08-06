#!/usr/bin/env python3
"""Rebuild every deck in TikTok's 4:5 photo-carousel format.

CLAUDE.md 9: 1080x1350 is the operator's top-performer reference format, and photo mode is a
different geometry rather than a resize. There is no 300px top inset because TikTok does not
paint its feed UI over a photo carousel the way it does over a 9:16 video, so the reserve drops
to a print-style margin and the working band gets that space back. Filenames carry `-45` so the
export guard targets 1350 instead of 1920.

The scenes are not rewritten. `_clay25` derives every measurement from the canvas, and the
scene functions read those constants when they run, so setting the format before the decks are
imported is enough to make the same composition correct in both frames.

Usage:
  python3 content/_deck45.py            # write content/clay-NN-name-45.html for every deck
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _clay25

_clay25.set_format("4x5")          # must happen BEFORE the decks build their scenes

import _deck25                     # noqa: E402  - importing is what renders the scenes


def main():
    for d in _deck25.DECKS:
        slug = f"{d['slug']}-45"
        p = _clay25.build(slug, d["title"], d["slides"])
        print(f"  {p.name:26} {len(d['slides'])} slides  {d['kw']:9} "
              f"{_clay25.CANVAS_W}x{_clay25.CANVAS_H}")
    print(f"{len(_deck25.DECKS)} decks at {_clay25.CANVAS_W}x{_clay25.CANVAS_H}, "
          f"column {_clay25.COL_W}, stage {_clay25.STAGE_W}x{_clay25.STAGE_H}")


if __name__ == "__main__":
    main()
