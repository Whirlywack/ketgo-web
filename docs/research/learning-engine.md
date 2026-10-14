# Learning engine at launch: evidence

Ticket: [#27 Learning engine at launch: evidence](https://github.com/Whirlywack/ketgo-web/issues/27) · Feeds: [#9 What 'smart' means at launch](https://github.com/Whirlywack/ketgo-web/issues/9) · Builds on: [#15](https://github.com/Whirlywack/ketgo-web/issues/15), [#17](https://github.com/Whirlywack/ketgo-web/issues/17), [#20](https://github.com/Whirlywack/ketgo-web/issues/20), [#7](https://github.com/Whirlywack/ketgo-web/issues/7) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1)

**Checked on 2026-10-14.** Sources are papers, official docs and source code: the FSRS benchmark, the `ts-fsrs` and `fsrs-rs` code, the Anki manual, and peer-reviewed studies. Each claim links to its source. Words like **Rule**, **Question**, **Option**, **Theme**, **Lesson**, **Review**, **Mock Exam**, **Remembered** and **Learner** mean what `GLOSSARY.md` says.

**Evidence strength** for each claim:

- **Strong**: large benchmark, meta-analysis, source code or official docs, or plain maths.
- **Moderate**: one or a few good studies, or indirect evidence.
- **Weak**: small, old, vendor or forum evidence.
- **Design guess**: no study tests it. A starting point to tune with KETGO data.
- **UNVERIFIED**: a number I saw only in a summary, not in the source itself.

Two warnings:

1. **The FSRS numbers come from Anki flashcards.** Anki users grade themselves with 4 buttons and must *recall* the answer. KETGO auto-grades multiple choice: right or wrong, all-or-nothing, and guessing is possible. Picking the right Option is easier than recalling it. So FSRS default parameters will probably be too optimistic for KETGO until they are fitted to KETGO data (**Design guess**, to check in the first weeks).
2. **No study here uses driving theory**, except one Dutch survey (section 4.4). Nobody has measured "pass rate at Regitra" for any engine design.

---

## Short answer

1. **FSRS cold start.** Ship FSRS-6 (`ts-fsrs` 5.x) with its **default parameters**. Map a right answer to *Good* and a wrong answer to *Again*. Defaults are clearly better than a flat guess, but worse than fitted parameters (prediction error, log loss: 0.366 default, 0.346 fitted per user, 0.395 for a flat average) (**Strong**, Anki data). **Do not fit per Learner at launch.** A 4–6 week Learner would only gain in the second half. Instead, fit **one KETGO-wide parameter set** from all Learners' answers once there are about 1,000 answers on later days (**Design guess**). Keep it only if it predicts the next weeks better than the defaults. `ts-fsrs` only schedules. Its sister package `@open-spaced-repetition/binding` (Rust `fsrs-rs` inside, runs in Node) does the fitting. No other language is needed (**Strong**, code and docs). Same-day repeats: FSRS-6 updates memory for them, but its same-day predictions are poor, no better than a flat average. So never use FSRS-6 for anything shown inside a Lesson (**Strong**). Exam date: FSRS has no deadline. Handle it outside FSRS: never schedule after the exam, and in the last 2 days ask every Rule whose predicted recall *on exam day* is below 90 % (**Design guess**, built on strong spacing evidence).
2. **Memory per Rule.** Keep **one FSRS memory per Rule**. Any Question about that Rule updates it. For 243 of 296 Rules this is the same as one memory per Question, so the choice only matters for about 53 Rules. Log the Question id on every answer. Add a per-Question difficulty adjustment later, when data allows (**Moderate**). Knowledge-tracing studies find that *item difficulty* is what helps prediction most. They also find that pooling practice across items of one skill helps a little. Anki's tools keep sibling cards apart to reduce interference.
3. **Question difficulty at cold start.** **No Elo in the beta.** A difficulty estimate needs about **30 answers per Question** to be within ±1 logit, and about **100 answers** to be within ±½ logit (Linacre). Simple "share correct" and IRT estimates were stable only after **200–250 learners per item** (Wauters et al.) (**Moderate**). With ~500 Questions and few Learners, most Questions stay below that for months. So: log first answers. When a Question has data, use a shrunk "share correct" from first answers, starting from the author's easy/medium/hard label. Add a guessing floor to every predicted P(correct) (**Design guess** for the details).
4. **Honest readiness.** Compute the score range **exactly** over the 30 blueprint slots (6/5/3/3/3/4/2/2/2). This is a 30-step sum, so Monte Carlo is not needed (**Strong**, maths). Exam luck alone is about ±2–3 Questions: a Learner with 85 % per Question has an 80 % range of 23–28 and passes 85 % of the time. So "likely 23–28" is mostly real exam luck, not model noise. **Check accuracy before real results** in two ways:
   - **Calibration of every logged P(correct)**: log loss, Brier score and a reliability chart. Compare against a flat-average baseline (**Strong**, method).
   - **Mock Exams as a test**: store the predicted score before each Mock Exam, then compare it with the actual score. About 16 Mock Exams across Learners show bias to ±1 Question; about 64 to ±½ (**Strong**, maths).

   Practice exams that copy the real exam predict well in medicine (NBME self-test explained 67 % of score variation, n = 12,224) (**Strong**, but not driving). For driving theory, no study was found (**Weak**). Checking against real results needs **≥ 100 passes and ≥ 100 fails** (≥ 200 each is better), so about **250–500 self-reported results** (**Strong**). Keep the word "estimate" until then. **Big catch:** 243 of 296 Rules have one Question. After a Lesson, most Rules have no *unseen* Question left to measure readiness with (see section 4.2).
5. **Logged random choice.** Randomise **uniformly among the top candidates within ~10 % of the best score (at most 4)**, plus a **5 % uniform pick among all eligible due Rules**. Log the candidate set, the scores, the true probability of the chosen one, and the policy version (**Design guess**; the method is **Strong**). Cost is very likely tiny. In Duolingo's notification system, exploring in 17 % of rounds kept essentially all of the gain (average reward 0.1319 vs 0.1320). A 5 % random holdout had a "very small impact" (**Moderate**: engagement, not learning). Do not randomise order when a Learner has a backlog. There, order matters (simulated retention 0.80 vs 0.65) (**Moderate**, simulation).
6. **Weak-Theme focus.** **No Theme steering of Reviews at launch.** FSRS already brings weak *Rules* back sooner. The best evidence for "smart" review (Lindsey et al. 2014) comes from choosing *items* by predicted recall, not Themes (**Moderate**). No study was found that adds topic steering on top of an item-level memory model (**gap**). Use Themes only in three places:
   - show per-Theme readiness;
   - when there is not enough time for all due Rules, rank them by exam points at stake;
   - keep sessions mixed across Themes.

   (**Design guess**.)

---

## What ships at launch, and what waits

| Part | At launch | Waits for | Trigger to switch on (design guess unless noted) |
|---|---|---|---|
| Memory model | FSRS-6 via `ts-fsrs` 5.x, default parameters, one memory per Rule, Good/Again only | One KETGO-wide fit (`@open-spaced-repetition/binding`) | ≥ ~1,000 answers on later days, pooled. Keep only if log loss is lower on the following 2 weeks (Anki rule: refit monthly) |
| | | FSRS-7 | `ts-fsrs` v6 stable (planned 28 Oct 2026) **and** an FSRS-7 optimiser in a released `fsrs-rs` / binding (not yet: only on `fsrs-rs` main) |
| | | Per-Learner fit | Only as an A/B test after the pooled fit. Most Learners finish in 4–6 weeks |
| Question difficulty | Not used for scheduling. Log first answers. Author label optional | Shrunk per-Question "share correct" on first answers | ≥ 30 first answers on that Question (±1 logit, Linacre) |
| | | Elo / IRT / 2PL | Only if selection becomes adaptive enough that simple shares are biased (Pelánek 2016) |
| Readiness | Exact score range over the blueprint, labelled "estimate". Weekly calibration check. Mock Exam predicted-vs-actual check | Recalibrate, drop the word "estimate" | ≥ 100 passes and ≥ 100 fails self-reported (Collins 2016; Riley 2021) |
| Next-Question choice | FSRS due list + Lesson rules + logged random choice | Bandit or new policy evaluated offline | Tens of thousands of logged decisions (section 5) |
| Themes | Per-Theme readiness on screen. Exam-points ranking only when time is short | Theme steering | Only after an A/B test shows a gain |
| May 2026 design: Elo, per-topic Mastery, Monte-Carlo readiness, embeddings, collaborative filtering, confidence gating | **Not at launch** | Revisit with data | None of these is needed for the launch features above |

---

## 1. FSRS cold start

### 1.1 How good are the default parameters?

The open FSRS benchmark tests algorithms on about 10,000 Anki users. Lower log loss and lower RMSE(bins) mean better predictions. Log loss and RMSE(bins) measure calibration ("is 80 % really 80 %?"). AUC measures ranking ("are the weak cards ranked below the strong ones?") ([srs-benchmark README](https://github.com/open-spaced-repetition/srs-benchmark)). Numbers below predict reviews on a later day (same-day reviews not scored).

| Model | Log loss ↓ | RMSE(bins) ↓ | AUC ↑ | Source |
|---|---|---|---|---|
| FSRS-6, fitted per user | 0.3456 | 0.0653 | 0.705 | [README, Oct 2025](https://github.com/open-spaced-repetition/srs-benchmark/blob/1d99d69747774e2de5a9fe53dbf6cbf2cb244e90/README.md) |
| FSRS-6 "binary" (only Again/Good used) | 0.3509 | 0.0671 | 0.685 | same |
| FSRS-6, only the 4 first-answer values fitted ("S0") | 0.3548 | 0.0790 | 0.700 | same |
| **FSRS-6, default parameters** | **0.3661** | **0.0927** | 0.696 | same |
| FSRS-7, fitted per user | 0.3401 | 0.0634 | 0.717 | [current README](https://github.com/open-spaced-repetition/srs-benchmark/blob/bd9110f791e5b37282c55a9aa8db35f68f0c4aa2/README.md) |
| FSRS-7, default parameters | 0.3620 | 0.0910 | 0.703 | same |
| MOVING-AVG (no memory model: the user's recent success rate) | 0.3369 | 0.0592 | 0.700 | same |
| AVG (one flat number: the user's average) | 0.3945 | 0.1034 | 0.500 | same |
| RWKV (one neural net trained on 5,000 *other* users) | 0.2773 | 0.0250 | 0.833 | same |

What this means:

- **Defaults work, but leave a lot on the table.** Measured against the flat average, defaults get about 60 % of the improvement that per-user fitting gets ((0.3945 − 0.3661) ÷ (0.3945 − 0.3456) ≈ 0.58). Fitted FSRS-6 (with recency weighting) beat defaults for **84 % of users** ([Expertium's benchmark write-up](https://expertium.github.io/Benchmark.html)). **Strong** (Anki data).
- **Right/wrong grading costs little.** Using only Again/Good raised log loss from 0.3456 to 0.3509. KETGO has only right/wrong anyway. **Strong**.
- **A Learner's overall level matters a lot.** MOVING-AVG, which only tracks the recent success rate, beats FSRS-6 on log loss but ranks cards slightly worse (AUC). For KETGO this suggests checking calibration *per Learner level*, not only overall (**Design guess**).
- **Training across many users works.** The best model in the benchmark (RWKV) is trained on other users, not per user. Unlike Anki, all KETGO Learners study the **same ~300 Rules**. So pooling data across Learners should help KETGO even more than it helps Anki (**Design guess**, supported by the benchmark).
- **Domain gap.** The defaults were fitted on self-graded flashcards. KETGO's "right" is a weaker signal: it is recognition, not recall, and a guess can be right. With defaults, a Rule answered right on day 0, day 3 and day 17 is not asked again before a day-35 exam. Its predicted recall on exam day is 0.96. (Simulation with `ts-fsrs` 5.4.2, defaults, no fuzz, short-term mode off. Intervals: 3 → 14 → 57 days.) If that is too optimistic for multiple choice, Rules get too few Reviews. That is why the first KETGO-wide fit is the most valuable engine step after launch (**Design guess**).

### 1.2 When does fitting the parameters pay off?

- **What the optimiser does with little data** (source code, `fsrs-rs` v6.5.0, the version inside the Node binding):
  - Fewer than 8 training items: it returns the defaults.
  - 8 to 63 items: it fits only the 4 first-answer stabilities (how long memory lasts after the first answer).
  - 64 items or more: it fits all 21 parameters.

  An item is one answer on a *later day*. Same-day repeats are not items ([`training.rs` L319–L336](https://github.com/open-spaced-repetition/fsrs-rs/blob/v6.5.0/src/training.rs#L319-L336); [`dataset.rs`](https://github.com/open-spaced-repetition/fsrs-rs/blob/v6.5.0/src/dataset.rs)). **Strong**.
- **Anki's guidance.** Anki used to require 1,000 reviews. Since Anki 24.06.3, "the optimizer can be used with any number of reviews". Refit about monthly, or each time the number of reviews doubles ([Anki FSRS FAQ, Q4 and Q6](https://faqs.ankiweb.net/frequently-asked-questions-about-fsrs.html)). The manual lists "low number of reviews (less than a few hundred)" as a reason FSRS fits badly ([Anki manual, deck options](https://docs.ankiweb.net/deck-options.html)). **Strong** (official docs).
- **How many reviews before fitting beats defaults.** A community analysis of 4,000 Anki collections (FSRS-4.5) found that fitted parameters beat defaults on average from very few reviews. The confidence bands separated at about **70–100 reviews**. The maintainers then adopted a rule: fit, compare with defaults and old parameters on the same data, and keep the best ([Anki issue #3094](https://github.com/ankitects/anki/issues/3094)). **Moderate** (benchmark notebook, not peer-reviewed).
- **KETGO arithmetic.** A Learner doing 1 Lesson a day (8 new Rules) passes 64 later-day answers in about the first week. They reach roughly 1,000 by exam day (#17 model: ~37 Questions a day). So a per-Learner fit is *possible* from week 2. But it would help only in the remaining 3–4 weeks, and every Learner's gain would be small. Pooled data from 20 Learners passes 1,000 later-day answers within days. **Design guess**: fit pooled first, per-Learner only as an experiment.

### 1.3 Does `ts-fsrs` fit parameters?

- **No. `ts-fsrs` is the scheduler only.** The same repository ships a second package, **`@open-spaced-repetition/binding`**, "the optimizer for parameter training", built on `fsrs-rs` through `napi-rs`. Its main call is `computeParameters(items, { enableShortTerm })`. It runs in Node ≥ 20 (native) or through WASI. It is marked "public beta" ([ts-fsrs README](https://github.com/open-spaced-repetition/ts-fsrs); [binding README](https://github.com/open-spaced-repetition/ts-fsrs/blob/main/packages/binding/README.md)). **Strong**.
- It fits FSRS-6 (it pins `fsrs-rs` v6.5.0: [Cargo.toml](https://github.com/open-spaced-repetition/ts-fsrs/blob/main/packages/binding/Cargo.toml)). It fits a SvelteKit server as a batch job (e.g. a nightly or monthly script). No Python or Rust service is needed.
- **Versions today:** `ts-fsrs` 5.4.2 is the latest stable release (1 Sep 2026, FSRS-6). `ts-fsrs` 6.0.0-beta.14 adds a choice of models, including **FSRS-7**. Its stable release is "planned for October 28" ([ts-fsrs v6 roadmap, issue #373](https://github.com/open-spaced-repetition/ts-fsrs/issues/373); [npm](https://www.npmjs.com/package/ts-fsrs)). FSRS-7 *fitting* exists only on `fsrs-rs` main, not in a released version (latest v6.6.2) nor in the binding. **Strong** (checked in code and on npm).
- **Recommendation:** launch on FSRS-6. Put the model name, version and parameter set on every `answer_event`, so a later switch to FSRS-7 can be checked on the same log.

### 1.4 Same-day repeats (the in-Lesson "ask again until right 2–3 times")

- **What FSRS does.** FSRS-5 added a separate formula for reviews on the same day. In FSRS-6 it is S′ = S · e^(w17·(G − 3 + w18)) · S^(−w19), so memory grows less when it is already strong ([FSRS algorithm wiki](https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm)). With default parameters, a second right answer on the same day barely changes stability. In the simulation, stability stayed at 2.31 days. **Strong** (formula, simulation).
- **FSRS-6 cannot predict same-day answers.** When same-day reviews are scored, fitted FSRS-6 has log loss 0.3839 and default FSRS-6 has 0.4873. The flat average scores 0.3816, so FSRS-6 is no better than a flat number here. FSRS-7, which uses fractional days, gets 0.3206 fitted and 0.3399 default ([README, Oct 2025](https://github.com/open-spaced-repetition/srs-benchmark/blob/1d99d69747774e2de5a9fe53dbf6cbf2cb244e90/README.md); [current README](https://github.com/open-spaced-repetition/srs-benchmark)). **Strong**.
- **Same-day repeats add little lasting memory.** The Anki manual says: "repeating a card multiple times in a single day does not significantly contribute to long-term memory". It advises few learning steps, all shorter than a day ([Anki manual](https://docs.ankiweb.net/deck-options.html)). #17 already reached the same view from studies. **Moderate** (the manual cites no study).
- **For KETGO (Design guess):**
  - The Lesson rules from #17 decide in-Lesson repeats, not FSRS.
  - Feed every answer to FSRS (`enable_short_term: true`), so its memory update matches how FSRS-6 was trained.
  - Never show or use FSRS-6's P(correct) for same-day answers. Readiness already excludes repeats (#20).
  - **Do not feed the "just guess" pretest answer** (#15) as a normal review. A wrong guess *before teaching* is not forgetting. With defaults, *Again* sets stability to 0.21 days and treats the Rule like a lapse. Start the Rule's memory at the first answer *after* the Rule Explainer. Log the pretest separately.

### 1.5 A fixed exam date 4–6 weeks away

- **FSRS has no deadline.** `ts-fsrs` offers `request_retention` (desired retention, default 0.9) and `maximum_interval`, nothing for a fixed date ([ts-fsrs package README](https://github.com/open-spaced-repetition/ts-fsrs/blob/main/packages/fsrs/README.md)). It can compute predicted recall at any date with `get_retrievability(card, date)`. **Strong**.
- **The gap between reviews should grow with how long memory must last.** For a 1-week test the best gap was about 20–40 % of that week ([Cepeda et al. 2008](https://pubmed.ncbi.nlm.nih.gov/19076480/), see #15). For a 4–6 week exam that means gaps of days to about 2 weeks. That is what FSRS gives anyway (3 → 14 days in the simulation). **Strong** (direction).
- **With a fixed deadline and limited time, models favour reviewing later than 90 %.** In simulations of a term-long course with fixed review time each week, "review the material whose predicted recall is closest to *h*" came close to the best possible schedule, with *h* ≈ 0.4. Well-timed review was up to 40 % better than badly timed review ([Khajah, Lindsey & Mozer 2014](https://home.cs.colorado.edu/~mozer/Research/Selected%20Publications/reprints/KhajahLindseyMozer2014.pdf)). The classroom study that beat generic spacing by 10 % used this kind of threshold (0.33) ([Lindsey et al. 2014](https://doi.org/10.1177/0956797613504302)). **Moderate** (simulation + one classroom study). So FSRS's 90 % is a comfort and workload default, **not a proven exam optimum**. It also matches #15's "aim for 70–90 % success". Keep desired retention as a setting that can be tested later.
- **Rule for KETGO (Design guess, matches #17 and #20):**
  1. Schedule normally with FSRS at desired retention 0.9.
  2. If the next due date falls after the exam and predicted recall *on exam day* is ≥ 0.9, do nothing: the Rule is **Remembered**.
  3. If predicted recall on exam day is < 0.9, move the Review into the last 2 days before the exam. #17's model says this costs only ~12–16 extra Questions on the last day.
  4. If the exam date changes, recompute steps 2–3 from the stored memory states. No replay is needed.

---

## 2. Memory per Rule or per Question

### 2.1 Evidence

- **Item difficulty helps prediction most; skill tags help less.** DAS3H combines item difficulty, skill-level practice counts and time windows. It beat DASH (item-level history only) on 3 datasets, for example AUC 0.826 vs 0.773 on Algebra 2005 ([Choffin et al. 2019, EDM](https://arxiv.org/abs/1905.06873)). An independent re-analysis of 9 datasets found that the gain came from the **item-difficulty term**, not the time windows. It also found that expert skill tags added "+0.01 AUC or less" on 7 of 9 datasets ([Gervet et al. 2020, JEDM](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/451)). **Strong** (tutoring data, not memory of facts).
- **Pooling practice across items of one skill helps a little.** Feeding a model the *skill* history while predicting *items* often beat item-only history (e.g. AUC 0.771 vs 0.718 on ASSISTments 2012) ([Gervet et al. 2020, Table 14](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/451)). Skill-level counts matter more when there are many items per skill. When there is one skill per item, a per-skill term "barely increases the performance" ([Vie & Kashima 2019, AAAI](https://arxiv.org/abs/1811.03388)). **Moderate** (indirect: no study practises item A and then tests memory of item B of the same skill).
- **Finer units mean less data per unit.** "Finer grained KCs lead to potentially more precise models, but also … fewer data per KC, and thus worse consistency of parameter estimates" ([Pelánek 2017, UMUAI review](https://doi.org/10.1007/s11257-017-9193-2)). With small data, simple logistic models win ([Gervet et al. 2020](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/451)). **Moderate**.
- **Anki siblings.**
  - Anki can bury a card's siblings (other cards from the same note) until the next day ([Anki manual, siblings and burying](https://docs.ankiweb.net/studying.html)).
  - The FSRS helper add-on spreads siblings apart because this "alleviates the interference" ([fsrs4anki-helper](https://github.com/open-spaced-repetition/fsrs4anki-helper)).
  - FSRS itself keeps one memory per card and cannot see sibling history. Maintainers judged sibling-aware FSRS hard to build and did not ship it ([Anki forum thread on siblings](https://forums.ankiweb.net/t/interval-determination-of-siblings/49267)).

  **Strong** for the mechanism. **Weak** for how much it matters: the benchmark has no sibling-only test. The only model that uses sibling information (RWKV) also uses many other features.
- **Driving theory: forgetting differs by item.** In a Dutch survey of 50,857 people who had passed the car theory test, about half of the 20 test items declined over the years and others improved. Items that were hard at the start were forgotten most ([Stefan, Heikoop, de Winter & Houwing 2025, *Sci. Rep.*](https://doi.org/10.1038/s41598-025-04796-6)). **Moderate** (cross-sectional). So memory should be tracked per Rule, not per Theme.

### 2.2 Recommendation for KETGO (Design guess, supported by the above)

1. **One FSRS memory per Rule.** Any Question whose main Rule is R updates R. A Question counts as right only if it is fully right (all-or-nothing, like the exam).
2. **For 243 of 296 Rules this equals one memory per Question.** The decision only affects about 53 Rules today, and more as second Questions are written.
3. **When a Rule is due, show its least recently shown Question.** This gives the "vary the Question" effect from #15.
4. **One answer per Rule per day counts as a Review.** A second Question on the same Rule the same day counts as a same-day repeat. This is the Anki "bury siblings" idea.
5. **Log the Question id, Options shown and Distractor ids on every answer** (already in #15). This allows adding a **per-Question difficulty adjustment** later, which the evidence says is the part that pays (section 3).
6. **Trade-off to accept:** a hard Distractor mix can make a known Rule look forgotten. The later per-Question adjustment, and the log of which Distractors were shown, fix this.

---

## 3. Question difficulty at cold start

### 3.1 Evidence

- **How many answers per Question.** The Rasch item calibration table gives:
  - **±1 logit at 95 % needs 16–36 answers ("use 30")**;
  - **±½ logit needs 64–144 ("use 100")**;
  - "at least 8 correct responses and 8 incorrect responses" for reasonable confidence within 1 logit.

  ([Linacre, *Rasch Measurement Transactions* 7(4):328](https://www.rasch.org/rmt/rmt74m.htm); current page is a later revision of the 1994 note.) **Strong**. One logit is a big step: it moves an 80 % Question to about 60 % or 92 %.
- **How many learners until estimates settle.** 318 students, 18 items: "Both IRT and proportion correct obtain stable estimates by the time 200–250 learners have answered the item. The Elo rating system requires more learners" (Elo with a fixed K). Accuracy against the final estimate: share correct r = 0.93, learners' own ratings 0.91, Elo 0.86, **expert ratings 0.82** ([Wauters, Desmet & Van den Noortgate 2012, *Computers & Education*](https://kulak.kuleuven.be/~u0006844/publications/2012,%20Wauters,%20Item%20difficulty%20estimation,%20Computers%20and%20Education.pdf)). **Moderate** (18 items, not driving).
- **Elo, when used.** Pelánek recommends a falling update size U(n) = a/(1 + b·n) with a = 1, b = 0.05. He notes "this exact choice of parameter values is not important". Elo agreed with full joint estimation at r = 0.97 in a geography app (250,000+ answers). He warns that with **adaptive** item selection, plain "share correct" gives poor estimates that do not improve with more students ([Pelánek 2016, *Computers & Education*](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf); [Papoušek, Pelánek & Stanislav 2014, EDM](http://educationaldatamining.org/EDM2014/uploads/procs2014/long%20papers/6_EDM-2014-Full.pdf)). **Moderate**. Neither paper gives "stable after N answers".
- **Guessing floor.** For multiple choice, P(correct) = g + (1 − g) · p, where g is the chance of guessing right ([Pelánek 2016](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf); [Papoušek et al. 2014](http://educationaldatamining.org/EDM2014/uploads/procs2014/long%20papers/6_EDM-2014-Full.pdf)). **Strong** (formula).

### 3.2 Recommendation for KETGO

1. **No Elo in the beta** (**Moderate**). With ~500 Questions and few Learners, most Questions need months to reach 30 answers, and 200+ for stable values. Elo also brings a Learner-ability side that must be tuned.
2. **Use first answers only for difficulty** (**Design guess**). Every Learner meets each Question in the same curated Program order, so first answers are not biased by adaptive selection (Pelánek's warning). Later Reviews *are* adaptive, so leave them out. Keep pretest (guess-before-teaching) answers separate from first answers after teaching.
3. **Shrink towards a prior** (**Design guess**). Start each Question at the author's easy/medium/hard label (expert ratings: r ≈ 0.82). Add 5–10 pseudo-answers. Let real first answers take over from about 30 answers.
4. **Add a guessing floor to every predicted P(correct)** (**Design guess**). g = 1/(number of shown Options) when exactly one Option is right and the Learner knows that. g is much lower when the Learner must find the exact set. For example, for any non-empty subset of 4 Options, g = 1/15. FSRS has no guessing term. So use the floor in readiness, and check it in the calibration chart.
5. **Use difficulty only to choose among due Rules or to adjust readiness.** Never use it to change a Rule's FSRS memory.

---

## 4. Honest readiness

### 4.1 Computing the score and its range

- **Exact is easy.** The number of right answers on 30 Questions with different chances is a "Poisson-binomial" count. It can be computed exactly, by a closed formula ([Hong 2013, *Comput. Stat. Data Anal.*](https://doi.org/10.1016/j.csda.2012.10.006)) or by a 30-step recursion. At n = 30 this takes microseconds. **Monte Carlo is not needed**. It adds random noise unless thousands of runs are used. Use simulation only to add model uncertainty (draw p values, then count). **Strong** (maths).
- **Inputs (Design guess).** For each Theme, p = the average predicted P(correct on an *unseen exam Question* on exam day) over that Theme's Rules. Use equal weight per Rule, since Regitra does not publish which Rules it asks most. Slots per Theme: 6/5/3/3/3/4/2/2/2.
- **Exam luck is most of the range.** My calculation, for a perfectly known Learner with the same p on every Question:

| p per Question | Expected score | 80 % range | P(score ≥ 24) |
|---|---|---|---|
| 0.75 | 22.5 | 19–25 | 0.35 |
| 0.80 | 24.0 | 21–27 | 0.61 |
| 0.85 | 25.5 | 23–28 | 0.85 |
| 0.90 | 27.0 | 25–29 | 0.97 |

  If the model is also unsure about p (p = 0.85 ± 0.05), the range widens to 22–29 and P(pass) falls to 0.80. So #20's "about 26 of 30, likely 23–28" is about the honest width. It cannot get much narrower, however good the model is. **Strong** (maths).

### 4.2 The single-Question problem (KETGO-specific)

Readiness should measure **transfer**: can the Learner apply the Rule to a *new* Question, as at Regitra? Practice transfers to new Questions (*d* = 0.40), but least of all to re-arranged versions of the same Question (Pan & Rickard 2018, see #15). #20 says readiness uses **only first answers to new Questions and Mock Exams, never repeats**. But:

- The first Question of each Rule is answered as a pretest, *before* teaching (#15). That measures prior knowledge, not readiness.
- **243 of 296 Rules have only one Question.** After its Lesson, such a Rule has no unseen Question left.
- So, for most Rules, the only post-teaching data are **repeats** (same stem, new Option mix), which #20 excludes.

**Options for #9 (Design guess):**

- **(a)** Write a second Question for Rules in the heavy Themes. Hold it back for Mock Exams only.
- **(b)** Build readiness from the memory model: FSRS recall on exam day per Rule, times a "transfer discount". Fit the discount later from Mock Exam answers on unseen Questions and from real results.
- **(c)** Both.

Without (a), Mock Exams are made of repeats and will overstate readiness. The top user complaint is "95 % in the app, failed Regitra" (#15).

### 4.3 Checking accuracy before any real results

1. **Calibration of every logged P(correct)** (**Strong**, method). #15 already logs the predicted P(correct) at serve time. Each week, on answers from later days and on first answers to unseen Questions, compute:
   - **log loss** and **Brier score** (mean squared error). Compare both with a flat-average baseline, as the FSRS benchmark does with AVG. A model that cannot beat the flat average is not good.
   - **A reliability chart**: 10 bins of predicted P. In each bin, plot predicted vs actual share right. Add a small histogram of how many answers fall in each bin.
   - **Calibration-in-the-large and slope**: is the average right, and are the extremes too extreme?

   Pelánek's review of student-model metrics: AUC "should not be used (as the only metric) in cases where we need absolute values of predictions to be well calibrated". Prefer RMSE or log-likelihood ([Pelánek 2015, JEDM](https://files.eric.ed.gov/fulltext/EJ1115277.pdf)). Aim for "moderate calibration" (the reliability chart is close to the diagonal), not perfect calibration ([Van Calster et al. 2016](https://pubmed.ncbi.nlm.nih.gov/26772608); [Van Calster et al. 2019, BMC Med](https://pmc.ncbi.nlm.nih.gov/articles/PMC6912996/)). With 10 bins and a few hundred answers per bin, each bin is accurate to about ±3–5 points. A beta of 50 Learners gives tens of thousands of answers within weeks.
2. **Mock Exam predicted vs actual** (**Strong** for the maths; method **Design guess**, since I found no published precedent for this exact use). Just before each Mock Exam, store the predicted score and the 80 % range that the readiness screen would show. Afterwards check two things:
   - The average of (actual − predicted) should be about 0. One Mock Exam score varies by about ±2 Questions, so about **16 Mock Exams** (across all Learners) estimate this bias to ±1 Question, and about **64** to ±½.
   - About 80 % of actual scores should fall inside their 80 % range.
3. **What this cannot check.** Mock Exams are still KETGO Questions, at home, without exam stress. They check the *model*, not the gap between KETGO and Regitra. Only real results check that gap (sections 4.4–4.5).

### 4.4 Do practice-exam scores predict real exam results?

- **Medicine, yes, when the practice exam copies the real one.** The NBME self-assessment (CBSSA) "explained 67 % of the variation in first Step 1 scores" (n = 12,224) ([Morrison et al. 2010, *Acad. Med.*](https://doi.org/10.1097/ACM.0b013e3181ed3f5c)). NBME itself warns that "different testing conditions (including the high-stakes nature of Step 1) as well as additional learning or forgetting are likely to affect future test results" ([NBME sample report](https://www.nbme.org/sites/default/files/2022-06/Comprehensive_Basic_Science_Self-Assessment_Sample.pdf)). Commercial practice tests showed similar R² ≈ 0.66–0.68, in a self-selected survey of 399 students ([PMC7198101](https://pmc.ncbi.nlm.nih.gov/articles/PMC7198101)). **Strong** for medicine.
- **Nursing exit exams** report 95–99 % "accuracy", mostly because most students pass. Proctored tests predicted better than unproctored ones ([HESI validity study](https://pubmed.ncbi.nlm.nih.gov/16913561)). **Moderate** (vendor studies).
- **Driving theory: no study found** that links practice-test scores to the official result. In the Dutch survey, 76 % of candidates used practice tests, and the national first-time pass rate was 36–43 % ([Stefan et al. 2025](https://doi.org/10.1038/s41598-025-04796-6)). **Weak** (gap).
- **Verdict.** A practice exam that is built like the real one, taken under similar conditions, predicts well. KETGO's Mock Exams use KETGO's own Questions, often repeats, at home. Expect them to be **optimistic** until checked against real results (**Moderate**).

### 4.5 How many real results are needed?

- **Rules from prediction-model research:**
  - at least **100 events and 100 non-events** to check calibration; for a full calibration curve, "a minimum of 200 events and 200 nonevents" ([Riley et al. 2021, *Stat. Med.*](https://onlinelibrary.wiley.com/doi/full/10.1002/sim.9025));
  - "a minimum of 100 events and ideally 200 (or more)" ([Collins, Ogundimu & Altman 2016](https://pubmed.ncbi.nlm.nih.gov/26553135));
  - these rules of thumb can still be too small ([Riley et al. 2024, *BMJ*](https://www.bmj.com/content/384/bmj-2023-074821)).

  **Strong**.
- **For KETGO**, an "event" is a pass or a fail, whichever is rarer. The Regitra first-attempt pass rate for category B was **38.3 % in 2025** (Regitra statistics as quoted by a prep site, [roboket.lt](https://roboket.lt/); **UNVERIFIED** against Regitra's own table). KETGO Learners may pass more often. My arithmetic:

| Pass rate of reporting Learners | Reports for 100 + 100 | Reports for 200 + 200 |
|---|---|---|
| 38 % | ~263 | ~526 |
| 50 % | 200 | 400 |
| 60 % | 250 | 500 |
| 70 % | ~333 | ~667 |

- **Self-reports are biased.** Self-reported grades are less valid than people think, and worse for weaker students ([Kuncel, Credé & Thomas 2005, meta-analysis](https://doi.org/10.3102/00346543075001063)). Self-reported SAT scores were over-reported by 25 points on average (39 % over, 51 % right, 10 % under, n = 650), and more by low scorers ([Mayer et al. 2007, *Educ. Psychol. Rev.* 19](https://doi.org/10.1007/s10648-006-9034-z)). So failers may report less or report wrongly (**Weak**, no pass/fail study found). **Design guess:**
  - Ask neutrally, with Passed / Failed / Not yet (#5).
  - Count who did *not* answer.
  - Compare the predicted readiness of answerers and non-answerers.

---

## 5. Logged random choice

### 5.1 Evidence

- **Why randomness is needed.** To judge a new policy from old logs, every choice the new policy might make must have had a non-zero, *known* chance under the old one ("support"). Otherwise the estimate can stay wrong however much data there is ([Swaminathan & Joachims 2015](https://arxiv.org/abs/1502.02362)). The simple "replay" method needs uniform random logging and keeps only 1 event in K ([Li, Chu, Langford & Wang 2011](https://arxiv.org/abs/1003.5956)). **Strong**.
- **Small probabilities make estimates noisy.** Inverse-propensity scoring has "a much larger variance … more severe when [the logged probability] gets smaller". The doubly robust method cut error by 10–20 % in experiments ([Dudík, Langford & Li 2011](https://arxiv.org/abs/1103.4601)). Unclipped weights have unbounded variance, so clip them ([Swaminathan & Joachims 2015](https://arxiv.org/abs/1502.02362)). **Strong**.
- **Log the real probability.** Microsoft's Decision Service logs every decision as (context, action, reward, probability). A common bug: staff override the chosen action and the logged probability becomes wrong ([Agarwal et al. 2016](https://arxiv.org/abs/1606.03966)). One deployment explored 33 % of the time. **Strong** (method). The 33 % is not a general recommendation.
- **Cost in practice.**
  - At Bing, randomisation for counterfactual analysis had no significant effect on clicks or revenue ([Bottou et al. 2013, *JMLR*](https://jmlr.org/papers/volume14/bottou13a/bottou13a.pdf)).
  - At **Duolingo** (choosing notification texts), a softmax policy that picked a non-top option in 17 % of rounds kept almost all the gain: average reward 0.1319 vs 0.1320 for always picking the best, and 0.1295 for fully random. After launch, Duolingo kept a **5 % uniform-random holdout**. They report a "very small impact on the gains" and two benefits: it catches bugs, and it gives data on rarely chosen options ([Yancey & Settles 2020, KDD](https://research.duolingo.com/papers/yancey.kdd20.pdf)).

  **Moderate**: engagement, not learning.
- **Education examples.** In the Refraction maths game, 11,300 players were served uniformly random choices. The policy picked offline from that data then beat random and expert policies by 32 % in a live test (N = 2,000) ([Mandel et al. 2014, AAMAS](https://grail.cs.washington.edu/wp-content/uploads/2015/08/mandel2014ope.pdf)). Adaptive (bandit) experiments help students more but need "at least twice as many participants" for the same statistical power ([Rafferty, Ying & Williams 2019, JEDM](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/357), abstract only). For policies that act over many steps, importance sampling can even pick the worse policy ([Doroudi, Thomas & Brunskill 2017](https://proceedings.mlr.press/r15/doroudi17a.html), abstract only). **Moderate**. Whole-schedule policies still need A/B tests; logs can only judge one-step choices well.
- **Learning cost: no direct study.** I found no study that measures learning lost through small exploration in spaced repetition. Two pieces of indirect evidence:
  - In an FSRS simulation with a cap of 80 Reviews a day (a backlog), random order gave true retention **0.65**, while "highest recall first" gave **0.80**, at about 10 % more time per remembered card ([review-sort-order-comparison](https://github.com/open-spaced-repetition/review-sort-order-comparison)).
  - Without a backlog, maintainers say order "doesn't matter" (forum, **Weak**).

  **Moderate** (simulation).

### 5.2 Recommendation for KETGO (Design guess; method Strong)

1. **Randomise within a near-tie band.** Take the candidates whose score is within ~10 % of the best, at most 4, and pick uniformly among them. The cost per choice is at most the score gap in the band, so it is small by design.
2. **Add a 5 % global pick.** In 5 % of choices, pick uniformly among *all* eligible due Rules. This gives support for future policies that would choose outside the band, as with Duolingo's 5 % holdout. Smallest probability = 0.05 ÷ (number eligible), e.g. 0.0025 with 20 due Rules. Clip weights at 10–20 when analysing.
3. **Turn the band off when the Learner has a backlog** (more due than fits today), or in the last 2 days before the exam. Then order matters: use "lowest predicted recall on exam day first" (section 6).
4. **Log per decision:**
   - the candidate set and each candidate's score;
   - the band;
   - the probability of the chosen item, **computed by the same code that sampled it**;
   - policy and model version;
   - and the outcome.

   Never let a later rule override the pick without logging the new probability.
5. **What it buys.** For a choice where a new policy disagrees with the logged one, only about q/k of decisions are usable (q = chance of randomising, k = band size). Expect to need **tens of thousands of logged decisions** for one clear offline comparison. A beta of 100 Learners × ~1,000 answers gives ~100,000 (my arithmetic). Use logs to screen ideas, then confirm with A/B tests.

---

## 6. Weak-Theme focus on top of FSRS

### 6.1 Evidence

- **Model-chosen review beats fixed spacing.**
  - 172–176 school students, Spanish vocabulary. Personalised review scored **+16.5 %** vs massed and **+10.0 %** vs generic spacing one month later ([Lindsey et al. 2014](https://doi.org/10.1177/0956797613504302)).
  - The personalised scheduler chose **items** by predicted recall (near a threshold), using item difficulty, student ability and study history. It did not choose topics. The generic scheduler reviewed "one chapter back".

  **Strong** that item-level, model-based choice helps. FSRS already does this kind of item-level choice.
- **Adaptive spacing beat fixed schedules at a delayed test.** Adaptive 42 % vs expanding 31 % vs equal 30 % (N = 72). The adaptive system used response times as well as accuracy ([Mettler, Massey & Kellman 2016, *JEP: General*](https://doi.org/10.1037/xge0000170)). In a later chemistry study (3 experiments, 130 students), adaptive spacing won in 2 experiments. The third "did not show the clear advantage of adaptive spacing" ([Mettler et al. 2020, CogSci](https://pmc.ncbi.nlm.nih.gov/articles/PMC8324178/)). **Moderate**.
- **Mastery learning** (re-teach a unit until passed) raised exam scores by about 0.5 SD in 108 evaluations, more for weaker students ([Kulik, Kulik & Bangert-Drowns 1990](https://doi.org/10.3102/00346543060002265)). That is unit gating, not Theme steering of Reviews. **Moderate** for gating, **Weak** for Theme steering.
- **Harder practice: more learning, more early drop-out.** A randomised trial with about 37,000 learners in a geography practice app set target error rates of 5 %, 20 %, 35 % and 50 %. After 10 answers, 89 % stayed in the easiest condition and 81 % in the hardest. After 100 answers all conditions were at 26 %. Learning was faster in the harder conditions ([Papoušek, Stanislav & Pelánek 2016, ITS](https://www.fi.muni.cz/~xpelanek/publications/its-target-difficulty.pdf)). In an online maths game (10,000 and 70,000 players), easier levels were more engaging but gave "the slowest rates of learning" ([Lomas et al. 2013, CHI](https://dx.doi.org/10.1145/2470654.2470668)). **Moderate**. Heavy weak-Theme blocks would push success down, and their effect is unknown.
- **No study found** that adds topic-level steering to an item-level memory scheduler and measures a gain (**gap**). Mixing confusable Rules helps (#15), which argues against "weak Theme only" sessions.

### 6.2 Recommendation for KETGO (Design guess)

1. **Reviews: FSRS alone at launch.** Weak Rules come back sooner by design (low stability means short gaps).
2. **When time is short** (backlog, or the last days before the exam), rank due Rules by **exam points at stake**:
   - Formula: (Questions per exam for the Theme ÷ Rules in the Theme) × (gain in predicted recall on exam day from one Review).
   - Divide by the number of Rules: a Theme with 6 exam Questions spread over 80 Rules gives each Rule less weight than a Theme with 2 Questions over 10 Rules.
   - This is the only Theme-based steering at launch.
3. **Program order** stays curated (Glossary). If the order is changed, putting high-weight Themes earlier gives their Rules more spaced Reviews before the exam (#17).
4. **Show** per-Theme readiness on the readiness screen. That is where Learners see "weak Themes".
5. **Keep sessions mixed** across Themes. Do not run "weak Theme only" Lessons.
6. **Test later.** Log per-Theme results so that a Theme-steering A/B test is possible after launch.

---

## Facts #9 needs

1. **Launch engine = FSRS-6 per Rule + exam-date rule + full logging + a calibration report.** Nothing else from the May 2026 design is needed at launch: no Elo, no per-topic Mastery, no Monte Carlo, no embeddings, no collaborative filtering, no bandit. Each can wait for data (table above).
2. **The most valuable engine step after launch is one KETGO-wide FSRS fit**, because multiple choice is a weaker signal than Anki recall. Plan it for about 2–4 weeks into the beta, keep it only if it beats the defaults on later data, and refit monthly.
3. **Pretest answers must not enter FSRS as normal Reviews.** A wrong "just guess" is not forgetting.
4. **Readiness has a data problem.** 243 of 296 Rules have one Question, so after the Lesson there are few unseen Questions to measure with. Decide: hold back second Questions for Mock Exams (content work), or accept a model-based estimate with a transfer discount, or both.
5. **Readiness can be checked before real results:** weekly calibration (log loss, Brier, reliability chart) and Mock Exam predicted-vs-actual. About 16–64 Mock Exams across all Learners are enough to see a bias of ±1 to ±½ Question. The real check needs about **250–500 self-reported results** (≥ 100–200 passes and fails each). Keep the word "estimate" until then.
6. **Exam luck is ±2–3 Questions.** Even a perfect model cannot show a narrower range than about 23–28 for a Learner at 85 %. That is honest, not a model weakness.
7. **Desired retention 0.9 is a comfort/workload default, not a proven exam optimum.** Exam-deadline models favour reviewing nearer 33–40 % predicted recall when time is fixed. Keep it a setting and test it.
8. **Random choice is cheap if kept to near-ties plus 5 %.** It must be logged with the true probability. Turn it off under a backlog.
9. **Weak Themes: show, don't steer.** Theme steering of Reviews has no evidence on top of FSRS. Use exam-points ranking only when time is short.
10. **FSRS-7 is close but not ready.** `ts-fsrs` v6 is planned for 28 Oct 2026, but there is no released FSRS-7 optimiser yet. Build behind the one wrapper function (#7) and log the model version, so the switch is cheap later.

## Open questions

1. Who writes second Questions for heavy-Theme Rules, and are they reserved for Mock Exams? (#4 coverage, #8 Distractor Pool)
2. What is the guessing chance on multi-correct Questions in our UI? Does the Learner know how many Options are right? This sets g in section 3.2.
3. Should the readiness screen show P(pass) as well as the score range, or only the range (#20)?
4. When the first KETGO-wide fit is done, do we reschedule existing Learners at once (Anki's "reschedule on change") or only for future answers?
