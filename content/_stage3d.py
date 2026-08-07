#!/usr/bin/env python3
"""Real 3D cards: extruded geometry, real lights, real cast shadows, in the render pipeline.

The clay objects across every deck and film are `box-shadow` stacks pretending to be
extrusion. There is no light in them, no material, and no shadow - just N offset copies of a
rectangle. That is the ceiling behind the operator's standing note that the elements are
"slabe" no matter how they are arranged, and it cannot be decorated away.

This replaces the fake with the thing itself, and the choice that makes it usable is the
camera: **orthographic, looking straight down -Z, one world unit per CSS pixel**. That keeps
the cards pixel-aligned with the page, so real typography stays in HTML on top - crisp, real
fonts, exact positions - while WebGL supplies only what CSS cannot fake: bevelled edges, a
material that responds to light, and shadows the objects actually cast on each other.

Determinism: WebGL has no clock to pause. The page exposes `window.__seek3d(seconds)`, which
places the light for that moment and draws exactly one frame; `_film.py` calls it on every
seek, alongside the CSS and GSAP clocks.
"""
import base64, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
THREE = REPO / "content" / "vendor" / "three.module.js"


def module_tag() -> str:
    """three.module.js as a data-URL import.

    The renderer has no network, and three dropped its UMD build, so the ES module is imported
    from a data URL and re-exposed on window. That is the whole trick: an inline <script
    type="module"> cannot be imported from, but it CAN import.
    """
    b64 = base64.b64encode(THREE.read_bytes()).decode()
    return (f'<script type="module">\n'
            f'import * as THREE from "data:text/javascript;base64,{b64}";\n'
            f'window.THREE = THREE;\n'
            f'window.dispatchEvent(new Event("three-ready"));\n'
            f'</script>')


