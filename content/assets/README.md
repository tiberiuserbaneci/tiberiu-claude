# Shared assets

| file | what it is |
|---|---|
| `fonts.css` | every face the renderer needs, base64 inlined by `content/_fonts.py`. The headless browser has no network, so a linked webfont silently falls back and the four-register type system ships as one face at four sizes. |
| `tex/desk.jpg` | the blurred desk plate the light films sit on |
| `icons/` | third party brand marks, only for materials where the operator has approved naming them. See its own README for which hosts this environment can actually reach. |
| `tiberiu.jpg` | **the operator's portrait for the reveal footer.** `content/_reveal.py` picks it up automatically when it exists, so no material has to remember to pass it. Square, at least 240px. Not present yet - the file has to be ATTACHED to a message, not pasted into it: a pasted image arrives as pixels in the model's context and never touches the disk, while an attachment lands in the session's upload directory where it can be read and committed. |
