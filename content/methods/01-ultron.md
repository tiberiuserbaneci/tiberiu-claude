# Metoda 1: Ultron Content

## Scop

Pipeline-ul Ultron pentru materiale IG Reel 1080x1350. Este un compositor reveal orientat pe execuție: păstrează asseturile existente, construiește cadrul HTML și produce MP4 deterministic.

## Flux

1. Brief și material de bază.
2. Analiză tehnică a referinței și a asseturilor.
3. Validare logo-uri și imagini. Asseturile greșite sunt înlocuite cu vectori locali sau surse verificate.
4. Poziționare card: header, body, footer.
5. HTML complet cu fonturi incorporate și bloc FILM-META.
6. Still de control la finalul reveal-ului.
7. Corecții înainte de filmul complet.
8. Render frame-by-frame prin `_film.py` cu ceas CSS înghețat.
9. Encode H.264 prin FFmpeg pipe.
10. Verificare rezoluție, durată, fps și cadre-cheie.
11. Livrare MP4 și, când este cerut, still/caption.

## Contract de cadru

- Canvas: 1080x1350 px.
- Header: 0..187 px, permanent vizibil.
- Body: 187..1190 px.
- Footer: 1190..1350 px.
- Reveal: body și footer, opacity 0.982 -> 0 între 0 și 3 secunde.
- Buclă: 7 secunde, 30 fps, 210 cadre.
- Headerul nu este acoperit și nu se schimbă.

## Principii

- Nu există screen recording.
- Nu se folosesc crossfade-uri.
- Conținutul există din primul frame și este acoperit de veil.
- HTML-ul este sursa de adevăr pentru layout și tipografie.
- MP4-ul este randat o singură dată după ce still-ul este validat.

## Scripturi

- `content/_reveal.py`: compozitorul HTML pentru header/body/footer/reveal.
- `content/_film.py`: clock-freezing, screenshot frame-by-frame și FFmpeg.
- `content/_fonts.py`: fonturi incorporate.

## Diferența față de referințe

Ultron este metoda operațională locală. Antigravity rămâne referința pentru sourcing, curățare și compoziție Pillow. Claude rămâne referința pentru SPECS, layouts, preflight, scrub și livrare editorială. Acestea sunt păstrate separat și nu se execută implicit în metoda Ultron.

## Starea bibliotecii offline, verificată la 18 august 2026

Setul complet Claude nu este prezent în acest checkout. Lipsesc `content/assets/logos/mono/`, `ai/`, `color/`, `png/`, `logos.json` și `content/_logos.py`. Sunt disponibile 42 de fișiere în `content/assets/icons/`, inclusiv `gemini-color.svg` și `perplexity-color.svg`. Ultron folosește aceste asseturi locale când există și nu consideră instalată biblioteca completă până când directoarele și indexul sunt prezente.
