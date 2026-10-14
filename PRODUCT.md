# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

Mobile web first (Lithuania is ~70 % Android; iPhone matters for Add to Home Screen and push). Must also work well on desktop. No native apps.

## Users

**Learners** preparing for the Regitra category-B **Theory Exam** in Lithuania. Mostly **17–21 year olds** who arrive from TikTok and social media and judge the look in a split second. Parents and older learners must still trust it. They study on a phone, often several short sessions a day, usually with an exam date a few weeks away.

**Partners** (driving schools, creators) send learners through a personal link or promo code. They do not use the app themselves in the beta.

## Product Purpose

KETGO gets learners ready for the Theory Exam and makes the Rules stick. It is free in the beta. Success: the learner passes the real exam, and on the way always knows what to study next.

## Positioning

A learning system, not another quiz app. Competitors give instant feedback, an explanation under the question and no sign-up; for KETGO that is the floor. KETGO adds spaced repetition aimed at the exam date (FSRS), a curated Program of Lessons, Questions that come back with shuffled Options and a new mix of Distractors, and an honest Readiness estimate shown only once it is earned. Truly free, no pressure tricks, no billing traps.

## Operating Context

- One main button, **Continue**, picks the next step: a Lesson, a Review or a Mock Exam.
- A Lesson is ~15–25 minutes: new Rules met question-first, then taught by a Rule Explainer, plus due Rules mixed in.
- Mock Exam copies Regitra: 30 Questions, 30 minutes, pass at 24, feedback only at the end.
- No sign-up ever needed. An optional Account (email + 6-digit code) is offered once after Lesson 2.
- One opt-in daily reminder by web push.
- Eight screens: Landing, Onboarding (short video, then exam date), Home, Lesson / Review, Lesson end, Mock Exam and results, Progress, Menu.

## Capabilities and Constraints

- All text in **Lithuanian**. Long words are common (1 word in 5 has 10+ letters; the longest have 19).
- Vocabulary: see `GLOSSARY.md` (Learner, Question, Option, Distractor, Rule, Lesson, Review, Mock Exam, Remembered, Readiness, Rule Explainer, Memory Hook, Exam Trap).
- Multi-correct Questions: checkboxes on every Question, never say how many are correct, all-or-nothing.
- Speed budget on a mid-range Android: LCP ≤ 2.5 s (aim 1.5 s), tap → feedback ≤ 100 ms, CLS ≤ 0.1, ≤ 170 KB to the first Question.
- Stack: SvelteKit 3, hosted in the EU (Scaleway Warsaw).
- About 83 % of exam Questions have a picture (road situations, signs). KETGO has no situation pictures yet; ~100 own drawn scenes are planned. Never use Regitra's pictures.

## Brand Commitments

- Name: **KETGO**.
- Must not look like a **generic tech startup** (gradients, glow, dark screen with neon, "AI" feel) or like an **official / government** site (grey, stiff, form-heavy, Regitra-like).
- 2025 mocks (`~/Documents/ketgo-docs-ui-mocks`, dark teal `#142627` + lime `#CCFF00`) are history, not binding; one look direction may evolve them.
- Look: commercial, sleek and clean, at the craft level of Apple, Revolut or Wise. No brutalism, nothing experimental, no look built on a metaphor (an orienteering-map look and a reflector look were rejected on 2026-10-14).
- No points, leaderboards, day streaks, mascots or animation during Questions. Progress tracking is fine.

## Evidence on Hand

- ~274 Own Questions today (`~/Documents/Claude/Projects/ket second brain/questions.jsonl`), ~500 by launch, each with an explanation and a KET rule link.
- Research behind every design rule: GitHub issues "First impression and mobile UI" (#21) and "Screen design that helps learning" (#20) on `Whirlywack/ketgo-web`.
- No testimonials, no learner numbers, no pass-rate claims yet. Do not invent them.

## Product Principles

1. **Learning first.** Colour and pictures go into the teaching (Rule Explainers, Memory Hooks, marked pictures), not decoration.
2. **One clear next step.** Every screen has one main action; Continue always says what comes next.
3. **Honest.** Readiness is an estimate, shown only when earned. No fake urgency, no pop-ups, no streak guilt.
4. **Fast on a cheap phone.** Speed is part of the look.
5. **Calm, not dull.** Beautiful enough to win the first look, easy enough to keep learners.

## Accessibility & Inclusion

WCAG 2.2 AA floor. Body text 18 px (min 16 px), line height 1.5, contrast 7:1 for body text (4.5:1 minimum), tap targets ≥ 48 px (Options and main button 56 px), right/wrong shown by icon + word + colour, never colour alone. Never block zoom; works at 320 px and 200 % text size. Follow the phone's light/dark setting with equal contrast. Respect reduced motion. No dyslexia fonts.
