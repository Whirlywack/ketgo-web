---
target: Question screen prototype (desktop + phone)
total_score: 26
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 3
timestamp: 2026-10-14T18-16-25Z
slug: prototypes-question-screen-index-html
---
Method: dual-agent (A: design review in Playwright · B: detect.mjs CLI + detect.js injected in Chrome)

## Design Health Score
| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Re-ask shows the same count twice; Exam Trap hidden in panel scroll; phone answer strip hides most numbers |
| 2 | Match system / real world | 3 | Plain Lithuanian + KET refs; "Spėju" vs "Tikrinti" unclear; drawn sign 533 looks like clip-art |
| 3 | User control and freedom | 3 | Lesson ✕ pauses safely; Mock ✕ wipes the exam |
| 4 | Consistency and standards | 2 | Picture/stem order flips phone vs desktop; ✕ jumps on narrow screens; timer 18 vs 40 px; "Enter – kitas" on last Mock Question |
| 5 | Error prevention | 2 | Mock ✕ resets with no confirm; "Baigti" primary while Questions are unanswered |
| 6 | Recognition rather than recall | 3 | Phone B/C hide the marked answer while reading the why |
| 7 | Flexibility and efficiency | 3 | Keys 1–3 + Enter good; no key for Spėju; Enter dead in review |
| 8 | Aesthetic and minimalist design | 2 | Wrong pretest repeats the rule 4 times; text-only desktop is 50–60 % empty |
| 9 | Error recovery | 3 | Per-Option reasons excellent; failed Mock gives no plan by Rule |
| 10 | Help and documentation | 2 | Multi-correct tip shown once (Q1), gone on Q3; Spėju/Kartojimas never explained |
| **Total** | | **26/40** | **Acceptable (top of band)** |

## Design specificity
Clean, consistent Teal system, but structurally a generic quiz screen (stem, three checkbox cards, two buttons). KETGO-specific parts: annotated picture after Check, lime key sentence, per-Distractor notes, KET refs, new/due/repeat chips. The "learning system" barely shows on phone. The drawn scenes are the biggest character opportunity and today read as placeholders (letterboxed roads, flat fills, clip-art pedestrian, system-ui labels).
Detector: 22 CLI findings (1 layout-transition on the progress bar; 13 off-scale font sizes; 5 off-scale radii; 3 colours). 8 are prototype chrome (false positives). In-page: text occluded by the sticky phone dock (agrees with review P1), cramped chip padding, no contrast failures.

## Priority issues
- [P1] Phone: verdict and the right answer are never visible together (A hides the right Option behind the dock, B covers Options, C pushes them ~330 px down). Fix: one refined layout A: collapse unchosen wrong Options to one muted line, scroll so the wrong pick and the right Option sit above the dock, dock ≤ 25 % of the screen with verdict + key sentence + Toliau, full why in flow below. → /impeccable layout
- [P1] Wrong-answer feedback is overloaded (rule said 4 times) and the Exam Trap is hidden in an inner panel scroll. Fix: verdict → key sentence → one short why; Trap only when the learner fell for it; Rule Explainer folded except after a pretest; no inner scroll. → /impeccable distill
- [P1] Mock Exam safety and results: ✕ wipes the exam, "Baigti" primary with unanswered Questions, results are a red wall with retry as primary. Fix: confirm or pause on ✕; "Grįžti" primary and name unanswered numbers; score as hero ("21 / 30 · reikia 24"); mistakes grouped by Rule with "Mokytis šių taisyklių" as primary. → /impeccable harden + /impeccable onboard
- [P2] Pretest and confidence: the first answer a new learner gives is a red ✕ "Neatspėjai", though pretest guesses don't count; "Spėju" unexplained; multi-correct tip gone after Q1. Fix: neutral teal verdict for pretest ("Dabar sužinosi"); "Nesu tikras" with a one-time hint; a quiet permanent "Pažymėk visus teisingus" line. → /impeccable clarify
- [P2] Craft bugs: desktop panel chips have 0 side padding; Memory Hook chip stretches to a full-width lime bar; scenes letterboxed; annotation labels in system-ui; 13 off-scale font sizes (17/19/20/21/26 px); progress fill animates width; lime glows on dark; disabled Spėju/Tikrinti look identical; the car you must yield to is the weakest colour in the scene. → /impeccable polish

## Persona red flags
- Casey (one thumb): stray tap on Mock ✕ deletes the exam; must scroll to find the right answer; B's inner scroll fights the page.
- Jordan (first-timer): doesn't know Spėju vs Tikrinti; Kartojimas / "kiti variantai" unexplained; loses the multi-correct hint before Q3.
- Sam (keyboard/screen reader): good focus rings; chip and tip come after the Options in DOM order on desktop; picture annotation never announced; no key for Spėju.
- Gabija (18, TikTok, mid-range Android): at 360 px only half of Option 1 shows above the dock and "Pirma išmokti" wraps; reads as a clean textbook, not Revolut; neon lime in dark mode.

## Minor observations
Faint card edges on cheap screens; empty desktop canvas on text-only Questions; dead gap above the button on learn/start/results screens; three-line lime key sentence becomes a heavy block; slashed zeros in numbers; results stems truncated mid-word; context line only on desktop.

## Questions to consider
- What if the Question itself turned into the explanation after Check (Options collapse to "your pick vs the right one", the picture teaches), instead of adding a dock, sheet or card?
- Pretest guesses don't count for FSRS. Why grade them with the same red ✕ as a real mistake, on the first answer a learner ever gives?
- What on this screen would Gabija screenshot? If it is the drawn scenes, should the ~100 scenes get art direction before more layout work?
