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
typography:
  display:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "40px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.3
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
    fontWeight: 700
    lineHeight: 1.3
  countdown:
    fontFamily: "Atkinson Hyperlegible Next, Segoe UI, system-ui, sans-serif"
    fontSize: "64px"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.03em"
    fontFeature: "tnum"
rounded:
  checkbox: "8px"
  control: "14px"
  option: "18px"
  card: "20px"
  panel: "24px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  gutter: "20px"
  xl: "24px"
  2xl: "32px"
  3xl: "40px"
components:
  button-primary:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0 20px"
    height: "56px"
  button-primary-hover:
    backgroundColor: "{colors.teal-hover}"
  button-primary-active:
    backgroundColor: "{colors.teal-press}"
  button-primary-disabled:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.ink-soft}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
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
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    size: "48px"
  chip:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.teal-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
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
    rounded: "{rounded.option}"
    padding: "14px 16px"
  option-chosen:
    backgroundColor: "{colors.teal-wash}"
  option-right-chosen:
    backgroundColor: "{colors.right-wash}"
  option-right-missed:
    backgroundColor: "{colors.right-wash}"
  option-wrong-chosen:
    backgroundColor: "{colors.wrong-wash}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "18px"
  next-step-panel:
    backgroundColor: "{colors.night-teal}"
    textColor: "{colors.on-night-teal}"
    rounded: "{rounded.panel}"
    padding: "20px"
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
- One font (Atkinson Hyperlegible Next), two weights.
- Soft-rounded, flat surfaces with 1 px lines; one shadow in the whole system.
- Right and wrong always shown by icon + word + colour.

## Colors

A teal family on a misty white page, with lime held back for one job and green, red and amber kept for meaning.

### Primary
- **Deep Teal** (`teal`): main buttons, the chosen Option's box and edge, the lesson progress bar, Remembered Rules. In dark mode it turns light (`dark-teal`) with dark text on it.
- **Night Teal** (`night-teal`): the next-step panel on Home and the answer preview on Landing. The only large dark field in light mode.
- **Teal Wash** (`teal-wash`): chips, the Rule Explainer block, the chosen Option's fill, icon tiles, the disabled button.

### Secondary
- **Highlighter Lime** (`highlighter-lime`): only behind the one sentence to remember (the "Kodėl" key line, the Landing headline word), the Memory Hook label and the "GO" of the logo. Always a solid fill behind dark text (`on-lime`).

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
- **Display** (700, 40 px, 1.1): the Landing headline only.
- **Headline** (700, 28 px, 1.2): section titles on Landing and in sheets.
- **Title** (700, 22 px, 1.3): the Question stem, card titles; 24 px inside the next-step panel.
- **Body** (400, 18 px, 1.5): Options, explanations, all running text. Never below 16 px.
- **Small** (400, 16 px, 1.45): meta lines, hints, notes.
- **Label** (700, 15 px, 1.3): chips and short captions only, never sentences.
- **Countdown** (700, 64 px, tabular): the days-to-exam number on Home.

### Named Rules
**The 16 px Floor Rule.** No sentence is smaller than 16 px. Label size (15 px) is for one- to four-word chips.

**The Lithuanian Text Rule.** Content is NFC-normalised at build time. Soft hyphens (U+00AD) are inserted at build time with `hyphen/lt` plus an exceptions list (for example `lygia·reikš·mių`, `dešinia·ran·kis`), with CSS `hyphens: manual`. Phones' own Lithuanian hyphenation is not relied on (it fails on iPhone and on Android 12 and older). Authors write plain text.

**The Font Budget Rule.** One self-hosted variable WOFF2, weights 400–700, subset to Basic Latin, the 18 Lithuanian letters and the punctuation used (13,340 bytes). ✓ and ✕ are not in the font: draw them as SVG icons.

## Layout

Mobile first, one column, a 20 px side gutter. Space steps are 4, 8, 12, 16, 20, 24, 32 and 40 px: 10–12 px between Options, 18–24 px between blocks, 40 px between Landing sections, more space above a heading than below it. Every screen has one main action; on Home and in a Question it sits in a dock at the bottom of the screen, in thumb reach. Works at 320 px and at 200 % text size. The desktop layout (a wider, centred column) is designed during the build in Claude Design from these rules.

## Elevation & Depth

Flat by default. Surfaces separate by tone (mist page, white surface, teal wash) and by a 1 px line, not by shadow. There is one shadow, under the sticky next-step panel, to show it floats above the page.

