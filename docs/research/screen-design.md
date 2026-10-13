# Screen design that helps learning

Ticket: [#20 Screen design that helps learning](https://github.com/Whirlywack/ketgo-web/issues/20) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1) · Builds on [#15 Learning techniques](https://github.com/Whirlywack/ketgo-web/blob/research/learning-techniques/docs/research/learning-techniques.md), [#17 Session rhythm](https://github.com/Whirlywack/ketgo-web/blob/research/session-rhythm/docs/research/session-rhythm.md) and [Regitra exam rules](https://github.com/Whirlywack/ketgo-web/blob/research/regitra-exam-rules/docs/research/regitra-exam-rules.md).

**Checked on 2026-10-13.** Sources are peer-reviewed papers and meta-analyses, plus one official guideline (W3C WCAG). Each claim links to its source, by DOI where one exists. **UNVERIFIED** marks a number I could only find in a secondary summary. **Design guess** marks a rule that no study tests directly. It is a starting point to A/B test in the beta.

**Method note.** The Consensus search tool could not be used: its monthly quota (30 searches) was already used up and resets on 1 November. So I found papers through OpenAlex, Semantic Scholar and Crossref instead. I checked each paper's title, authors, year and abstract on the publisher page, PubMed/PMC, or the DOI record, and I cite it by DOI.

**What #15 already settled, and is not repeated here:** feedback with a short "why" is required; an explanation beats "correct / incorrect" alone; practice gives feedback at once, a Mock Exam only at the end; one optional confidence tap; sure-and-wrong mistakes come back sooner (hypercorrection).

**How to read effect sizes:** the same as in #15. *g* or *d* of 0.2 is small, 0.5 is medium, 0.8 is large.

**Warning:** almost none of this research uses phones, and none uses driving theory. Most feedback studies use students at a computer. Most gamification studies use university courses. So many rules below are "moderate" at best for KETGO, and several are design guesses to test in the beta.

---

## A. Design rules

Evidence strength: **Strong** = several meta-analyses or many replications, and a good fit for KETGO. **Moderate** = one meta-analysis or several good studies, or strong evidence that fits KETGO only indirectly. **Weak** = one study, or a different field. **Design guess** = no direct study.

### A1. Question screen on a phone ([#11](https://github.com/Whirlywack/ketgo-web/issues/11))

| # | Rule | Evidence | Section |
|---|---|---|---|
| Q1 | After the learner answers, **show the correct Option(s) at once**, with the "why". Do not offer "try again" on the same screen. The second try is the re-ask later in the Lesson, with shuffled Options (as #5 already plans). | Moderate | B1.1 |
| Q2 | **Feedback starts with one line: the verdict plus the key point of the Rule.** Then 1–2 short sentences of "why", plus a note on the Distractor the learner picked. The full Rule Explainer and any Memory Hook sit behind one tap. Aim for 40 words or fewer before the tap. | Moderate for "short and focused"; the 40 words is a design guess | B1.3 |
| Q3 | **Put the "why" directly under the picture and the Question, on the same screen.** Mark the key part of the picture (a circle or an arrow) and bold the key words. | Moderate to strong (meta-analyses, but not on phones) | B1.3 |
| Q4 | **No extras in the "why":** no fun facts, jokes or pictures that do not explain the Rule. | Moderate | B1.3 |
| Q5 | **Colour + icon + word, never colour alone.** Green ✓ "Correct" / red ✗ "Wrong", with the correct Option marked. Red for "wrong" is fine. Use enough contrast. | Strong (official guideline) for "not colour alone"; moderate that red does no harm | B1.2 |
| Q6 | **No timer that moves on by itself.** One big "Continue" button at the bottom. After a correct and sure answer, keep the feedback short (the "why" folded to one line) so the learner can move on fast. After a wrong or unsure answer, show the "why" open. | Moderate | B1.4 |
| Q7 | **Confidence without an extra tap:** the main button is "Check" (= sure). A smaller "Not sure – check" button sits next to it. Use the answer to choose the feedback: unsure + correct → "why" open; sure + wrong → Exam Trap and an earlier re-ask (#15). | Moderate that knowing confidence helps; design guess for the two buttons | B1.5 |
| Q8 | **Talk about the Rule, not the person.** No "Genius!", no "Oops, you failed". After a wrong answer, always say how to get it right. After a missed "New rule, take a guess", say that missing a first guess is normal. | Moderate | B1.6 |
| Q9 | **Pleasant colours and friendly visuals on the screen** (the owner's "easy and beautiful"), but keep the explanation itself plain. | Moderate | B1.2 |
| Q10 | **Big tap targets.** Each Option is a full-width row, at least about 9–10 mm tall (roughly 44–48 px). Never below WCAG's 24 px minimum. | Moderate (one touch-screen study + official guideline) | B1.2 |
| Q11 | **Progress inside a Lesson only moves forward.** Count Rules (or Questions) done. A re-asked Question must not make the bar go back. | Weak (web-survey studies, not learning) | B3.1 |
| Q12 | **Expect many learners to skip the "why".** Weaker learners skip it most. So the key point must be in the verdict line itself. Log "why opened" and time spent on it (#15 log list). | Moderate | B1.3 |

### A2. Progress and readiness screen ([#13](https://github.com/Whirlywack/ketgo-web/issues/13))

| # | Rule | Evidence | Section |
|---|---|---|---|
| P1 | **Show progress the learner can act on:** Lesson X of Y; Rules Remembered / Learning / Not met yet per Theme; a "practise" button on each Theme. | Moderate | B3.1, B3.2 |
| P2 | **Early in the Program, show what is done** ("18 Rules Remembered"). **Near the end, show what is left** ("4 Lessons left"). | Moderate | B3.1 |
| P3 | **Do not lead with a bar that starts slowly.** Overall "Rules Remembered" stays near zero for weeks, because Remembered means "still known on exam day". Lead with Lessons done; show Remembered as counts per Theme. | Weak to moderate | B3.1 |
| P4 | **Keep "Remembered" strict and honest.** Never inflate a state to motivate. A threshold that is too easy creates false confidence. | Strong that overconfidence harms learning; moderate on thresholds | B3.2, B3.3 |
| P5 | **Build readiness only from evidence that predicts the exam:** first answers to Questions the learner has not seen before, and Mock Exams. Never from repeats of the same Question. | Moderate | B3.3 |
| P6 | **Show readiness as a band word + a predicted Mock Exam score with a range, in exam units** ("Nearly ready: about 26 of 30, likely 23–28. Pass is 24."). Do not make a bare "87 % pass chance" the headline. | Moderate for "number with a range, plus words" (risk-communication research, not learners); the exact wording is a design guess | B3.4 |
| P7 | **Always pair readiness with the next step** ("Theme 4 is weak. Practise it."). A score alone teaches less than a score with advice. | Moderate | B3.3 |
| P8 | **Show learners their own overconfidence, kindly:** "You were sure on 12 answers. 3 of them were wrong." | Weak to moderate | B3.3 |
| P9 | **Call readiness an "estimate" until it has been checked against real exam results** (#15, section C2). | Moderate | B3.3 |
| P10 | **No leaderboards and no XP points.** | Moderate | B4 |
| P11 | **Milestones are fine if they mark learning:** a Lesson done, a Theme fully Remembered, a first Mock Exam passed. No badges for time spent or for taps. | Weak to moderate | B4 |
| P12 | **Keep #5's "no day streak".** If a consistency display is ever tested, show what was done this week, let a missed day be repaired, and never show a broken chain. | Moderate | B4 |
| P13 | **Celebrate the learning, not the learner:** "The right-hand rule is now Remembered", not "You're amazing!". | Moderate | B1.6, B4 |
| P14 | **Do not rely on game elements to carry a 4–6 week Program.** Their pull tends to fade after about 4 weeks. | Weak (one long study) | B4 |

### A3. Answering multi-correct Questions ([#8](https://github.com/Whirlywack/ketgo-web/issues/8))

| # | Rule | Evidence | Section |
|---|---|---|---|
| M1 | **Checkboxes on every Question, also single-correct ones, exactly like Regitra.** Never radio buttons: they tell the learner "only one is correct". | Strong (exam facts) | B2 |
| M2 | **Never say how many Options are correct,** in practice or in a Mock Exam. One standing hint, shown as a first-time tip: "One or more Options can be correct. Check each one." | Moderate | B2 |
| M3 | **The verdict is all-or-nothing, like the exam, also in practice.** The Question counts as right (for FSRS, stats and readiness) only if every correct Option and no wrong one is ticked. | Moderate | B2 |
| M4 | **Feedback is per Option:** ✓ correct and ticked, ✗ ticked but wrong, ○ "missed" (correct but not ticked). Give the "why" for the wrong and missed Options. Do not show a partial score such as "2/3". | Moderate for per-Option feedback; design guess for "no partial score" | B2 |
| M5 | **Log per-Option results for analysis, not for scoring** (already in the #15 log list as "partial overlap"). | Design guess | B2 |
| M6 | **Practice and Mock Exam answer the same way** (same checkboxes, same "Check"). Only the feedback timing differs. | Moderate | B2 |
| M7 | **Distractor Pool on multi-correct Questions:** because the count is never shown, the number of correct Options shown may change between repeats. No study tests this; A/B test it. | Design guess | B2 |

Cost to accept: with checkboxes everywhere, every Question needs a "Check" tap. That is one tap more than "tap an Option to answer". It is the price of practising the way the exam works.

---

## B. Details with citations

### B1. Feedback after an answer

#### B1.1 Show the answer at once, or let the learner try again?

- **Trying again teaches no more than being shown the answer.** Learners who kept answering until correct did as well on a later test as learners who were simply shown the correct answer ([Butler, Karpicke & Roediger 2007, *JEP: Applied*](https://doi.org/10.1037/1076-898x.13.4.273)).
- **An explanation beats trying again.** In 97 students answering 36 hard science Questions, explained feedback raised later recall more than answer-until-correct. Both kinds of feedback lifted mood more than no feedback, even after wrong answers ([Mertens & Lindner 2025, *JCAL*](https://doi.org/10.1111/jcal.13112)).
- **Learners like "try again"**: students rated an answer-until-correct format very highly ([DiBattista, Mitterer & Gosse 2004](https://doi.org/10.1080/1356251032000155803)). Liking it is not the same as learning more from it.
- **Timing update to #15:** #15 called feedback timing "mixed". A newer meta-analysis (51 studies, 160 effect sizes) found **no difference on average** between immediate and delayed feedback in computer-based learning (*g* = 0.03), with large differences between contexts ([Kandemir et al. 2026, *Educational Psychology Review*](https://doi.org/10.1007/s10648-026-10117-8)). So immediate feedback in practice costs nothing.
- **KETGO reasoning:** with 3–4 Options, a second try right after a miss is mostly elimination (a 1-in-2 or 1-in-3 guess). With multi-correct Questions, "try again" gets confusing. The re-ask later in the Lesson (#5) is a better second try, because it adds spacing.

#### B1.2 Colour, icons and touch

- **Official rule:** "Color is not used as the only visual means of conveying information". WCAG names green-for-valid / red-for-invalid as a case that needs an extra marker ([WCAG 2.2, SC 1.4.1, Level A](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)).
- **Why it matters:** about 8 % of European men and 0.4 % of women have red-green colour deficiency ([Birch 2012, *JOSA A*](https://doi.org/10.1364/josaa.29.000313)).
- **Red is fine.** An early study found that seeing red before a test lowered scores ([Elliot et al. 2007](https://doi.org/10.1037/0096-3445.136.1.154)). A meta-analysis of 67 effect sizes later found no effect on knowledge tests (*d* = −0.04), and no evidence of any effect after correcting for publication bias ([Gnambs 2020, *Psychonomic Bulletin & Review*](https://doi.org/10.3758/s13423-020-01772-1)). Regitra's own demo review also marks correct Options green and wrong ones red ([Regitra exam rules](https://github.com/Whirlywack/ketgo-web/blob/research/regitra-exam-rules/docs/research/regitra-exam-rules.md)).
- **Pleasant design helps a little.** Pleasant colours and friendly faces in learning graphics improved retention (*d* = 0.39) and transfer (*d* = 0.33), raised intrinsic motivation (*d* = 0.26), and made material feel less difficult (33 samples, N = 2,924) ([Brom, Stárková & D'Mello 2018, *Educational Research Review*](https://doi.org/10.1016/j.edurev.2018.09.004)).
- **Tap targets:** for one-handed thumb use, targets of 9.2 mm (single taps) and 7.6 mm (series of taps) were large enough without hurting speed or errors ([Parhi, Karlson & Bederson 2006, MobileHCI](https://doi.org/10.1145/1152215.1152260)). WCAG's minimum is 24 × 24 CSS px, Level AA ([WCAG 2.2, SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)).

#### B1.3 How long should the "why" be?

- **A review of feedback research gives these guidelines:** "Provide elaborated feedback in small enough pieces so that it is not overwhelming and discarded", and "Keep feedback as simple and focused as possible. Generate only enough information to help students and not more." It also cites a study where too complex feedback did not help more than simpler feedback ([Shute 2008, *Review of Educational Research*, Table 2](https://doi.org/10.3102/0034654307313795)).
- **Interesting but irrelevant extras hurt learning** ("seductive details"). Two meta-analyses agree ([Rey 2012](https://doi.org/10.1016/j.edurev.2012.05.003); [Sundararajan & Adesope 2020](https://doi.org/10.1007/s10648-020-09522-4), 58 papers, 68 effect sizes). The size reported in summaries is about *g* = −0.33 (**UNVERIFIED** against the full text).
- **Overview of all multimedia meta-analyses** (29 reviews, 1,189 studies, 78,177 people): the largest benefits came from **putting words next to the picture they explain** and from **signaling** (highlighting what matters). Removing extras and splitting content into pieces also had robust effects ([Noetel et al. 2022, *Review of Educational Research*](https://doi.org/10.3102/00346543211052329)).
  - Words next to the picture: *g* = 0.63 (58 comparisons) ([Schroeder & Cenkci 2018](https://doi.org/10.1007/s10648-018-9435-9)).
  - Signaling (bold key words, arrows, highlights): retention *g* = 0.53, transfer *g* = 0.33, with lower cognitive load (103 studies, N = 12,201) ([Schneider et al. 2018](https://doi.org/10.1016/j.edurev.2017.11.001)).
- **Many learners skip long feedback.** In a German grammar app (20,058 cases, 2,826 students), students with more prior knowledge were far more likely to open the error feedback (odds ratio 6.85). Many students clicked through quickly ([Maier & Klotz 2025, *Contemporary Educational Psychology*](https://doi.org/10.1016/j.cedpsych.2025.102395)). Earlier work found that students look at feedback mostly after wrong answers ([Timmers & Veldkamp 2011](https://doi.org/10.1016/j.compedu.2010.11.007), as summarised by Maier & Klotz).
- **Verdict:** one key line, then 1–2 sentences, next to the picture, with the key part marked. The 40-word limit is a design guess to test.

#### B1.4 Move on automatically, or tap to continue?

No study compares a timer with a "Continue" button in a learning app. The nearest evidence:

- **Feedback matters most after errors.** Showing the correct answer after an error raised retention a week later by 494 %. Feedback after correct answers made little difference ([Pashler et al. 2005, *JEP: LMC*](https://doi.org/10.1037/0278-7393.31.1.3); word pairs, N = 258).
- **Except for unsure correct answers.** In multiple-choice tests, feedback **doubled** the retention of correct answers given with low confidence ([Butler, Karpicke & Roediger 2008, *JEP: LMC*](https://doi.org/10.1037/0278-7393.34.4.918)). Plain right/wrong feedback also helped low-confidence correct answers ([Fazio et al. 2010, *Memory*](https://doi.org/10.1080/09658211003652491)).
- **Feedback costs time.** When total study time was fixed, giving feedback could hurt overall. Learners allowed to skip unneeded feedback did so and gained from it ([Hays, Kornell & Bjork 2010, *Psychonomic Bulletin & Review*](https://doi.org/10.3758/pbr.17.6.797)).
- **Self-pacing:** good design matters more when the system sets the pace than when the learner does ([Noetel et al. 2022](https://doi.org/10.3102/00346543211052329)). Splitting material into segments helps learning, with small to medium effects ([Rey et al. 2019, segmenting meta-analysis](https://doi.org/10.1007/s10648-018-9456-4)).
- **Verdict:** a timer risks cutting off the feedback that matters (after a wrong or unsure answer). After a sure, correct answer, feedback adds little, so make that screen short and quick to leave.

#### B1.5 A confidence check before the reveal: help or delay?

- **What it buys:** confidence tells us which feedback is worth the learner's time. Sure + correct: feedback adds little ([Pashler et al. 2005](https://doi.org/10.1037/0278-7393.31.1.3)). Unsure + correct: feedback doubles retention ([Butler et al. 2008](https://doi.org/10.1037/0278-7393.34.4.918)). Sure + wrong: best corrected, but comes back most ([Butler, Fazio & Marsh 2011](https://doi.org/10.3758/s13423-011-0173-y), see #15).
- **What it costs:** one more decision per Question, and ratings can change learning (mixed evidence, #15). I found no study that measures the time cost of a confidence tap in an app.
- **Verdict:** put confidence into the submit step ("Check" / "Not sure – check") so it costs no extra tap. A/B test it (#15, open question 5). This UI is a design guess.

#### B1.6 Tone

- Feedback helps on average (*d* = 0.41, 607 effect sizes), but **more than a third of feedback interventions made performance worse**. Feedback helps less as it moves attention from the task to the self ([Kluger & DeNisi 1996, *Psychological Bulletin*](https://doi.org/10.1037/0033-2909.119.2.254)).
- Negative feedback did **not** lower intrinsic motivation compared with neutral or no feedback (78 studies). It did compared with positive feedback. The harm was smaller when the feedback said how to improve and used a clear standard ([Fong et al. 2019, *Educational Psychology Review*](https://doi.org/10.1007/s10648-018-9446-6)).
- Use praise "sparingly, if at all"; do not compare learners with others ([Shute 2008, Table 3](https://doi.org/10.3102/0034654307313795)).
- Feedback with more information has more effect (435 studies, *d* = 0.48 overall) ([Wisniewski, Zierer & Hattie 2020](https://doi.org/10.3389/fpsyg.2019.03087)).

### B2. Multi-correct Questions

**What the exam does** ([Regitra exam rules](https://github.com/Whirlywack/ketgo-web/blob/research/regitra-exam-rules/docs/research/regitra-exam-rules.md)): scoring is all-or-nothing. Every Option has a checkbox, also on single-correct Questions. The screen never says how many to tick. In one demo test, 4 of 30 Questions had more than one correct Option.

**No study tests multi-correct answering *for learning*.** The research below is about tests, so the rules in A3 combine it with reasoning.

- **Judging each Option alone shows hidden gaps.** When the same Questions were asked as single-choice or as true/false per Option, nearly half of the students who picked the right single answer likely still held wrong ideas about the other Options ([Couch, Hubbard & Brassil 2018, *BioScience*](https://doi.org/10.1093/biosci/biy037)). True/false-per-Option results estimated real mastery and misconceptions more accurately ([Brassil & Couch 2019, *IJ STEM Education*](https://doi.org/10.1186/s40594-019-0169-0)). → Per-Option feedback can target exactly the Option the learner got wrong.
- **Not telling the count cuts lucky guesses.** Items where the number of correct Options was unknown ("x of 5") were harder than "1 of 6" items, and lucky guessing almost disappeared ([Kubinger & Gottschall 2007, *Psychology Science* 49(4)](https://www.researchgate.net/publication/26514556_Item_difficulty_of_multiple_choice_tests_dependant_on_different_item_response_formats_-_An_experiment_in_fundamental_research_on_psychological_assessment)). → Hiding the count makes practice harder in a useful way, and it matches the exam.
- **Partial credit makes the same answers look much better.** Applying 41 scoring methods to the same real exam answers gave scores anywhere from 0.02 to 0.98, depending on the method ([Kanzow et al. 2023, *JMIR Medical Education*](https://doi.org/10.2196/43792)). Systematic reviews list dozens of scoring rules for such items ([Schmidt et al. 2021](https://doi.org/10.1016/j.edurev.2021.100409); [Schmidt et al. 2022](https://doi.org/10.1016/j.edurev.2022.100483)). Partial credit can make an exam score more reliable ([Bauer et al. 2011](https://doi.org/10.1007/s10459-010-9256-1)). An older review concluded that complex scoring gains little, and that partial-credit formats survive mainly for "providing feedback to enhance learning" ([Frary 1989](https://doi.org/10.1207/s15324818ame0201_5)).
- **Why all-or-nothing in practice too:** a "2 of 3" score feels like progress, but Regitra counts it as wrong. Overconfident learners stop studying too early (B3.3). → Score all-or-nothing; *explain* per Option.
- **Distractor Pool on multi-correct Questions (#8 owner question):** I found no study. Because the count is hidden and each Option is judged alone, letting the number of correct Options vary between repeats looks safe, but it must be tested.

### B3. Progress and readiness

#### B3.1 Progress displays

- **Watching progress helps reach goals.** Across 138 experiments (N = 19,951), getting people to monitor their progress improved goal attainment (*d* = 0.40). The effect was larger when progress was physically recorded or reported ([Harkin et al. 2016, *Psychological Bulletin*](https://doi.org/10.1037/bul0000025)).
- **Progress bars can backfire.** In 32 web-survey experiments, a steady progress bar did not reduce quitting. A bar that moved fast first and slow later reduced quitting; a bar that moved slow first and fast later increased it ([Villar, Callegaro & Yang 2013](https://doi.org/10.1177/0894439313497468)).
- **Goal gradient:** people speed up as they get close to a goal. An "illusion of progress" (a 12-stamp card with 2 stamps already given) sped them up too ([Kivetz, Urminsky & Zheng 2006](https://doi.org/10.1509/jmkr.43.1.39); [Nunes & Drèze 2006](https://doi.org/10.1086/500480)). KETGO should only use honest progress, so do not fake a head start.
- **Show the smaller number.** Early on, pointing at progress made ("20 % done") motivated more than pointing at what remains. Near the end, pointing at what remains ("20 % left") motivated more ([Koo & Fishbach 2012](https://doi.org/10.1086/663827)). Motivation tends to dip in the middle ([Bonezzi, Brendl & De Angelis 2011](https://doi.org/10.1177/0956797611404899)).

#### B3.2 Rule states (Remembered / Learning / Not met yet)

- **Showing learners the system's model of their skills can help.** In two classroom experiments (302 students), an "open learner model" with self-assessment support improved learning in an equation tutor ([Long & Aleven 2017, *UMUAI*](https://doi.org/10.1007/s11257-016-9186-6)).
- **But dashboards in general have weak evidence:** most learning-analytics dashboards are not grounded in learning theory and cannot be said to support metacognition ([Matcha et al. 2020, *IEEE TLT*](https://doi.org/10.1109/tlt.2019.2916802)).
- **The threshold matters most.** For "mastered" decisions, which data you use and where you set the threshold mattered more than which model you use ([Pelánek & Řihák 2017](https://doi.org/10.1145/3079628.3079667)). → Set the Remembered threshold carefully and check it against Mock Exam results.
- **Wording such as "Not met yet"** is about tone. Mindset interventions have only weak effects on achievement ([Sisk et al. 2018, *Psychological Science*](https://doi.org/10.1177/0956797617739704)), so do not expect the label itself to improve learning.

#### B3.3 Readiness, calibration and overconfidence

- **Learners are overconfident, weaker ones most.** Students' predictions of their exam grades were almost always too high, especially for low performers ([Miller & Geraci 2011](https://doi.org/10.1007/s11409-011-9083-7); [Hacker et al. 2000](https://doi.org/10.1037/0022-0663.92.1.160)). Students stayed overconfident even after 13 weekly exams ([Foster et al. 2017](https://doi.org/10.1007/s11409-016-9158-6)).
- **Overconfidence causes underachievement.** Overconfident learners stopped studying too early and remembered less later ([Dunlosky & Rawson 2012, *Learning and Instruction*](https://doi.org/10.1016/j.learninstruc.2011.08.003)). → A readiness display that flatters learners would make them stop too early.
- **Repeats inflate scores.** Retaking a test raised scores (*d* = 0.26; 107 samples, 134,436 people), more so when the *same* form was used ([Hausknecht et al. 2007, *J. Applied Psychology*](https://doi.org/10.1037/0021-9010.92.2.373)). → This fits the "95 % in the app, failed Regitra" complaint (#15). Readiness must come from new Questions and Mock Exams.
- **Concrete feedback can improve self-judgement:** with concrete feedback, low performers' predictions got more accurate, though their scores did not rise ([Miller & Geraci 2011](https://doi.org/10.1007/s11409-011-9083-7)).
- **A score alone teaches less than advice.** Compared with written comments, grades led to lower achievement and less healthy motivation ([Koenka et al. 2019, *Educational Psychology*](https://doi.org/10.1080/01443410.2019.1659939)). Feedback reviews advise caution with overall grades ([Shute 2008, Table 3](https://doi.org/10.3102/0034654307313795)).

#### B3.4 A pass-probability number, or bands?

None of these studies is about exam readiness. They are about how people read uncertain numbers.

- **Words alone are read very differently.** People gave very different numbers to words like "likely" and "very likely", even with a guide next to them ([Budescu, Broomell & Por 2009, *Psychological Science*](https://doi.org/10.1111/j.1467-9280.2009.02284.x)).
- **A number with a range keeps trust.** Showing uncertainty as a numeric range barely lowered trust (5 experiments, n = 5,780); verbal uncertainty lowered it more ([van der Bles et al. 2020, *PNAS*](https://doi.org/10.1073/pnas.1913678117)).
- **Number + advice works best.** Forecasts with uncertainty improved decisions and trust; advice alone did not; the two together worked well ([Joslyn & LeClerc 2012, *JEP: Applied*](https://doi.org/10.1037/a0025185)).
- **"x out of y" is easier than %.** People reason better with counts than with percentages ([Gigerenzer & Hoffrage 1995, *Psychological Review*](https://doi.org/10.1037/0033-295x.102.4.684)).
- **Verdict (design inference):** band word + "about 26 of 30, likely 23–28 (pass is 24)" + next step. This uses the exam's own units, shows the uncertainty, and gives advice.

### B4. Gamification

**Meta-analyses (gamified course vs. the same course without game elements):**

| Source | Result |
|---|---|
| [Sailer & Homner 2020](https://doi.org/10.1007/s10648-019-09498-w) | Learning *g* = 0.49 (k = 19), motivation *g* = 0.36, behaviour *g* = 0.25. The learning effect held in rigorous studies; the motivation and behaviour effects were less stable. |
| [Bai, Hew & Huang 2020](https://doi.org/10.1016/j.edurev.2020.100322) | Learning *g* = 0.50 (30 interventions, 3,202 people). |
| [Huang et al. 2020](https://doi.org/10.1007/s11423-020-09807-z) | Learning *g* = 0.46 (30 studies, 3,083 people); different elements had different effects. |
| [Li, Hew & Du 2024](https://doi.org/10.1007/s11423-023-10337-7) | Intrinsic motivation *g* = 0.26 (35 interventions); almost no gain in feeling competent. A common problem: discomfort of learners ranked low on public leaderboards. |

Caution: gamified courses often also add more quizzes and feedback, so these numbers do not show what points or badges add on their own.

**Element by element:**

- **Points, levels, leaderboards:** they raised the *amount* of work but not intrinsic motivation, and not quality. They acted as outside incentives ([Mekler et al. 2017, *Computers in Human Behavior*](https://doi.org/10.1016/j.chb.2015.08.048)).
- **Leaderboard + badges in a real course** (71 students, 16 weeks): students became less motivated, less satisfied and less empowered, and scored **lower on the final exam** ([Hanus & Fox 2015, *Computers & Education*](https://doi.org/10.1016/j.compedu.2014.08.019)).
- **Badges:** in a 2-year field experiment, badges increased activity on a trading service (not a learning service) ([Hamari 2017](https://doi.org/10.1016/j.chb.2015.03.036)).
- **Rewards and motivation:** expected tangible rewards lowered intrinsic motivation (*d* −0.28 to −0.40); positive informational feedback raised it (*d* = 0.33) (128 studies) ([Deci, Koestner & Ryan 1999, *Psychological Bulletin*](https://doi.org/10.1037/0033-2909.125.6.627)).
- **Streaks:**
  - An intact streak in a log made people more likely to continue than a broken one. The drop after a break was larger when people blamed themselves, and smaller when the streak could be repaired (7 studies, including fitness-app data) ([Silverman & Barasch 2023, *J. Consumer Research*](https://doi.org/10.1093/jcr/ucac029)).
  - In a randomised trial with about 60,000 pupils on a maths platform in Peru, highlighting streaks increased platform use and maths scores compared with control (only about 1,500 took the final test; streaks were not better than personalised reminders) ([Aulagnon et al. 2025, *Economics of Education Review*](https://doi.org/10.1016/j.econedurev.2025.102721)).
  - Goals with a built-in "emergency reserve" (like a streak freeze) increased persistence ([Sharif & Shu 2017, *J. Marketing Research*](https://doi.org/10.1509/jmr.15.0231)).
- **Novelty fades:** in a 14-week study (N = 756), the effect of gamification dropped after about 4 weeks, then partly recovered from week 6 to 10 ([Rodrigues et al. 2022](https://doi.org/10.1186/s41239-021-00314-6)).

**Summary for KETGO:**

| Element | Helps learning? | Helps engagement? | Risk |
|---|---|---|---|
| Progress toward a learning goal (Lessons, Rules Remembered) | Yes, indirectly (progress monitoring *d* = 0.40) | Yes | Low, if honest |
| Points / XP | No evidence | More activity, not better activity | Learners farm easy Questions |
| Badges / milestones | Weak | Yes (one field study) | Low, if tied to learning |
| Levels | KETGO's numbered Lessons already are levels | — | — |
| Leaderboards | Mixed to negative | For the top players | Pressure, discomfort for low-ranked learners, lower exam scores in one course |
| Day streaks | One RCT: small gain | Yes | Quitting after a break, guilt; repair softens it |

---

## C. Open questions worth adding to the map

1. **Streaks vs. #5.** #5 decided "no day streak". The evidence says streaks raise engagement, one RCT found a learning gain, and #17 suggested a repairable streak. Should the beta A/B test a gentle, repairable "days studied this week" display?
2. **Readiness format.** Test "about 26 of 30 (range)" vs. a band word only vs. a percentage, and measure which one learners read correctly and whose predictions match Mock Exam results.
3. **Distractor Pool on multi-correct Questions** (#8): may the number of correct Options shown change between repeats? No research; A/B test.
4. **Confidence as a second "Check" button:** does it change speed or accuracy? (#15, open question 5.)
5. **How short can the "why" be?** Test one sentence vs. three on accuracy for never-seen Questions.
6. **Checkboxes everywhere** cost one "Check" tap per Question. Does this slow learners enough to matter? (We think matching the exam is worth it.)
