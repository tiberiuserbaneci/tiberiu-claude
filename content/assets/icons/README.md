# Brand marks, the working set

This is what the material scripts read: `_stack.py` and `_layouts.py` resolve a tool name to
`<slug>.svg` or `<slug>-color.svg` in this directory. The renderer has no network, so it has to
be a local file.

**Do not add files here by hand unless a source has no mark for that tool.** The set is generated
by `content/_logos.py` from four sources; run `python3 content/_logos.py --install` and it fills
this directory, writes the index and reports what is missing.

```
<slug>.svg            monochrome, one path, tint it any colour
<slug>-color.svg      full colour official artwork
<slug>-wordmark.svg   the brand's wordmark, when that is the only colour artwork it has
```

The full library, the index with the brand hex, the raster exports and the contact sheet live one
directory up: **`content/assets/logos/`**. Read its README first. It documents the sources, the
`dark` and `wide_ink` flags a material has to respect, and the 41 tools that have no vector mark
in any source and therefore render as a monogram tile.

Only for materials where the operator has approved naming third party products: CLAUDE.md 18
treats a third party logo in a commercial piece as its own permission, separate from naming the
product in copy. The tool stack materials have it.

## Superseded notes

An earlier version of this file recorded that Simple Icons carries no openai, canva, midjourney or
copy.ai. That is still true of Simple Icons, and it no longer matters: OpenAI and Midjourney come
from `gilbarbara/logos`, and Canva is the real mark fetched earlier and kept as a local file. The
reachability table it carried has moved to `../logos/README.md`, where it is maintained.