### Shadow Vocabulary
- **Panel lift** (`box-shadow: 0 -10px 30px -18px rgb(20 38 39 / .22)`; dark: `rgb(0 0 0 / .5)`): the next-step panel only.

### Named Rules
**The One Shadow Rule.** If a new element seems to need a shadow, give it a tone or a line instead.

## Shapes

Soft, even corners that grow with the size of the element: checkbox 8 px, buttons, icon buttons and inputs 14 px, Options 18 px, cards 20 px, panels 24 px, chips fully round. Edges are 1–1.5 px lines; a chosen or answered Option gets a 2.5 px edge. A right Option the learner missed gets a 2.5 px dashed edge. No coloured side stripes on cards.

## Components

### Buttons
- **Shape:** gently rounded (14 px), 56 px high, full width on phones.
- **Primary:** Deep Teal with white bold 18 px text. Hover darker teal, pressed darker again (colour change only, 120 ms). Focus: 3 px teal ring, 3 px gap.
- **Secondary:** white with a 1.5 px line, ink text ("Spėju" beside "Tikrinti").
- **Disabled:** Teal Wash with soft ink text. "Tikrinti" stays disabled until at least one Option is ticked.
- **Working:** a small spinner plus the action in progress ("Siunčiame kodą…").
- **On the night-teal panel:** white button with ink text (light teal in dark mode).
- **Text button:** teal text, 48 px high, for quiet actions ("Vėliau", "Keisti datą").
- **Icon button:** 48 × 48 px, 14 px corners, white with a 1 px line, 24 px line icon.

### Chips
- **Style:** fully round, 32 px high, Label type. Teal Wash for "Nauja taisyklė", white with a line for "Kartojimas", Trap Wash for "Egzamino spąstai", lime for "Įsiminimui".

### Answer options
- **Style:** a white card per Option (18 px corners), checkbox on the left (28 px, 8 px corners), 18 px text, at least 56 px high. Always checkboxes, even for one right answer, and never a count.
- **Chosen:** Teal Wash fill, 2.5 px teal edge, teal box with a white tick.
- **After Check (four states):** right and chosen (green fill and edge, green box, "Teisinga · tavo pasirinkimas"); right but missed (green fill, dashed green edge, empty green box, "Teisingas variantas · nepažymėjai"); wrong and chosen (red fill and edge, red box with ✕, "Neteisinga · tavo pasirinkimas"); wrong and not chosen (no mark, soft text).
- **Result line:** after Check, a 40 px round icon with "Teisingai" or "Neteisingai" and one short line sits above "Toliau" in the dock.

### Learning blocks
- **Kodėl:** a teal label, the key sentence in Title weight with the lime highlighter, then the explanation and the KET point link.
- **Rule Explainer:** Teal Wash block with a book icon and the Rule's name.
- **Memory Hook:** white block with a line, lime "Įsiminimui" chip, one bold sentence.
- **Exam Trap:** Trap Wash block with a warning icon and amber title.

### Cards / Containers
- **Corner Style:** 20 px.
- **Background:** Surface on the Mist page.
- **Shadow Strategy:** none (see Elevation & Depth).
- **Border:** 1 px Line.
- **Internal Padding:** 18 px.
- **Row:** a card that is a button: 48 px teal icon tile, title, soft meta line, chevron; at least 72 px high.

### Inputs / Fields
- **Style:** 56 px high, 14 px corners, 1.5 px strong line, white, 18 px text; bold 16 px label above, soft 16 px hint below.
- **Focus:** the edge turns teal with a 2 px teal ring.
- **Error:** red edge and an error line under the field with an icon that names the problem and the fix ("Trūksta „@“. Patikrink el. pašto adresą.").
- **Code:** six one-digit boxes, 24 px bold tabular digits.

### Navigation
- **Top bar:** logo on the left, 48 px icon buttons on the right (Progress, Menu). In a Lesson: close button, progress bar (8 px, teal on Teal Wash) and "5 / 22".
- **Next-step panel (signature):** the night-teal panel docked at the bottom of Home: "Toliau · 7 pamoka iš 36", a thin progress bar, the Lesson name in Title type, a meta line, and the white "Tęsti" button.

### Progress
- **Rules bar:** a 12 px segmented bar, Remembered in Deep Teal, Learning in Teal Middle, Not met in Teal Wash, with a legend and tabular counts.

## Do's and Don'ts

### Do:
- **Do** give every screen one Deep Teal main button, at the bottom when the screen is a task.
- **Do** show right and wrong with an icon, a word and a colour, every time.
- **Do** keep sentences at 16 px or larger and body text at 18 px with 1.5 line height.
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
