---
name: KETGO
description: Calm, teal-led learning app for the Lithuanian category-B Theory Exam, mobile web first.
colors:
  teal: "#145457"
  teal-hover: "#0F4346"
  teal-press: "#0A3436"
  on-teal: "#FFFFFF"
  teal-wash: "#E0EDEA"
  teal-wash-2: "#CFE3DE"
  teal-ink: "#145457"
  teal-middle: "#7DB3AC"
  night-teal: "#142627"
  on-night-teal: "#F4F7F5"
  on-night-teal-soft: "#B9CCC4"
  night-teal-2: "#1E3A3B"
  night-teal-fill: "#5CC3B8"
  highlighter-lime: "#CCFF00"
  on-lime: "#142627"
  mist: "#F4F7F5"
  surface: "#FFFFFF"
  surface-2: "#EBF1EE"
  ink: "#142627"
  ink-soft: "#3E5557"
  line: "#D5E0DB"
  line-strong: "#6B847D"
  right: "#16703A"
  right-wash: "#E2F3E5"
  wrong: "#B3261E"
  wrong-wash: "#FBE8E6"
  trap: "#7F4A00"
  trap-wash: "#FFF0D4"
  dark-mist: "#0E1B1C"
  dark-surface: "#162728"
  dark-surface-2: "#1D3233"
  dark-ink: "#EEF4F1"
  dark-ink-soft: "#B0C4BE"
  dark-line: "#27403F"
  dark-line-strong: "#6E8C86"
  dark-teal: "#5CC3B8"
  dark-teal-hover: "#74D0C6"
  dark-teal-press: "#4AAFA4"
  dark-on-teal: "#0E1B1C"
  dark-teal-wash: "#1B3536"
  dark-teal-wash-2: "#22413F"
  dark-teal-ink: "#8FDCD3"
  dark-teal-middle: "#3F8079"
  dark-night-teal: "#1B3334"
  dark-night-teal-2: "#24403F"
  dark-right: "#6FDC97"
  dark-right-wash: "#173A2A"
  dark-wrong: "#FF8F86"
  dark-wrong-wash: "#432222"
  dark-trap: "#FFC56B"
  dark-trap-wash: "#3A2A10"
  dark-highlighter-lime: "#B2D62A"
typography:
  display:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "40px"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.015em"
  headline-compact:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.5
  small:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.01em"
  countdown:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "64px"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.03em"
    fontFeature: "tnum"
rounded:
  highlighter: "4px"
  checkbox: "6px"
  control: "12px"
  container: "20px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  2xl: "32px"
  3xl: "48px"
  4xl: "64px"
  gutter: "16px"
  gutter-desktop: "48px"
components:
  button-primary:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.body}"
    fontWeight: 600
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "56px"
    heightDesktop: "52px"
  button-primary-hover:
    backgroundColor: "{colors.teal-hover}"
  button-primary-active:
    backgroundColor: "{colors.teal-press}"
  button-disabled:
    opacity: 0.4
  button-secondary:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.teal-ink}"
    rounded: "{rounded.control}"
    height: "56px"
  button-on-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "56px"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.teal-ink}"
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "48px"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    size: "48px"
  keycap:
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.checkbox}"
    height: "24px"
  chip:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.teal-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "2px 10px"
    height: "28px"
  chip-trap:
    backgroundColor: "{colors.trap-wash}"
    textColor: "{colors.trap}"
  chip-memory-hook:
    backgroundColor: "{colors.highlighter-lime}"
    textColor: "{colors.on-lime}"
  option:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "14px 16px"
    paddingDesktop: "16px"
  option-chosen:
    backgroundColor: "{colors.teal-wash}"
  option-right-chosen:
    backgroundColor: "{colors.right-wash}"
  option-right-missed:
    backgroundColor: "{colors.right-wash}"
  option-wrong-chosen:
    backgroundColor: "{colors.wrong-wash}"
  result-bar:
    rounded: "{rounded.container}"
    padding: "16px 16px 16px 24px"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "16px"
  next-step-panel:
    backgroundColor: "{colors.night-teal}"
    textColor: "{colors.on-night-teal}"
    rounded: "{rounded.container}"
    padding: "24px"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "56px"
---

# Design System: KETGO

## Overview

**Creative North Star: "The Highlighted Rule"**

