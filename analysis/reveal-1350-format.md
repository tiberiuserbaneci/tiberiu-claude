# Infografic reveal 4:5

## Format

- Canvas: 1080 x 1350 px.
- Raport: 4:5.
- Durată: 7.00 secunde.
- Cadru: 30 fps, 210 cadre.
- Audio: absent.
- Buclă: ultimul cadru trebuie să fie identic vizual cu cadrul de start al următoarei bucle, cu excepția progresiei de reveal resetate la început.

## Geometrie

Coordonatele sunt măsurate în pixeli de canvas și sunt ancore, nu procente.

| Zonă | X | Y | Lățime | Înălțime | Comportament |
|---|---:|---:|---:|---:|---|
| Canvas | 0 | 0 | 1080 | 1350 | fix |
| Header / hook | 72 | 72 | 936 | 246 | vizibil complet din cadrul 0 |
| Linie de separare | 72 | 318 | 936 | 3 | fixă, nu se animă |
| Body / infografic | 72 | 321 | 936 | 837 | conținutul principal |
| Footer | 72 | 1158 | 936 | 120 | apare cu reveal-ul body-ului |
| Margine sigură | 72 | 72 | 936 | 1206 | niciun text în afara ei |

Headerul nu se mută, nu își schimbă mărimea și nu își schimbă opacitatea. Dacă headerul este pe două rânduri, ambele rânduri fac parte din aceeași zonă și păstrează aceeași poziție pe toată durata.

Body-ul trebuie să aibă scheletul prezent din primul cadru la opacitate redusă: carduri, coloane, linii, sloturi și numerotare. Reveal-ul umple sloturile existente. Nu introduce structuri noi printr-un cut.

Footerul este în partea de jos a canvasului, într-o singură linie dacă textul încape. Nu este lipit de marginea de jos. Footerul folosește aceeași mască și aceeași rampă ca body-ul, nu fade-in separat.

## Timeline

| Interval | Acțiune |
|---|---|
| 0.00–0.20 s | Canvas, fundal, schelet body și headerul există deja. Headerul este la intensitate 100%. |
| 0.00–3.00 s | Un reveal monotonic se deplasează de sus în jos peste body și footer. Conținutul devine vizibil prin acumulare. Nimic nu dispare și nimic nu se dizolvă. |
| 3.00–5.80 s | Infograficul complet rămâne lizibil. Se permite o mișcare ambientală foarte mică, fără deplasarea textului. |
| 5.80–7.00 s | Hold final. Păstrează compoziția completă și pregătește resetarea buclei fără flash sau cut. |

Reveal-ul este `linear` sau `ease-out` controlat, cu durată exactă de 3 secunde. Pentru o citire clară, fiecare rând poate avea un decalaj de maximum 0.08 secunde, dar toate rândurile trebuie să fie complet vizibile la secunda 3.

## Reguli de continuitate

1. Un singur fundal, o singură textură și o singură lumină de la cadrul 0 până la cadrul 209.
2. Headerul este în poziția finală încă din cadrul 0.
3. Masca de reveal acoperă body-ul și footerul, dar nu headerul.
4. Nu se folosește crossfade între o versiune goală și una completă.
5. Ultimul cadru nu conține un element care dispare la resetarea buclei.
6. Textul de body trebuie redus la etichete și rezultate scurte. Nu se folosesc paragrafe lungi într-o fereastră de 3 secunde.

## Verificare pentru `reveal_1350.mp4`

Materialul de referință confirmă: 1080 x 1350 px, 7.00 s, 30 fps, 210 cadre și fără audio. OCR-ul arată un hook permanent în partea superioară, un body în grilă care devine lizibil în jurul secundei 3 și un CTA/footer în zona inferioară care rămâne vizibil până la final.
