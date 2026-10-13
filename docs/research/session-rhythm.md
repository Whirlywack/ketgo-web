# Session length, daily rhythm and new-Rule pace

Ticket: [#17 Session length, daily rhythm and new-Rule pace](https://github.com/Whirlywack/ketgo-web/issues/17) · Builds on: [#15 Learning techniques](https://github.com/Whirlywack/ketgo-web/issues/15) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1)

**Checked on 2026-10-13.** Sources are meta-analyses, peer-reviewed studies, the Anki manual and source code, and Duolingo's published research. Each claim links to its source. Most numbers were checked in the paper or its abstract. **UNVERIFIED** marks a number seen only in a secondary summary. **Design guess** marks a choice that no study tests directly.

Words like **Program**, **Lesson**, **Review**, **Rule**, **Question**, **Theme**, **Mock Exam**, **Remembered** and **Theory Exam** mean what `GLOSSARY.md` says. A **sitting** (not a glossary term) is one block of time in the app without a long break. One sitting can hold several Lessons.

How to read effect sizes: *g* or *d* = how far the average learner moves, in standard deviations. 0.2 = small, 0.5 = medium, 0.8 = large.

Two warnings:

1. **No study tests the exact questions in this ticket.** Nobody has measured "best Lesson length for driving theory" or "best number of new Rules per Lesson". The evidence is indirect: lab and classroom studies, mostly with word pairs, facts, texts or maths. The numbers below are a starting point that KETGO must tune with its own data.
2. **The model numbers in section 8 come from FSRS with its default settings.** They estimate *workload* (how many Questions per day). They do not prove that learning works.

---

## A. Recommended Program defaults

For about **250 Rules** (the real count is still open; about 230 KET points have Own Questions, see #4). Strength = how strong the evidence is for the *direction* and for the *number*.

| Setting | Default | Strength |
|---|---|---|
| **Lesson size** | **8 new Rules** (range 6–10), plus due Rules mixed in. Each new Rule is asked until it is answered right 2–3 times in the Lesson, with other Questions in between. About **15–25 min** (model: ~37 Questions on a 1-Lesson day). | Direction: moderate (spacing inside a sitting; 3 correct answers then later relearning). Number: **weak / design guess**. |
| **Minimum day** | 15 min is a sensible floor for an exam about 5 weeks away. No study supports any fixed minimum. On a busy day, finishing just the due Rules (a short Review, ~5 min) still counts as "done" for the streak. | Minimum: **none** (no study). "Short day beats a broken streak": moderate. |
| **Longest sitting** | No hard stop. After about 45–60 min in one sitting, suggest a 5–10 min quiet break (no other screen). | Attention drops over time: moderate. Break helps memory: moderate (quiet rest *g* ≈ 0.45). The 45–60 min point: **design guess**. |
| **Lessons per day** | Suggested: **1**. Allowed: up to **3** (≈ 24 new Rules, close to Anki's default of 20 new cards a day). After 3, no more new Rules that day. | Too many new items a day overloads later days: moderate. The cap of 3: **weak**. |
| **Sittings per day** | One sitting a day is the default. If the learner needs 2+ Lessons a day, split them into 2 sittings a few hours apart, best evening + next morning. Spreading over more days beats more per day. | More days > more per day: **strong**. Sleep between sittings: weak to moderate (sleep helps memory, but the "relearn faster" result did not replicate). |
| **Pace by days to exam** | Lessons per day = remaining Lessons ÷ (days to exam − 2), rounded up. Last 2 days: **no new Rules**. See the table in section 3. If that needs more than 3 Lessons a day, say so honestly and put the heaviest Themes first. | Spread out, don't cram: **strong**. The exact table: model + **design guess**. |
| **Learning / repeating / examining** | Rule Explainers short; most time on Questions. New-Rule Questions fall from ~60 % of a day's Questions early in the Program to ~35 % near the end (model). Mock Exams ≈ 15 % of all Questions, about half of each day in the last days. | Questions > re-reading: **strong**. The shares: model + **design guess**. |
| **Mock Exam timing** | First one when about half the Lessons are done. Then about every 4 Lessons. Every day in the last 3–4 days. Last one the day before the Theory Exam. A Mock Exam takes up to 30 min. Mistakes from it go back into the schedule. | Practice tests help and fix overconfidence: **moderate to strong**. How often: **none** (no study); design guess. |
| **Reviews when there are several Lessons a day** | Mix due Rules into each Lesson. Today's due Rules are **one pool**, shared across today's Lessons: each due Rule is asked once a day, not in every Lesson. If more is due than fits in one Lesson (~30 Questions), put a **separate Review first** and hold new Rules until it is done. | Mixing: moderate. Same-day repeats add little: moderate. "Stop new items when behind": moderate. The ~30 threshold: **design guess**. |
| **Binge** (hours on day 1) | Let them go on. Stop new Rules after 3 Lessons. Then offer, in order: one Review of today's misses, a Mock Exam (only after half the Program), or "take a break and come back tonight or tomorrow". | Extra new Rules → review spike, no gain (model + Anki + Reddy et al.): moderate. Drilling the same Rule again → little lasting gain: moderate. |
| **Reminders** | **1 a day**, at the time the learner chose ("When will you study?"). Change the wording often. No reminder once today's Lesson is done. After several ignored days, send *fewer*, not more. A second daily reminder only if the learner chose two study times. | Daily reminder helps a little: moderate. Planning "when": moderate (*d* = 0.65). Wording goes stale: moderate. Two or more a day: **none**. |

---

## B. Short answer per question

1. **Session length.** Attention and mind wandering get worse the longer a task runs. But there is no proven cut-off, and the popular "10–15 minute attention span" has no good evidence behind it. Answering Questions (not reading) keeps attention up. 15 minutes is a fine *minimum*; no study supports a specific *maximum*. Suggest a quiet break after long sittings.
2. **Sittings and Lessons per day.** Spreading the same study time over more days beats doing more per day. This is one of the strongest findings in learning science. A second sitting on the same day helps less than a sitting on the next day. If a learner must do more per day (exam soon), split it, ideally with a night's sleep in between.
3. **New Rules per Lesson and per day.** No study gives a safe number. Sessions with up to ~20 new items do fine *if* repeats are spaced inside the session. The real danger is not the Lesson but the *day*: every new Rule creates Reviews over the next days. Too many new Rules at once makes Reviews pile up and learning collapse. So: about 8 new Rules per Lesson, at most about 3 Lessons a day.
4. **Pace near the exam.** Front-load: meet every Rule early enough for at least a few spaced Reviews. Stop new Rules about 2 days before the Theory Exam. Use the last days for Reviews of Rules that are not yet Remembered, plus Mock Exams.
5. **Learning, repeating, examining.** After a short Rule Explainer, time on Questions beats time re-reading by a lot (61 % vs 40 % recall after a week). Reviews take a growing share as the Program goes on. Mock Exams are useful once most Rules are known, and they correct overconfidence. Before that, they mostly produce wrong answers.
6. **Reviews with several Lessons a day.** Mix them into Lessons, because mixing old and new Rules helps learners tell Rules apart and spaces the new ones. But don't re-ask the same due Rule in every Lesson that day: same-day repeats add little. If a big pile is due, do a separate Review first.
7. **Bingeing.** Extra new Rules on day 1 cause a wave of Reviews two days later and, in the model, no gain on exam day. Extra drilling of today's Rules fades within weeks. Let motivated learners continue, but steer them to Reviews, a Mock Exam (later in the Program), or a break.
8. **Reminders.** One reminder a day, at the learner's own chosen time, with changing wording. Effects are small (a few percent). Reminders lose power over 2–4 weeks if they repeat. No study shows that more than one reminder a day helps a learner like ours.

---

## 1. Session length: when does learning per minute fall?

**There is no proven attention limit in minutes.**
- The "attention drops after 10–15 minutes" claim is not supported. A review found that the research behind it "provides little support for the belief that students' attention declines after 10 to 15 min" ([Wilson & Korn 2007, *Teaching of Psychology*](https://doi.org/10.1080/00986280701291291)). A second review found that differences between teachers mattered more than time ([Bradbury 2016, *Advances in Physiology Education*](https://doi.org/10.1152/advan.00109.2016)).

**But attention does drift as a task goes on.**
- An individual-participant meta-analysis (68 reports, more than 10,000 people, about half a million probe answers) confirmed that "mind-wandering increases in frequency over time during task performance" ([Zanesco, Denkova & Jha 2025, *Psychological Bulletin*](https://doi.org/10.1037/bul0000424)). It gives no cut-off in minutes.
- Not everywhere: in a real 12-week course, mind wandering did not rise across lectures ([Wammes et al. 2016](https://doi.org/10.1037/stl0000053), abstract only).

**Answering Questions protects attention.**
- In a 21-minute online lecture, short tests after each part cut mind wandering to 19 % of probes, vs 39–41 % without tests. Final test: 90 % vs 68–76 % ([Szpunar, Khan & Schacter 2013, *PNAS*](https://doi.org/10.1073/pnas.1221764110)). → A KETGO Lesson is mostly Questions, which is the right format for a long sitting.
- People stop watching *passive* video early: median watch time was at most about 6 minutes, whatever the video length (6.9 million sessions on edX; [Guo, Kim & Rubin 2014, *Learning@Scale*](https://doi.org/10.1145/2556325.2566239)). This measures watching, not learning. → Keep each Rule Explainer short.

**Shorter, more frequent study is more efficient per hour.**
- Postal workers learning to type: "Learning was most efficient in the group given one session of one hour per day, and least efficient in the group trained for two 2-hour sessions" ([Baddeley & Longman 1978, *Ergonomics*](https://doi.org/10.1080/00140137808931764)). This is a motor skill, not facts.
- Meta-analysis of 63 studies: spaced practice beat massed practice, *d* = 0.46 ([Donovan & Radosevich 1999, *J. Applied Psychology*](https://doi.org/10.1037/0021-9010.84.5.795)).
- In 20 HarvardX courses, learners who split the same total time into *more* sessions were more likely to finish (about 3–4 % higher odds of a certificate per extra session). This is correlation, not cause ([Miyamoto et al. 2015, *J. Learning Analytics*](https://doi.org/10.18608/jla.2015.22.5)).

**Breaks.**
- Short breaks (≤ 10 min) raise energy (*d* = 0.36) and lower fatigue (*d* = 0.35). They did **not** reliably improve performance, and not at all after mentally demanding tasks (*d* = −0.09, not significant) ([Albulescu et al. 2022, *PLOS ONE*](https://doi.org/10.1371/journal.pone.0272460)).
- *Quiet* rest right after learning helps memory: meta-analysis of 37 studies, *g* = 0.45; 5–10 minutes is as good as 10–30; still *g* = 0.27 after 7 days in the cleanest studies; *g* = 0.29 after correcting for publication bias ([*Psychonomic Bulletin & Review* 2025, "Effects of wakeful rest on memory consolidation"](https://doi.org/10.3758/s13423-025-02665-x)). The original study used 10 minutes of quiet rest vs a game ([Dewar et al. 2012, *Psychological Science*](https://doi.org/10.1177/0956797612441220)). → A break means "close your eyes", not "scroll another app".
- Fixed breaks (e.g. 24 min work + 6 min break) gave less fatigue and more motivation than self-chosen breaks, with the same amount of work done. Learning was not tested ([Biwer et al. 2023, *Br. J. Educational Psychology*](https://doi.org/10.1111/bjep.12593)).
- Do not justify a time cap with "willpower runs out". A 23-lab replication found no such effect (*d* = 0.04; [Hagger et al. 2016](https://doi.org/10.1177/1745691616652873)).

**Verdict.** 15 minutes is a sensible *minimum* because of the workload (section 8), not because of any attention limit. No study gives a maximum. Suggest a short, quiet break after about 45–60 minutes in one sitting (design guess), and measure in KETGO whether accuracy and answer time drift as a sitting goes on.

---

## 2. Sittings and Lessons per day

**Spread over days beats more per day (strong).**
- A meta-analysis of 839 results found that the best gap between study sessions grows as the time until the test grows ([Cepeda et al. 2006, *Psychological Bulletin*](https://doi.org/10.1037/0033-2909.132.3.354)). For tests more than a month away, "learning within a single day impaired learning, compared with a 1-day interval" (quote from the full text).
- For a test 1 week away, the best gap was about 20–40 % of that week, i.e. 1–2 days. For a test 1 year away, 5–10 % ([Cepeda et al. 2008, *Psychological Science*](https://pubmed.ncbi.nlm.nih.gov/19076480/), more than 1,350 people).
- School French vocabulary: three 10-minute parts on three days vs all 30 minutes on one day. Same score at once, but **35 % better 4 days later** for the spread group ([Bloom & Shuell 1981, *J. Educational Research*](https://doi.org/10.1080/00220671.1981.10885317)).
- Spacing beat cramming on the last day before the test, even with study time equal. Spacing helped 90 % of learners, yet 72 % believed massing worked better ([Kornell 2009, *Applied Cognitive Psychology*](https://doi.org/10.1002/acp.1537)).

**Two sittings on the same day help less (moderate).**
- Repeating a card several times on one day "does not significantly contribute to long-term memory" ([Anki manual, deck options](https://docs.ankiweb.net/deck-options.html); the manual cites no study). FSRS gives same-day Reviews a separate, damped formula ([FSRS algorithm wiki](https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm)).
- More sittings a day reach a goal in fewer *calendar days*, but with less learning *per hour* ([Baddeley & Longman 1978](https://doi.org/10.1080/00140137808931764); calendar-day point from a commentary by Newell 1988, **UNVERIFIED** against the original tables). → When the exam is close, a second sitting is a way to fit more practice in, not a way to learn more per minute.

**Sleep between sittings (weak to moderate).**
- Sleep helps memory: meta-analysis of 271 samples, *g* = 0.44 ([Berres & Erdfelder 2021, *Psychological Bulletin*](https://doi.org/10.1037/bul0000350), abstract only).
- Learning in the evening and relearning next morning (with sleep in between) halved the practice needed and gave much better memory after 1 week and 6 months, vs morning + evening of the same day. But only 40 people ([Mazza et al. 2016, *Psychological Science*](https://doi.org/10.1177/0956797616659930)).
- A similar study with 52 people did **not** replicate the faster relearning (*d* = 0.1). Sleep helped overnight memory (*d* = 0.72), but the gain after 1 week was small and not significant (*d* = 0.35) ([Cousins et al. 2021, *Sleep*](https://doi.org/10.1093/sleep/zsaa210)).
- Sleep soon after learning helped vocabulary ([Gais, Lucas & Born 2006](https://doi.org/10.1101/lm.132106)), but another study found the timing of sleep did not matter ([Tucker et al. 2011, *PLOS ONE*](https://doi.org/10.1371/journal.pone.0021737)).

**Time of day and "morning/evening person" (weak).** A systematic review found a "best time of day" effect in only 29 of 64 adult studies ([*Chronobiology International* 2025](https://doi.org/10.1080/07420528.2025.2490495), abstract only). A study of 446 people found no robust effect ([*Collabra: Psychology* 2023](https://online.ucpress.edu/collabra/article/9/1/88337/197502), abstract only). → Let the learner choose the time. Don't build the schedule around chronotype.

**Verdict.** Default: one sitting a day, every day. If more is needed, two sittings a few hours apart, best evening + next morning. The order of benefit is: more days > a night in between > a few hours in between > back-to-back.

---

## 3. New Rules per Lesson, Lessons per day, and pace to the exam

**What the evidence says.**
- **Inside one sitting, spacing matters more than set size.** One stack of 20 cards beat four stacks of 5, because each card came back after a longer gap: 49 % vs 36 % (Exp. 1) and 65 % vs 34 % (Exp. 3) ([Kornell 2009](https://doi.org/10.1002/acp.1537)). With spacing matched, learning 4, 10 or 20 words at a time made little difference ([Nakata & Webb 2016, *SSLA*](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/does-studying-vocabulary-in-smaller-sets-increase-learning/E17B75ABAE1300734AF014C363D59FBC), abstract only). → 6–10 new Rules in a Lesson is safe if their Questions are mixed, not asked back to back.
- **How many correct answers in the first Lesson.** 533 students: practising to 3 correct recalls, then relearning in 3 later sessions, worked well. The extra benefit of more correct answers on day one shrank once later relearning happened ([Rawson & Dunlosky 2011, *JEP: General*](https://pubmed.ncbi.nlm.nih.gov/21707204/)). Easy repeats give "diminishing returns" ([Pyc & Rawson 2009](https://eric.ed.gov/?id=EJ834321)). → 2–3 correct answers per new Rule in the Lesson, then hand it to the scheduler.
- **The danger is the day, not the Lesson.** Anki's manual: "If you are consistently learning 20 new cards a day, you can expect your daily reviews to be roughly about 200 cards/day", and "More than one Anki user has excitedly studied hundreds of new cards over their first few days … and then has become overwhelmed by the reviews required" ([Anki manual](https://docs.ankiweb.net/deck-options.html)). Anki's built-in defaults are 20 new cards and 200 reviews a day ([Anki source, `deckconfig/mod.rs`](https://github.com/ankitects/anki/blob/main/rslib/src/deckconfig/mod.rs)).
- A queueing model of spaced repetition predicts a "sharp phase transition": above a certain rate of new items, items pile up and learning drops toward zero. A Mechanical Turk study (331 people, 15-minute sessions) showed the same pattern ([Reddy, Labutov, Banerjee & Joachims 2016, *KDD*](https://arxiv.org/abs/1602.07032)). The threshold depends on the task, so it gives no number for Rules.
- **Interference.** The more similar items share one cue, the harder each one is to recall ([Watkins & Watkins 1975](https://psycnet.apa.org/record/1975-28897-001), abstract only). A Lesson is "a small group of related new Rules" (glossary). That is fine *if* the Lesson contrasts them on purpose (interleaving helps most with similar categories, see #15 D3), with feedback that names the difference.

**Pace by days to exam (model, 250 Rules, 8 per Lesson = 32 Lessons, last 2 days without new Rules).**

Time per day assumes 20–30 s per Question with feedback, plus 30–60 s per Rule Explainer (**design guess**; the Theory Exam allows 60 s per Question). KETGO must measure real times.

| Days to exam | Lessons per day | New Rules per day | Questions per day (model: average / peak) | Time per day (rough) |
|---|---|---|---|---|
| 34 or more | 1 | 8 | 37 / 50 | 15–25 min |
| about 18 | 2 | 16 | 64 / 86 | 30–45 min, 2 sittings |
| about 13 | 3 | 24 | 81 / 104 | 40–65 min, 2 sittings |
| about 10 | 4 | 32 | 99 / 130 | 50–80 min, 2 sittings; above the cap |
| under 10 | too many to cover all Rules at a safe pace | — | — | Tell the learner. Put heavy Themes first (6/5/3/3/3/4/2/2/2 Questions per Theme in the exam). |

- With more than ~34 days, 1 Lesson a day still works. The Program simply ends early, and the rest is Reviews and Mock Exams. In the model, FSRS keeps Rules Remembered with few Reviews.
- **Last 2 days:** no new Rules. Ask once more every Rule that is not Remembered (predicted below 90 % on exam day). In the model this costs only ~12–16 extra Questions on the last day and lifts the share of Rules at ≥ 90 % from 94–96 % to 100 % (section 8, table C).
- Why stop new Rules before the exam: cramming new material at the end loses to spacing ([Kornell 2009](https://doi.org/10.1002/acp.1537)), and a Rule met on the last day gets no spaced Review. The exact "2 days" is a **design guess**; no study tests a cut-off.

---

## 4. Balance of learning, repeating and examining

**Most time should go to Questions, not reading (strong).**
- Students who read a text once and then took 3 recall tests remembered **61 %** after a week. Students who read it 4 times remembered **40 %**. After 5 minutes the order was reversed (71 % vs 83 %), and re-reading made students *more confident* ([Roediger & Karpicke 2006, *Psychological Science*](https://doi.org/10.1111/j.1467-9280.2006.01693.x)).
- Practice tests beat re-study and every other comparison condition ([Adesope, Trevisan & Sundararajan 2017, *Review of Educational Research*](https://doi.org/10.3102/0034654316689306)).
- → Rule Explainers should be short. The Lesson flow from #15 (guess → Rule Explainer → Questions) already does this.

**Share of new Rules vs Reviews (model).** Share of a day's Questions that are on Rules met that same day:

| Lessons per day | First third of Program | Middle third | Last third |
|---|---|---|---|
| 1 | 62 % | 44 % | 34 % |
| 2 | 67 % | 53 % | 32 % |
| 3 | 74 % | 56 % | 36 % |

So Reviews grow from about a third of the day to about two thirds. No study says this split is "right"; it is simply what FSRS asks for at 90 % target retention.

**Mock Exams (moderate that they help; none on how often).**
- A Mock Exam is retrieval practice in the exact exam format: mixed Themes, 30 Questions, feedback at the end. In 54 school classes, practice that mixed different kinds of problems beat practice in blocks of one kind: 61 % vs 38 % on a surprise test one month later, *d* = 0.83 ([Rohrer et al. 2020, *J. Educational Psychology*](https://doi.org/10.1037/edu0000367)).
- It corrects overconfidence. Students whose self-judgements were too high stopped studying too early and remembered less two days later ([Dunlosky & Rawson 2012, *Learning and Instruction*](https://doi.org/10.1016/j.learninstruc.2011.08.003)). Re-reading also makes learners feel more ready than they are ([Roediger & Karpicke 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)). Mock Exam scores also feed readiness (#15 C2).
- Too early is not useful. Testing can lose its benefit when success is low (#15 D9, Racsmány et al. 2020). A Mock Exam in the first Lessons is mostly guessing on unseen Rules. Guessing first helps only the guessed item (#15 D7).
- **No study says how often to take a full mock exam.** Suggested (design guess):
  - Optional "where do I stand?" Mock Exam on day 1, never pushed, not counted in readiness.
  - First suggested Mock Exam when about half the Lessons are done.
  - Then about every 4 Lessons.
  - Every day in the last 3–4 days. The last one the day before the Theory Exam.
  - Every Mock Exam answer is also a Review event: a wrong answer brings its Rule back soon (successive relearning, #15 D8).
- Size: a Mock Exam can take up to 30 minutes, twice the 15-minute minimum day. On a Mock Exam day, it can replace the Lesson. Over a 5-week Program this plan gives about 8 Mock Exams, roughly 15 % of all Questions, and about half of each day's Questions in the last days (estimate from the model numbers above).

---

## 5. Several Lessons in one day: how to fit Reviews in

**Mix due Rules into each Lesson (moderate).**
- Assignments that mixed different kinds of problems beat assignments in blocks of one kind, in a randomised trial in 54 classes (*d* = 0.83; [Rohrer et al. 2020](https://doi.org/10.1037/edu0000367)). Interleaving helps most when categories are easy to confuse ([Brunmair & Richter 2019](https://consensus.app/papers/details/621345c33c1c5d6ab95c10b54896bbb1/), see #15 D3).
- Due Questions placed between the repeats of a new Rule create the gaps that make the 2nd and 3rd answer effortful. That is what made the big stack win in [Kornell 2009](https://doi.org/10.1002/acp.1537). The *absolute* gap matters more than the exact pattern ([Karpicke & Bauernschmidt 2011, *JEP: LMC*](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Bauernschmidt_JEPLMC.pdf)).
- Learners choose badly on their own. They prefer blocking and cramming even when it scores worse ([Kornell & Bjork 2008](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/Kornell_Bjork_2008_PsychScience.pdf); [Kornell 2009](https://doi.org/10.1002/acp.1537)). An optional "Review" button is likely to be skipped. So KETGO should put the due Rules into the Lesson itself.

**But treat the day's due Rules as one pool (moderate).**
- FSRS decides which Rules are due *today*. If a learner does Lessons 2, 3 and 4 the same day, asking the same due Rule in each Lesson is a same-day repeat, which adds little ([Anki manual](https://docs.ankiweb.net/deck-options.html); [Cepeda et al. 2006](https://doi.org/10.1037/0033-2909.132.3.354)).
- So: share today's due Rules across today's Lessons, a few per Lesson, each one asked once. Later Lessons that day hold mostly new Rules, plus misses coming back a few Questions later.

**A separate Review when a lot is due (moderate).**
- Anki: "If you have a backlog of overdue review cards, it is recommended that you stop introducing new cards until you catch up with that backlog" ([Anki manual](https://docs.ankiweb.net/deck-options.html)). The queueing model shows why: new items on top of a backlog make it grow ([Reddy et al. 2016](https://arxiv.org/abs/1602.07032)).
- Rule (design guess): if more is due than fits in one Lesson (~30 Questions, e.g. after missed days or a binge), the next step is a **Review** with no new Rules. Then Lessons continue.

---

## 6. Bingeing: hours on day one

**What happens if day one has many new Rules (model, exam in 30 days).**

| New Rules on day 1 | Questions on days 1–7 | Total Questions | Predicted exam-day recall |
|---|---|---|---|
| 8 (1 Lesson) | 19, 24, 30, 38, 34, 34, 37 | 1,244 | 0.96 |
| 40 (5 Lessons) | 93, 34, 52, 43, 33, 35, 34 | 1,299 | 0.96 |
| 80 (10 Lessons) | 181, 42, 90, 52, 31, 38, 34 | 1,336 | 0.96 |
| 150 | 340, 58, 141, 68, 16, 28, 29 | 1,410 | 0.95 |

A big day one creates a **wave of Reviews on day 3** (90 Questions instead of 30) and more work in total. The model shows **no gain** on exam day. If the learner does not come back for that wave, the Rules from day one are forgotten.

**Extra drilling of today's Rules fades.**
- Extra study after a first perfect answer gave a big gain at 1 week that "decreased dramatically thereafter"; the authors call it "an inefficient strategy" ([Rohrer et al. 2005, *Applied Cognitive Psychology*](https://digitalcommons.usf.edu/psy_facpub/1772)). Six extra maths problems in one session had "no effect" 1 or 4 weeks later ([Rohrer & Taylor 2006](https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.1266)). An overlearning meta-analysis found a moderate effect that "declined sharply" with time ([Driskell, Willis & Copper 1992](https://psycnet.apa.org/doi/10.1037/0021-9010.77.5.615), abstract only).

**Recommended handling (design guess, built on the above).**
1. Let the learner keep going. Do not lock them out; new users are the ones most sensitive to how the app treats them (Duolingo saw its biggest reminder gains in new users; [Yancey & Settles 2020](https://research.duolingo.com/papers/yancey.kdd20.pdf)).
2. After 3 Lessons in a day, no more new Rules. Say why in one line: "New Rules today will all come back in 2 days. More now means a pile later."
3. Offer instead: one Review of today's misses → a Mock Exam (only after half the Program) → a break: "Come back tonight or tomorrow; sleep between sittings helps."
4. If the learner wants a quick break inside a long sitting, suggest 5–10 minutes of quiet rest (section 1).

---

## 7. Reminders

**One a day helps a little (moderate).**
- Duolingo optimised the *content* of its daily practice reminder with a bandit algorithm. In a two-week A/B test with millions of users: daily active users +0.5 %, lessons +0.4 %, new-user next-day retention +2.2 %, new-user 7-day retention +2.0 %, existing-user 7-day retention +0.2 % (not significant) ([Yancey & Settles 2020, *KDD*](https://research.duolingo.com/papers/yancey.kdd20.pdf)). The gain came from *better wording*, not from more reminders. I found no primary source for *when* Duolingo sends its reminder.
- A health app trial (1,255 users, one possible notification a day): a notification raised use within 24 hours by 3.9 %. Weekends +8.7 %, weekdays +2.5 % (difference not significant). Best slot in an exploratory test: 12:30 on weekends (+11.8 %) ([Bidargaddi et al. 2018, *JMIR mHealth*](https://doi.org/10.2196/10123)).
- In an alcohol app (350 users, daily 8 pm notification), a notification made opening the app in the next hour 3.5 times more likely, but long-term drop-out did not change ([Bell et al. 2023, *JMIR mHealth*](https://consensus.app/papers/details/8a55b1fe2b365f80be76909cc7421a1d/), abstract only).
- Daily notifications did not reduce engagement compared with occasional ones in a small stress-app trial (77 people) ([Morrison et al. 2017, *PLOS ONE*](https://doi.org/10.1371/journal.pone.0169162)).

**The same reminder goes stale (moderate).**
- Duolingo's algorithm penalises recently used templates, because repeating one "will get repetitive, desensitize users". Based on earlier A/B tests, they set the penalty to fade over about 15 days ([Yancey & Settles 2020](https://research.duolingo.com/papers/yancey.kdd20.pdf)).
- In a 6-week trial with up to 5 suggestions a day, the first-day effect (+66 % steps) shrank by about 2 % a day and was gone by about day 28. Participants said the messages "became boring after 2–4 weeks" ([Klasnja et al. 2019, *Annals of Behavioral Medicine*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6401341/)). Steps, not study, and 44 people.
- → KETGO's typical window (2–5 weeks) is exactly where this happens. Rotate wording, and tie it to real progress ("3 Rules due", "12 days to your exam").

**Let the learner choose the time (moderate).**
- Making an "if–then" plan (when and where) raised goal attainment, *d* = 0.65 across 94 tests ([Gollwitzer & Sheeran 2006](https://doi.org/10.1016/S0065-2601(06)38002-1)). → At sign-up ask "When will you study?" and use that as the reminder time.
- Habits take long to form: median 66 days, range 18–254, longer than most exam windows. "Missing one opportunity to perform the behaviour did not materially affect the habit formation process" ([Lally et al. 2010](https://doi.org/10.1002/ejsp.674); median from a secondary source). → Do not promise a habit. One missed day is not a disaster, so don't send a guilt message.

**Streaks.** In seven studies (including two with language-learning questions), an intact streak made people more likely to continue than a broken one. In one study (word and number games): 93 % vs 69 %, and a chance to *repair* the broken streak cut most of that loss (85 %) ([Silverman & Barasch 2023, *J. Consumer Research*](https://doi.org/10.1093/jcr/ucac029)). → Count a short day (just the due Rules) as "done", and allow one repair.

**Where reminders stop helping (weak).**
- No study I found compares 1 vs 2 vs 3 study reminders a day. Several studies show small effects only ([Bidargaddi et al. 2018](https://doi.org/10.2196/10123)) or no change in long-term behaviour ([Bell et al. 2023](https://consensus.app/papers/details/8a55b1fe2b365f80be76909cc7421a1d/)). Nudging college students by message barely moved study hours ([Oreopoulos & Petronijevic 2019, NBER w26059](https://www.nber.org/system/files/working_papers/w26059/w26059.pdf), excerpt only).
- Getting phone alerts all day raised inattention ([Kushlev, Proulx & Dunn 2016, *CHI*](https://www.kushlev.com/s/Kushlev-et-al-Silence-Your-Phones.pdf)). Batching notifications 3 times a day improved well-being ([Fitz et al. 2019, *Computers in Human Behavior*](https://www.sciencedirect.com/science/article/abs/pii/S0747563219302596)). Both are about *all* phone notifications, not one study reminder.

---

## 8. Model method and results

Script: [`session-rhythm-sim.py`](session-rhythm-sim.py) (uses the open-source `fsrs` 6.3.2 package with FSRS-6 default parameters). Results vary by a few Questions between runs because FSRS adds random "fuzz" to intervals.

**Assumptions (all design guesses):** 250 Rules, one FSRS memory per Rule, 8 new Rules per Lesson. The first answer after the Rule Explainer is right 75 % of the time; later answers are right with the FSRS-predicted probability. Target retention 90 %. Learning steps 1 and 10 minutes (Anki's defaults), so a new Rule is asked 2–3 times on its first day. All of a day's Lessons happen in one evening sitting. No Reviews after the exam.

**A. Lessons per day**

| Lessons/day | Days to exam | Questions/day (average) | Peak day | Predicted exam-day recall |
|---|---|---|---|---|
| 1 | 34 | 37 | 50 | 0.96 |
| 2 | 18 | 64 | 86 | 0.96 |
| 3 | 13 | 81 | 104 | 0.95 |
| 4 | 10 | 99 | 130 | 0.96 |

**B. Day-one binge:** see the table in section 6.

**C. Last-day sweep of Rules below 90 %**

| Lessons/day | Sweep | Questions on last day | Rules at ≥ 90 % predicted on exam day |
|---|---|---|---|
| 1 | no | 20 | 96 % |
| 1 | yes | 36 | 100 % |
| 2 | no | 38 | 94 % |
| 2 | yes | 50 | 100 % |

**Limits.**
- FSRS default parameters come from Anki users grading their own flashcards. KETGO has auto-graded multiple choice, where guessing is possible. The model's recall numbers are too optimistic for KETGO: in *every* scenario it predicts about 95 % recall on exam day, even for a 10-day cram. So it cannot tell good pacing from bad. **Use it for workload only.**
- The Theory Exam asks *new* Questions about a Rule, not the card the learner practised (#15 D6).
- The model has no fatigue, no interference, no drop-out and no learner who skips days.

---

## 9. What to measure in the beta

Everything below uses the event log from #15 C. Add these fields if they are missing:

1. **Position in sitting** (Question number and minutes since the sitting started). Plot accuracy and answer time against it to find KETGO's real fatigue point.
2. **Lesson id and Lesson number of the day** (1st, 2nd, 3rd …), and the time since the learner's last sitting. This tests whether later Lessons on the same day are learned worse.
3. **Next-day and 3-day accuracy on Rules from big days vs normal days.** This tests the cap of 3 Lessons a day.
4. **Reminder events:** sent time, template id, opened, Lesson started within 2 hours (Duolingo's measure). Randomise a small share of reminder times and templates, so the effect can be measured (#15 C3).
5. **Mock Exam score vs real Theory Exam result** (#15 C2). This is the only way to set the Mock Exam schedule and readiness with data.
6. **Real seconds per Question and per Rule Explainer,** to replace the design guess for minutes per day.

---

## Open questions this raises

1. **How many Rules are there?** All numbers scale with it. At 300 Rules, every number in section 3 grows by a fifth.
2. **The 15-minute minimum vs the exam date.** For exams less than about 3 weeks away, 15 minutes is not enough to meet every Rule. Should the Program show the learner the time they need per day at sign-up?
3. **Should a Mock Exam replace the Lesson on its day,** or come on top? It can take up to 30 minutes.
4. **Day-one binge limit.** Is the owner happy with "no new Rules after 3 Lessons in a day", given that many learners spend hours on day one?
5. **Rule order in the Program.** Should the heaviest Themes come first, so a learner with a short window covers the most exam Questions?
