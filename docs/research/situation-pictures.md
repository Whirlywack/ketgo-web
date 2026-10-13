# Situation pictures: learning value and sources

Research for issue [#22](https://github.com/Whirlywack/ketgo-web/issues/22). It feeds [#14 Situation-picture questions](https://github.com/Whirlywack/ketgo-web/issues/14). Checked on 2026-10-13.

Words like **Theory Exam**, **Question**, **Option**, **Own Question**, **Reference Bank** and **Rule Explainer** mean what `GLOSSARY.md` says. A "situation picture" here means a picture of a road scene (a crossing, a lane, traffic, weather), not a picture of one sign alone.

> **The legal part (section B) gives facts, not legal advice.** It quotes the law and the providers' terms, and says where we are unsure. The map already plans a lawyer check before launch. Section B lists what that check should cover.

**How the papers were found.** The plan was to use the Consensus search tool. Its monthly quota was already used up ("You've used all 30 searches this month; resets on November 1st"), so no Consensus results are used here. Instead, papers were found through OpenAlex and PubMed (scholarly databases) and checked on the publisher, PubMed, PMC or ERIC page. Every paper is cited with its DOI link. Effect sizes are taken from the abstract unless the text says otherwise.

## Short answer

| Question | Answer | Evidence strength |
|---|---|---|
| Do pictures help learners answer? | **Yes, if the picture shows what the Question is about.** In tests, such "representational" pictures raised scores (*g* = 0.35, 42 studies). Decorative pictures did nothing (*g* = −0.02). | Moderate to strong, but no study is about driving theory. |
| Do situation pictures carry over to real driving? | **Partly.** PC training with **still** road pictures and top-down plans made novices look at hidden dangers on real roads much more often (60.6 % vs 31.8 %). Crash effects are mixed: −23.7 % for young men, no effect for young women. | Moderate for "where to look"; weak for crashes. |
| Which multimedia principles apply? | Words + pictures beat words alone (Mayer's multimedia principle). Keep pictures clean (coherence: extra decoration hurts). Put words near the picture (contiguity). Point to the key part (signalling). | Strong in general learning research. |
| Still or animated? | **Still first.** Animation beats still pictures on average (*d* = 0.37), mainly when the movement itself must be learned. The Theory Exam uses only still pictures. Animation fits later Rule Explainers about movement (who goes first). | Moderate. |
| Photos or drawings? | **Mixed results.** Simple drawings often teach better than realistic ones. But learners score best when the test looks like what they practised. Use both, like the exam. | Weak to moderate (small studies). |
| What style does Regitra use? | Simple computer-drawn 3D scenes (driver's-eye view, often with the car's dashboard, or a bird's-eye view of a crossing) with a Regitra watermark, road-sign drawings, and a few low-resolution real photos. One picture above the text, Options in text, no video. In the demo, 17 of 30 Questions (57 %) show a road situation. | Primary (Regitra demo, issue #2). |
| Does matching the exam matter? | **Matching the task matters most:** look at a scene, then decide. Practice transfers best when the learner must give the same kind of response as in the final test. The exact look matters less. | Moderate, indirect. |
| Best picture source | **Our own drawn scenes** (made by a freelancer under a written rights contract, or by us in Blender with free CC0 parts), **plus our own photos**. Use KET sign images from the law text. **Never** Regitra's images or random web images. | Legal facts below; costs are our estimates. |
| Can AI images be owned? | AI providers give you whatever rights they have. But under Lithuanian and EU law the author must be a **natural person**, so a purely AI-made picture very likely has **no copyright**, and anyone could copy it. | Law text: high. No CJEU ruling yet. |
| Are KET sign images free to use? | **Very likely yes.** Legal acts and official documents have no copyright (Copyright Law Art. 5(2)), and the signs are drawn in KET annex 1. The law does not name "images in annexes", and we found no court decision. Redrawn SVGs on Wikimedia can have their own licence. | Medium. Lawyer to confirm. |

## Recommendation for [Situation-picture questions](https://github.com/Whirlywack/ketgo-web/issues/14)

1. **Yes, the beta needs them.** The Theory Exam shows a road situation in most Questions (17 of 30 in the demo). Our 274 Own Questions have **none** (issue #4). Pictures that show the situation make test Questions easier to understand, and practice transfers best when it asks for the same kind of decision as the exam.
2. **How many: about 100 situation pictures for the beta, about 200 later.**
   - Beta: about 40 crossings and priority, 25 road position, lanes and overtaking, 25 risk (hazards, weather, night) and 10 special road users and manoeuvres. This gives roughly 120–150 Questions.
   - Grow to about 200 after the beta, guided by which themes learners fail. Exam themes 1–5 (risk, behaviour, priority, special roads, safe driving) are 20 of the 30 exam Questions.
   - Prefer **different pictures for the same rule** over many Questions on one picture. Varied practice transfers better (see `docs/research/learning-techniques.md` on branch `research/learning-techniques`, technique 6).
3. **Source:**
   - **Main source: our own drawn scenes in a simple 3D or 2D style close to Regitra's**, with both bird's-eye and driver's-eye views. Start with bird's-eye crossings: they are the cheapest, clearest and easiest to change. Use a freelancer with a **written contract that transfers the rights** (worldwide, for the full term, all uses we need), or build the scenes ourselves in Blender with CC0 parts. Take sign drawings from KET annex 1 on e-TAR.
   - **Second source: our own photos of Lithuanian roads** for risk, weather and signs in real streets. Blur faces and number plates.
   - **Do not use:** Regitra's pictures, pictures found on the web, or Street View screenshots.
   - **Do not use AI images as the main source for the beta.** Pure AI output likely cannot be owned. Older benchmarks show these tools often get the positions of objects wrong, and a wrong sign or lane on a teaching picture teaches the wrong rule. A small pilot can test whether today's tools are good enough. Any AI picture we keep must be checked detail by detail and labelled.
4. **Cost and time (our estimates, from Upwork's published rates):**
   - About **USD 3,000–8,000 and 4–8 weeks** for 100–150 drawn scenes from one freelancer (illustrators USD 15–30 per hour, 3D artists USD 25–40 per hour).
   - Or **150–300 hours** of our own time in Blender.
   - Own photos: almost no cash and about 1–2 weeks.
   - Stock photos would cost about USD 350–1,400 for 150, but they rarely show Lithuanian signs and markings, and we cannot choose the situation.
5. **Still pictures now; animation later**, and only in Rule Explainers where the movement matters.
6. **Measure it.** Show some learners a text-only version and others a picture version of the same Question. Compare their later answers on new exam-like picture Questions.

**Overall evidence strength:**
- **Moderate** that representational pictures help learners answer, and that practice should match the exam task.
- **Moderate** that still-picture hazard training changes where learners look on real roads.
- **No direct study** of situation pictures and the Regitra pass rate.
- **Legal part:** facts only, to be checked by a lawyer.

---

## A. Learning value

### A1. Do pictures help, compared with text only?

- **Multimedia principle.** "People learn better from words and pictures than from words alone." In Mayer's own studies, this held in 13 of 13 tests, with a median effect of *d* = 1.35 on transfer tests ([Mayer 2024, *Educational Psychology Review*, Table 6](https://doi.org/10.1007/s10648-023-09842-1)). These are lab studies of science lessons by one research group, so the real-world effect is likely smaller.
- **Pictures inside test Questions** are the closest match to our case: a picture above a multiple-choice Question.
  - A 2026 meta-analysis covered 42 studies (158 effect sizes). **Representational pictures**, which show what the Question describes, raised performance (*g* = 0.35), confidence judgements (*g* = 0.32) and test-taker satisfaction (*g* = 0.21). **Decorative pictures** had no effect on performance (*g* = −0.02). "Informative" pictures, which add information that is not in the text, gave very mixed results ([Schewior & Lindner 2026, *Journal of Educational Psychology*](https://doi.org/10.1037/edu0001016)).
  - In a computer-based experiment (n = 404), representational pictures improved scores, perceived ease and test-taking pleasure. Decorative pictures did not ([Lindner 2020, *Learning and Instruction*](https://doi.org/10.1016/j.learninstruc.2020.101345)).
  - In a classroom experiment (N = 410), representational pictures raised scores at every Question position and reduced rapid guessing ([Lindner et al. 2017, *Contemporary Educational Psychology*](https://doi.org/10.1016/j.cedpsych.2017.09.009)).
  - Eye tracking (n = 62): with a picture, students read less text and looked less at wrong Options. The picture acts as a "mental scaffold" ([Lindner et al. 2016, *Learning and Instruction*](https://doi.org/10.1016/j.learninstruc.2016.10.007)).
- **KET fit.** Most of the Theory Exam's situation pictures are not decoration: the Question cannot be answered without them ("Is overtaking allowed in this situation?"). Our practice Questions should be the same. The picture must carry the situation, and the text asks about it.

### A2. Which multimedia principles apply

From a meta-review of 29 reviews (1,189 studies, 78,177 participants): the largest benefits were for **temporal/spatial contiguity** and **signalling**. There was also robust evidence for **coherence** (removing seductive details), animation, segmenting and others ([Noetel et al. 2022, *Review of Educational Research*](https://doi.org/10.3102/00346543211052329)).

| Principle | What it says | Rule for our pictures |
|---|---|---|
| Multimedia | Words + pictures > words alone (*d* = 1.35, 13 tests; [Mayer 2024](https://doi.org/10.1007/s10648-023-09842-1)) | Add a situation picture wherever the rule is about a situation. |
| Coherence / seductive details | Interesting but irrelevant details hurt learning: small to medium effect on retention, medium effect on transfer, over 39 effects ([Rey 2012](https://doi.org/10.1016/j.edurev.2012.05.003)). A later meta-analysis also found that they hinder learning ([Sundararajan & Adesope 2020](https://doi.org/10.1007/s10648-020-09522-4)). | No decoration, no clutter, no brand logos. Show only the cars, signs and markings that matter, plus a little realistic background. |
| Spatial contiguity | Put words close to the picture parts they describe. Mayer's median *d* = 0.82, 9 tests ([Mayer 2024](https://doi.org/10.1007/s10648-023-09842-1)). | Label cars "A", "B", "C" on the picture itself, so Options can say "Car B goes first". |
| Signalling | Cues that point to the key element help (one of the largest benefits in [Noetel et al. 2022](https://doi.org/10.3102/00346543211052329)). | In the **feedback** after an answer, highlight the key sign or car. Do **not** do this in the Question itself, because the exam does not. |

### A3. Still pictures or animation?

- **On average, animation beats still pictures.** A meta-analysis of 26 studies (76 comparisons) found *d* = 0.37. The advantage was larger for representational animations (*d* = 0.40), very realistic or video-based animations (*d* = 0.76), and procedural-motor skills (*d* = 1.06) ([Höffler & Leutner 2007, *Learning and Instruction*](https://doi.org/10.1016/j.learninstruc.2007.09.013), abstract via [ERIC](https://eric.ed.gov/?id=EJ780451)).
- **Animation helps mainly when the change itself must be learned.** A review of 194 studies, with a re-analysis of one meta-analysis, found animation clearly better than still pictures only "if the features of the displayed changes had to be learned" ([Ploetzner, Berney & Bétrancourt 2020, *Journal of Computer Assisted Learning*](https://doi.org/10.1111/jcal.12476)).
- **In test Questions,** both static and animated representational pictures raised correct answers compared with text only (456 students). The effects depended on prior knowledge and text modality ([Ehrhart & Lindner 2023, *Contemporary Educational Psychology*](https://doi.org/10.1016/j.cedpsych.2023.102151)).
- **KET fit.** The Theory Exam has **no video** (issue #2), so practice Questions should be still pictures. Animation is worth it later in Rule Explainers about movement: order at a crossing, merging, overtaking. Still pictures are also much cheaper to make and to change.

### A4. Photos or illustrations (realism)?

- **Simple drawings can teach better.** A schematic animation of cell division beat a realistic one on a multiple-choice and a picture test (37 students). Watching the realistic version twice gave "far lower learning outcomes" ([Scheiter et al. 2009, *Learning and Instruction*](https://doi.org/10.1016/j.learninstruc.2008.08.001), abstract via [ERIC](https://eric.ed.gov/?id=EJ856612)).
- **But realism helps when the test is realistic.** Learners who studied with a realistic picture scored much higher when the test also used a realistic picture. "Matching the realism and concreteness in the learning and testing stages lead[s] to the best performance" (N = 40, anatomy; [Skulmowski & Rey 2021, *Human Behavior and Emerging Technologies*](https://doi.org/10.1002/hbe2.209)).
- A review proposes that realism helps or hurts depending on the task and the test, and that "the nature of these tests is emerging as a major factor" ([Skulmowski et al. 2022, *Educational Psychology Review*](https://doi.org/10.1007/s10648-021-09638-1)).
- **KET fit.** Regitra mixes simple 3D drawings with real photos. So should we: mostly simple drawn scenes, which make the rule clear, plus some real photos so that learners also see real Lithuanian streets. Small studies only, so this is weak evidence.

### A5. Driving-specific evidence

- **Still pictures can train where to look.**
  - RAPT, a PC program, used "sequences of still snapshots" of the driver's view and top-down "plan views". On a real-road drive with eye tracking, trained novices looked at the risk area in 60.6 % of scenarios. Untrained novices did so in 31.8 % (t(22) = 4.58, p < .001).
  - The effect held for scenarios like those trained (72.7 %) and for new ones (46.0 %) ([Pradhan, Pollatsek, Knodler & Fisher 2009, *Ergonomics*](https://doi.org/10.1080/00140130802550232); full text [PMC2707454](https://pmc.ncbi.nlm.nih.gov/articles/PMC2707454)).
  - The sample is small (about 24 drivers).
- **Reviews.**
  - 19 studies of hazard anticipation training for drivers under 21: "In all studies, young drivers showed improvement in selected hazard anticipation outcomes, but none investigated crash effects." Most outcomes were short-term ([McDonald et al. 2015, *Journal of Adolescent Health*](https://doi.org/10.1016/j.jadohealth.2015.02.013)).
  - A meta-analysis of 19 eye-tracking training studies found that training with **both** driver's-eye (egocentric) and bird's-eye (exocentric) views gave better hazard anticipation than either view alone ([Unverricht, Samuel & Yamani 2018, *Transportation Research Record*](https://doi.org/10.1177/0361198118768530)). Regitra also uses both views.
- **Crashes: mixed.** In a California study, 5,251 new teen drivers were followed for 12 months after licensing. There was **no overall** crash effect. RAPT-trained males had about **23.7 % fewer crashes** (p = .019). Females showed a non-significant 10.7 % increase ([Thomas et al. 2016, NHTSA DOT HS 812 235](https://www.nhtsa.gov/sites/nhtsa.gov/files/812235-awarenessperceptiontrainingnoviceteendrivers.pdf)).
- **Video-based training.** A six-session online course using real crash videos improved hazard perception response time, hazard prediction and following distance in a randomised controlled trial ([Horswill et al. 2021, *Accident Analysis & Prevention*](https://doi.org/10.1016/j.aap.2020.105969)).
- **Still-picture tests measure something real.**
  - A static-image hazard test told novices from experienced drivers apart with 78 % accuracy (reliability α = .91) ([Scialfa et al. 2012](https://doi.org/10.1016/j.aap.2011.09.005)).
  - A **Lithuanian** test built from 27 static traffic scenes separated inexperienced from experienced drivers. It also separated drivers with fewer than three past crashes from those with three or more ([Tūskė, Šeibokaitė, Endriulaitienė & Lehtonen 2019, *IATSS Research*](https://doi.org/10.1016/j.iatssr.2018.10.001)).
  - But static and video tests correlate only about .40, so they measure partly different skills ([Scialfa et al. 2013](https://doi.org/10.1016/j.aap.2012.12.006)).
  - Failing Queensland's video hazard test predicted 25 % more active crashes in the next year ([Horswill, Hill & Wetton 2015](https://doi.org/10.1016/j.aap.2015.05.019)).
- **Multiple-choice after a scene still works.** Learners and experienced drivers saw 21 animated driving scenarios. Multiple-choice Questions after the scene were easier than reacting during it, but both formats separated experts from novices equally well ([Malone & Brünken 2015, *Procedia Manufacturing*](https://doi.org/10.1016/j.promfg.2015.07.713)).
- **Caveat.** Most of this research is about **hazard perception** (Theory Exam theme 1, 6 of 30 Questions). Situation pictures for **rules** (priority, lanes, overtaking) are closer to the "pictures in test items" research in A1. No study measured a theory-exam pass rate.

### A6. Exam fit: Regitra's style and transfer-appropriate processing

**Regitra's style** comes from demo test 284 (issue #2) plus a look at Questions 1–3 on 2026-10-13:

- The **situation pictures are simple computer-drawn 3D scenes** with flat colours (green grass, grey road, blue sky) and little detail.
  - Driver's-eye scenes often show the inside of the car: windscreen frame, steering wheel, mirror.
  - Bird's-eye scenes show a crossing from above, with cars and signs.
  - Each has a "REGITRA" watermark.
- **Real photos** are low-resolution street photos of signs or markings.
- One picture of about 500 × 300 px sits above the text. Options are text only. There is no video.
- Counts in the demo: 13 drawn situations (10 driver's-eye or street level, 3 bird's-eye), 4 road or sign photos, 7 sign drawings, 1 photo of the exam car, and 5 Questions without a picture.

**Does matching the style matter?**

- **Transfer-appropriate processing.** Memory is best when the processing at study matches the processing the test needs ([Morris, Bransford & Franks 1977](https://doi.org/10.1016/S0022-5371(77)80016-9)).
- **Testing research.** A meta-analysis (192 effect sizes, N = 10,382) found that practice testing transfers (*d* = 0.40), including **across test formats** and to application Questions. **Response congruency**, meaning the same kind of response on both tests, strongly affects transfer ([Pan & Rickard 2018, *Psychological Bulletin*](https://doi.org/10.1037/bul0000151)). Earlier KETGO research also found that application quizzes helped application exam Questions, while definition quizzes did not (`docs/research/learning-techniques.md` on branch `research/learning-techniques`, section D6).
- **Realism match.** Scores were best when the realism of the study pictures matched the test pictures ([Skulmowski & Rey 2021](https://doi.org/10.1002/hbe2.209)). Small study.
- **So:** match the **task** closely: a still scene, a text Question about it, and Options to tick (all-or-nothing scoring, issue #2), with both driver's-eye and bird's-eye views. Match the **look** roughly: simple 3D drawings plus some photos. **Do not copy Regitra's look**, its pictures or its watermark (see B5).

### A7. What we do not know

- No study compared text-only and picture practice for a theory test like Regitra's, measured by pass rate.
- The "pictures in test items" studies use school science and maths, not traffic.
- The hazard-training studies are small or short. Crash results are mixed.
- KETGO must measure this itself (Recommendation, point 6).

---

## B. Sources and law (facts, not legal advice)

### B0. Basic rules that apply to every source

- **What is protected.** Copyright protects "originalūs literatūros, mokslo ir meno kūriniai" (original literary, scientific and artistic works) (Lithuanian Copyright Law VIII-1185, **Art. 4(1)**). Photographs count only if original in "kompozicijos, objektų parinkimo ar jų fiksavimo" (composition, choice of objects or capture) (**Art. 2(12)**, **Art. 4(2)(8)**). Copyright starts when the work is created (**Art. 13**) and lasts the author's life plus 70 years (**Art. 34(1)**). We found no separate rule for "simple" photos.
- **Who is the author.** "Autorius yra kūrinį sukūręs fizinis asmuo." (The author is the natural person who created the work.) (**Art. 6(1)**).
- **EU originality test (CJEU).** A work must be "its author's own intellectual creation" ([Infopaq C-5/08, para 37](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62008CJ0005)). For photos, it must reflect "the author's personality" through "free and creative choices" such as framing, angle and lighting ([Painer C-145/10, paras 88–92](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62010CJ0145)). There is no originality where the result is "dictated by technical considerations, rules or other constraints which have left no room for creative freedom" ([Brompton C-833/18, para 24](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62018CJ0833); see also [Cofemel C-683/17, para 29](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0683)).
- **Pictures found online.** Posting someone's photo on our site, even if it was freely shown elsewhere, is a new "communication to the public" and needs the rightholder's consent ([Renckhoff C-161/17, paras 44 and 47](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0161)).
- **Teaching exception: does not apply.** Art. 22(1)(1) allows use only for "nekomerciniais mokymo ... tikslais" (non-commercial teaching purposes), tied to educational institutions. A paid study app cannot rely on it.
- **Version caveat.** The Copyright Law articles were read in the 2022 consolidated text (amendment XIV-970), from [WIPO Lex](https://www.wipo.int/wipolex/en/legislation/details/21605). e-seimas lists later editions from 2024-01-01, 2024-05-01 and 2026-06-01 ([edition list](https://e-seimas.lrs.lt/portal/legalActEditions/lt/TAD/TAIS.81676)). **These were not read.** The lawyer should check Arts. 5, 9, 28 and 38–42 in the current text.

### B1. Our own photos

- **Copyright.** The person who takes an original photo is its author (Art. 6(1)).
  - If an **employee** takes it as part of the job, the economic rights pass to the employer **for only 5 years** "jeigu kitaip nenustatyta sutartyje" (unless the contract says otherwise) (**Art. 9(2)**).
  - If a friend or freelancer takes it, we need a written transfer (see B2).
- **People in the picture.** A person's photo may be reproduced or shown "tik jo sutikimu" (only with their consent), but consent is not needed when the photo is taken "viešoje vietoje" (in a public place), unless it would harm the person's honour or reputation (**Civil Code Art. 2.22(1)–(2)**; 2021 text, the current edition was not read).
  - Under the GDPR, an identifiable person is personal data (**[Art. 4(1)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679)**). The household exemption does not cover commercial activity (Art. 2(2)(c), recital 18).
  - Whether a number plate alone is personal data is not settled in the sources we read. The **safest practice is to blur faces and plates.**
- **Buildings.** Buildings and sculptures in public places may be shown (**Art. 28(1)(1)**). This does not apply when the building or sculpture is "pagrindinis vaizdavimo objektas" (the main subject) and the use is commercial (**Art. 28(2)**). A building in the background of a road scene is normally not the main subject, but this is a judgement call.
- **Fit.** Real Lithuanian signs, markings and weather are good for risk Questions and signs in context. But we cannot arrange other cars in exact positions, so photos are a poor fit for most priority puzzles.
- **Cost and speed (estimate).** Almost no cash: a phone or dashcam and fuel. About 1–2 weeks to shoot, choose and blur about 100 usable photos.

### B2. Commissioned illustrations, or our own 3D scenes

- **Contract rules (Copyright Law).**
  - Contracts that transfer economic rights, licence contracts and commissioned-work contracts "sudaromos raštu" (must be in writing) (**Art. 42(1)**).
  - The contract should name the work, the rights or uses transferred, exclusive or not, the territory, the term, and the fee (**Art. 40(1)**).
  - **Defaults if the contract is silent** (Art. 40(2)):
    - Only the rights needed for the contract's purpose pass.
    - With **no territory, it covers Lithuania only.**
    - With **no term, either side may end it on one year's notice.**
  - A licence is exclusive only if the contract says so (**Art. 39(2)**).
  - Rights in "all future works" cannot be transferred (**Art. 38(3)**).
  - **Moral rights** (name, integrity) stay with the author and cannot be transferred (**Art. 14(2), 38(4)**).
  - Commissioned works: **Art. 41**.
- **Building the scenes ourselves.**
  - [Blender](https://www.blender.org/about/license/) is free (GPL) and says: "What you create with Blender is your sole property ... Blender can be used commercially."
  - CC0 3D parts can be used commercially without credit: [Poly Haven](https://polyhaven.com/license) ("You can use our assets for any purpose, including commercial work"), [ambientCG](https://ambientcg.com/license) and [Kenney](https://kenney.nl/support).
  - [CARLA](https://github.com/carla-simulator/carla) driving-simulator assets are CC-BY, which requires credit. Its Unreal Engine licence was not checked.
- **Fit.** This is the best control: exact positions, Lithuanian signs and markings, a style close to the exam's, the same scene with small changes for varied Questions, and easy fixes when KET changes. Regitra's style (A6) is simple enough to make with these tools.
- **Cost (published rates + our estimate).**
  - [Upwork](https://www.upwork.com/hire/illustrators/cost) lists illustrators at USD 15–30 per hour, and [3D rendering artists](https://www.upwork.com/hire/3d-rendering-artists/cost/) at USD 25–40 per hour. These are marketplace figures, not an independent benchmark.
  - Our estimate: a reusable kit (roads, cars, signs) and then about 0.5–2 hours per scene. That makes about **USD 1,500–5,500** for 150 bird's-eye scenes, or **USD 5,000–15,000** for 150 driver's-eye 3D scenes.
  - A mix of about 100–150 scenes costs roughly **USD 3,000–8,000**.
- **Speed (estimate).** 4–8 weeks for one freelancer. In-house: 150–300 hours, plus time to learn Blender.

### B3. AI-generated images

- **What the providers' terms say.**
  - **OpenAI:** "you ... own the Output. We hereby assign to you all our right, title, and interest, if any, in and to Output" ([terms](https://openai.com/policies/row-terms-of-use/)).
  - **Midjourney:** "You own all Assets You create ... to the fullest extent possible under applicable law". A company with more than USD 1 M yearly revenue must be on the Pro or Mega plan to own them. Pictures are "publicly viewable and remixable" by default, and Stealth mode is Pro/Mega only ([ToS sec. 4](https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service)).
  - **Google Gemini API:** "Google won't claim ownership ... Google may generate the same or similar content for others" ([terms](https://ai.google.dev/gemini-api/terms)).
  - **Adobe Firefly:** outputs "can be used for commercial purposes". IP indemnity is offered only to "eligible enterprise customers" ([plans FAQ](https://www.adobe.com/products/firefly/plans.html)).
- **Can the output be owned under the law?** Probably not, if a person only wrote the prompt.
  - Lithuanian law requires a natural-person author (Art. 6(1)).
  - CJEU originality needs the author's own "free and creative choices" (Painer, above).
  - The EUIPO study notes "the prevailing view that AI-generated content is not copyright eligible" ([EUIPO 2025, *The Development of Generative AI from a Copyright Perspective*](https://www.euipo.europa.eu/en/publications/genai-from-a-copyright-perspective-2025)).
  - A European Parliament study says: "works generated entirely by machines without human intervention do not benefit from copyright protection" ([EP 2025](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/774095/IUST_STU(2025)774095_EN.pdf)).
  - The Prague Municipal Court (10 C 13/2023, 2023) held that an AI-made image was not a work because it was not the result of a natural person's creative activity.
  - **No CJEU ruling yet.** Case [C-250/25 *Like Company v Google*](https://infocuria.curia.europa.eu/tabs/affair?publishedId=C-250%2F25) is pending, but it is about AI training and press content, not about who owns AI output.
  - **Consequence:** we could use pure AI pictures, but we probably could not stop a competitor from copying them. Real human editing may add protection, but where the line is remains unsettled.
- **EU AI Act** ([Regulation 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689)).
  - **Art. 50(2):** providers of image generators must mark outputs "in a machine-readable format". Art. 50 applies from 2 Aug 2026 (Art. 113). A 2026 amendment gives generators already on the market until 2 Dec 2026 ([Reg. 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744)).
  - **Art. 50(4):** a deployer (us) must disclose a **"deep fake"**. Art. 3(60) defines this as AI content that "resembles existing persons, objects, places, entities or events and would falsely appear ... to be authentic".
  - Whether a realistic AI road scene counts is not decided in any source we read.
- **Accuracy risk.** Benchmarks from 2023 found that image models "often struggle to effectively compose objects with different attributes and relationships", including spatial relationships ([Huang et al. 2023, T2I-CompBench, NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f8ad010cdd9143dbb0e9308c093aff24-Abstract-Datasets_and_Benchmarks.html)). Newer models may be better. **We did not test today's tools on Lithuanian signs or markings.** A pilot of about 20 scenes would show this.
- **Cost and speed.**
  - OpenAI lists about USD 0.006 / 0.053 / 0.211 per 1024×1024 image (low / medium / high quality, GPT Image 2) ([guide](https://platform.openai.com/docs/guides/image-generation)).
  - Google lists USD 0.039–0.24 per image depending on model and size ([pricing](https://ai.google.dev/gemini-api/docs/pricing)).
  - Midjourney costs USD 10–120 per month ([plans](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans)).
  - Generating is fast (OpenAI: "up to 2 minutes" for complex prompts), so cash cost is tiny. The real cost is checking and redoing pictures until every sign, line and car is right.

### B4. Licensed stock and free photo sites

- **Paid stock.**
  - Standard licences allow use in apps and websites:
    - [Shutterstock](https://www.shutterstock.com/license) 1.a.i.1: "mobile 'apps', software".
    - [Adobe Stock](https://stock.adobe.com/plans): the print limit "doesn't apply when the image is only for display on websites ... or mobile applications".
    - [iStock](https://www.istockphoto.com/legal/license-agreement): the cap "does not apply to electronic reproduction".
    - [Depositphotos](https://depositphotos.com/license.html) sec. 3.
  - The same licences set common limits:
    - "Editorial Use Only" pictures may **not** be used commercially. Street photos with readable plates or faces are often editorial-only.
    - No making pictures downloadable as standalone files, and no "gallery" for users to browse.
    - No AI training.
  - **Prices:**
    - iStock from USD 2.90 per download (annual plan), USD 12 for a single credit ([pricing](https://www.istockphoto.com/plans-and-pricing)).
    - Adobe: 40 standard images for USD 359.99.
    - Shutterstock: from USD 25 per month.
    - So 150 pictures cost about **USD 350–1,400**.
  - **Fit:** we can only pick existing scenes. Lithuanian signs and markings are probably rare (search counts not checked).
- **Free sites.**
  - [Pexels](https://www.pexels.com/license/) and [Pixabay](https://pixabay.com/service/license-summary/): free for commercial use, no credit needed, but no reselling the files as such. Pixabay also bans commercial use of recognisable brands. Unsplash's licence page did not load, so it was not checked.
  - [Wikimedia Commons, CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en): you must credit the author and the licence (sec. 3(a)), and changed versions must use the same licence (sec. 3(b)).
  - **Mapillary** street photos are CC BY-SA ([help](https://help.mapillary.com/hc/en-us/articles/115001770409-Licenses)). But its [terms](https://www.mapillary.com/terms) sec. 12 allow commercial use only "for the following commercial purposes" (product development, client services), so showing them in a paid app is unclear. Ask Mapillary first.
  - **Google Street View screenshots are not allowed:** "You may not screenshot Street View imagery ... for any purpose" ([Google geo guidelines](https://about.google/brand-resource-center/products-and-services/geo-guidelines/)).

### B5. Regitra's and the KET's own images

- **Regitra's exam and demo pictures: do not use.**
  - Exam Questions are confidential (1V-115 part A p. 3, issue #2).
  - Order 1V-329 p. 31 says: "AB „Regitra" darbuotojams ir egzaminuojamiesiems draudžiama kopijuoti ar kitaip platinti egzamino klausimus." (Regitra staff and examinees may not copy or otherwise distribute exam Questions.) Regitra may claim damages ([edition list](https://e-seimas.lrs.lt/portal/legalActEditions/lt/TAD/TAIS.327051); read via a mirror).
  - Regitra is now **AB Regitra**, a joint-stock company. Its pictures are not legal acts, and we found no exemption or reuse permission for them. The demo pictures carry a Regitra watermark.
  - The general definition of an "official document" in the Law on Documents and Archives is about record keeping ([e-TAR](https://e-tar.lt/rs/actualedition/TAR.1FEF229DA7C6/iHxgXXcDDA)). We found nothing that makes a state company's pictures free.
  - Using Regitra's pictures would also break our own rule that only Own Questions are shown (`GLOSSARY.md`).
- **KET sign and marking images: very likely free to use.**
  - The Copyright Law does not protect "teisės aktai, oficialūs administracinio, teisinio ar norminio pobūdžio dokumentai ... taip pat jų oficialūs vertimai" (legal acts and official administrative, legal or normative documents, and their official translations) (**Art. 5(2)**).
  - The KET is a Government resolution (No. 1950, 2002-12-11). In the current version, signs are in **annex 1 "Kelio ženklai"** and markings in **annex 3** ([KET on e-TAR](https://www.e-tar.lt/portal/lt/legalAct/TAR.BBE7D61A0416/asr)).
  - An annex is part of the legal act. Our conclusion that the annex drawings are covered is an **inference**: the law does not say "images in annexes", and we found no court decision. Wikimedia's [PD-LT-exempt](https://commons.wikimedia.org/wiki/Template:PD-LT-exempt) tag uses the same reasoning.
  - The KET itself says nothing about reuse and names no LST standard. We could not check whether a separate LST standard for sign design exists or what its copyright terms are.
- **Redrawn sign files are different.** Someone's own redrawing can carry its own licence. Example: "LT road sign 414.svg" on Commons is **CC BY 4.0**, which requires credit. Use the drawings from the e-TAR annex, or draw our own from them.

### B6. Comparison for about 100–200 pictures

| Source | Who owns it / main condition | Cash cost (≈150 pictures) | Time | Fit for KET Questions |
|---|---|---|---|---|
| Own photos | We do, if taken by us. Employee: 5-year default unless the contract says otherwise. Blur faces and plates. | ~0 | 1–2 weeks | Good for risk, weather and signs in streets. Poor for exact priority setups. |
| Commissioned drawings / 3D | We do, **only with a written contract** that names the rights, territory and term. Moral rights stay with the artist. | ~USD 3,000–8,000 (estimate) | 4–8 weeks | **Best.** Exact, Lithuanian, close to the exam style, editable. |
| Own 3D (Blender + CC0) | We do. Blender output is ours. CC0 parts are free. | ~0 cash, 150–300 hours | 6–10 weeks part-time (estimate) | Best, if we have the skills. |
| AI-generated | Providers assign rights, but **pure AI output likely has no copyright**. AI Act labelling questions. | < USD 500 | Days, plus heavy checking | Risky for exact signs and positions. Pilot only. |
| Licensed stock | Licence, not ownership. No editorial-only, no standalone files. | ~USD 350–1,400 | Days, but hard to find matching scenes | Weak. Few Lithuanian scenes. |
| Free sites / Mapillary | Pexels and Pixabay are free. CC BY-SA needs credit and share-alike. Mapillary commercial use is unclear. Street View is banned. | 0 | Days | Weak to medium. |
| Regitra images | **Not allowed** (exam secrecy, p. 31, Regitra's own work) | — | — | — |
| KET annex sign drawings | Very likely no copyright (Art. 5(2)). Lawyer to confirm. | 0 | Hours | Use them for the signs inside our scenes. |

### B7. What the lawyer check should cover

1. Confirm that KET annex 1 and annex 3 drawings are free under Art. 5(2) in the current Copyright Law text (2026-06-01 edition).
2. A template rights-transfer contract for illustrators and 3D artists (Arts. 38–42): worldwide, full term, exclusive, all uses (web, app, print, marketing, changes), and the right to edit.
3. Whether AI-made or AI-assisted scenes need a label under AI Act Art. 50(4).
4. Photos: are blurred faces and plates enough under the GDPR and Civil Code Art. 2.22?
5. That none of our pictures could be confused with Regitra's (no watermark lookalikes).

---

## Open questions worth adding to the map

1. **Who makes the pictures, and what is the budget?** A freelancer under contract, or our own Blender work? This decides the cost (USD 3,000–8,000) or the time (150–300 hours).
2. **AI pilot:** test about 20 scenes with a current image model for sign, marking and position accuracy before ruling AI in or out.
3. **Lawyer check scope:** add the five points in B7 to the planned pre-launch check.
4. **A/B test of picture value:** text-only vs picture versions of the same rule, measured on later new picture Questions. This needs the logging planned in the learning-techniques research.
5. **Animated Rule Explainers** for movement rules (crossing order, merging): after the beta, if still pictures leave gaps.

## Sources

### Papers (learning value)

1. Schewior, L. & Lindner, M. A. (2026). Multimedia effects in testing: A meta-analysis on cognitive, metacognitive, and affective effects of pictures in test items. *Journal of Educational Psychology*. https://doi.org/10.1037/edu0001016
2. Lindner, M. A. (2020). Representational and decorative pictures in science and mathematics tests: Do they make a difference? *Learning and Instruction*. https://doi.org/10.1016/j.learninstruc.2020.101345
3. Lindner, M. A., Lüdtke, O., Grund, S. & Köller, O. (2017). The merits of representational pictures in educational assessment. *Contemporary Educational Psychology*. https://doi.org/10.1016/j.cedpsych.2017.09.009
4. Lindner, M. A., Eitel, A., Strobel, B. & Köller, O. (2016). Identifying processes underlying the multimedia effect in testing: An eye-movement analysis. *Learning and Instruction*. https://doi.org/10.1016/j.learninstruc.2016.10.007
5. Mayer, R. E. (2024). The past, present, and future of the cognitive theory of multimedia learning. *Educational Psychology Review*, 36, 8. https://doi.org/10.1007/s10648-023-09842-1
6. Noetel, M. et al. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research*, 92(3). https://doi.org/10.3102/00346543211052329
7. Rey, G. D. (2012). A review of research and a meta-analysis of the seductive detail effect. *Educational Research Review*, 7(3). https://doi.org/10.1016/j.edurev.2012.05.003
8. Sundararajan, N. & Adesope, O. (2020). Keep it coherent: A meta-analysis of the seductive details effect. *Educational Psychology Review*, 32(3). https://doi.org/10.1007/s10648-020-09522-4
9. Höffler, T. N. & Leutner, D. (2007). Instructional animation versus static pictures: A meta-analysis. *Learning and Instruction*, 17(6). https://doi.org/10.1016/j.learninstruc.2007.09.013
10. Ploetzner, R., Berney, S. & Bétrancourt, M. (2020). A review of learning demands in instructional animations. *Journal of Computer Assisted Learning*. https://doi.org/10.1111/jcal.12476
11. Ehrhart, T. & Lindner, M. A. (2023). Computer-based multimedia testing: Effects of static and animated representational pictures and text modality. *Contemporary Educational Psychology*, 73. https://doi.org/10.1016/j.cedpsych.2023.102151
12. Scheiter, K., Gerjets, P., Huk, T., Imhof, B. & Kammerer, Y. (2009). The effects of realism in learning with dynamic visualizations. *Learning and Instruction*, 19(6). https://doi.org/10.1016/j.learninstruc.2008.08.001
13. Skulmowski, A. & Rey, G. D. (2021). Realism as a retrieval cue. *Human Behavior and Emerging Technologies*, 3. https://doi.org/10.1002/hbe2.209
14. Skulmowski, A., Nebel, S., Remmele, M. & Rey, G. D. (2022). Is a preference for realism really naive after all? *Educational Psychology Review*. https://doi.org/10.1007/s10648-021-09638-1
15. Morris, C. D., Bransford, J. D. & Franks, J. J. (1977). Levels of processing versus transfer appropriate processing. *Journal of Verbal Learning and Verbal Behavior*, 16(5). https://doi.org/10.1016/S0022-5371(77)80016-9
16. Pan, S. C. & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin*, 144(7). https://doi.org/10.1037/bul0000151
17. Pradhan, A. K., Pollatsek, A., Knodler, M. & Fisher, D. L. (2009). Can younger drivers be trained to scan for information that will reduce their risk...? *Ergonomics*, 52(6). https://doi.org/10.1080/00140130802550232
18. McDonald, C. C. et al. (2015). A review of hazard anticipation training programs for young drivers. *Journal of Adolescent Health*. https://doi.org/10.1016/j.jadohealth.2015.02.013
19. Unverricht, J., Samuel, S. & Yamani, Y. (2018). Latent hazard anticipation in young drivers: Review and meta-analysis of training studies. *Transportation Research Record*. https://doi.org/10.1177/0361198118768530
20. Thomas, F. D. et al. (2016). *Evaluation of the Safety Benefits of the Risk Awareness and Perception Training Program for Novice Teen Drivers* (DOT HS 812 235). NHTSA. https://www.nhtsa.gov/sites/nhtsa.gov/files/812235-awarenessperceptiontrainingnoviceteendrivers.pdf
21. Horswill, M. S., Hill, A., Silapurem, L. & Watson, M. (2021). A thousand years of crash experience in three hours. *Accident Analysis & Prevention*. https://doi.org/10.1016/j.aap.2020.105969
22. Horswill, M. S., Hill, A. & Wetton, M. (2015). Can a video-based hazard perception test used for driver licensing predict crash involvement? *Accident Analysis & Prevention*, 82. https://doi.org/10.1016/j.aap.2015.05.019
23. Scialfa, C. T. et al. (2012). The effects of driving experience on responses to a static hazard perception test. *Accident Analysis & Prevention*, 45. https://doi.org/10.1016/j.aap.2011.09.005
24. Scialfa, C. T. et al. (2013). A comparison of static and dynamic hazard perception tests. *Accident Analysis & Prevention*, 51. https://doi.org/10.1016/j.aap.2012.12.006
25. Tūskė, V., Šeibokaitė, L., Endriulaitienė, A. & Lehtonen, E. (2019). Hazard perception test development for Lithuanian drivers. *IATSS Research*, 43(2). https://doi.org/10.1016/j.iatssr.2018.10.001
26. Malone, S. & Brünken, R. (2015). Hazard perception assessment – How much ecological validity is necessary? *Procedia Manufacturing*, 3. https://doi.org/10.1016/j.promfg.2015.07.713
27. Huang, K. et al. (2023). T2I-CompBench. *NeurIPS 36, Datasets and Benchmarks*. https://proceedings.neurips.cc/paper_files/paper/2023/hash/f8ad010cdd9143dbb0e9308c093aff24-Abstract-Datasets_and_Benchmarks.html

### Law and official texts

- Lithuanian Law on Copyright and Related Rights No. VIII-1185: edition list <https://e-seimas.lrs.lt/portal/legalActEditions/lt/TAD/TAIS.81676>. Text read: the 2022 consolidation on WIPO Lex <https://www.wipo.int/wipolex/en/legislation/details/21605>. Articles used: 2(12), 4, 5, 6, 9, 13, 14, 22, 28, 34, 38–42.
- KET (Government resolution No. 1950, 2002-12-11), annexes 1 and 3: <https://www.e-tar.lt/portal/lt/legalAct/TAR.BBE7D61A0416/asr>
- Order 1V-329 (Theory Exam conditions), p. 31: <https://e-seimas.lrs.lt/portal/legalActEditions/lt/TAD/TAIS.327051>
- Regitra demo exam: <https://www.eregitra.lt/public-egzis/>. Regitra exam rules and picture counts: issue #2 and `docs/research/regitra-exam-rules.md` (branch `research/regitra-exam-rules`).
- Law on Documents and Archives (definition of "official document"): <https://e-tar.lt/rs/actualedition/TAR.1FEF229DA7C6/iHxgXXcDDA>
- Lithuanian Civil Code Art. 2.22 (right to one's image). The 2021 consolidated text was read via a mirror. Check the current e-seimas edition.
- GDPR (Regulation 2016/679): <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679>
- AI Act (Regulation 2024/1689), Arts. 3(60), 50, 113: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689>. Amendment Reg. 2026/1744: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202601744>
- CJEU cases:
  - Infopaq C-5/08: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62008CJ0005>
  - Painer C-145/10: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62010CJ0145>
  - Cofemel C-683/17: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0683>
  - Brompton C-833/18: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62018CJ0833>
  - Renckhoff C-161/17: <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0161>
  - C-250/25 (pending): <https://infocuria.curia.europa.eu/tabs/affair?publishedId=C-250%2F25>
- EUIPO (2025), *The Development of Generative AI from a Copyright Perspective*: <https://www.euipo.europa.eu/en/publications/genai-from-a-copyright-perspective-2025>
- European Parliament study (2025), *Generative AI and Copyright*: <https://www.europarl.europa.eu/RegData/etudes/STUD/2025/774095/IUST_STU(2025)774095_EN.pdf>
- Municipal Court in Prague, 10 C 13/2023 (2023). Read in English translation; the Czech original was not checked.

### Provider terms and prices (read 2026-10-13)

- Shutterstock licence <https://www.shutterstock.com/license> and pricing <https://www.shutterstock.com/pricing>
- Adobe Stock plans and FAQ <https://stock.adobe.com/plans>
- iStock licence <https://www.istockphoto.com/legal/license-agreement> and pricing <https://www.istockphoto.com/plans-and-pricing>
- Depositphotos licence <https://depositphotos.com/license.html>
- Pexels <https://www.pexels.com/license/>; Pixabay <https://pixabay.com/service/license-summary/>; CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/legalcode.en>
- Mapillary terms <https://www.mapillary.com/terms>; Google geo guidelines <https://about.google/brand-resource-center/products-and-services/geo-guidelines/>
- OpenAI terms <https://openai.com/policies/row-terms-of-use/> and image guide <https://platform.openai.com/docs/guides/image-generation>
- Midjourney ToS <https://docs.midjourney.com/hc/en-us/articles/32083055291277-Terms-of-Service> and plans <https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans>
- Google Gemini API terms <https://ai.google.dev/gemini-api/terms> and pricing <https://ai.google.dev/gemini-api/docs/pricing>
- Adobe Firefly plans <https://www.adobe.com/products/firefly/plans.html>; Stability AI licence <https://stability.ai/license>
- Blender licence <https://www.blender.org/about/license/>; Poly Haven <https://polyhaven.com/license>; ambientCG <https://ambientcg.com/license>; Kenney <https://kenney.nl/support>; CARLA <https://github.com/carla-simulator/carla>
- Upwork rate pages: illustrators <https://www.upwork.com/hire/illustrators/cost>; 3D rendering artists <https://www.upwork.com/hire/3d-rendering-artists/cost/>
- Wikimedia Commons: PD-LT-exempt template <https://commons.wikimedia.org/wiki/Template:PD-LT-exempt>; example file "LT road sign 414.svg" (CC BY 4.0)