SCENE_JS = """
<script>
// Waits for the module import above, then builds the scene. Everything is in CSS pixels:
// the orthographic camera maps one world unit to one pixel, so a card at x=0,y=-177 sits
// exactly where the HTML text for that row sits.
window.addEventListener('three-ready', () => {
  const T = window.THREE;
  const W = %(W)d, H = %(H)d;
  const cv = document.getElementById('gl');
  const renderer = new T.WebGLRenderer({canvas: cv, antialias: true, alpha: true});
  renderer.setPixelRatio(1);
  renderer.setSize(W, H, false);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = T.PCFSoftShadowMap;
  // Khronos PBR Neutral: the curve built for product visualisation. It rolls the highlights
  // off without touching hue or saturation, which is the whole requirement here - AgX is a
  // FILM curve and desaturates by design, so it turned deep terracotta into pale salmon.
  renderer.toneMapping = T.NeutralToneMapping;
  renderer.toneMappingExposure = 1.02;
  renderer.outputColorSpace = T.SRGBColorSpace;

  const scene = new T.Scene();
  // one unit per pixel, origin at the centre of the canvas
  const cam = new T.OrthographicCamera(-W/2, W/2, H/2, -H/2, -2000, 4000);
  cam.position.set(0, 0, 1000);
  cam.lookAt(0, 0, 0);

  function roundedRect(w, h, r) {
    const s = new T.Shape();
    s.moveTo(-w/2 + r, -h/2);
    s.lineTo(w/2 - r, -h/2);   s.quadraticCurveTo(w/2, -h/2, w/2, -h/2 + r);
    s.lineTo(w/2, h/2 - r);    s.quadraticCurveTo(w/2, h/2, w/2 - r, h/2);
    s.lineTo(-w/2 + r, h/2);   s.quadraticCurveTo(-w/2, h/2, -w/2, h/2 - r);
    s.lineTo(-w/2, -h/2 + r);  s.quadraticCurveTo(-w/2, -h/2, -w/2 + r, -h/2);
    return s;
  }
  function slab(w, h, r, depth, color, rough) {
    const g = new T.ExtrudeGeometry(roundedRect(w, h, r), {
      depth: depth, bevelEnabled: true, bevelThickness: 5, bevelSize: 5,
      bevelSegments: 4, curveSegments: 16,
    });
    g.translate(0, 0, -depth / 2);
    const m = new T.MeshPhysicalMaterial({
      color: color, roughness: rough, metalness: 0.0,
      clearcoat: 0.55, clearcoatRoughness: 0.28,   // a finished surface, not raw plastic
      sheen: 0.35, sheenColor: new T.Color(0xffe9d8), sheenRoughness: 0.6,
      envMapIntensity: 0.55,
    });
    const mesh = new T.Mesh(g, m);
    mesh.castShadow = true; mesh.receiveShadow = true;
    return mesh;
  }

  // the ground the cards sit on and cast onto - the same cream as the page
  // A STUDIO, not three bare lights. This is the difference between "3D" and "expensive":
  // emissive panels in a box, prefiltered into an environment map, so every curved surface
  // carries a real reflection gradient instead of a single flat highlight. It is what a
  // product render has and a CSS gradient can never fake.
  function studio() {
    const s = new T.Scene();
    const box = new T.BoxGeometry(1, 1, 1);
    box.deleteAttribute('uv');
    const lit = (c, i) => new T.MeshBasicMaterial({color: c, side: T.BackSide});
    const room = new T.Mesh(box, lit(0xf0e9df));
    room.scale.setScalar(14); s.add(room);
    const panel = (col, x, y, z, sx, sy, sz) => {
      const m = new T.Mesh(box, new T.MeshBasicMaterial({color: col}));
      m.position.set(x, y, z); m.scale.set(sx, sy, sz); s.add(m);
    };
    panel(0xffffff, -3.4,  4.2,  2.2, 5.0, 0.2, 4.0);   // key softbox, above left
    panel(0xfff1e2,  4.4,  2.0,  2.6, 0.2, 4.0, 4.0);   // warm bounce, right
    panel(0xdfe6ef, -4.6, -1.0, -1.4, 0.2, 3.0, 4.0);   // cool rim, back left
    panel(0xffffff,  0.0, -4.4,  1.0, 6.0, 0.2, 3.0);   // floor bounce
    return s;
  }
  const pmrem = new T.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(studio(), 0.04).texture;
  scene.environmentIntensity = 0.34;

  // The shadow is WARM, not grey. A neutral shadow on a cream ground is the single clearest
  // tell of a cheap render: real light bouncing off a warm surface tints what it fills.
  const ground = new T.Mesh(new T.PlaneGeometry(W * 2, H * 2),
                            new T.ShadowMaterial({opacity: 0.19, color: 0x6b4b34}));
  ground.position.z = -34; ground.receiveShadow = true;
  scene.add(ground);

  scene.add(new T.AmbientLight(0xfff6ec, 0.42));
  const hemi = new T.HemisphereLight(0xfff4e8, 0xd9c9b6, 0.35);
  scene.add(hemi);
  const key = new T.DirectionalLight(0xfff2e4, 1.35);
  key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048);
  key.shadow.camera.left = -W; key.shadow.camera.right = W;
  key.shadow.camera.top = H; key.shadow.camera.bottom = -H;
  key.shadow.camera.near = 1; key.shadow.camera.far = 3000;
  key.shadow.bias = -0.0012;
  scene.add(key); scene.add(key.target);
  // a cool rim from behind separates the object from the ground - the second thing every
  // product render has and a flat scene does not
  const rim = new T.DirectionalLight(0xcfe0f2, 0.85);
  rim.position.set(720, -420, -560);
  scene.add(rim);

  // ---- the object library. Every form is real geometry, so it takes the same light and
  // casts the same shadow; none of them is a shadow trick.
  function mat(color, rough) {
    return new T.MeshPhysicalMaterial({
      color: color, roughness: rough, metalness: 0.0,
      clearcoat: 0.55, clearcoatRoughness: 0.28,
      sheen: 0.35, sheenColor: new T.Color(0xffe9d8), sheenRoughness: 0.6,
      envMapIntensity: 0.55,
    });
  }
  function mesh(g, color, rough) {
    const m = new T.Mesh(g, mat(color, rough));
    m.castShadow = true; m.receiveShadow = true; return m;
  }
  const OB = {
    slab:   (w, h, r, d, c, ro) => slab(w, h, r, d, c, ro),
    ring:   (R, tube, c, ro) => mesh(new T.TorusGeometry(R, tube, 24, 96), c, ro),
    disc:   (R, d, c, ro) => mesh(new T.CylinderGeometry(R, R, d, 72), c, ro),
    ball:   (R, c, ro) => mesh(new T.SphereGeometry(R, 48, 32), c, ro),
    pill:   (R, len, c, ro) => mesh(new T.CapsuleGeometry(R, len, 16, 32), c, ro),
    prism:  (R, d, sides, c, ro) => mesh(new T.CylinderGeometry(R, R, d, sides), c, ro),
    cone:   (R, hgt, c, ro) => mesh(new T.ConeGeometry(R, hgt, 48), c, ro),
    torusK: (R, tube, c, ro) => mesh(new T.TorusKnotGeometry(R, tube, 160, 20), c, ro),
  };
  window.__OB = OB; window.__T = T; window.__scene = scene;

  const cards = [];
  %(CARDS)s

  // No clock in WebGL - it draws when told. _film.py calls this on every seek.
  window.__seek3d = function (t) {
    // the key light swings slowly across the scene: this is the whole point of real 3D,
    // the bevels and the cast shadows change because the LIGHT moved, not because a
    // box-shadow was re-declared
    const a = Math.sin(t * 0.42) * 0.55;
    key.position.set(-260 + a * 300, 1500, 1500);   // high, so the shadow stays a contact
    key.target.position.set(a * 80, -120, 0);
    key.target.updateMatrixWorld();
    %(SEEK)s
    renderer.render(scene, cam);
  };
  window.__seek3d(0);
});
</script>
"""


def build_cards(cards):
    """cards: list of (x, y, w, h, radius, depth, hex color, roughness)."""
    out = []
    for i, (x, y, w, h, r, d, col, rough) in enumerate(cards):
        out.append(
            f"const m{i} = slab({w}, {h}, {r}, {d}, 0x{col}, {rough});\n"
            f"  m{i}.position.set({x}, {y}, 0);\n"
            f"  scene.add(m{i}); cards.push(m{i});")
    return "\n  ".join(out)


def scene(width, height, cards, seek_js=""):
    return module_tag() + SCENE_JS % {
        "W": width, "H": height,
        "CARDS": build_cards(cards),
        "SEEK": seek_js,
    }


if __name__ == "__main__":
    print(f"three.module.js  {THREE.stat().st_size:,} bytes")
    print("import via data URL, orthographic camera, 1 unit = 1 CSS px")
