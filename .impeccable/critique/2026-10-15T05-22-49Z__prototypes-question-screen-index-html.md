---
target: Question screen prototype (desktop + phone), round 3
total_score: 28
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 1
timestamp: 2026-10-15T05-22-49Z
slug: prototypes-question-screen-index-html
---
Method: dual-agent (A: design review in Playwright incl. 1366×650 and 360×660 · B: detect.mjs CLI + detect.js in a same-origin iframe harness in Chrome)

## Design Health Score
| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Desktop: verdict on your own pick can sit below the fold |
| 2 | Match system / real world | 3 | "Nesu tikras" as a submit button reads like "skip" |
| 3 | User control and freedom | 3 | Pause, quit confirm, Atgal, answer sheet, "Rezultatai" back |
| 4 | Consistency and standards | 2 | Disabled secondary looks enabled; two disclosure styles; neutral verdict beside a red Option; hint kept on desktop but removed on phone |
| 5 | Error prevention | 3 | Check disabled until a tick; finish lists unanswered; tapping a disabled button says nothing |
| 6 | Recognition rather than recall | 3 | Phone after Check: stem and (at 360) the marked picture scroll away |
| 7 | Flexibility and efficiency | 3 | 1–3 / N / Enter with exact hints; answer-sheet jumps |
| 8 | Aesthetic and minimalist design | 3 | Calm; desktop sparse; panel is a card-in-card stack |
| 9 | Error recovery | 3 | Strongest concept, weakened by placement (below the fold) |
| 10 | Help and documentation | 2 | All-or-nothing never explained; KET refs are plain text |
| **Total** | | **28/40** | **Good** |

## Design specificity
Specific in behaviour and copy (four Option states with reasons, Trap only when earned, Regitra-true Mock, honest copy); generic in shape (white cards, chip, sticky right card, icon-in-circle verdict). The phone after-Check layout is the one screen that feels designed for KETGO. Detector: 10 CLI findings, 8 prototype chrome; app-level: `.q-stem` 20 px at ≤ 380 px and `mark` 4 px radius are off DESIGN.md's scales. No contrast failures in any view or theme.

## Priority issues
- [P1] After Check the key feedback is off-screen: desktop has no scroll handling (1366×650: both marked Options and Toliau below the fold; panel taller than the screen); phone scroll pushes the marked picture out, and after a first guess the Rule Explainer and Trap sit below the dock with no cue. Fix: desktop scrolls picks into view, panel footer (Toliau) pinned with the body scrolling; phone dock gets a one-line pointer ("Taisyklė ↓") when the why holds the Rule or the Trap. → /impeccable layout
- [P2] First guess: neutral "Dabar sužinosi" beside a red "✕ Neteisinga" Option. Fix: the picked wrong Option in a neutral "Tavo spėjimas" state on first guesses. → /impeccable clarify
- [P2] All-or-nothing never explained (Q3 one right + one wrong → "Neteisingai"). Fix: sub-line "Pažymėjai ne visus teisingus" / "Vienas pažymėtas variantas neteisingas". → /impeccable clarify
- [P2] Disabled "Nesu tikras" / "Atgal" look enabled; tapping says nothing; "Nesu tikras" reads as skip. Fix: visibly inert disabled state; a hint on tap ("Pirma pažymėk bent vieną variantą"). → /impeccable polish
- [P2] Focus lost in 7 places (after Pirma išmokti, Į klausimą, Mock nav, confirms, results); confirms are role=group, not dialogs. Fix: focus the stem on every Question; focus the confirm heading and return focus on cancel; focus the results heading. → /impeccable harden

## Persona red flags
- Casey: taps Toliau and never sees the Rule or Trap below the dock; disabled "Nesu tikras" does nothing.
- Jordan: "Nesu tikras" = skip?; red ✕ on a guess that "doesn't count"; partly right = "Neteisingai" with no reason.
- Sam: focus lost in 7 places; disabled Options after Check skip their verdicts in Tab order.
- Gabija (360×660): stem, small picture, one Option; clean but "school app"; failed Mock stings, pass has no warmth.

## Minor observations
Desktop hole where the hidden hint was; phone Options jump ~20 px at Check; "Vis tiek baigti" wraps in the desktop panel; 15 px key-hint sentences below the 16 px floor; dark-mode other car outshines "you"; Trap wash reads brown in dark; re-ask says "su kitais variantais" though one Option repeats; "Peržiūrėti klaidas" walks through all Questions; Q4 Rule Explainer gives the reason but not the rule; thin desktop learn screen; answer sheet at 30 Questions scrolls sideways on phone with no cue.

## Questions to consider
- If the verdict is the heart, why is it the smallest thing in the desktop panel? A tinted header band on the panel?
- Does every Question need a "how sure" decision before Check, or could a one-tap "Spėjau" after Check give the same signal?
- After a first guess the Rule is the feedback: should it live in the dock or a pull-up sheet?
