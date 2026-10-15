---
target: Question screen prototype after design-language rework, round 4
total_score: 30
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 3
timestamp: 2026-10-15T11-53-43Z
slug: prototypes-question-screen-index-html
---
Method: dual-agent (A: design review in Playwright at 390×844, 360×740, 1470×830, 1366×650, 1400×1140, 1024×700, 735×415 zoom; light + dark · B: detect.mjs CLI + detect_live.js injected via Playwright, plus mechanical checks)

Round 4: after the design-language rework (4-pt spacing by role, shared edges, radii 4/6/12/20, weights 400/600, tonal secondary, frameless icons, desktop = question left / sticky answer column right).

## Design Health Score
| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Clear progress, timer, verdict; desktop "why" had no pointer; 30-square sheet pushed the timer off-screen |
| 2 | Match system / real world | 3 | Plain Lithuanian, KET refs; slashed zero ("1Ø0 m") reads technical |
| 3 | User control and freedom | 3 | Pause, learn-first, Atgal, in-page confirms; no Esc |
| 4 | Consistency and standards | 3 | Tonal secondary and result bar consistent; Learn screen showed the Trap unconditionally; header width jumped |
| 5 | Error prevention | 3 | Check inactive until a tick; double Enter skipped feedback |
| 6 | Recognition rather than recall | 3 | Keycaps on controls; "why" in the other column on desktop |
| 7 | Flexibility and efficiency | 3 | 1–4 / N / Enter; untimed Mock |
| 8 | Aesthetic and minimalist design | 3 | Clean grid; lime chopped into blocks, 0 px phone gaps, text-only half-empty |
| 9 | Error recovery | 3 | Per-Option notes; Rule/Trap below the fold on laptops |
| 10 | Help and documentation | 3 | One-time tip, hint line, Rule fold, KET links |
| **Total** | | **30/40** | **Good** |

## Design specificity
Desktop now reads professionally built: measured shared edges (left track x=143, right 767–1327, header aligned), role-based gaps (8/12/16/24/32), two weights, one 12 px radius for content. Specific in behaviour (teal guess state, marked picture, per-Option notes, Regitra-like sheet); category-standard in frame, which fits "commercial, not conceptual". Detector: 11 CLI findings, 8 chrome, 3 app (26 px verdict, 13 px keycap, mask #000 false positive). In-page: no app findings beyond false positives (mark padding, sr figcaption, scroll occlusion). Contrast passes everywhere except inactive controls (exempt, ~2:1).

## Priority issues
- [P1] Desktop "why" outside the reading path and below the fold on laptops (1366×650: Rule 46/119 px visible, Trap hidden). → /impeccable layout
- [P1] Phone 0 px gap between picture/stem and the first Option (`fieldset.q-opts { margin: 0 }` overrode `.q-opts` margin-top). → /impeccable polish
- [P1] Mock answer sheet in the header could not hold 30 Questions (44 px minimum squares; timer pushed off-screen at every width). → /impeccable adapt
- [P2] Result bar squeezed the key sentence (phone 176–206 px column, 3–4 lime blocks; desktop 284 px beside Toliau); icon/text 6 and 14 px off the Options' edges; lime clashes on pink and maroon. → /impeccable layout
- [P2] Text-only Questions leave half of a large window empty (Q2 566 px empty below at 1400×1140). → /impeccable layout

## Persona red flags
- Jordan: "Dabar sužinosi" but the Rule is half below the fold; the Learn screen gives away Q1's distractor via the Trap.
- Sam: Toliau before the "why" in Tab order; Enter after the verdict skips it; no Esc; at 200 % zoom the bar covers 38–44 % and overlaps the answer.
- Alex: 30-square sheet overflows the header.
- Greta (360×740): partly right answer gives a 283 px bar.
- Parent: slashed zeros in distances and "Ø iš 6".

## Minor observations
Scroll fade sat on real content after Check; close button jumped between the Question frame and 720 px screens; Rule text in soft ink; dark inactive primary louder than the tonal secondary; tap message pushed desktop buttons 36 px; off-grid values (2/6/7/10/14/18 px); browser-default button padding; type sizes 15/16/18/22/26/28 too close.

## Questions to consider
- Do text-only Questions need two tracks, or one 720 px column?
- Does the answer sheet belong in the header, or behind a "Klausimas 3 iš 30" button?
- What would the result bar look like designed around the lime sentence?

## Fixed after this round (same day)
All three P1s and the P2s except text-only layout: 16 px phone gap; desktop scrolls the "why" into view with the answer column fixed in place (1366×650: pick, Toliau and the Rule all on screen); sheet wraps to 2 × 15 (fits at 920 px); result = tinted verdict strip + key sentence on a plain ground, icon centred on the checkbox column and words on the Option text edge (measured equal); Learn screen in the same frame without the Trap; Rule text in ink; inactive opacity .45 light / .35 dark; tap message under the buttons; Esc closes confirms; 600 ms Enter guard; static dock below 480 px tall; all spacing on the 4-pt grid; verdict 22 px, phone stem 24 px. Kept by decision: one two-track frame for text-only Questions (the "why" then sits right under the stem, visible without scrolling); slashed zero (the font's legibility design).
