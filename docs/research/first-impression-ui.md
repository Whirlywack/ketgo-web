# First impression and mobile UI

Ticket: [#21 First impression and mobile UI](https://github.com/Whirlywack/ketgo-web/issues/21) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1) · Feeds: [#12 Look and feel](https://github.com/Whirlywack/ketgo-web/issues/12) and the onboarding video in [#5](https://github.com/Whirlywack/ketgo-web/issues/5)

**Checked on 2026-10-13.**

**How I checked.** Sources are peer-reviewed papers and meta-analyses, plus official guidelines: WCAG 2.2 (W3C), Apple Human Interface Guidelines, Android developer guidance, Chrome and WebKit autoplay policies, web.dev / Lighthouse, the British Dyslexia Association style guide and the Netflix subtitle guides. I wanted to use the Consensus paper search as the main source, but its monthly quota was used up (30 searches; it resets on 1 November). So papers were found with OpenAlex, Semantic Scholar, PubMed and ERIC instead. Every paper below was checked against its DOI record (publisher metadata via Crossref, and the DOI resolving to the publisher's page), and is cited by DOI. Numbers come from the abstract on the publisher, PubMed, ERIC or JSTOR page. No blog posts are used as evidence.

I also made two small checks of my own:
1. **Word lengths in the official KET text.** I counted all 22,179 words of the consolidated Kelių eismo taisyklės (version in force from 2026-01-01, [e-tar.lt](https://www.e-tar.lt/portal/lt/legalAct/TAR.BBE7D61A0416/asr)).
2. **Automatic hyphenation.** I tested whether a browser (Chromium/Chrome 155 on macOS) hyphenates Lithuanian.

**UNVERIFIED** marks a design guess, or a number I could not trace to a primary source.

**Evidence strength used in this file:**

- **Strong.** Meta-analyses or many replications.
- **Moderate.** A few good experiments, or a meta-analysis in a nearby field.
- **Weak.** One small study, indirect evidence, or mixed results.
- **Standard.** An official guideline or spec. It is not a study, but it is the agreed bar, and often a legal one.
- **Design guess.** My judgement from the evidence. Test it.

---

## A. Short answer

1. **Beauty wins the first look and trust, but ease of use keeps people.** People judge how a site looks in about 0.05 s, and that judgement stays. Clean, simple, familiar layouts score best. "Design look" is the cue people mention most when they judge credibility. But after real use, poor usability makes a site look *less* beautiful. Studies disagree on whether beauty changes how easy an app feels once people use it. (Moderate)
2. **Beauty helps learning only a little, and only inside the learning material.** Pleasant colours and friendly pictures in the lesson material itself raise memory and understanding by about 0.3 SD. Fun but off-topic extras (seductive details) *hurt* learning. Hard-to-read fonts do not help. (Strong: meta-analyses)
3. **No study compares a video, first-run tips and no onboarding for an app like KETGO.** The nearest large A/B test (45,000+ players) found that tutorials helped only the most complex game. In simpler games, people learned by trying. Watching a demo makes the first try faster, but people just copy it and remember less a week later. So the video should be short, skippable and show real screens, then lead quickly to the first Question. Teach with one-line tips at the moment they are needed. (Moderate, indirect)
4. **Muted video with captions plays reliably on phones.** Chrome and Safari allow muted video to play on its own. Words read on screen while pictures move on their own clock are the weaker format, because spoken words beat on-screen text by d = 0.72 (system-paced). So use few words, one idea per scene, and add a pause button and a text version. (Standard + strong)
5. **Text on phones.** Use 18 px body text, line height 1.5, left-aligned, no italics and no ALL CAPS. Contrast must be at least 4.5:1; aim for 7:1. On big screens, keep lines to 60–70 characters. **Taps:** every target at least 48 × 48 px. Options are full width and at least 56 px tall. The main button sits at the bottom, where the thumb reaches. (Standard + moderate)
6. **Lithuanian words are long.** In the KET text, 1 word in 5 has 10 or more letters, and the longest have 19 ("persirikiuojantysis"). Chrome did **not** auto-hyphenate Lithuanian in my test. So: one column of Options, no fixed-width boxes, soft hyphens in long headings, a font that has all of ą č ę ė į š ų ū ž, and `lang="lt"`. (Own measurement + Standard)
7. **Dark mode.** Dark text on a light background reads best in normal light. Dark mode may tire the eyes less at night. Follow the phone's setting, and design both themes to the same contrast. (Moderate)
8. **Speed: slower pages lose people.** In Vodafone's A/B test, a 31 % faster LCP gave 8 % more sales. **Budget:**
   - LCP ≤ 2.5 s (aim 1.5 s)
   - Option tap → feedback ≤ 100 ms (INP ≤ 200 ms)
   - CLS ≤ 0.1
   - ≤ 170 KB for the landing page plus the first Question
   - the video loads only after **Start**

   (Standard + moderate)
9. **WCAG 2.2 AA is the floor.**
   - Never block zoom.
   - Never show right/wrong by colour alone: about 8 % of European men have red-green colour deficiency.
   - Keep focus visible.
   - Use real text, not pictures of text.

   No "dyslexia font": tested fonts gave no benefit. Size, spacing and clear layout help instead. (Standard + moderate)

---

## B. Design rules for Look and feel (#12)

| # | Rule | Number | Evidence strength | Main sources |
|---|---|---|---|---|
| L1 | Calm, simple, familiar layout. Few colours, lots of space, standard mobile patterns (top bar, big bottom button). No fake urgency, no ads, no pop-ups. | One accent colour plus neutrals; one main action per screen | **Moderate.** Low visual complexity and a familiar layout raise first-look beauty, even at 17 ms. Design flaws drive distrust and quick rejection. | Tuch et al. 2012b; Reinecke et al. 2013; Seckler et al. 2015; Sillence et al. 2004 |
| L2 | Beauty must not cost ease of use. Test every screen with real learners; usability problems make it look worse. | — | **Moderate** | Tuch et al. 2012a; Hassenzahl & Monk 2010 |
| L3 | Body text (Question, Options, "why", Rule Explainer) **18 px**. Nothing a learner must read below **16 px**. Headings at least 20 % larger than body. | 18 px body; min 16 px; headings ≥ 22 px | **Moderate** (bigger text read and understood better in a lab study; phones not shown) + **Standard** (BDA 16–19 px; Apple default body 17 pt, min 11 pt) | Rello et al. 2016; BDA 2023; Apple HIG |
| L4 | Line height **1.5**; paragraphs spaced. Layout must survive the WCAG 1.4.12 text-spacing override. | line-height 1.5 | **Standard** (WCAG 1.4.12, BDA) + **Weak** (1.8 and 0.8 were both worse) | WCAG 2.2; BDA 2023; Rello et al. 2016 |
| L5 | Line length: on phones it is naturally about 35–45 characters at 18 px. On tablet or desktop, cap the reading column at **60–70 characters** (about `max-width: 36em`). | ≤ 70 characters per line | **Weak–moderate** (55 characters per line best in one study) + **Standard** (WCAG 1.4.8 ≤ 80; BDA 60–70) | Dyson & Haselgrove 2001; WCAG 2.2; BDA 2023 |
| L6 | Left-aligned, never justified. No italics or underline for emphasis (use bold). No ALL CAPS for sentences or buttons. | — | **Standard** (BDA, WCAG 1.4.8) + **Moderate** (italic fonts read slower) | BDA 2023; Rello & Baeza-Yates 2016 |
| L7 | One clear, humanist **sans-serif** font with full Lithuanian support (Latin Extended-A: ą č ę ė į š ų ū ž and capitals). At most 2 weights. Self-host it, subset to Latin + Latin Extended-A. Do **not** use OpenDyslexic or Dyslexie. | ≤ 2 font files | **Moderate.** Sans-serif and upright fonts read faster. Humanist type is more legible at a glance. Dyslexia fonts gave no benefit. | Rello & Baeza-Yates 2016; Dobres et al. 2016; Wery & Diliberto 2017; Kuster et al. 2018 |
| L8 | Contrast: body text **≥ 7:1**. All text ≥ 4.5:1. Borders, icons, focus rings and Option outlines ≥ 3:1. Check both themes. | 7:1 / 4.5:1 / 3:1 | **Standard** | WCAG 2.2 (1.4.3, 1.4.11); Apple HIG Dark Mode ("strive for 7:1, especially in small text") |
| L9 | Light theme is the main design: dark text on an **off-white** background. Dark theme follows the phone setting (`prefers-color-scheme`) and meets the same contrast. | — | **Moderate** (light background reads better in daylight; dark may tire eyes less at night) + **Standard/Weak** (BDA off-white) | Piepenbrock et al. 2013; Dobres et al. 2016; Xie et al. 2021; Apple HIG; BDA 2023 |
| L10 | Tap targets **≥ 48 × 48 px** everywhere. Options and the main button full width and **≥ 56 px** tall. **≥ 12 px** gap between Options. | 48 px min; 56 px Options/main; 12 px gaps | **Standard** (WCAG 2.5.8 min 24 px; WCAG AAA and Apple 44; Android 48) + **Moderate** (one-thumb targets of about 9.2–9.6 mm, about 55–60 CSS px; small buttons fail more while walking) | WCAG 2.2; Apple HIG; Android; Parhi et al. 2006; Conradi et al. 2015 |
| L11 | Main actions (**Continue**, Next, submit) at the **bottom**, in thumb reach. Rare actions (menu) can sit at the top. Nothing important only in a top corner. | Main action in bottom third | **Moderate** (thumb-reach models; reach shrinks on big phones) + **Design guess** for the exact zone | Bergstrom-Lehtovirta & Oulasvirta 2014; Le et al. 2018 |
| L12 | Right/wrong feedback is never colour alone: always an icon (✓ / ✗) **and** a word ("Teisingai" / "Neteisingai"), plus the colour. | — | **Standard** (WCAG 1.4.1) + **Strong** (about 8 % of European men have red-green colour deficiency) | WCAG 2.2; Birch 2012 |
| L13 | Long Lithuanian words: Options in **one column**. No fixed-width chips or two-column grids for text. Allow wrapping (`overflow-wrap: anywhere` as a safety net). Add soft hyphens (`&shy;`) to words of 14+ letters in headings and buttons. Do not rely on `hyphens: auto`. | Check at 200 % text size | **Own measurement** + **Standard** (WCAG 1.4.4, 1.4.10) | Section D10 |
| L14 | `<html lang="lt">`. Never disable zoom (no `user-scalable=no`, no `maximum-scale=1`). Layout works at 320 px wide and at 200 % text. | 320 px; 200 % | **Standard** | WCAG 2.2 (3.1.1, 1.4.4, 1.4.10) |
| L15 | Pictures and colour belong in the **learning content** (Rule Explainer illustrations, Memory Hook pictures): pleasant, clear, on-topic. No decorative mascots or animations during Questions, and no off-topic fun facts. | — | **Strong** (emotional design about +0.3 SD; seductive details hurt) | Brom et al. 2018; Wong & Adesope 2021; Sundararajan & Adesope 2020 |
| L16 | Motion: short, purposeful transitions only. Respect `prefers-reduced-motion`. Nothing flashes more than 3 times a second. | 3 flashes/s max | **Standard** | WCAG 2.2 (2.3.1, 2.3.3); Apple HIG; CSS Media Queries 5 |
| L17 | Rule Explainers are short and self-paced: short paragraphs, the key rule in one line at the top. Reading on screen is slightly worse than paper, and worse under time pressure. | Sentences ≈ 60–70 characters | **Strong** (screen inferiority, g = −0.21) + **Standard** (BDA) | Delgado et al. 2018; BDA 2023 |
| L18 | Speed is part of the look: see the budget in section C. | — | — | — |

## C. Performance budget

KETGO's market: in September 2026, 70.4 % of mobile web traffic in Lithuania was Android and 29.6 % iOS ([StatCounter](https://gs.statcounter.com/os-market-share/mobile/lithuania)). So test on a mid-range Android phone first. Lighthouse's mobile test already copies one: a Moto G Power with 4× slower CPU, 150 ms latency and 1.6 Mbps download ([Lighthouse throttling docs](https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md)).

| Metric | Google "good" bar | KETGO target | Evidence strength |
|---|---|---|---|
| LCP (main content shown) | ≤ 2.5 s at the 75th percentile of mobile visits | ≤ 1.5 s on the Lighthouse mobile profile | **Standard** ([web.dev](https://web.dev/articles/vitals)); target is a **design guess** |
| INP (tap → next frame) | ≤ 200 ms | Option tap → visible feedback ≤ 100 ms | **Standard**; 0.1 s feels instant (Miller 1968; Card et al. 1991, as used by [web.dev](https://web.dev/articles/defining-core-web-vitals-thresholds)) |
| CLS (layout jumps) | ≤ 0.1 | < 0.05 (reserve space for Question images and fonts) | **Standard**; target is a **design guess** |
| Critical-path weight (landing + first Question) | web.dev default: < 170 KB compressed | ≤ 170 KB total, of which JS ≤ 100 KB | **Standard** ([web.dev budgets](https://web.dev/articles/performance-budgets-101)); JS split is a **design guess** |
| Fonts | — | ≤ 2 files, ≤ 60 KB total, self-hosted | **Design guess** |
| Question images | — | WebP/AVIF, ≤ 50 KB each; prefetch the next Question's image | **Design guess** |
| Onboarding video | — | Not loaded until **Start** is tapped. Poster frame first. HTML/SVG animation ≤ 200 KB if Claude Design can export it; otherwise MP4 ≤ 2.5 MB. | **Design guess** |

For comparison, from the [competitor teardown](https://github.com/Whirlywack/ketgo-web/blob/research/competitor-teardown/docs/research/competitor-teardown.md): the RoboKET landing page is about 370 KB, the ketbilietai home page about 170 KB, and eKET about 2.6 MB. eKET also blocks pinch-zoom.

---

## D. Details with citations

### D1. Does beauty make an app feel easier? (aesthetic-usability effect)

- **For:**
  - People rated apparent usability mostly by looks, not by actual usability ([Kurosu & Kashimura 1995](https://doi.org/10.1145/223355.223680)).
  - In an ATM simulation, beauty changed how usable people rated the system *after* use; actual usability did not ([Tractinsky et al. 2000](https://doi.org/10.1016/s0953-5438(00)00031-x)).
  - In a simulated mobile phone test (60 teenagers), the attractive phone was rated more usable *and* tasks were done faster ([Sonderegger & Sauer 2010](https://doi.org/10.1016/j.apergo.2009.09.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19892317/)).
- **Against or limits:**
  - A review of 25 correlations from 15 papers found very variable results. Its own study suggests the link "has been overplayed": beauty mostly works through a general "this is good" judgement ([Hassenzahl & Monk 2010](https://doi.org/10.1080/07370024.2010.500139)).
  - In an online shop study with 80 people, beauty did **not** change perceived usability. But poor usability **lowered** perceived beauty after use, through frustration ([Tuch et al. 2012a](https://doi.org/10.1016/j.chb.2012.03.024)).
  - In a web experiment with 331 people, an attractive site gave no better task performance ([Thielsch et al. 2019](https://doi.org/10.7717/peerj.6516)).
  - One explanation for the link is *visual clarity* (order, alignment, low clutter), which affects both beauty and ease ([Schrepp et al. 2021](https://doi.org/10.9781/ijimai.2020.12.005)).
- **For KETGO:** a clean, clear look helps the first impression and the "it's easy" feeling. Real ease of use decides whether that feeling survives the first Lesson. **Moderate.**

### D2. How fast do people judge a site?

- Visual appeal can be judged in **50 ms**. Ratings at 50 ms and 500 ms were highly correlated ([Lindgaard et al. 2006](https://doi.org/10.1080/01449290500330448)).
- Visual complexity and prototypicality (looking like a typical site of its kind) changed beauty ratings even at **17 ms**. Low complexity and high prototypicality looked best ([Tuch et al. 2012b](https://doi.org/10.1016/j.ijhcs.2012.06.003)).
- Across 450 sites and 548 people, perceived complexity and colourfulness, plus age and education, explained about half of the appeal ratings after 500 ms ([Reinecke et al. 2013](https://doi.org/10.1145/2470654.2481281)). The authors note that this first impression later affects opinions of usability and trust.
- **For KETGO:** the landing page and first screen are judged before anyone reads a word. Keep them simple, with familiar structure and modest colour. **Moderate** (lab studies with short exposure).

### D3. Trust

- In a study of 2,684 people judging site credibility, the "design look" was the most-mentioned cue: **46.1 %** of comments ([Fogg et al. 2003](https://doi.org/10.1145/997078.997097)).
- Women researching a health decision rejected sites early for poor design. Trust in the sites they kept came from content credibility ([Sillence et al. 2004](https://doi.org/10.1145/985692.985776)).
- With 221 participants, *distrust* came mostly from graphic and structural design problems. *Trust* came mostly from social factors such as reviews and recommendations ([Seckler et al. 2015](https://doi.org/10.1016/j.chb.2014.11.064)).
- **For KETGO:** design flaws (clutter, pop-ups, fake countdowns, ads) cause distrust fast. The competitor teardown found exactly these on eKET and the vairavimotestai cookie wall. Trust itself is then earned by content and word of mouth (Partners, friends). **Moderate.**

### D4. Does beauty change learning, or only first impressions?

- **Emotional design** means pleasant colours and friendly, face-like shapes in the learning material itself. A meta-analysis of 33 samples (N = 2,924) found:
  - retention d = 0.39, comprehension d = 0.32, transfer d = 0.33
  - intrinsic motivation d = 0.26, but only small effects on enjoyment (d = 0.11)

  ([Brom et al. 2018](https://doi.org/10.1016/j.edurev.2018.09.004)). A replication found much the same: retention g = 0.35, transfer g = 0.27, comprehension g = 0.29, and less perceived difficulty, g = −0.21 ([Wong & Adesope 2021](https://doi.org/10.1007/s10648-020-09545-x)). One key study: [Um et al. 2012](https://doi.org/10.1037/a0026609).
- **Seductive details**, interesting but off-topic content, hurt learning. A meta-analysis confirmed this and found the size depends on pacing and format ([Sundararajan & Adesope 2020](https://doi.org/10.1007/s10648-020-09522-4); [ERIC abstract](https://eric.ed.gov/?id=EJ1263249)).
- **Hard-to-read fonts** gave no learning benefit: recall d = −0.01, transfer d = 0.03. They did make learners *feel* they learned less (d = −0.43) and took longer ([Xie et al. 2018](https://doi.org/10.1007/s10648-018-9442-x)). Some coding errors in that meta-analysis were later pointed out ([Weissgerber et al. 2021](https://doi.org/10.1007/s10648-020-09579-1)), so "no reliable benefit" is the fair summary.
- **Screen vs paper:** across 54 studies, reading comprehension on screens was a little worse than on paper (g = −0.21). The gap was bigger under time limits and for informational texts ([Delgado et al. 2018](https://doi.org/10.1016/j.edurev.2018.09.003)).
- **For KETGO:** looks matter for learning only when they are *in* the material: clear, pleasant pictures in Rule Explainers and Memory Hooks. Decoration elsewhere does not help learning and can distract. Keep Rule Explainers short and self-paced. **Strong** (meta-analyses), but mostly short lab lessons with students.

### D5. Onboarding: video, first-run tips, or nothing?

No study compares these three options for a web learning app. The nearest evidence:

- **Tutorials help only complex interfaces.** In a 45,000+ player A/B test across three games:
  - tutorials raised play time by up to 29 % in the most complex game, but had "surprisingly negligible" effect in the two simpler games
  - instructions given *at the moment they were needed* beat an up-front manual (+16 % play time) only in the complex game
  - on-demand help did nothing or was even harmful in the simpler games

  The authors conclude that players "seem to learn more from experimentation than from reading text" ([Andersen et al. 2012](https://doi.org/10.1145/2207676.2207687)). **Moderate** (large, randomised, but games).
- **Demos make the first try easy but shallow.** People who watched animated demonstrations were faster and more accurate during training. A week later, people who had read text instructions were faster and just as accurate. The demo group had mimicked the steps ([Palmiter & Elkerton 1993](https://doi.org/10.1207/s15327051hci0803_1)). **Moderate** (one classic experiment).
- **Animation helps when it shows the real thing.** A meta-analysis of 76 comparisons found:
  - animation beat static pictures overall (d = 0.37)
  - more for *representational* animation (d = 0.40)
  - more for realistic video (d = 0.76)
  - most for procedural-motor skills (d = 1.06)

  ([Höffler & Leutner 2007](https://doi.org/10.1016/j.learninstruc.2007.09.013), [ERIC](https://eric.ed.gov/?id=EJ780451)). **Strong.** So a video should *show* KETGO's real screens and actions, not abstract decoration.
- **Users want onboarding short, with a quick win.** Interviews (n = 16) and prototype tests (n = 16) of onboarding for two cryptocurrency apps found that well-designed onboarding can improve perceived usability in feature-rich apps. Users expected short, light onboarding and an early "quick win". Informational tutorial cards "get in the way" ([Fröhlich et al. 2021](https://doi.org/10.1145/3461778.3462047)). **Weak** (small, qualitative).
- **Shorter videos hold attention better.** In 6.9 million MOOC video sessions, shorter videos were much more engaging ([Guo et al. 2014](https://doi.org/10.1145/2556325.2566239)). **Moderate** (but long lecture videos, not 30 s clips).
- **For KETGO:** the decided 30–45 s video is fine as *orientation* ("how KETGO works"), not as teaching. Aim for 30 s. The real teaching is learning by doing: the first Question plus one-line tips the first time each thing happens. The video adds time before the first Question, and the evidence does not show it helps a simple interface. So measure it, and A/B test video vs no video once traffic allows (section F).

### D6. Muted autoplay with captions: does it work?

- **Technically, yes.**
  - Chrome: "Muted autoplay is always allowed" ([Chrome autoplay policy](https://developer.chrome.com/blog/autoplay)).
  - Safari on iOS: `<video muted>` may play without a user gesture, and `play()` called from a click handler always counts as a user gesture ([WebKit: New video policies for iOS](https://webkit.org/blog/6784/new-video-policies-for-ios/)).
  - KETGO's video starts after the **Start** tap, so it plays in both. Use `muted playsinline` so the iPhone does not jump to fullscreen.
  - **Standard.**
- **For understanding, it is the weaker format.**
  - Pictures plus *spoken* words beat pictures plus *printed* words by d = 0.72 when the media runs at its own pace. The advantage shrinks or disappears when learners control the pace ([Ginns 2005](https://doi.org/10.1016/j.learninstruc.2005.07.001)). A muted captioned video is the system-paced printed-text case.
  - Splitting media into learner-paced segments improves retention and transfer (small to medium) and lowers cognitive load ([Rey et al. 2019](https://doi.org/10.1007/s10648-018-9456-4); [ERIC](https://eric.ed.gov/?id=EJ1217373)).
  - So: very few words, one idea per scene, captions next to the thing they describe, a pause button, and replay. **Strong** (meta-analyses).
- **Captions help.** More than 100 studies show captions improve comprehension of, attention to, and memory for video ([Gernsbacher 2015](https://doi.org/10.1177/2372732215602130)). **Moderate** (a review; mostly captions *with* sound).
- **Reading speed.**
  - Netflix allows at most 42 characters per line. Its Czech guide (an inflected European language like Lithuanian) allows up to 17 characters per second for adults ([Netflix Czech guide](https://partnerhelp.netflixstudios.com/hc/en-us/articles/115002884887-Czech-Timed-Text-Style-Guide)). A subtitle stays on screen for 5/6 s to 7 s ([Netflix general requirements](https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements)). Netflix has no Lithuanian guide.
  - In the onboarding video, viewers must also watch the animation, so stay well under 17 characters per second. At 12–13 characters per second, a 30 s video holds about **400 characters, about 50 Lithuanian words**. **Standard** for the limits; **design guess** for 12–13.
- **Accessibility rules that apply:**
  - Moving content that starts by itself and lasts over 5 s needs a pause, stop or hide control: WCAG 2.2.2, Level A. Skip counts as stop, but a pause is better.
  - A video with no audio is "video-only", so it needs a text alternative: WCAG 1.2.1, Level A.
  - Text should be real text, not pictures of text: WCAG 1.4.5.
  - Nothing may flash more than 3 times a second: WCAG 2.3.1.
  - Respect reduced motion: WCAG 2.3.3; [CSS `prefers-reduced-motion`](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion).
  - Apple: "Avoid autoplaying audio and video content without also providing controls to start and stop it" ([Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)).

  ([WCAG 2.2](https://www.w3.org/TR/WCAG22/))
- **Do most people watch phone video with the sound off?** I found no peer-reviewed or first-party source for the often-quoted figures. **UNVERIFIED.** Muted is still the safer default for a first visit, which may happen in public.

### D7. Font size, line length, spacing

- **Size.** In an eye-tracking study of web pages (sizes 10–26 points), readability rose with font size. Comprehension was better at 18 and 26 points. The authors recommend 18+ for text-heavy sites ([Rello et al. 2016](https://doi.org/10.1145/2858036.2858204)). It was a lab eye-tracking study of web pages, and I could not confirm the screen type (UNVERIFIED). So treat the exact number with care; the direction (bigger is better, up to a point) transfers.
- **Guidelines on size.**
  - The BDA style guide: 12–14 pt, "e.g. 1–1.2em / 16–19 px"; headings at least 20 % larger ([BDA Dyslexia Style Guide 2023](https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf)).
  - Apple: default iOS body text 17 pt, minimum 11 pt ([Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)). On iPhone, 1 pt ≈ 1 CSS px.
  - **Moderate + Standard → 18 px body, 16 px minimum.**
- **Line length.** 55 characters per line gave the best comprehension and was read faster than short lines ([Dyson & Haselgrove 2001](https://doi.org/10.1006/ijhc.2001.0458)). WCAG 1.4.8 (AAA) says at most 80 characters. BDA says 60–70. **Weak–moderate + Standard.**
- **Line spacing.**
  - Rello et al. found only marginal effects; both extremes tested (0.8 and 1.8) hurt.
  - BDA recommends 1.5.
  - WCAG 1.4.12 requires that layouts survive line-height 1.5, paragraph spacing 2× the font size, letter spacing 0.12× and word spacing 0.16×.

  **Standard → 1.5.**
- **Word length and reading.** Longer words get more and longer eye fixations ([Rayner 1998](https://doi.org/10.1037/0033-2909.124.3.372)). Lithuanian has many long words (D10), so short sentences matter even more.

### D8. Contrast

- WCAG 1.4.3: text ≥ 4.5:1. Large text (≥ 18 pt, or 14 pt bold) ≥ 3:1.
- WCAG 1.4.11: UI parts and graphics ≥ 3:1 ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).
- Apple: "At a minimum, make sure the contrast ratio between colors is no lower than 4.5:1. For custom foreground and background colors, strive for a contrast ratio of 7:1, especially in small text" ([Apple HIG Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)).
- Higher text-background contrast also went with less visual fatigue in a night-reading study ([Xie et al. 2021](https://doi.org/10.1109/access.2021.3061770)).
- **Standard.**

### D9. Tap targets and one-hand reach

- **Official minimums:**
  - WCAG 2.5.8 (AA, new in 2.2): 24 × 24 CSS px. WCAG 2.5.5 (AAA): 44 × 44 ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).
  - Apple: 44 × 44 pt default control size, 28 × 28 pt minimum. Add about 12 pt padding around bezeled controls ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)).
  - Android: "at least 48dp × 48dp. Larger is even better" ([Android accessibility guide](https://developer.android.com/guide/topics/ui/accessibility/apps)).
- **One thumb.** For one-handed thumb use, errors stopped dropping at about 9.6 mm (single taps). The authors recommend 9.2 mm for single taps and 9.6 mm for sequences ([Parhi et al. 2006](https://doi.org/10.1145/1152215.1152260)). On today's phones 1 CSS px is roughly 0.16 mm, so this is about **55–60 CSS px**; the conversion is approximate.
- **Walking.** Walking raised tap errors, especially on small (5 mm and 8 mm) buttons ([Conradi et al. 2015](https://doi.org/10.1016/j.promfg.2015.07.182)). Learners study on buses and while walking.
- **Reach.** The area the thumb of the holding hand can reach depends on screen size, hand size and grip ([Bergstrom-Lehtovirta & Oulasvirta 2014](https://doi.org/10.1145/2556288.2557354)). With bigger phones, the grip shifts ([Le et al. 2018](https://doi.org/10.1145/3173574.3173605)).
- **→ 48 px minimum, 56 px Options and main button, 12 px gaps, main action at the bottom.** **Standard + moderate.**

### D10. Long Lithuanian words and diacritics (own measurements)

**KET word lengths.** I counted all words in the official consolidated KET text (version from 2026-01-01, 22,179 words; [e-tar.lt](https://www.e-tar.lt/portal/lt/legalAct/TAR.BBE7D61A0416/asr)).

| Measure | KET text |
|---|---|
| Mean word length | 6.8 letters |
| Words with ≥ 10 letters | 20.3 % (1 in 5) |
| Words with ≥ 12 letters | 6.0 % |
| Words with ≥ 14 letters | 1.6 % |
| Longest words | 19 letters: *persirikiuojantysis*, *persirikiuojančioms*; 18: *prisijungiančiuoju*, *nepasinaudojusiems* |
| Words with at least one of ą č ę ė į š ų ū ž | 37.8 % |

**Widths.** At 18 px Arial in Chromium, *persirikiuojantysis* is 142 px wide and *automagistralėmis* 146 px.

- On a 360 px phone with 16 px side margins, the column is 328 px. A full-width Option with padding and a marker leaves about 250 px for text.
- So one long word fits per line in a one-column Option.
- In a two-column grid (about 140 px per cell), it does not.
- At 200 % text size (WCAG 1.4.4), a 19-letter word is about 285 px. That overflows a full-width Option unless the word can break.

**Hyphenation test.** In Chromium (Chrome 155, macOS), `hyphens: auto` with `lang="lt"` did **not** hyphenate the long Lithuanian words. The same test in German did hyphenate.

- Android Chrome, iOS Safari and Firefox were not tested: **UNVERIFIED**.
- Do not rely on automatic hyphenation. Allow soft hyphens in content, and keep `overflow-wrap: anywhere` as a safety net.

**Diacritics.**

- All nine Lithuanian letters are in Unicode Latin Extended-A, U+0100–017F ([Unicode chart](https://www.unicode.org/charts/PDF/U0100.pdf)). The chosen font must include them, in both cases.
- Capitals with a dot or macron (Ė, Ū) and letters with an ogonek (Ą, Ę, Į, Ų) need room above and below. Check that tight line heights or `overflow: hidden` do not clip them.
- Avoid ALL CAPS: it is harder to read (BDA), and capitals with diacritics clip first.
- `lang="lt"` (WCAG 3.1.1) makes screen readers pronounce Lithuanian correctly.

### D11. Dark mode and reading

- **Light background reads better in normal light.**
  - Dark text on a light background gave better acuity and proofreading for both younger and older adults ([Piepenbrock et al. 2013](https://doi.org/10.1080/00140139.2013.790485)).
  - In glance reading, black-on-white was more legible than white-on-black, and humanist type more legible than square grotesque ([Dobres et al. 2016](https://doi.org/10.1080/00140139.2015.1137637), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26727912/)).
- **At night it is less clear.**
  - Under low light at night, dark mode reduced eye-measured fatigue, but people *preferred* light mode out of habit ([Xie et al. 2021](https://doi.org/10.1109/access.2021.3061770)).
  - In a 30-person tablet study, there was no difference in reported visual fatigue between modes ([Sengsoon & Intaruk 2025](https://doi.org/10.3390/ijerph22040609), [PubMed](https://pubmed.ncbi.nlm.nih.gov/40283833/)).
- **Platform advice.**
  - Apple advises following the system appearance rather than an app-only setting, and checking contrast in both appearances ([Apple HIG Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)).
  - WCAG 1.4.8 (AAA) asks that users can choose colours.
- **→ Light theme first. Dark theme follows `prefers-color-scheme`, with the same contrast.** **Moderate.**

### D12. Speed and drop-off on mobile

- **Lab studies.**
  - People's tolerable wait for a web page was about **2 s**. Showing feedback (a progress sign) made them willing to wait longer ([Nah 2004](https://doi.org/10.1080/01449290410001669914)).
  - With delays of 0–12 s (196 students), performance and intentions to return fell as delay grew. The drop flattened after about 4 s ([Galletta et al. 2004](https://doi.org/10.17705/1jais.00044)).
- **Field data published by Google (web.dev):**
  - Vodafone ran an A/B test: a 31 % better LCP gave **8 % more sales** ([web.dev case study](https://web.dev/case-studies/vodafone)).
  - Renault: across 10 million visits, 1 s better LCP went with **14 percentage points lower bounce** and 13 % more conversions. This is a correlation, not a test ([web.dev case study](https://web.dev/case-studies/renault)).
  - web.dev also reports that the BBC lost 10 % more users for every extra second of load ([web.dev](https://web.dev/articles/why-speed-matters)).
  - Chrome's own data shows no single "give-up" time. Abandonment rises smoothly with delay ([web.dev thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds)).
- **Jank.** INP (≤ 200 ms) and CLS (≤ 0.1) are Google's measures of slow responses and layout jumps ([web.dev](https://web.dev/articles/vitals)). Human-response research puts "feels instant" at about 0.1 s ([Miller 1968](https://doi.org/10.1145/1476589.1476628); [Card et al. 1991](https://doi.org/10.1145/108844.108874)). I found no good field study that measures drop-off caused by jank alone. **UNVERIFIED** beyond the thresholds.
- **Not used:** the often-quoted "Google: 53 % of mobile visits are abandoned after 3 s". The original Google page is no longer online, and only second-hand reports remain.
- **Overall: Moderate** (consistent direction; few randomised tests).

### D13. Accessibility basics for learners (WCAG 2.2 AA)

The essentials for KETGO's screens ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)):

| WCAG 2.2 criterion (level) | What it means for KETGO |
|---|---|
| 1.4.3 Contrast (AA), 1.4.11 Non-text contrast (AA) | 4.5:1 text; 3:1 Option borders, icons, focus rings. |
| 1.4.1 Use of colour (A) | Right/wrong never by colour alone. Red-green colour deficiency affects about 8 % of European men and 0.4 % of women ([Birch 2012](https://doi.org/10.1364/JOSAA.29.000313)). |
| 1.4.4 Resize text (AA), 1.4.10 Reflow (AA) | Text to 200 % and 320 px width with no loss. Never block zoom. |
| 1.4.12 Text spacing (AA) | Nothing breaks when users increase spacing. |
| 2.5.8 Target size (AA, new in 2.2) | 24 px minimum; KETGO uses 48 px. |
| 2.4.7 Focus visible (AA), 2.4.11 Focus not obscured (AA, new in 2.2) | A sticky bottom **Continue** bar must not hide the focused element. |
| 2.2.2 Pause, stop, hide (A) | The onboarding video. |
| 2.2.1 Timing adjustable (A) | The 30-minute Mock Exam timer (see open questions). |
| 1.2.1 Video-only (A) | A text version of the onboarding video. |
| 2.3.1 Three flashes (A) | Nothing flashes more than 3 times a second. |
| 3.1.1 Language of page (A) | `lang="lt"`. |
| 4.1.2 Name, role, value (A) | Options are real radio buttons or checkboxes, so screen readers announce "selected" and multi-answer Questions. |
| 3.3.2 Labels (A) | A clear label on the exam-date field, and "Don't know yet" as a real button. |

### D14. Dyslexia-friendly text

- **Special fonts do not help.**
  - OpenDyslexic gave no gain in reading rate or accuracy, and no student preferred it ([Wery & Diliberto 2017](https://doi.org/10.1007/s11881-016-0127-1)).
  - The Dyslexie font gave no gain for 170 + 147 children, and most preferred Arial ([Kuster et al. 2018](https://doi.org/10.1007/s11881-017-0154-6)).
- **What does help.**
  - Sans-serif, monospaced and upright (roman) fonts read faster than serif, proportional and italic fonts, for readers with and without dyslexia ([Rello & Baeza-Yates 2016](https://doi.org/10.1145/2897736)).
  - Bigger text (Rello et al. 2016).
- **Spacing is mixed.**
  - Extra-large letter spacing improved reading in Italian and French dyslexic children ([Zorzi et al. 2012](https://doi.org/10.1073/pnas.1205566109), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22665803/)).
  - But wider letter spacing *without* wider word spacing slowed reading, and dyslexia-style letter shapes had no effect ([Galliussi et al. 2020](https://doi.org/10.1007/s11881-020-00194-x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32172467/)).
- **BDA guide** ([2023](https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf)):
  - sans-serif, 16–19 px
  - letter spacing about 35 % of average letter width, and word spacing at least 3.5× the letter spacing
  - line spacing 1.5
  - left-aligned, no justification
  - no underline, italics or capitals for continuous text; bold for emphasis
  - dark text on a light, not white, background
  - short sentences of 60–70 characters
- **→ Use a clear sans-serif at 18 px, line height 1.5, normal spacing, and an off-white background. Let users' own spacing settings work (WCAG 1.4.12). No special font.** **Moderate + Standard.**

---

## E. Design rules for the onboarding video

| # | Rule | Number | Evidence strength | Main sources |
|---|---|---|---|---|
| V1 | Orientation only: show *how KETGO works* (Question first → short "why" → **Continue** picks the next step → exam date). Do not teach Rules in it. | — | **Moderate** (demos lead to copying and weak retention; people learn simple apps by doing) | Palmiter & Elkerton 1993; Andersen et al. 2012 |
| V2 | Show **real KETGO screens and real taps**, not abstract decoration or a mascot story. | — | **Strong** (representational animation helps, d = 0.40; procedural d = 1.06; off-topic details hurt) | Höffler & Leutner 2007; Sundararajan & Adesope 2020 |
| V3 | **≤ 30 s** (the low end of the decided 30–45 s), in 4–6 scenes, one idea per scene. | ≤ 30 s; 4–6 scenes | **Weak–moderate** (shorter videos hold attention; segmenting helps) + **design guess** for 30 s | Guo et al. 2014; Rey et al. 2019; Fröhlich et al. 2021 |
| V4 | Captions: ≤ 2 lines, ≤ 42 characters per line, about 12–13 characters per second. Each caption shown ≥ 2 s and ≤ 7 s. Place it next to the thing it describes, at body size or larger (≥ 18 px). About 400 characters (about 50 words) in total. | 42 chars/line; ≤ 13 chars/s; ≈ 400 chars | **Standard** (Netflix limits: 42 chars, 17 chars/s, 5/6–7 s) + **Strong** (printed text with system-paced media is the weaker format, so keep it minimal) + **design guess** for 12–13 chars/s and the 2 s minimum | Netflix guides; Ginns 2005; Gernsbacher 2015 |
| V5 | Captions are **real text** (HTML over the animation, or a WebVTT track), not baked into the pixels. They then scale with zoom, stay sharp, can be edited and are read as Lithuanian. | — | **Standard** | WCAG 1.4.4, 1.4.5, 3.1.1 |
| V6 | Muted, with no sound needed. Start it from the **Start** tap handler with `muted playsinline`. | — | **Standard** (browser policy) | Chrome autoplay policy; WebKit video policies |
| V7 | **Skip** visible from second 0, plus a **pause** control. Both ≥ 48 px and in thumb reach. | ≥ 48 px | **Standard** (WCAG 2.2.2; Apple HIG) | WCAG 2.2; Apple HIG |
| V8 | A text version ("Read instead"), and replay from the menu (already decided). | — | **Standard** (WCAG 1.2.1) | WCAG 2.2 |
| V9 | With `prefers-reduced-motion`, show the same scenes as still slides the learner taps through. No flashes (≤ 3 per second), no fast zooms or spins. | ≤ 3 flashes/s | **Standard** | WCAG 2.3.1, 2.3.3; Apple HIG; CSS Media Queries 5 |
| V10 | Do not load the video on the landing page. Load it after **Start**, poster frame first. Prefer an HTML/SVG animation (≤ 200 KB); otherwise MP4 ≤ 2.5 MB. | ≤ 200 KB / ≤ 2.5 MB | **Design guess** (protects LCP; see section C) | web.dev |
| V11 | End on one clear button into the exam-date step. Then the first Question. From **Start** to the first Question should take ≤ about 60 s for someone who watches it all. | ≤ 60 s to first Question | **Design guess** (quick win; learning by doing) | Fröhlich et al. 2021; Andersen et al. 2012 |
| V12 | After the video, teach with **one-line tips the first time each thing happens**. They disappear when the learner does the action and never cover the Question. | 1 sentence each, shown once | **Moderate** (just-in-time beats up-front, but only clearly in complex interfaces) | Andersen et al. 2012; Fröhlich et al. 2021 |
| V13 | Measure it (section F), and compare with no video when traffic allows. | — | — | — |

---

## F. What to measure in the beta

These numbers check the five-minute promise ("it looks great, it's easy and beautiful"). They need no cookies beyond what the privacy ticket decides.

- **Landing:** share of visitors who tap **Start**, and time to that tap.
- **Video:** the second at which people skip; share who watch to the end; share who replay it from the menu.
- **First Question:** share who answer it, and time from **Start** to the first answer.
- **First Lesson:** share who finish it; share who come back the next day.
- **Speed in the field:** LCP, INP and CLS at the 75th percentile, split by Android and iOS. Use the browser's own `PerformanceObserver`; no third-party script is needed.
- **A one-tap question after Lesson 1** (optional): "Was KETGO easy to use?" (1–5). This tracks the "it's easy" promise.
- **A/B test, when traffic allows:** video vs no video (straight to the exam date, then the first Question with tips). Compare first-Question start, Lesson 1 completion and next-day return.

---

## G. Open questions for the map

1. **Video vs no video.** The evidence does not show that an up-front video helps a simple interface. Should the beta A/B test it (needs enough traffic), or ship the video and only watch skip and finish rates?
2. **Lithuanian hyphenation on real phones.** Chrome on Android, Safari on iOS and Firefox are untested. Content authors need a soft-hyphen rule for long words in headings and buttons. This belongs to the content-format or Look-and-feel work.
3. **Mock Exam timer and WCAG 2.2.1 (Timing adjustable).** The 30-minute limit copies the real Theory Exam. Should learners who need it (dyslexia, low vision) be able to turn on extra time? Regitra's own accommodations for the real exam would guide this. They are not checked here.
4. **Video format from Claude Design.** HTML/SVG animation (light, real-text captions, easy reduced-motion version) or MP4 (heavier, needs a text track)? This decides V5, V9 and V10.
5. **Font choice.** It needs a humanist sans-serif with full Lithuanian glyphs, a licence that allows self-hosting, and a total of ≤ 60 KB. Self-hosting also avoids a third-party request, which matters for the no-cookie-banner goal.
6. **Field speed and usage data without a cookie banner.** This links to the analytics and privacy open question from the competitor teardown.

---

## H. Sources

### Papers (all checked by DOI against the publisher record)

- Andersen, E., O'Rourke, E., Liu, Y.-E., et al. (2012). The impact of tutorials on games of varying complexity. *CHI '12*. https://doi.org/10.1145/2207676.2207687
- Bergstrom-Lehtovirta, J., & Oulasvirta, A. (2014). Modeling the functional area of the thumb on mobile touchscreen surfaces. *CHI '14*. https://doi.org/10.1145/2556288.2557354
- Birch, J. (2012). Worldwide prevalence of red-green color deficiency. *JOSA A*, 29(3). https://doi.org/10.1364/JOSAA.29.000313
- Brom, C., Stárková, T., & D'Mello, S. K. (2018). How effective is emotional design? A meta-analysis on facial anthropomorphisms and pleasant colors during multimedia learning. *Educational Research Review*, 25. https://doi.org/10.1016/j.edurev.2018.09.004
- Card, S. K., Robertson, G. G., & Mackinlay, J. D. (1991). The information visualizer, an information workspace. *CHI '91*. https://doi.org/10.1145/108844.108874
- Conradi, J., Busch, O., & Alexander, T. (2015). Optimal touch button size for the use of mobile devices while walking. *Procedia Manufacturing*, 3. https://doi.org/10.1016/j.promfg.2015.07.182
- Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018). Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review*, 25. https://doi.org/10.1016/j.edurev.2018.09.003
- Dobres, J., Chahine, N., Reimer, B., et al. (2016). Utilising psychophysical techniques to investigate the effects of age, typeface design, size and display polarity on glance legibility. *Ergonomics*, 59(10). https://doi.org/10.1080/00140139.2015.1137637
- Dyson, M. C., & Haselgrove, M. (2001). The influence of reading speed and line length on the effectiveness of reading from screen. *IJHCS*, 54(4). https://doi.org/10.1006/ijhc.2001.0458
- Fogg, B. J., Soohoo, C., Danielson, D. R., et al. (2003). How do users evaluate the credibility of Web sites? *DUX '03*. https://doi.org/10.1145/997078.997097
- Froehlich (Fröhlich), M., Kobiella, C., Schmidt, A., & Alt, F. (2021). Is it better with onboarding? Improving first-time cryptocurrency app experiences. *DIS '21*. https://doi.org/10.1145/3461778.3462047
- Galletta, D. F., Henry, R., McCoy, S., & Polak, P. (2004). Web site delays: How tolerant are users? *JAIS*, 5(1). https://doi.org/10.17705/1jais.00044
- Galliussi, J., Perondi, L., Chia, G., Gerbino, W., & Bernardis, P. (2020). Inter-letter spacing, inter-word spacing, and font with dyslexia-friendly features. *Annals of Dyslexia*, 70. https://doi.org/10.1007/s11881-020-00194-x
- Gernsbacher, M. A. (2015). Video captions benefit everyone. *Policy Insights from the Behavioral and Brain Sciences*, 2(1). https://doi.org/10.1177/2372732215602130
- Ginns, P. (2005). Meta-analysis of the modality effect. *Learning and Instruction*, 15(4). https://doi.org/10.1016/j.learninstruc.2005.07.001
- Guo, P. J., Kim, J., & Rubin, R. (2014). How video production affects student engagement: An empirical study of MOOC videos. *L@S '14*. https://doi.org/10.1145/2556325.2566239
- Hassenzahl, M., & Monk, A. (2010). The inference of perceived usability from beauty. *Human–Computer Interaction*, 25(3). https://doi.org/10.1080/07370024.2010.500139
- Höffler, T. N., & Leutner, D. (2007). Instructional animation versus static pictures: A meta-analysis. *Learning and Instruction*, 17(6). https://doi.org/10.1016/j.learninstruc.2007.09.013
- Kurosu, M., & Kashimura, K. (1995). Apparent usability vs. inherent usability. *CHI '95 Companion*. https://doi.org/10.1145/223355.223680
- Kuster, S. M., van Weerdenburg, M., Gompel, M., & Bosman, A. M. T. (2018). Dyslexie font does not benefit reading in children with or without dyslexia. *Annals of Dyslexia*, 68. https://doi.org/10.1007/s11881-017-0154-6
- Le, H. V., Mayer, S., Bader, P., & Henze, N. (2018). Fingers' range and comfortable area for one-handed smartphone interaction beyond the touchscreen. *CHI '18*. https://doi.org/10.1145/3173574.3173605
- Lindgaard, G., Fernandes, G., Dudek, C., & Brown, J. (2006). Attention web designers: You have 50 milliseconds to make a good first impression! *Behaviour & Information Technology*, 25(2). https://doi.org/10.1080/01449290500330448
- Miller, R. B. (1968). Response time in man-computer conversational transactions. *AFIPS '68 (Fall)*. https://doi.org/10.1145/1476589.1476628
- Nah, F. F.-H. (2004). A study on tolerable waiting time: How long are Web users willing to wait? *Behaviour & Information Technology*, 23(3). https://doi.org/10.1080/01449290410001669914
- Palmiter, S., & Elkerton, J. (1993). Animated demonstrations for learning procedural computer-based tasks. *Human–Computer Interaction*, 8(3). https://doi.org/10.1207/s15327051hci0803_1
- Parhi, P., Karlson, A. K., & Bederson, B. B. (2006). Target size study for one-handed thumb use on small touchscreen devices. *MobileHCI '06*. https://doi.org/10.1145/1152215.1152260
- Piepenbrock, C., Mayr, S., Mund, I., & Buchner, A. (2013). Positive display polarity is advantageous for both younger and older adults. *Ergonomics*, 56(7). https://doi.org/10.1080/00140139.2013.790485
- Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. *Psychological Bulletin*, 124(3). https://doi.org/10.1037/0033-2909.124.3.372
- Reinecke, K., Yeh, T., Miratrix, L., et al. (2013). Predicting users' first impressions of website aesthetics with a quantification of perceived visual complexity and colorfulness. *CHI '13*. https://doi.org/10.1145/2470654.2481281
- Rello, L., & Baeza-Yates, R. (2016). The effect of font type on screen readability by people with dyslexia. *ACM TACCESS*, 8(4). https://doi.org/10.1145/2897736
- Rello, L., Pielot, M., & Marcos, M.-C. (2016). Make it big! The effect of font size and line spacing on online readability. *CHI '16*. https://doi.org/10.1145/2858036.2858204
- Rey, G. D., Beege, M., Nebel, S., et al. (2019). A meta-analysis of the segmenting effect. *Educational Psychology Review*, 31. https://doi.org/10.1007/s10648-018-9456-4
- Schrepp, M., Otten, R., Blum, K., & Thomaschewski, J. (2021). What causes the dependency between perceived aesthetics and perceived usability? *IJIMAI*, 6(6). https://doi.org/10.9781/ijimai.2020.12.005
- Seckler, M., Heinz, S., Forde, S., Tuch, A. N., & Opwis, K. (2015). Trust and distrust on the web: User experiences and website characteristics. *Computers in Human Behavior*, 45. https://doi.org/10.1016/j.chb.2014.11.064
- Sengsoon, P., & Intaruk, R. (2025). Immediate effects of light mode and dark mode features on visual fatigue in tablet users. *IJERPH*, 22(4). https://doi.org/10.3390/ijerph22040609
- Sillence, E., Briggs, P., Fishwick, L., & Harris, P. (2004). Trust and mistrust of online health sites. *CHI '04*. https://doi.org/10.1145/985692.985776
- Sonderegger, A., & Sauer, J. (2010). The influence of design aesthetics in usability testing: Effects on user performance and perceived usability. *Applied Ergonomics*, 41(3). https://doi.org/10.1016/j.apergo.2009.09.002
- Sundararajan, N., & Adesope, O. (2020). Keep it coherent: A meta-analysis of the seductive details effect. *Educational Psychology Review*, 32. https://doi.org/10.1007/s10648-020-09522-4
- Thielsch, M. T., Haines, R., & Flacke, L. (2019). Experimental investigation on the effects of website aesthetics on user performance in different virtual tasks. *PeerJ*, 7. https://doi.org/10.7717/peerj.6516
- Tractinsky, N., Katz, A. S., & Ikar, D. (2000). What is beautiful is usable. *Interacting with Computers*, 13(2). https://doi.org/10.1016/s0953-5438(00)00031-x
- Tuch, A. N., Roth, S. P., Hornbæk, K., Opwis, K., & Bargas-Avila, J. A. (2012a). Is beautiful really usable? Toward understanding the relation between usability, aesthetics, and affect in HCI. *Computers in Human Behavior*, 28(5). https://doi.org/10.1016/j.chb.2012.03.024
- Tuch, A. N., Presslaber, E. E., Stöcklin, M., Opwis, K., & Bargas-Avila, J. A. (2012b). The role of visual complexity and prototypicality regarding first impression of websites. *IJHCS*, 70(11). https://doi.org/10.1016/j.ijhcs.2012.06.003
- Um, E. R., Plass, J. L., Hayward, E. O., & Homer, B. D. (2012). Emotional design in multimedia learning. *Journal of Educational Psychology*, 104(2). https://doi.org/10.1037/a0026609
- Weissgerber, S. C., Brunmair, M., & Rummer, R. (2021). Null and void? Errors in meta-analysis on perceptual disfluency and recommendations to improve meta-analytical reproducibility. *Educational Psychology Review*, 33. https://doi.org/10.1007/s10648-020-09579-1
- Wery, J. J., & Diliberto, J. A. (2017). The effect of a specialized dyslexia font, OpenDyslexic, on reading rate and accuracy. *Annals of Dyslexia*, 67. https://doi.org/10.1007/s11881-016-0127-1
- Wong, R. M., & Adesope, O. O. (2021). Meta-analysis of emotional designs in multimedia learning: A replication and extension study. *Educational Psychology Review*, 33. https://doi.org/10.1007/s10648-020-09545-x
- Xie, H., Zhou, Z., & Liu, Q. (2018). Null effects of perceptual disfluency on learning outcomes in a text-based educational context: A meta-analysis. *Educational Psychology Review*, 30. https://doi.org/10.1007/s10648-018-9442-x
- Xie, X., Song, F., Liu, Y., et al. (2021). Study on the effects of display color mode and luminance contrast on visual fatigue. *IEEE Access*, 9. https://doi.org/10.1109/access.2021.3061770
- Zorzi, M., Barbiero, C., Facoetti, A., et al. (2012). Extra-large letter spacing improves reading in dyslexia. *PNAS*, 109(28). https://doi.org/10.1073/pnas.1205566109

### Guidelines, specs and first-party data

- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2.* https://www.w3.org/TR/WCAG22/
- W3C. *Media Queries Level 5* (`prefers-reduced-motion`, `prefers-color-scheme`). https://www.w3.org/TR/mediaqueries-5/
- Apple. *Human Interface Guidelines: Accessibility* and *Dark Mode.* https://developer.apple.com/design/human-interface-guidelines/accessibility · https://developer.apple.com/design/human-interface-guidelines/dark-mode
- Android Developers. *Make apps more accessible* (48 dp targets). https://developer.android.com/guide/topics/ui/accessibility/apps
- Chrome for Developers. *Autoplay policy in Chrome.* https://developer.chrome.com/blog/autoplay
- WebKit. *New video policies for iOS* (2016). https://webkit.org/blog/6784/new-video-policies-for-ios/
- web.dev. *Web Vitals*; *How the Core Web Vitals metrics thresholds were defined*; *Performance budgets 101*; *Why does speed matter?*; case studies *Vodafone* and *Renault*. https://web.dev/articles/vitals · https://web.dev/articles/defining-core-web-vitals-thresholds · https://web.dev/articles/performance-budgets-101 · https://web.dev/articles/why-speed-matters · https://web.dev/case-studies/vodafone · https://web.dev/case-studies/renault
- Google Lighthouse. *Network throttling* docs. https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md
- British Dyslexia Association. *Dyslexia Style Guide 2023.* https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf
- Netflix Partner Help. *Timed Text Style Guide: General Requirements* and *Czech Timed Text Style Guide.* https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements · https://partnerhelp.netflixstudios.com/hc/en-us/articles/115002884887-Czech-Timed-Text-Style-Guide
- Unicode Consortium. *Latin Extended-A code chart* (U+0100–017F). https://www.unicode.org/charts/PDF/U0100.pdf
- StatCounter Global Stats. *Mobile OS market share, Lithuania, September 2026.* https://gs.statcounter.com/os-market-share/mobile/lithuania
- Lietuvos Respublikos Vyriausybė. *Kelių eismo taisyklės* (nutarimas Nr. 1950, suvestinė redakcija nuo 2026-01-01). https://www.e-tar.lt/portal/lt/legalAct/TAR.BBE7D61A0416/asr
