---
target: Question screen prototype (desktop + phone), round 2
total_score: 29
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
timestamp: 2026-10-14T18-42-04Z
slug: prototypes-question-screen-index-html
---
Method: dual-agent (A: design review in Playwright · B: detect.mjs CLI + detect.js injected in Chrome, iframe harness for 1280×800 and 400×850)

## Design Health Score
| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Desktop: own red pick below the fold after Check (1470×830); re-ask repeats "5 / 7" |
| 2 | Match system / real world | 3 | "kita tvarka / kiti variantai" chip is system wording |
| 3 | User control and freedom | 2 | Paused Lesson only offers "Tęsti"; Mock start/results have no exit; review back is an unlabeled list icon |
| 4 | Consistency and standards | 3 | Two disclosure styles; "Be laiko ribos" reuses the Option card; "Neatsakyta" uses the wrong-answer ✕ |
| 5 | Error prevention | 3 | Confirms work; keys 1–3 still tick Options behind the open quit confirm |
| 6 | Recognition rather than recall | 3 | Phone: collapsed Options truncate to the same prefix; stem scrolls off |
| 7 | Flexibility and efficiency | 3 | Good desktop keys with exact hints; nothing extra on phone |
| 8 | Aesthetic and minimalist design | 3 | Calm; Q1 trap feedback states one idea 4–5 times; text-only desktop ~55 % empty |
| 9 | Error recovery | 3 | Best-in-class per-Option reasons; partly-right multi-correct gets a bare red verdict |
| 10 | Help and documentation | 3 | One-time "Nesi tikras?" tip, context lines, key hints work; neutral "Atspėjai" unexplained |
| **Total** | | **29/40** | **Good** |

## Design specificity
Behaviour is distinctly KETGO (four Option states with reasons, trap only when earned, neutral first-guess verdict, Regitra-true Mock); the visual layer still reads as calm generic edtech. Gap to Apple/Wise is finish: picture framing, typographic details (slashed zeros, unit split from number), dock height, repetition.
Detector: 22 → 9 CLI findings; only one in app code (`.app mark` 4px radius, off the DESIGN.md scale). No contrast failures in any view or theme. All in-page hits are prototype chrome, intentional DESIGN.md choices, or below-fold text under the prototype bar.

## Priority issues
- [P1] Desktop pictures are cropped (regression): 16:9 frame capped at 34cqh + `slice` cuts ~1/3 of the scene at 1470×830 (Q1 own car cut, Q5 sign top cut). Fix: never slice; frame keeps the scene's ratio and caps width instead of height. → /impeccable layout
- [P1] Phone first view shows no full Option (360×740; one at 390×844). Fix: merge the context line into the chip, cap picture height ~26–28svh on short screens, stem 20 px below 380 px; target two full Options visible at 360×740. → /impeccable adapt
- [P2] Collapsed wrong Options are indistinguishable (shared long prefix) and their tap-to-expand is invisible and not keyboard-reachable. Fix: keep full text in a quiet style, or clamp to 2 lines with a chevron. → /impeccable clarify
- [P2] Feedback still repeats one idea; 3-line key sentence makes the phone dock ~35 %; "100 m." breaks inside the lime. Fix: every block adds a new fact; Trap as a transferable heuristic; key sentence ≤ 60 chars; nbsp between number and unit. → /impeccable distill
- [P2] Layout shifts 32 px on Check (hint and key column removed); Mock ending is flat (no headline, unlabeled score, retry as primary). Fix: reserve the space; "Išlaikei / Dar ne" headline, labelled score, primary "Tęsti". → /impeccable polish + /impeccable delight

## Persona red flags
- Casey: scrolls before seeing Options; answer strip out of thumb reach; collapsed rows have no expand cue; "Vis tiek baigti" wraps.
- Jordan: neutral teal "Atspėjai" — was I right?; "kita tvarka" jargon; paused Lesson is a dead end.
- Sam: focus drops to body after Toliau; disabled Tikrinti not discoverable; keys tick behind the quit confirm.
- Gabija: first view is a wall of text + pastel schematic; slashed zeros read technical; clean but not screenshot-worthy.

## Minor observations
Red "kertasi" marker bends the Meaning Colours Rule (use teal like the sign marker); "Neatsakyta" should be a neutral dash; "irgi" note reads oddly when nothing was ticked; "Be laiko ribos" should be a switch row; text-wrap balance leaves one-word lines at 360 px; quit confirm appears far from ✕ on desktop; check Atkinson for an unslashed zero.

## Questions to consider
- If the lime sentence is the one thing to remember, what survives if every other block must add a new fact?
- Would a single centred desktop column with inline feedback feel more Apple/Wise than the two-column frame?
- Should the illustration language for the ~100 scenes be fixed before more screen polish?
