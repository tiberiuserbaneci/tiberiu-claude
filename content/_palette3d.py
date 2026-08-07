#!/usr/bin/env python3
"""Solve a 3D material's base colour so the RENDERED pixel lands on a brand token.

WHY THIS EXISTS. Typing `#CC785C` into a `MeshPhysicalMaterial` does not produce Book Cloth
on screen. The studio environment adds light, the clearcoat adds a specular layer and
NeutralToneMapping rolls the top off, so the rendered surface lands somewhere else entirely -
on the first pass of film 15 a base of `#CC785C` rendered as `#964321`, a rust that reads as
RED, which is exactly the rejection that produced this file. The tokens in CLAUDE.md 7 are a
contract about what the VIEWER sees. Nothing else is a defensible reading of them.

So base colours are SOLVED, never typed:

    render -> measure the lit mid-tone per surface -> correct in linear light -> repeat

Correction happens in LINEAR light because that is where the shader multiplies. Correcting in
sRGB converges slowly and stalls, because the same ratio means a different thing at each end
of the gamma curve.

The mid-tone is a MEDIAN over an annulus with the specular highlight and the terminator cut
off at the 28th and 72nd percentiles. A mean would be dragged by the highlight, which is the
one pixel guaranteed not to be the colour of the object. Near-black pixels are dropped so
type painted over a surface does not poison its reading.

A surface whose base saturates at 255 cannot get brighter. That is a physical limit of the
exposure, not a failure to converge, and `solve()` reports it as `clamped` rather than
looping forever.

USAGE. The build script must declare each base as a module-level `NAME = 0xRRGGBB` line;
this rewrites those lines in place until the render matches.

    from _palette3d import solve
    solve(build="content/_build15still.py",
          html="content/pipeline-film-15-still.html",
          png="content/pipeline-film-15-still.png",
          centre=(540, 1041), squash=0.965,
          surfaces={"ring": ("CC785C", "RING_BASE", (245, 346))})
"""
import importlib.util, pathlib, re, subprocess, sys
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
LUMA = np.array([.2126, .7152, .0722])


def _lin(c):
    c = np.asarray(c, dtype=float) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _srgb(c):
    c = np.clip(c, 0, 1)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055) * 255


def _hex(tok):
    return np.array([int(tok[i:i + 2], 16) for i in (0, 2, 4)], dtype=float)


def chromium() -> str:
    """The renderer's own resolver, so this agrees with _film.py about which binary runs."""
    s = importlib.util.spec_from_file_location("_film", REPO / "content" / "_film.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.chromium_path()


def render(build: pathlib.Path, html: pathlib.Path, png: pathlib.Path,
           exe: str, seek_t: float = 1.4, sel: str = "#film") -> None:
    subprocess.run([sys.executable, str(build)], check=True, capture_output=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe, args=[
            "--force-color-profile=srgb", "--font-render-hinting=none",
            "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto(f"file://{html.resolve()}")
        pg.wait_for_timeout(2600)
        pg.evaluate("""t => {
            document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; });
            if (typeof window.__seek3d === 'function') window.__seek3d(t/1000);
        }""", seek_t * 1000)
        pg.wait_for_timeout(350)
        pg.locator(sel).screenshot(path=str(png))
        b.close()


def midtone(png: pathlib.Path, centre, squash, lo_r, hi_r):
    """Median colour of one annulus, highlight, terminator and painted type excluded."""
    a = np.asarray(Image.open(png).convert("RGB"), dtype=float)
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    d = np.hypot(xx - centre[0], (yy - centre[1]) / squash)
    px = a[(d >= lo_r) & (d < hi_r)]
    px = px[(px @ LUMA) > 70]                       # drop slate type painted on the surface
    if len(px) < 200:
        raise ValueError(f"annulus {lo_r}..{hi_r} has only {len(px)} usable pixels")
    lum = px @ LUMA
    lo, hi = np.percentile(lum, [28, 72])
    return np.median(px[(lum >= lo) & (lum <= hi)], axis=0), len(px)


def _get(build: pathlib.Path, sym):
    m = re.search(rf"{sym}\s*=\s*0x([0-9A-Fa-f]{{6}})", build.read_text())
    if not m:
        raise KeyError(f"{sym} is not a `{sym} = 0xRRGGBB` line in {build.name}")
    return _hex(m.group(1))


def _set(build: pathlib.Path, sym, v):
    build.write_text(re.sub(rf"({sym}\s*=\s*)0x[0-9A-Fa-f]{{6}}",
                            rf"\g<1>0x{v[0]:02X}{v[1]:02X}{v[2]:02X}",
                            build.read_text(), count=1))


def solve(build, html, png, surfaces, centre, squash=1.0,
          seek_t=1.4, tol=3, passes=6, quiet=False) -> dict:
    """Iterate every surface's base until its render matches its token. Returns the report."""
    build, html, png = (pathlib.Path(x) for x in (build, html, png))
    exe, report = chromium(), {}
    for it in range(passes):
        render(build, html, png, exe, seek_t)
        done, line = True, []
        for name, (tok, sym, (lo_r, hi_r)) in surfaces.items():
            target, base = _hex(tok), _get(build, sym)
            got, n = midtone(png, centre, squash, lo_r, hi_r)
            err = float(np.abs(got - target).max())
            clamped = bool(err > tol and (base >= 255).any()
                           and (_lin(target) > _lin(got)).any())
            report[name] = {"base": f"#{int(base[0]):02X}{int(base[1]):02X}{int(base[2]):02X}",
                            "render": f"#{int(got[0]):02X}{int(got[1]):02X}{int(got[2]):02X}",
                            "token": f"#{tok}", "err": err, "n": n, "clamped": clamped}
            line.append(f"{name} #{int(got[0]):02X}{int(got[1]):02X}{int(got[2]):02X}"
                        f"/#{tok} e{err:4.0f}{'*' if clamped else ''}")
            if err > tol and not clamped:
                done = False
                ratio = np.clip(_lin(target) / np.clip(_lin(got), 1e-4, None), .5, 2.0)
                _set(build, sym, np.clip(np.round(_srgb(_lin(base) * ratio)), 0, 255).astype(int))
        if not quiet:
            print(f"pass {it}   " + "   ".join(line))
        if done:
            break
    if not quiet:
        for name, r in report.items():
            note = "  CLAMPED at max exposure" if r["clamped"] else ""
            print(f"  {name:6} base {r['base']} -> {r['render']}  token {r['token']}{note}")
    return report


if __name__ == "__main__":
    print(__doc__)
    print(f"chromium: {chromium()}")
