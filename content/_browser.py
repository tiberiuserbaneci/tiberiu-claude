#!/usr/bin/env python3
"""One place that knows how to launch the renderer.

The sandbox ships Chromium under /opt/pw-browsers, but the pinned Playwright build number
and the installed one drift apart (today: the library wants chromium_headless_shell-1234,
the image has 1194). When they disagree, `p.chromium.launch()` fails with "Executable doesn't
exist" and suggests `playwright install`, which the environment explicitly says not to run.

So every render goes through here, and here resolves the binary that is actually on disk.
The alternative is the same three-line fix pasted into every build script, which works until
the day one of them is missed.
"""
import pathlib

ROOT = pathlib.Path("/opt/pw-browsers")


def executable() -> str | None:
    """The newest Chromium on disk, or None to let Playwright pick its default."""
    cands = []
    for d in sorted(ROOT.glob("chromium*"), reverse=True):
        for rel in ("chrome-linux/chrome", "chrome-linux/headless_shell",
                    "chrome-linux64/chrome-headless-shell"):
            p = d / rel
            if p.exists():
                cands.append(p)
    return str(cands[0]) if cands else None


def launch(pw, **kw):
    """`launch(p)` in place of `p.chromium.launch()`."""
    exe = executable()
    if exe:
        kw.setdefault("executable_path", exe)
    return pw.chromium.launch(**kw)


if __name__ == "__main__":
    print(executable() or "no chromium found under /opt/pw-browsers")