KETGO looks like a calm, well-made study space. The page is light and quiet, deep teal does the work (the main button, the chosen option, the next-step panel), and one highlighter-lime mark shows the single sentence worth remembering, the way a learner marks a textbook. Everything else stays out of the way so the Rule can be read.

The look is commercial, sleek and clean, at the craft level of Apple, Revolut or Wise. It is never a generic tech startup (no gradients, glow, neon on dark) and never an official or government site (no grey, stiff, form-heavy screens). It grew out of the 2025 dark-teal-and-lime mocks but turned them light-first and took lime off buttons. Brutalist, experimental and metaphor-led looks were tried and rejected (2026-10-14).

The Question screen is the calmest place in the app: no motion, no decoration, one clear main button at the bottom. Landing and Home may carry a little more presence, through the night-teal panel and big tabular numbers, never through ornament.

**Key Characteristics:**
- Light first; dark follows the phone and keeps the same contrast.
- Deep teal for action, night teal for the "next step", lime only as a highlighter.
- One font (Atkinson Hyperlegible Next), two weights: 400 and 600.
- One 4-pt spacing scale used by role, and every edge in a column shared.
- Two corner sizes (12 px for things, 20 px for containers), flat surfaces with 1 px lines, one shadow in the whole system.
- Nothing framed that doesn't need a frame: no boxes around icons, numbers or keys.
- Right and wrong always shown by icon + word + colour.

## Colors

A teal family on a misty white page, with lime held back for one job and green, red and amber kept for meaning.

### Primary
- **Deep Teal** (`teal`): main buttons, the chosen Option's box and edge, the lesson progress bar, Remembered Rules. In dark mode it turns light (`dark-teal`) with dark text on it.
- **Night Teal** (`night-teal`): the next-step panel on Home and the answer preview on Landing. The only large dark field in light mode.
- **Teal Wash** (`teal-wash`): chips, the Rule Explainer block, the chosen Option's fill, icon tiles, the disabled button.

### Secondary
- **Highlighter Lime** (`highlighter-lime`): only behind the one sentence to remember (the "Kodėl" key line, the Landing headline word), the Memory Hook label and the "GO" of the logo. Always a solid fill behind dark text (`on-lime`). In dark mode it is calmer (`dark-highlighter-lime`, 9.4:1 with `on-lime`), so it never glows like neon.

### Tertiary (meaning only)
- **Right** (`right` on `right-wash`) and **Wrong** (`wrong` on `wrong-wash`): answer states and the result line, always with ✓ or ✕ and a word.
- **Trap** (`trap` on `trap-wash`): the Exam Trap block and chip.

### Neutral
- **Mist** (`mist`): the page.
- **Surface** (`surface`) and **Surface 2** (`surface-2`, hover): cards, Options, inputs.
- **Ink** (`ink`) and **Ink, soft** (`ink-soft`): text and second text. Ink reaches at least 7:1 on every light surface; soft ink at least 4.5:1.
- **Line** (`line`) for card edges; **Line, strong** (`line-strong`) for checkbox and input edges, at least 3:1.

### Named Rules
**The Highlighter Rule.** Lime marks the one thing to remember, at most once per screen, plus the logo and the Memory Hook label. Never a button, never text colour, never a border.

**The Meaning Colours Rule.** Green, red and amber mean right, wrong and trap. They are never used for decoration, and they never appear without an icon and a word.

## Typography

**Body and display font:** Atkinson Hyperlegible Next (fallback Segoe UI, system-ui, sans-serif)

**Character:** a font drawn for easy reading (Braille Institute), with clear shapes for look-alike letters. It reads as friendly and serious at once, which suits learners of 17–21 and their parents.

### Hierarchy
- **Display** (600, 40 px, 1.1, −0.02em): the Landing headline only.
- **Headline** (600, 28 px, 1.25, −0.015em): page titles, the Question stem on desktop, the result score. On phones the Question stem uses **Headline, compact** (24 px), so it stands clearly above the 18 px Options.
- **Title** (600, 22 px, 1.3, −0.01em): the verdict word, sheet and dialog titles, section titles.
- **Body** (400, 18 px, 1.5; Options 1.45): Options, explanations, all running text. Never below 16 px. The key sentence is Body in 600.
- **Small** (400, 16 px, 1.45): meta lines, hints, notes.
- **Label** (600, 15 px, 1.3, +0.01em): chips, keycaps and short captions only, never sentences.
- **Countdown** (600, 64 px, tabular): the days-to-exam number on Home, the Mock Exam score.

