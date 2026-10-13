# Learning techniques that make rules stick

Ticket: [#15 Learning techniques that make rules stick](https://github.com/Whirlywack/ketgo-web/issues/15) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1)

**Checked on 2026-10-13.** Sources are peer-reviewed papers and meta-analyses, plus the FSRS project's own benchmark and docs. Each claim links to its source. **UNVERIFIED** marks a number I could only find in a secondary summary, or a design guess that no study tests directly.

How to read the effect sizes: *g* or *d* = how far the average learner moves, in standard deviations. Roughly: 0.2 = small, 0.5 = medium, 0.8 = large. A medium effect (0.5) moves an average learner from the 50th to about the 69th percentile.

A warning before everything else: almost none of this research uses driving theory. Most of it uses students, facts, word pairs, science texts or maths. The Theory Exam is a picture-based multiple-choice test about rules and road situations, so the findings carry over well, but **no study here measured "pass rate at Regitra"**. KETGO has to measure that itself (see section C).

---

## A. Ranked table

Ranked by (strength of evidence × how well it fits the Theory Exam).

| # | Technique | Evidence strength | Effect in plain words | Fit for KET learning | What it needs (content / screen / data) |
|---|---|---|---|---|---|
| 1 | **Retrieval practice** (answer a Question from memory instead of re-reading the rule) | **Strong.** Several large meta-analyses, lab and classroom. | Answering Questions beats re-reading by a medium amount (classroom *g* ≈ 0.50). | Very high. The Theory Exam *is* a Question test, so practice and exam match. | Content: Own Questions. Screen: Question first, rule text after. Data: every answer. |
| 2 | **Spacing** (spread practice over days, not one long session) | **Strong.** Meta-analysis of 839 results; large web study; classroom software study. | The same study time gives much better memory later. Best gap grows with how long you must remember. | Very high. Learners have a fixed exam date, usually weeks away. | Content: none extra. Screen: "today's review", exam date at start. Data: timestamps of every answer. |
| 3 | **Feedback with a short "why"** after each answer | **Strong** that feedback helps; **moderate** that an explanation beats only showing the correct Option. Timing (now vs later) is **mixed**. | Feedback stops Distractors from being learned as facts. An explanation helps more than "correct/incorrect" alone. | Very high. | Content: short "why" per Question and a note per Distractor. Screen: inline under the Question. Data: whether the explanation was opened, and for how long. |
| 4 | **Successive relearning** (get it right, then get it right again in later sessions) | **Strong to moderate.** Lab plus classroom studies. | Re-learning in 3 later sessions is cheap and gives large long-term gains. Extra drilling on day 1 adds little. | High. This is what a "my mistakes" mode should be. | Content: none. Screen: missed Questions come back later in the same session and on later days. Data: per-Question history. |
| 5 | **Interleaving** (mix rules that are easy to confuse) | **Moderate.** One meta-analysis, *g* = 0.42 overall; depends on material. | Mixing similar categories helps you tell them apart. It *hurts* for simple word-like facts. Learners wrongly feel it is worse. | High for confusable rules (who goes first, look-alike signs, overtaking vs passing). Low for single facts. | Content: tag "easily confused with" between rules. Screen: mixed sessions by default. Data: theme and rule tags on every Question. |
| 6 | **Varied Questions for the same rule** (different picture or wording; new Distractor mix) | **Moderate** that varied practice transfers to new Questions. **Weak / no direct study** for changing only the Distractors. | Practice transfers to new Questions (*d* = 0.40), but transfer is weakest when the new Question just re-arranges old parts. | Very high. It attacks the top complaint: "95 % in the app, failed Regitra". | Content: ≥ 2 different Questions per rule matters more than many Distractors. Every Distractor must be a real misconception. Data: which Distractors were shown and chosen. |
| 7 | **Confidence check** ("Sure?") and the **hypercorrection effect** | **Moderate.** Many replications, including a classroom. Asking for ratings can itself change learning (**mixed**). | Mistakes made while *sure* are fixed best after feedback, but they also come back most if forgotten. | Medium-high. It finds dangerous misconceptions and gives calibration data. | Content: Exam Traps for common sure-and-wrong mistakes. Screen: one optional tap, no slider. Data: confidence per answer. |
| 8 | **Worked examples** (a solved road situation, step by step) | **Moderate.** Maths meta-analysis *g* = 0.48; "expertise reversal" meta-analysis. | Helps beginners a lot (*d* ≈ 0.5). Hurts learners who already know the topic (*d* ≈ −0.4). | Medium-high for situation pictures (priority, intersections). Must fade out as the learner improves. | Content: step-by-step for situation Questions. Screen: "show me how" on beginners' first misses. Data: learner level per theme. |
| 9 | **Pretesting** (guess first, then learn) | **Moderate.** Meta-analysis: *g* = 0.54 for the guessed Question, ≈ 0 for the rest of the lesson. | Guessing before the Rule Explainer helps you remember *that* point. It does not help other points. Some learners give up. | Medium. Good as one "guess first" Question before a new Rule Explainer. | Content: Rule Explainer right after. Screen: label "just guess". Data: flag pretest answers; do not count them in stats. |
| 10 | **Explaining "why" a rule exists** (elaborative interrogation) | **Moderate** (rated "moderate utility" by Dunlosky et al.). | Linking a rule to its reason helps memory. | High. Rules have reasons (safety, visibility). | Content: one "why" line in each Rule Explainer. |
| 11 | **Memory Hooks** (mnemonics) | **Low / mixed.** Keyword mnemonic rated "low utility"; gains often fade within days. | Fast short-term gain; fragile after a delay unless the learner is also tested. Pictures help. | Narrow. Useful for arbitrary numbers (distances, speeds, limits). Not for judging situations. | Content: hooks only for arbitrary facts, with a picture. Always followed by a Question. Data: a flag to A/B test hooks. |
| 12 | **Re-reading, highlighting, summarising** | Rated **low utility**. | Feels like learning, little effect. | Avoid as the main path. | Do not build a "read all rules" screen as the core. |
| — | **Desirable difficulty** (how hard practice should be) | A principle, not one technique. Evidence for "how hard" is **moderate for "not too hard", weak for an exact number**. | Practice should be effortful but mostly successful. With low success, testing can lose its benefit. | Applies to all of the above. | Data: predicted chance of success at serve time, so difficulty can be tuned. |

---

## B. Recommended for the beta

1. **Question first, then a short "why" (techniques 1, 3, 10).** In practice modes, show correct/incorrect at once, then a 1–3 sentence "why", plus a note on the Distractor the learner picked. Mock exam mode keeps feedback until the end, like the real Theory Exam. Feedback is not optional: without it, multiple-choice Questions can teach Distractors as facts.
2. **FSRS as the memory model, aimed at the exam date (techniques 2, 4).** Ask for the exam date at the start. Use FSRS with its default parameters and 90 % target retention. Never schedule a review after the exam date. In the last days, cover every theme in proportion to the exam blueprint (6/5/3/3/3/4/2/2/2). A missed Question comes back a few Questions later in the same session and again on a later day (successive relearning).
3. **Mixed sessions by default (technique 5).** After a learner first meets a rule, give a short block (2–3 Questions on that rule), then switch to mixing. Put rules that are easy to confuse next to each other on purpose. Tell learners that mixing feels harder but works better, because learners judge it wrongly.
4. **Vary the Question, not only the Distractors (technique 6).** Every rule should be tested by **at least 2 different Own Questions** (different picture or situation). Treat this as more important than a large Distractor Pool. Keep the Distractor Pool, but only with Distractors that are real misconceptions, and always shuffle Option order. Measure whether pool variation helps (see section D6).
5. **One-tap confidence (technique 7).** An optional "Not sure" tap before submit, defaulting to "sure". A sure-and-wrong answer gets the Exam Trap note (if one exists) and comes back sooner. Use the data to show learners when they are overconfident.
6. **New-rule flow: guess → Rule Explainer → worked example → practice (techniques 8, 9).** One "just guess" Question, then the Rule Explainer, then (for situation rules) a step-by-step worked example, then normal Questions. Pretest answers do not count in stats or readiness. Stop showing worked examples once the learner gets that theme mostly right.
7. **Memory Hooks only where they fit (technique 11).** Write Memory Hooks for arbitrary facts (numbers, limits) and attach Exam Traps to the most-chosen Distractors. Always follow a hook with a Question. Ship hooks behind a flag so their effect can be tested.
8. **Aim for "mostly right" (difficulty).** In review, prefer Questions the model predicts the learner gets right about 70–90 % of the time (UNVERIFIED range: a design starting point, not a tested number). Avoid long runs of failures; they also make learners quit.

---

## C. Log from day one

The rule: **store raw events, never only totals.** Every later model (FSRS fitted to KETGO data, ability models, bandits, readiness) is trained on history that cannot be rebuilt later. This matches the earlier design notes (`~/Documents/ketgo-grilled/DESIGN.md`, "append-only, event-sourced log").

### C1. One row per answer (the core event)

| Group | Fields |
|---|---|
| Who / when | pseudonymous learner id, session id, event id, time the Question was shown, time of submit (UTC + learner time zone), device type |
| What was shown | Question id **and content version**, rule / KET point ids, theme (1–9), picture id, **the Option ids shown, in the order shown** (so we know which Distractors came from the Distractor Pool), the correct Option set |
| What the learner did | selected Option ids, correct (all-or-nothing, like the Theory Exam), partial overlap for multi-correct, number of answer changes, response time, confidence tap (sure / not sure), explanation opened (yes/no) and time on it, which Memory Hook / Exam Trap / worked example was shown |
| Why it was shown (needed for bandits / RL) | mode (learn, review, pretest, mock exam, free practice), scheduler reason, **model version**, **predicted chance of a correct answer at serve time**, **the candidate Questions the scheduler chose from, and the probability it gave the chosen one** (the "propensity"), experiment flags and arm |
| Learner context | exam date as entered (and every change), days to exam, position in session, time since this Question and this rule were last seen |

### C2. Other events

- **Mock exams:** the 30 Questions, the per-Question results, the score, pass/fail, and the readiness value we showed *before* the mock exam.
- **Real Theory Exam result:** after the exam date, ask "Did you take the Theory Exam? Did you pass? Which attempt?" This is the only true label for readiness. Without it, readiness can never be checked.
- **Rule Explainer views:** which one, how long, scroll depth.
- **Session start/end and return visits** (to see drop-off).
- **Content changes:** a version log for every Question, Option and explanation, so old answers can be linked to the text the learner actually saw.

### C3. Two small design rules that make later AI possible

1. **Some controlled randomness.** Offline testing of a new bandit policy needs logged choices that were at least partly random, with the probability stored ([Li et al. 2011](https://arxiv.org/abs/1003.5956) assume random logging, or a known logging probability). So: among the scheduler's top few candidates (all good for learning), pick with a known random rule and store the probability. This costs learners almost nothing.
2. **Keep learning science as the guard rail.** A review of RL for teaching found it worked best when limited by learning-science ideas and checked with robust offline analysis ([Doroudi, Aleven & Brunskill 2019](https://doi.org/10.1007/s40593-019-00187-x)). So the bandit should choose *among* evidence-based options (which rule to review, which Distractor mix, hook on/off). It should not invent the method.

---

## D. Details with citations

### D1. Retrieval practice (active recall)

- Dunlosky et al. reviewed 10 study techniques and rated **practice testing** and **distributed practice** the only two of "high utility". Summarising, highlighting and rereading were rated low ([Dunlosky et al. 2013, *PSPI* 14(1)](https://doi.org/10.1177/1529100612453266); ratings confirmed via [APS press release](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html) and the authors' summary in [American Educator, 2013](https://www.aft.org/ae/fall2013/dunlosky)).
- Classroom meta-analysis: 222 studies, 48,478 students. Quizzing raised achievement by *g* = 0.499. Its size depended on, among other things, whether corrective feedback was given and how many times learners were tested ([Yang et al. 2021, *Psychological Bulletin*](https://consensus.app/papers/details/d5865595581856df817e7452b18cbdc4/)).
- Practice tests beat restudying and every other comparison condition ([Adesope, Trevisan & Sundararajan 2017, *Review of Educational Research*](https://doi.org/10.3102/0034654316689306)). The pooled *g* = 0.61 is reported only in secondary summaries: **UNVERIFIED**.
- Testing vs restudy, lab meta-analysis: *g* ≈ 0.50, larger with feedback (≈ 0.73 vs 0.39 without) ([Rowland 2014, *Psychological Bulletin*](https://doi.org/10.1037/a0037559)). These numbers come from secondary summaries: **UNVERIFIED** against the full text.
- KET fit: the Theory Exam is multiple-choice, and well-built multiple-choice Questions do cause real retrieval when the Distractors are plausible ([Little et al. 2012, *Psychological Science*](https://consensus.app/papers/details/dc5205afe7a352c79c2c4403d1c4a859/)).

### D2. Spacing, and FSRS vs SM-2 vs Leitner

**Spacing works.** A meta-analysis of 839 assessments in 317 experiments found that the best gap between sessions grows as the time until the test grows ([Cepeda et al. 2006, *Psychological Bulletin*](https://consensus.app/papers/details/a804ac03928753dbaff03c4b92036866/)). In a study of 1,350+ people, the best gap was about **20–40 % of a 1-week test delay** and **5–10 % of a 1-year delay** ([Cepeda et al. 2008, *Psychological Science*](https://consensus.app/papers/details/34958740cf745be8a116db57e78c849c/)). The same pattern held in 10,514 workplace learners ([Kim et al. 2019](https://consensus.app/papers/details/ac07cbd03fa555a3834346a03ac1d07c/)).

**Personalised spacing beats fixed spacing.** In a semester-long school course, review chosen by a memory model gave **+16.5 %** retention vs massed study and **+10.0 %** vs one-size-fits-all spacing ([Lindsey et al. 2014, *Psychological Science*](https://home.cs.colorado.edu/~mozer/Research/Selected%20Publications/reprints/LindseyShroyerPashlerMozer2014.pdf)).

**Algorithms compared.** The open FSRS benchmark uses about 10,000 Anki users and ~350 million reviews. It scores how well each algorithm predicts whether a card will be remembered (log loss and RMSE(bins); lower is better) ([srs-benchmark README](https://github.com/open-spaced-repetition/srs-benchmark)).

| Algorithm | Log loss | RMSE (bins) | Source |
|---|---|---|---|
| FSRS-7 (newest) | 0.337 | 0.059 | current README |
| FSRS-6 | 0.346 | 0.065 | current README |
| FSRS-7 with *default* parameters (no fitting) | 0.362 | 0.091 | current README |
| HLR (Duolingo) | 0.469 | 0.128 | current README |
| SM-2 (classic Anki / SuperMemo) | 0.72 | 0.203 | [Nov 2024 README](https://github.com/open-spaced-repetition/srs-benchmark/blob/06587123dee85246162867f5a1beb678378db5cc/README.md) |

- That README says FSRS-5 beat SM-2 for **99.0 % of users**, but warns that SM-2 was never designed to output probabilities, so extra formulas were added to it ([Nov 2024 README](https://github.com/open-spaced-repetition/srs-benchmark/blob/06587123dee85246162867f5a1beb678378db5cc/README.md)).
- **Leitner boxes are not in the benchmark.** Leitner gives no probability of recall, so it cannot feed a readiness score. How it compares on memory is **UNVERIFIED**.
- FSRS models memory as stability *S* and retrievability *R*. FSRS-6 uses R(t,S) = (1 + factor·t/S)^(−w20), with 21 parameters and published defaults ([FSRS algorithm wiki](https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm)). Anki's default target is **90 % retention**. Above 90 % the workload "increases very quickly", and Anki advises staying below 97 % ([Anki manual, deck options](https://docs.ankiweb.net/deck-options.html)).

**Limits for KETGO.**
- The benchmark is self-graded flashcards with 4 buttons. KETGO has auto-graded multiple-choice: pass/fail only, with guessing possible. Default FSRS parameters will be less accurate for us until we fit them on our own data.
- FSRS models one card. The Theory Exam tests *rules* through *new* Questions. So we need memory per Question plus a roll-up per rule.
- **Aiming at an exam date:** FSRS has no built-in deadline. This is a design inference, not a tested method: use FSRS to predict *R* on exam day for each rule. Choose reviews that raise the predicted exam-day pass chance most. Keep gaps roughly in line with Cepeda's ratio (for an exam in 4 weeks, gaps of a few days). Never schedule past the exam date.

### D3. Interleaving vs blocking

- Meta-analysis of 59 studies: overall *g* = 0.42. Best for visual material (paintings *g* = 0.67) and maths (*g* = 0.34). **Blocking won for word material (*g* = −0.39)**, and expository texts were unclear. Interleaving helped more when categories were **similar to each other** and complex ([Brunmair & Richter 2019, *Psychological Bulletin*](https://consensus.app/papers/details/621345c33c1c5d6ab95c10b54896bbb1/)).
- Classroom RCT in 54 maths classes: interleaved 61 % vs blocked 38 % one month later, *d* = 0.83 ([Rohrer et al. 2019](https://consensus.app/papers/details/9981c1c7ff815a94907701539d2d89cc/)).
- Learners judged massed study as better even when their own scores showed the opposite ([Kornell & Bjork 2008, *Psychological Science*](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/Kornell_Bjork_2008_PsychScience.pdf)). So KETGO should choose the mix, not leave it to the learner.
- A mix of some blocked and some interleaved practice also beat blocked-only ([Mielicki et al. 2022](https://consensus.app/papers/details/19acbe6ef72650e99d7821ce5df272f2/)).
- KET fit: many Theory Exam Questions are picture situations that need *discrimination* (which rule applies here?). That is where interleaving is strongest. Isolated facts (a number) are closer to "words", where it may not help.

### D4. Feedback: when and what kind

- Multiple-choice testing without feedback can make learners later give the Distractors as answers, and more Distractors make this worse ([Roediger & Marsh 2005, *JEP:LMC*](https://doi.org/10.1037/0278-7393.31.5.1155)). Feedback, immediate or delayed, raised later correct answers and **reduced these intrusions** ([Butler & Roediger 2008, *Memory & Cognition*](https://pubmed.ncbi.nlm.nih.gov/18491500/)).
- **Timing is mixed.** In lab studies, delayed feedback beat immediate feedback, probably because the delay adds spacing ([Butler, Karpicke & Roediger 2007, *JEP: Applied*](https://profiles.wustl.edu/en/publications/the-effect-of-type-and-timing-of-feedback-on-learning-from-multip/)). An older meta-analysis found the opposite in applied classroom studies: immediate feedback usually won there ([Kulik & Kulik 1988, *RER* 58(1)](https://journals.sagepub.com/toc/rera/58/1), as summarised by [Smith & Kimball 2010](https://www.ou.edu/memorylab/pdfs/SmithKimball_2010_LearningFromFeedback_ms.pdf); details **UNVERIFIED** against the full text). A computer-based feedback meta-analysis also linked delayed feedback to smaller effects ([van der Kleij et al. 2015](https://acuresearchbank.acu.edu.au/item/86y84/effects-of-feedback-in-a-computer-based-learning-environment-on-students-learning-outcomes-a-meta-analysis)).
  → For KETGO: immediate feedback in practice (a learner on a phone may leave before delayed feedback arrives), and the spacing comes from the scheduler instead.
- **Type:** in computer-based learning, elaborated feedback (with explanation) *ES* ≈ 0.49, correct answer only ≈ 0.32, "right/wrong" only ≈ 0.05 ([van der Kleij, Feskens & Eggen 2015, *RER* 85(4)](https://people.acer.org/en/publications/effects-of-feedback-in-a-computer-based-learning-environment-on-s/)). A later network meta-analysis (77 studies) also ranked elaborated feedback most likely to be best ([Mertens, Finn & Lindner 2022](https://www.leibniz-ipn.de/en/research/publications/effects-of-computer-based-feedback-on-lower-and-higher-order-learning-outcomes)).

### D5. Confidence checks and the hypercorrection effect

- Mistakes made with high confidence are **more** likely to be corrected after feedback, not less ([Butterfield & Metcalfe 2001](https://consensus.app/papers/details/ec26368ccc7a5a9085c3791e95c4a06e/)). A likely reason: surprising feedback gets more attention ([Butterfield & Metcalfe 2006](https://consensus.app/papers/details/783416579afb58f186fba4122f556ca4/); [Fazio & Marsh 2009](https://consensus.app/papers/details/41f0bb370c5b5ca3ace9ccb97f781c72/)).
- It also appeared in a real college class ([Carpenter et al. 2018](https://consensus.app/papers/details/22663195ea795b9f92b7b07ca6c7c00d/)) and in 219,826 online school maths answers ([Foster et al. 2021](https://consensus.app/papers/details/650ae4c2bde15a59a480776f0423a580/)).
- **Catch:** after a week the effect remained, but high-confidence errors were also **more likely to come back** if the correct answer was forgotten ([Butler, Fazio & Marsh 2011](https://consensus.app/papers/details/f970030e32b2586da064f23681499545/)). → Re-ask sure-and-wrong Questions sooner.
- Rating confidence for every Option (confidence-weighted multiple-choice) improved later answers to *new related* Questions over standard multiple-choice ([Sparck, Bjork & Bjork 2016](https://consensus.app/papers/details/0d819a07a8fc5f839d4c20f1f7a0cea3/)).
- **Mixed:** asking learners to rate their memory can itself change learning. In one study a required rating reversed the usual testing benefit ([Higham et al. 2023](https://consensus.app/papers/details/94c801d2b505524ea9e786511d0e7feb/)). Meta-analyses of this "reactivity" disagree: about zero overall in [Double, Birney & Walker 2018](https://durham-repository.worktribe.com/output/2253677/a-meta-analysis-and-systematic-review-of-reactivity-to-judgements-of-learning), and small positive in Ingendahl, Halamish & Undorf 2025 (**UNVERIFIED**, seen only in a search summary). → Keep it to one optional tap, and A/B test it.

### D6. Varying Distractors between repeats (does a Distractor Pool help or hurt?)

**No study I found tests "same Question, different Distractors each time" directly. That exact claim is UNVERIFIED.** The nearest evidence:

- **For variation (helps):** testing transfers to *new* Questions (*d* = 0.40), most to application and inference Questions. It transfers **least to re-arranged versions of the same Question** ([Pan & Rickard 2018, *Psychological Bulletin*](https://consensus.app/papers/details/c5cee08032d85fd58244269b72d268a6/)). The authors warn that once publication bias is corrected, transfer is often near zero unless certain conditions hold, such as elaborated retrieval. Repeated testing beat repeated study on new inference Questions ([Butler 2010](https://consensus.app/papers/details/a2891bb1b6dc5e3c93866dfd06291350/)). In middle-school science, quizzes helped exam Questions that were new versions about the same content as much as identical ones ([McDaniel et al. 2013](https://consensus.app/papers/details/f06e918f0d4950ea84fd8548152cc4ef/)). In the same paper, *application* quizzes helped both definition and application exam Questions, but *definition* quizzes did not help application Questions. → Practise rules through road situations, not by asking for the rule text.
- **In a real course,** asking a *new* Question about the same concept each time gave better transfer than repeating the same Question, but "not as strongly as predicted". Lower-aptitude students did *worse* on new final-exam Questions in the varied condition ([Foss et al. 2023](https://consensus.app/papers/details/fe3c5b77e9855a3890974f8766c80f3b/)).
- **Plausible Distractors help:** competitive Distractors make learners retrieve why each one is wrong. That improves later answers on related Questions ([Little et al. 2012](https://consensus.app/papers/details/dc5205afe7a352c79c2c4403d1c4a859/); [Little et al. 2014, *Memory & Cognition*](https://consensus.app/papers/details/7badef67cdd851e0987003cae1ab7947/)).
- **Risk (hurts):** more Distractors seen means more chance of learning a false fact, but feedback removes most of this ([Roediger & Marsh 2005](https://doi.org/10.1037/0278-7393.31.5.1155); [Butler & Roediger 2008](https://pubmed.ncbi.nlm.nih.gov/18491500/)).

**Verdict:** a Distractor Pool is *probably helpful, or at least not harmful*, if every Distractor is a real, plausible misconception and feedback always follows. But it is a weaker lever than **writing a second, genuinely different Question for each rule**. Shuffling Options and changing Distractors stops learners from remembering "the second Option, the long one". Only a new situation forces them to apply the rule. Test the pool with a randomised flag (pool vs fixed Distractors) and compare accuracy on *never-seen* Questions.

### D7. Memory Hooks, worked examples, and teaching before practice

- **Memory Hooks (mnemonics):** Dunlosky et al. rated the keyword mnemonic and imagery for text "low utility" ([Dunlosky et al. 2013](https://www.aft.org/ae/fall2013/dunlosky)). Keyword learners did better at once but *worse* after 2 days than learners using meaning-based study ([Wang et al. 1995](https://consensus.app/papers/details/2f70a933958556c1947143e535a712e7/)). Giving a picture helped long-term retention ([Thomas et al. 1996](https://consensus.app/papers/details/4f548d73584557b9928f18d776c9af50/)). → Hooks are fine for arbitrary facts, with a picture, and always followed by retrieval.
- **Worked examples:** maths meta-analysis, *g* = 0.48 (55 studies) ([Barbieri et al. 2023](https://doi.org/10.1007/s10648-023-09745-1)). Expertise-reversal meta-analysis (60 studies): beginners gain from more help (*d* = 0.505), while learners with more knowledge do better with less help (*d* = −0.428) ([Tetzlaff et al. 2025](https://consensus.app/papers/details/7b980614e49a5ab7a2eb2c6643d67ba5/)). Fading worked examples to match each learner beat fixed fading in a tutoring system ([Salden et al. 2010](https://consensus.app/papers/details/c57a1f11134c5c659cf36b22099d6ddf/)).
- **Pretesting (guess first):** benefits are well shown when learners study the correct answer afterwards ([Pan & Carpenter 2023](https://consensus.app/papers/details/8d88a6d146c65df182d1bcda7966b8f3/)). Preregistered meta-analysis: *g* = 0.54 for the pre-asked content, *g* = 0.04 for other content ([St. Hilaire, Chan & Ahn 2023](https://consensus.app/papers/details/ae47f3256d405351ba11ef75d04f388d/)). In 30 real classes (n = 1,571), prequestions helped on average, but some students skipped the video afterwards, and the benefit went mostly to students who already knew more ([Motz et al. 2025](https://consensus.app/papers/details/caa6fab33e845e8bbc5ed856ef954bb5/)). → One gentle "just guess" Question per new rule, not a hard test at the start.
- **Rule Explainer with a "why":** elaborative interrogation and self-explanation were rated "moderate utility" ([Dunlosky et al. 2013](https://www.aft.org/ae/fall2013/dunlosky)).

### D8. Successive relearning

- Practise to 3 correct recalls, then relearn 3 times at wide intervals. Relearning gave large long-term gains at low extra cost ([Rawson & Dunlosky 2011](https://consensus.app/papers/details/274149f10b225287956727743a98072b/)). Extra correct answers on day 1 stopped mattering once relearning happened ([Vaughn et al. 2016](https://consensus.app/papers/details/9cf633dd7c125e9e86b512d44a071b64/)). It beat restudy in a real course, with lower anxiety and a higher sense of mastery ([Higham et al. 2021](https://consensus.app/papers/details/451ef4da8f0c5561ab8a5de27bcdfa48/)).

### D9. Desirable difficulties, and how much is too much

- Testing can *lose* its benefit when practice success is low. A feedback-driven reversal of the testing effect appeared only at low retrieval success, not at moderate or high success ([Racsmány et al. 2020](https://consensus.app/papers/details/feb06aeec29651738bd6dfa63aae4177/)).
- Practice quizzes **reduce** test anxiety (*g* = −0.52), and easy quizzes reduce it more than hard ones ([Yang et al. 2023](https://consensus.app/papers/details/b59a30c6ddd058ecb7d98e45c4d52c9a/)).
- The "85 % rule" (about 15 % errors is optimal) comes from a mathematical model of machine learners, not human studies. Even its lead author says the exact number matters less than the idea of a sweet spot ([Wilson et al. 2019, *Nature Communications*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6831579/)). → **Weak** as a number for humans.
- FSRS/Anki's default 90 % target retention fits this "mostly right" zone ([Anki manual](https://docs.ankiweb.net/deck-options.html)).
- Practical rule for KETGO (**UNVERIFIED**, to be tuned with data): about 70–90 % predicted success in review; lower is fine for a pretest, which does not count; break up long runs of misses with an easier Question or a Rule Explainer.

### D10. Bandits / reinforcement learning later

- RL-chosen teaching sequences beat baselines in a little over half of the studies reviewed. RL worked best when limited by learning-science theory and checked with robust offline analysis ([Doroudi, Aleven & Brunskill 2019](https://doi.org/10.1007/s40593-019-00187-x)).
- An unbiased offline "replay" test of a new bandit policy needs logs where actions were chosen at random, or with known probabilities ([Li, Chu, Langford & Wang 2011](https://arxiv.org/abs/1003.5956)). This is why section C asks for the candidate set and the selection probability.

---

## Open questions this raises

1. **Memory per Question or per rule?** Coverage work (#4) found ~230 KET points with about one Own Question each. Variation (D6) and transfer need ≥ 2 Questions per rule, so the question-writing plan may need to change.
2. **How do we get the real Theory Exam result?** It is the only true check for readiness. A follow-up prompt after the exam date? A reason to come back?
3. **Randomised exploration:** is the owner fine with a small, logged random choice among good options (needed for later bandits)?
4. **Distractor Pool vs a second Question:** which gives more learning per hour of writing? Run it as an experiment in the beta.
5. **Confidence tap:** is the friction worth it on a phone? A/B test it (reactivity is mixed).
