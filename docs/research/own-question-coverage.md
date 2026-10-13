# Own Question coverage and gaps

Answers [issue #4](https://github.com/Whirlywack/ketgo-web/issues/4) on the [KETGO Free Beta map](https://github.com/Whirlywack/ketgo-web/issues/1). Checked on 2026-10-13.

The data is the 274 Own Questions in `~/Documents/Claude/Projects/ket second brain/questions.jsonl` (last change 2026-07-31). One row per Own Question, with its theme and KET chapter, is in [`own-question-coverage.csv`](own-question-coverage.csv).

## Summary

Each Own Question was given one of the 9 Regitra exam themes. The "needed at 500" column assumes the ~500 Own Questions planned for the beta are split the same way as the exam. Our notes list two possible splits, A and B, and [#2](https://github.com/Whirlywack/ketgo-web/issues/2) will decide which one is right. Only two themes differ between them: Behaviour (5 or 4 exam questions) and Safe driving (3 or 4).

| Theme | Own Questions now | Share now | Exam share A (6/5/4/3/3/3/2/2/2) | Exam share B (6/4/4/3/3/4/2/2/2) | Needed at 500 (A / B) | Still to write (A / B) |
|---|--:|--:|--:|--:|--:|--:|
| Risk associated with driving | 10 | 3.6% | 6 of 30 (20%) | 6 of 30 (20%) | 100 | **+90** |
| Behaviour on public roads | 43 | 15.7% | 5 of 30 (17%) | 4 of 30 (13%) | 83 / 67 | +40 / +24 |
| Signs / markings / lights / signals | 59 | 21.5% | 4 of 30 (13%) | 4 of 30 (13%) | 67 | +8 |
| Right of way & passing | 38 | 13.9% | 3 of 30 (10%) | 3 of 30 (10%) | 50 | +12 |
| Special roads / users / manoeuvres | 61 | 22.3% | 3 of 30 (10%) | 3 of 30 (10%) | 50 | 0 (11 too many) |
| Safe driving & critical situations | 19 | 6.9% | 3 of 30 (10%) | 4 of 30 (13%) | 50 / 67 | +31 / +48 |
| Responsible & eco driving | 13 | 4.7% | 2 of 30 (7%) | 2 of 30 (7%) | 33 | +20 |
| General KET & legal | 21 | 7.7% | 2 of 30 (7%) | 2 of 30 (7%) | 33 | +12 |
| Knowledge about vehicles | 10 | 3.6% | 2 of 30 (7%) | 2 of 30 (7%) | 33 | +23 |
| **Total** | **274** | 100% | 30 | 30 | 500 | +226 |

**Short version:**

- **Coverage is wide but flat.** About 230 KET points have at least one Own Question, and about 200 of those have exactly one. The writing went through the rulebook point by point. The result is that a big exam topic like intersections, overtaking or speed gets about as many questions as a small topic like tracked vehicles on asphalt.
- **Risk is the biggest gap.** We have 10 Risk questions, but the exam asks 6 of its 30 questions on Risk. Two mock exams would use up every Risk question we have.
- **Safe driving, vehicles and eco driving are thin.** These topics are not KET rules. They are physics, technique and car knowledge: stopping distance, skids, eco driving, brakes and car maintenance. Today 0 Own Questions cover them.
- **Special roads / users is already full.** We have 61 and need about 50. Pedestrians, cyclists, e-scooters and riders take up much more of our bank than of the Reference Bank.
- **Pictures:** 46 Own Questions (17%) have an image, and every one of those images is a sign or a road marking. There are **0 road-situation pictures**. In the Reference Bank, 79% of category-B questions have a picture. On intersection and traffic-control topics the figure is 97%.
- **Every Own Question has an explanation and a rule link.**
- **Oddities to fix before import:** the 15 `draft` questions are really approved. One question has 5 Options. Two pairs are near-duplicates. In 78% of single-choice questions the correct Option comes first, so Options must be shuffled.

## The biggest gaps, in plain terms

The plan is to reach ~500 Own Questions. That means about 226 more. The split below sends almost all of them to the thin themes and none to Special roads / users.

1. **Risk: we need ~90 more questions.** Topics with no or almost no Own Questions today:
   - risk from road and weather conditions (rain, ice, fog, night, gravel): the Reference Bank has 79 questions here, we have 0
   - seeing danger early and reacting to it: 29 vs 2
   - risk linked to different vehicle types and drivers (for example trucks, motorbikes): 7 vs 0

   The driver's own condition (alcohol, drugs, tiredness, phone) is covered about as well as in the Reference Bank, but with only 4 questions. Much of Risk is about reading a road situation, so many of these questions will need pictures (#14).
2. **Safe driving & critical situations: we need ~31 more (blueprint A) or ~48 more (blueprint B).** Missing topics are reaction time, braking and stopping distance, safe following distance, skidding and aquaplaning, braking on slippery roads and brake failure. We do already have the KET rules for breakdowns, the warning triangle, seat belts, child seats and duties after an accident.
3. **Behaviour on public roads: we need ~40 more (A) or ~24 more (B).** Speed (KET XV) has only 7 questions and lights at night and in fog (KET XII) only 4. Manoeuvres and parking are better covered.
4. **Knowledge about vehicles: we need ~23 more.** Missing topics are brakes, clutch and gearbox, cooling, tyres and wheels, fluids and maintenance (Reference Bank: 64 vs our 0), active and passive safety and the forces on a moving car (20 vs 0), and faults that ban driving (11 vs 1).
5. **Responsible & eco driving: we need ~20 more.** No Own Question covers eco driving: smooth driving, fuel use, idling, tyre pressure. The 13 we have are about carrying passengers, children, pets and cargo.
6. **Right of way & passing: we need ~12 more.** Overtaking (KET XVI) has only 4 questions, while the Reference Bank has 101 on speed and overtaking together. But the bigger problem is intersections. The Reference Bank puts 20% of its category-B questions on intersections, traffic lights and the traffic controller, and almost all of those have a picture. We have 24 such questions (9%), and none has a picture. Good intersection questions need situation pictures (see #14).
7. **General KET & legal: we need ~12 more.** Topics include documents, licence rules, liability and police checks.
8. **Signs / markings: we need only ~8 more** to match the exam share. But only 63 of the ~300 signs and plates in Annex 1, and 18 of the 46 markings, have any Own Question. The next sign questions should cover the most common signs, not try to cover every sign.
9. **Special roads / users / manoeuvres: no more for now.** We have 61, which is 11 more than the target.

The theme of a question is a judgment call (see Method). The Risk gap does not depend on that call. If all 28 questions about pedestrians, cyclists, e-scooters, riders and people with disabilities moved from Special roads into Risk, Risk would have 38 questions (14%). That is still well under the exam's 20%.

## Gaps by KET chapter

Each Own Question is counted once, under the KET chapter of its first rule link.

| KET chapter | Own Questions |
|---|--:|
| I General provisions | 1 |
| II Definitions | 17 |
| III General duties of road users | 9 |
| IV Duties of drivers and vehicle owners | 12 |
| V Drivers and pedestrians | 8 |
| VI Pedestrians | 10 |
| VII Passengers | 1 |
| VIII Cyclists | 7 |
| VIII¹ Electric micro-mobility (e-scooters) | 7 |
| IX Riders and animal drovers | 2 |
| X Traffic lights and controller signals | 9 |
| XI Warning signals | 10 |
| XII Use of lights | **4** |
| XIII Starting and manoeuvring | 14 |
| XIV Position on the road and lanes | 9 |
| XV Speed | **7** |
| XVI Overtaking and passing | **4** |
| XVII Stopping and parking | 15 |
| XVIII Intersections | 14 |
| XIX Railway crossings | 5 |
| XX Motorways and expressways | 1 |
| XXI Residential zones | 5 |
| XXI¹ Bicycle streets | 3 |
| XXII Public transport | 4 |
| XXIII Vehicles of people with disabilities | 2 |
| XXIV Special (emergency) vehicles | 4 |
| XXV Carrying passengers | 5 |
| XXVI Seat belts and other safety equipment | 8 |
| XXVII Carrying cargo | 5 |
| XXVIII Towing | 6 |
| XXIX After a road accident | 4 |
| XXX Vehicle requirements | 8 |
| Annex 1 Road signs | 37 |
| Annex 3 Road markings | 11 |
| Annex 4 Vehicle identification marks | **0** |
| Not KET: SEAKĮ (Road Traffic Safety Law) | 6 |
| Not KET: driving technique, physics, car mechanics | **0** |

What stands out:

- **Too few compared with the size of the topic and with the Reference Bank:** XVI Overtaking (4), XV Speed (7), XII Lights (4) and XVIII Intersections (14, one per KET point).
- **Nothing at all:** Annex 4, the identification marks shown on vehicles such as "Asmuo su negalia". A few Own Questions mention these marks, but none is about them. Also nothing on any topic that is not in the KET text.
- Small chapters such as I and VII have only a few KET points, so 1 question each is in line with their size.

## Reference Bank topics with zero or very few Own Questions

The Reference Bank has 70 topics. For a fair comparison, they are grouped into 36 topic areas and matched to KET chapters. Own Questions are matched to the same areas through their KET point. The counts are active, not-deleted questions linked to category B. The Reference Bank is a competitor's bank, not the Regitra exam, so its shares are only a hint about which topics exist and roughly how big they are.

**Topics where we have no or very few Own Questions** (our share is below 60% of the Reference Bank's share):

| Topic area (Reference Bank code) | Reference Bank, cat. B | Share | Own Questions | Share |
|---|--:|--:|--:|--:|
| Unregulated intersections (1.6.1) | 182 | 11.4% | 8 | 2.9% |
| Speed, overtaking, passing (1.4.4) | 101 | 6.3% | 10 | 3.7% |
| Risk from road and weather conditions (1.1.6) | 79 | 5.0% | **0** | 0% |
| Vehicle mechanics and maintenance (2.x, 3.x, 7.x) | 64 | 4.0% | **0** | 0% |
| Risky situations, anticipation, reaction (1.1.4) | 29 | 1.8% | 2 | 0.7% |
| Vehicle safety systems and driving physics (1.8.1) | 20 | 1.3% | **0** | 0% |
| Technical faults that ban driving (1.8.2) | 11 | 0.7% | 1 | 0.4% |
| Risk of different vehicle types and drivers (1.1.7) | 7 | 0.4% | **0** | 0% |
| Identification marks on vehicles (1.2.2) | 5 | 0.3% | **0** | 0% |

Three more areas are lower than the Reference Bank, but not by as much: traffic lights and controller (1.5.1, 1.5.3: 9 Own Questions vs 77), signal-controlled intersections (1.5.2: 5 vs 41) and lights at night (1.4.2: 4 vs 37). Together with 1.6.1, **intersections and traffic control are 20% of the Reference Bank but only 9% of our Own Questions.**

**Topics where we have more than the Reference Bank** (more than twice its share): pedestrians, cyclists, e-scooters and riders (27 vs 3.5% share), safety equipment (10), vulnerable road users (11), general laws (3) and cargo (5). This is fine, partly because the e-scooter rules are new in 2026. But new writing should go elsewhere.

<details>
<summary>Full table: all 36 topic areas</summary>

| Topic area (Reference Bank code) | Reference Bank, cat. B | Share | Own Questions | Share | At 500, if we matched its share |
|---|--:|--:|--:|--:|--:|
| Getting a licence, novice drivers (1.1.1) | 498 | catch-all, left out | 1 | – | – |
| Laws and general provisions (1.1.2) | 5 | 0.3% | 3 (high) | 1.1% | ~2 |
| Driver condition: alcohol, drugs, tiredness, phone (1.1.3+1.1.5) | 19 | 1.2% | 4 | 1.5% | ~6 |
| Risky situations, anticipation, reaction (1.1.4) | 29 | 1.8% | 2 **(low)** | 0.7% | ~9 |
| Risk from road and weather conditions (1.1.6) | 79 | 5.0% | 0 **(low)** | 0.0% | ~25 |
| Risk of different vehicle types and drivers (1.1.7) | 7 | 0.4% | 0 **(low)** | 0.0% | ~2 |
| Safety equipment, getting out safely (1.1.8) | 10 | 0.6% | 10 (high) | 3.7% | ~3 |
| Vulnerable road users (pedestrians, children, disability) (1.1.9) | 9 | 0.6% | 11 (high) | 4.0% | ~3 |
| Definitions (1.1.10) | 66 | 4.1% | 20 | 7.3% | ~21 |
| Road accidents, first aid (1.1.11) | 28 | 1.8% | 5 | 1.8% | ~9 |
| Duties of road users and drivers (1.1.12) | 72 | 4.5% | 8 | 2.9% | ~23 |
| Registration, insurance, number plates (1.1.13) | 16 | 1.0% | 3 | 1.1% | ~5 |
| Pedestrians, passengers, cyclists, e-scooters, riders (1.1.14) | 56 | 3.5% | 27 (high) | 9.9% | ~18 |
| Road signs (1.2.1) | 163 | 10.2% | 37 | 13.6% | ~51 |
| Identification marks on vehicles (1.2.2) | 5 | 0.3% | 0 **(low)** | 0.0% | ~2 |
| Road markings (1.3.1) | 67 | 4.2% | 11 | 4.0% | ~21 |
| Warning signals (indicators, horn, hazard lights) (1.4.1) | 47 | 2.9% | 10 | 3.7% | ~15 |
| Night, poor visibility, use of lights (1.4.2) | 37 | 2.3% | 4 | 1.5% | ~12 |
| Starting, manoeuvring, position on the road (1.4.3) | 112 | 7.0% | 23 | 8.4% | ~35 |
| Speed, overtaking, passing (1.4.4) | 101 | 6.3% | 10 **(low)** | 3.7% | ~32 |
| Stopping and parking (1.4.5) | 66 | 4.1% | 14 | 5.1% | ~21 |
| Traffic lights and traffic controller (1.5.1+1.5.3) | 77 | 4.8% | 9 | 3.3% | ~24 |
| Signal-controlled intersections (1.5.2) | 41 | 2.6% | 5 | 1.8% | ~13 |
| Unregulated intersections (1.6.1) | 182 | 11.4% | 8 **(low)** | 2.9% | ~57 |
| Conflicting signals (controller / lights / signs) (1.6.2) | 12 | 0.8% | 2 | 0.7% | ~4 |
| Railway crossings (1.7.1) | 27 | 1.7% | 5 | 1.8% | ~8 |
| Motorways, tunnels, residential zones, bicycle streets (1.7.2) | 29 | 1.8% | 9 | 3.3% | ~9 |
| Public transport (1.7.3) | 26 | 1.6% | 4 | 1.5% | ~8 |
| Special (emergency) vehicles (1.7.4) | 24 | 1.5% | 5 | 1.8% | ~8 |
| Towing (1.7.5) | 19 | 1.2% | 6 | 2.2% | ~6 |
| Carrying passengers (1.7.6) | 26 | 1.6% | 6 | 2.2% | ~8 |
| Carrying cargo (1.7.7) | 12 | 0.8% | 5 (high) | 1.8% | ~4 |
| Vehicle safety systems and driving physics (1.8.1) | 20 | 1.3% | 0 **(low)** | 0.0% | ~6 |
| Technical faults that ban driving (1.8.2) | 11 | 0.7% | 1 **(low)** | 0.4% | ~3 |
| Technical condition and required equipment (1.8.3) | 31 | 1.9% | 6 | 2.2% | ~10 |
| Vehicle mechanics and maintenance (2.x/3.x/7.x) | 64 | 4.0% | 0 **(low)** | 0.0% | ~20 |

Shares use the 1,595 category-B questions that have a real topic. Some questions were left out:

- 498 sit in topic 1.1.1. This is a catch-all: most of its questions have nothing to do with getting a licence.
- 21 sit in a mixed "category B specific" bucket.
- 9 sit in a mixed "extra training" bucket.
- 7 are tagged to other categories.

</details>

## Counts

| What | Count |
|---|--:|
| Own Questions | 274 (259 `approved`, 15 `draft`; see Oddities) |
| With any image | 46 (16.8%) |
| … one image on the question | 38: 27 signs, 11 road markings |
| … one image on each Option | 8: all signs (5 with 4 images, 3 with 3) |
| … road-situation pictures | **0** |
| With an explanation | 274 (all, 126–464 characters, Lithuanian) |
| With a rule link | 274 (all). 217 have 1 link, 57 have 2–5. Every link has a clause such as "KET 155", "KET 1 priedas, ženklas 206" or "SEAKĮ 2 str. 43 d." |
| Single-correct (`select_mode: single`) | 193 (70.4%) |
| Multi-correct (`select_mode: multi`) | 81 (29.6%): 45 with 2 correct, 36 with 3 correct |
| … all Options correct | 3 (gen-0105, gen-0157, gen-0173) |
| 2 Options | 64 (23%), all single-correct; 30 of them are yes/no ("Taip…" / "Ne…") |
| 3 Options | 162 (59%) |
| 4 Options | 47 (17%) |
| 5 Options | 1 (gen-0206) |
| KET edition stamp | all `ket_redakcija: 2026-01-01` |

All 46 image questions are in the Signs / markings theme, so the other 8 themes are text only. All 67 image files the questions point to exist in the second-brain folder `data/all-images-webp/`, where they are named by official sign or marking number.

## Oddities

1. **15 questions are still `status: draft` but were approved.** They are gen-0301 to gen-0315, which is batch 24. The `log.md` entry dated 2026-07-31 says "15/15 approved" and that the bank grew from 259 to 274, but the `status` field was never changed. Their `generated` date also says 2026-07-12, not 07-31. Fix: set them to `approved` in the source file. (This research is read-only, so they were not changed here.)
2. **One question has 5 Options.** This is gen-0206: which vehicles may use an "A+" lane without extra lane marking. It is multi-correct, with 2 of 5 correct. It was approved on 2026-07-12. Our glossary says a Question has *up to four* Options, so either trim this question to 4 or change the glossary (#10).
3. **The correct answer is nearly always first.** In single-correct questions, the correct Option is the first one in 151 of 193 (78%). In multi-correct questions, the first Option is correct in 74 of 81. Only a few later batches were shuffled. **The app must shuffle Options every time it shows a Question**, or a learner can score well by always picking the first Option.
4. **The correct answer is often the longest.** In single-correct questions with 3 or more Options, the correct Option is the longest in 85 of 129 (66%). Random chance would give about 33%. Test-wise learners can use this, so new questions should vary Option length (a writing rule for #10).
5. **Near-duplicates.**
   - gen-0023 and gen-0314 both show sign 325 ("Lenkti draudžiama"), ask what it means or bans, and have the same correct answer. Keep one. gen-0314 is still a draft.
   - gen-0108 and gen-0311 both show sign 203 ("Duoti kelią"). They test different things (meaning vs what to do), but should not be served close together.
   - gen-0201 and gen-0286 reuse one Option text: it is the correct answer in one and a wrong Option in the other. `log.md` already notes this.
6. **3 questions have every Option correct** (gen-0105, gen-0157, gen-0173). Our exam notes say the real exam allows this, and #2 will confirm. Our answer screen and scoring (#8) must allow "all of them".
7. **Gaps in the id numbers.** gen-0051 to gen-0085 are missing (batches withdrawn on 2026-07-11). gen-0264, 0266, 0267, 0278, 0280 and 0283 are missing too (rejected on 2026-07-12). The file is also not sorted by id. None of this is harmful, but the importer must not expect continuous ids.
8. **`schema_version` is mixed.** 266 questions say `1` and the 8 option-image questions say `1.1`, stored as a number. Treat it as text when importing.
9. **Fields the app needs are missing.** There is no field for theme, KET chapter, sub-topic or difficulty. The CSV here is a first guess for theme and chapter; #10 should decide the real fields.
10. **Rule-link `page` values are private file paths** (such as `wiki/taisykles/desines-rankos-taisykle.md`). Learners cannot open them. Only the `clause` text, such as "KET 155", is usable in the app.

## Open questions this raises

- **Where will the Risk, Safe driving, eco and vehicle questions come from?** The second brain has 8 "technika" pages that cover exactly these topics: stopping distance, following distance, reaction time, skids, braking on slippery roads, eco driving and night driving. 0 Own Questions use them yet. The pages themselves say they come from the "Saugaus vairavimo pagrindai" publication on ketbilietai.lt, the same company as the Reference Bank. Writing many of the missing questions from those pages would add to the legal risk the map already notes. These topics need a source of our own, such as general physics, official road-safety material or a driving instructor.
- **Do we keep yes/no questions?** 30 Own Questions have just "Taip" or "Ne" as Options, so learners can guess them half the time. Whether the real exam uses 2-Option questions is a question for #2.
- **Should writing go by theme instead of KET point?** Going point by point gave wide coverage. Matching the exam now needs targets per theme, using the table above, and per topic for heavy topics like intersections and overtaking.

## Method

1. **Reading the data.** A small Python script read all 274 records in `questions.jsonl` without changing the file. It counted modes, Options, correct Options, images (question vs Option, `traffic-signs/` vs `road-markings/` folder), explanations and rule links. It also checked that every image file exists, and looked for repeated images, repeated Option texts and the position of the correct Option.
2. **KET chapter.** The chapter comes from the clause of the first rule link. The KET point number is matched to its chapter using the KET 2026-01-01 table of contents. "KET 3.x" is chapter II (definitions), sign and marking clauses are Annex 1 and Annex 3, and "SEAKĮ" is the Road Traffic Safety Law (not KET).
3. **Theme.** Each Own Question got one theme, by reading its stem and KET point. Regitra publishes only the theme names, so these working rules were used:
   - **Risk:** the driver's state (alcohol, drugs, tiredness, phone, fitness), extra care for children and people with disabilities, hazards (obstacles, dazzle) and choosing a safe speed.
   - **Behaviour on public roads:** where to drive and lanes, starting, turning, U-turns, indicating, speed limits, lights and horn, stopping and parking, and passengers' duties.
   - **Signs / markings / lights / signals:** every sign or marking question, plus traffic lights, controller signals and which signal wins.
   - **Right of way & passing:** every "who gives way" question (intersections, roundabouts, pedestrian crossings, merging, emergency corridor), plus overtaking and passing oncoming traffic.
   - **Special roads / users / manoeuvres:** railway crossings, motorways, residential zones, bicycle streets, bus lanes, rules for pedestrians, cyclists, e-scooters and riders, vehicles of people with disabilities, special vehicles and towing.
   - **Safe driving & critical situations:** breakdowns, hazard lights, the warning triangle, the high-visibility vest, duties after an accident, first aid, reacting to sudden danger, seat belts and child seats.
   - **Responsible & eco driving:** carrying passengers, children, pets and cargo with care, no racing, EV charging bays.
   - **General KET & legal:** the KET itself, definitions, documents, licence and novice rules, registration and insurance, police checks.
   - **Knowledge about vehicles:** technical condition and faults, required equipment, tyres, number plates, vehicle mass, trailers.

   This is a first pass. A few questions in each theme could reasonably sit somewhere else. The CSV lets the owner change any row.
4. **Targets.** Exam share × 500 (the beta goal), for both candidate blueprints. Blueprint A comes from `ketgo-grilled/CONTEXT.md` and `DESIGN.md`. Blueprint B is the other split in our notes. Issue #2 decides between them.
5. **Reference Bank.** From the SQL dump, only these columns were read: question id, topic id, active and deleted flags, image id, and the question-to-category links. The script counted active, not-deleted questions linked to category B (2,130 in total; 1,687 with an image), grouped by topic. No question text, Option text or explanation from the Reference Bank was read into this report or copied anywhere. Topic names in this report are short English descriptions of the topic headings, not translations of questions.

## Sources

- Own Questions: `~/Documents/Claude/Projects/ket second brain/questions.jsonl` (274 records).
- Approval history: `~/Documents/Claude/Projects/ket second brain/log.md`. The entries used are "batch 24 — 15/15 PATVIRTINTA" (2026-07-31) and "queue verdicts (20–23)" (2026-07-12), with the rejected ids. The batch 06–08 withdrawals are dated 2026-07-11.
- Exam scoring facts (all-or-nothing; 1 to all Options can be correct): `wiki/klausimu-modeliai/egzamino-formatas.md` in the same folder.
- Source of the "technika" pages: `wiki/technika/index.md` in the same folder.
- KET chapters: `data/KET_2026_rules/00_KET_2026_Turinys.md` and the chapter files (VIII¹ and XXI¹ headings), same folder.
- Themes and blueprint A: `~/Documents/ketgo-grilled/CONTEXT.md` (Tema) and `~/Documents/ketgo-grilled/DESIGN.md` §1.
- Reference Bank: `~/Downloads/question answers ket db/2026-07-01-export.sql` (tables `Klausimas`, `KetSkyrius`, `Klausimas_Kategorija`). Row counts match the export notes in `2026-07-01-export.md`: 4,309 questions, 3,351 active and not deleted.
- Vocabulary: [`GLOSSARY.md`](../../GLOSSARY.md).