### Named Rules
**The 16 px Floor Rule.** No sentence is smaller than 16 px. Label size (15 px) is for one- to four-word chips.

**The Two Weights Rule.** Regular (400) for reading, semibold (600) for everything that labels or leads. No 700: at this font's shapes, 700 headings look heavy (moved to 600 in the 2026-10-15 rework). Big text gets slightly tighter tracking, small labels slightly looser.

**The Lithuanian Text Rule.** Content is NFC-normalised at build time. Soft hyphens (U+00AD) are inserted at build time with `hyphen/lt` plus an exceptions list (for example `lygia·reikš·mių`, `dešinia·ran·kis`), with CSS `hyphens: manual`. Phones' own Lithuanian hyphenation is not relied on (it fails on iPhone and on Android 12 and older). Authors write plain text.

**The Font Budget Rule.** One self-hosted variable WOFF2, weights 400–600, subset to Basic Latin, the 18 Lithuanian letters and the punctuation used (13,340 bytes). ✓ and ✕ are not in the font: draw them as SVG icons.

## Layout

Mobile first. Space comes from one 4-pt scale, used by role and never by eye (reworked 2026-10-15, when the owner said the old spacing "looks like it was made by an amateur"):

- **8 px inside a group:** between Options, between a label and its text.
- **16 px between parts of a block:** the stem and the picture on phone, the Options and the one-time tip.
- **24 px between groups:** the stem and the picture on desktop, the Options and the buttons.
- **32–48 px between sections;** 64 px between the two desktop columns.
- More space above a heading than below it. No odd values (10, 14, 18, 20, 22 px are gone).

**Shared edges.** In every column, the stem, picture, Options, buttons and result bar share both the left and the right edge. The close icon's glyph, not its tap area, lines up with the text: the button hangs into the gutter. Phone gutter 16 px; desktop side margins 48 px (32 px below 1100 px).

Every screen has one main action; on phone it sits in a dock at the bottom of the screen, in thumb reach. Works at 320 px and at 200 % text size. The Question screen's layouts were settled in [Question screen on a phone](https://github.com/Whirlywack/ketgo-web/issues/11) and reworked on 2026-10-15; other screens' desktop layouts are designed during the build from these rules.

- **Question screen, phone:** one column: chip, question (24 px), a quiet "Pažymėk visus teisingus" line, picture, Options. After Check the app scrolls so your pick and the right answer sit above the result bar (verdict, key sentence, Toliau; tinted by the verdict); the "why" follows below. On short screens the picture gets narrower, never cropped.
- **Question screen, desktop (900 px and wider):** one frame for every Question, at most 1280 px wide, two equal tracks.
  - **Left, "the question":** the chip, the question (28 px), the picture in a frame that keeps the scene's own shape (never cropped, never letterboxed). After Check, the "why" (explanation, the folded Rule, the Exam Trap) appears right under the picture it explains. Words next to the picture they refer to are learned better than words placed apart (spatial contiguity: Mayer; Ginns 2006 meta-analysis).
  - **Right, "your answer":** sticky. It holds the quiet hint line, the Options with their number keys, then the buttons. After Check the hint becomes "Tavo atsakymas" and the result bar takes the buttons' place, so the verdict appears where the eye already is. The column is sticky exactly where it starts, so it never moves. It never grows past the screen: the buttons and result bar stay put, the Options scroll, and a fade shows only while more is below. After Check, if the "why" starts low on the screen, the page scrolls until it starts mid-screen (never past the picture's top) while the answer column stays still. On a 1366 × 650 laptop your pick, Toliau and the first "why" block are all on screen.
  - **Keys:** 1–4 tick, N = "Nesu tikras", Enter = the screen's main action. Each key is shown on the control it triggers (a keycap inside the button, the number on the Option), never as a separate hint line.
  - **Reading a Rule first** ("Pirma išmokti") uses the same frame: the Rule where the "why" goes, "Į klausimą" where the buttons are. The Exam Trap is not shown before answering (it would give away a distractor).
  - On tall windows the frame starts a little lower (6 % of the window height minus 24 px, 16–64 px), so it doesn't hug the top.
- **Mock Exam, desktop:** the same frame. The answer sheet (one numbered square per Question, in two rows of 15 for the full 30; answered = Teal Wash with a dot, current = 2 px teal edge) is the header's progress bar, with the time left and "Baigti egzaminą" on the right. The left track has "Klausimas 2 iš 30 · atsakyta 1" above the question; the right track has the Options and Atgal / Kitas. Leaving, and finishing with unanswered Questions, ask first, in the page.
- **Single-column screens** (Mock Exam start and results, Lesson end) use a centred 720 px column. The button follows the content, 320 px wide and left-aligned.

## Elevation & Depth

Flat by default. Surfaces separate by tone (mist page, white surface, teal wash) and by a 1 px line, not by shadow. There is one shadow, under the sticky next-step panel, to show it floats above the page.

### Shadow Vocabulary
- **Panel lift** (`box-shadow: 0 -10px 30px -18px rgb(20 38 39 / .22)`; dark: `rgb(0 0 0 / .5)`): the next-step panel only.

### Named Rules
**The One Shadow Rule.** If a new element seems to need a shadow, give it a tone or a line instead.

## Shapes

Two corner sizes carry almost everything:
- **12 px:** every control and content object: buttons, icon buttons, inputs, Options, the picture, learning blocks, cards, rows.
- **20 px:** containers that hold other things: the result bar, sheets, in-page dialogs, the next-step panel.
- **Smaller:** 6 px for the checkbox and keycaps, 4 px for the highlighter. Chips and progress bars are fully round.

Edges are 1 px lines (1.5 px only on an empty checkbox and the Switch track). A chosen or answered Option gets a 2 px edge; a right Option the learner missed gets a 2 px dashed edge. No coloured side stripes, and no card inside a card.

## Components

### Buttons
- **Shape:** 12 px corners, 56 px high on phones (full width), 52 px on desktop; 18 px semibold (600) text.
- **Primary:** Deep Teal with white text. Hover darker teal, pressed darker again (colour change only, 120 ms). Focus: 3 px teal ring, 3 px gap.
- **Secondary:** tonal: Teal Wash fill with teal text ("Nesu tikras" beside "Tikrinti", "Pirma išmokti", "Atgal"). Quieter than the primary, so the one solid teal button always leads.
- **Disabled:** the button keeps its own colours at 40 % opacity, so it still reads as "the main button, not ready yet". "Tikrinti" stays disabled until at least one Option is ticked. A tap on a disabled button says why ("Pirma pažymėk bent vieną variantą.").
- **Keycap (desktop):** the key that triggers a button sits inside it ("Tikrinti [Enter]", "Nesu tikras [N]").
- **Working:** a small spinner plus the action in progress ("Siunčiame kodą…").
- **On the night-teal panel:** white button with ink text (light teal in dark mode).
- **Text button:** teal text, 48 px high, for quiet actions ("Vėliau", "Keisti datą").
- **Icon button:** 48 × 48 px tap area, no frame: the 24 px line icon alone, a Surface 2 wash on hover. Its glyph lines up with the text edge.

### Chips
- **Style:** fully round, 28 px high, Label type. Teal Wash for "Nauja taisyklė", no fill with a 1 px line and soft ink for "Kartojimas", Trap Wash for "Egzamino spąstai", lime for "Įsiminimui".

### Answer options
- **Style:** a white card per Option (12 px corners, 1 px line), checkbox on the left (24 px, 6 px corners, centred on the first line of text), 18 px text, at least 56 px high, 8 px apart. Always checkboxes, even for one right answer, and never a count. On desktop the Option's number key sits at the right as a plain number, framed as a keycap only on hover or when ticked.
- **Chosen:** Teal Wash fill, 2 px teal edge, teal box with a white tick.
- **After Check (four states):** right and chosen (green fill and edge, green box, "Teisinga · tavo pasirinkimas"); right but missed (green fill, dashed green edge, empty green box, "Teisingas variantas · nepažymėjai"); wrong and chosen (red fill and edge, red box with ✕, "Neteisinga · tavo pasirinkimas"); wrong and not chosen (no mark, soft text; on phone also no border and 16 px). Each wrong pick and each missed right Option gets one short line saying why.
- **Your guess (fifth state):** on a first guess at a new Rule, a wrong pick is teal (Teal Wash fill, teal edge, "Tavo spėjimas"), never red: guesses don't count.
- **Result bar:** after Check the result takes the main button's place, tinted by the verdict (Right Wash, Wrong Wash, Teal Wash for a guess, Surface 2 for unanswered). A tinted strip carries a 32 px round icon and the verdict word (Title), with any note under it ("Pažymėjai ne visus teisingus."). Under the strip, on the plain page or surface, the key sentence (Body 600, lime highlighter, balanced lines). The lime never sits on a tint. The icon centres on the Options' checkbox column and the words start on the Options' text edge. On phone the strip runs edge to edge at the top of the dock, with "Kodėl ↓" on its right, and "Toliau" below. On desktop it is a 20 px-corner block at the foot of the answer column, with "Toliau" on the strip's right; in a Mock Exam review, Atgal / Kitas sit under the block. A partly right multi-correct answer adds why it counts as wrong ("Pažymėjai ne visus teisingus."). A first guess shows a teal "Dabar sužinosi" (book icon) when wrong and a green "Atspėjai" when right; an unanswered Mock Exam Question shows a neutral dash. When the "why" below holds more, a "Kodėl ↓" or "Taisyklė ↓" text button scrolls to it.

### Learning blocks
- **Kodėl:** a teal label, the key sentence in Title weight with the lime highlighter, then the explanation and the KET point link.
- **Rule Explainer:** Teal Wash block with a book icon and the Rule's name.
- **Memory Hook:** white block with a line, lime "Įsiminimui" chip, one bold sentence.
- **Exam Trap:** Trap Wash block with a warning icon and amber title. Shown only when the learner ticked the Option it warns about; it teaches a reading habit, not the Rule again.

### Cards / Containers
- **Corner Style:** 12 px.
- **Background:** Surface on the Mist page.
- **Shadow Strategy:** none (see Elevation & Depth).
- **Border:** 1 px Line.
- **Internal Padding:** 16 px.
- **Row:** a card that is a button: 48 px teal icon tile, title, soft meta line, chevron; at least 72 px high.

### Inputs / Fields
- **Style:** 56 px high, 12 px corners, 1.5 px strong line, white, 18 px text; bold 16 px label above, soft 16 px hint below.
- **Focus:** the edge turns teal with a 2 px teal ring.
- **Error:** red edge and an error line under the field with an icon that names the problem and the fix ("Trūksta „@“. Patikrink el. pašto adresą.").
- **Code:** six one-digit boxes, 24 px bold tabular digits.
- **Switch:** a setting row (bold title, soft 16 px hint) with a 52 × 32 px track; on = Deep Teal. Used for settings such as "Be laiko ribos". Never use an answer Option card for a setting.

### Navigation
- **Top bar:** logo on the left, 48 px icon buttons on the right (Progress, Menu). In a Lesson: close button, progress bar (6 px, teal on Teal Wash) and "5 / 22". In a Mock Exam on desktop: close button, the answer sheet, time left and "Baigti egzaminą".
- **Next-step panel (signature):** the night-teal panel docked at the bottom of Home: "Toliau · 7 pamoka iš 36", a thin progress bar, the Lesson name in Title type, a meta line, and the white "Tęsti" button.

### Progress
- **Rules bar:** a 12 px segmented bar, Remembered in Deep Teal, Learning in Teal Middle, Not met in Teal Wash, with a legend and tabular counts.

## Do's and Don'ts

### Do:
- **Do** give every screen one Deep Teal main button, at the bottom when the screen is a task.
- **Do** show right and wrong with an icon, a word and a colour, every time.
- **Do** keep sentences at 16 px or larger and body text at 18 px with 1.5 line height.
- **Do** take every space from the scale by its role (8 inside a group, 16 inside a block, 24 between groups, 32–64 between sections), and let every element in a column share both edges.
- **Do** check every new colour pair: 7:1 for body text, 4.5:1 minimum, 3:1 for edges and icons.
- **Do** build the onboarding video from these real components as HTML/SVG animation with real-text captions and a still version for reduced motion.
- **Do** keep motion to 120 ms colour changes; respect reduced motion.

### Don't:
- **Don't** use lime on a button, as text colour, or more than once on a screen.
- **Don't** add gradients, glow, glass, or neon on dark: the generic-startup look is ruled out.
- **Don't** use grey, stiff, form-heavy layouts: the official or government look is ruled out.
- **Don't** add brutalist or experimental treatments, or a look built on a metaphor.
- **Don't** animate anything on the Question screen, and don't add points, streaks or mascots.
- **Don't** say how many Options are right, and don't use radio buttons.
- **Don't** add a second shadow or a coloured side stripe on cards.
- **Don't** frame what doesn't need a frame (icons, numbers, keys), and never put a card inside a card.
- **Don't** use bold (700): semibold (600) is the heaviest weight.
