# Competitor teardown

Ticket: [#3 Competitor teardown](https://github.com/Whirlywack/ketgo-web/issues/3) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1)

**All facts were checked on 2026-10-13** unless a different date is given. Sources are the competitors' own websites, their App Store and Google Play pages, and Regitra's own site. **UNCONFIRMED** marks anything I could not check directly. No competitor Question text is copied here.

How I checked mobile experience: I opened each site in a real browser (Chromium) at phone size (390 × 844 px), solved part of each free test, and measured page weight. A real phone on mobile data will be slower. The numbers show how sites compare with each other. They are not exact speeds.

Words: "Theory Exam" means the real Regitra exam. "Mock exam" means a competitor's practice test in the same format: 30 Questions, 30 minutes, pass with 80 % or more, so at most 6 mistakes for category B ([Regitra](https://www.regitra.lt/paslaugos/egzaminai/teorijos-egzaminas/)).

---

## 1. Comparison table

Mobile UX score: 5 = excellent, 1 = painful. It is my judgement from the phone-size test.

| Competitor | Main features | "Smart" features | Price for about 1 week (EUR) | Free tier | Mobile UX (1–5) and why |
|---|---|---|---|---|---|
| **ketbilietai.lt** (DrivingEd UAB). Market leader. | Mock exam, topic tests, "new rules" test, explanations with KET point, "ask a teacher", 6 languages on web, iOS + Android app | AI readiness chart that says when you are ready (app). A Question counts as "learned" after 2 correct answers in a row and is not asked again. "Unlearned only" tests. | **7 days: 9.03** (1.29/day). 1 day: 2. 14 days: 14.98. Monthly auto-renew: 15.50/month. Day credits are used only on days you study. | About 200 Questions with explanations, no sign-up | **3.5**: clean question screen, light page. But the cookie banner covers about 2/3 of the screen, there is no instant feedback, and reviews report app bugs after the 2026 update. |
| **eket.lt** (UAB 4MARK) | Mock exam, filters (topic, difficulty, mistakes, unseen), study mode, explanations, live online lectures, teacher Q&A, KET course, first-aid certificate, "faster Regitra date" service | "Learning wizard" / individual programme builds tasks from your weakest topics | **7 days: 9.17** (1.31/day, "sale" from 1.70). 31 days: 17.36. 62 days: 29.76. Extra payment fees. | 200-Question demo, but **explanations locked** | **2**: heavy page (251 requests, about 2.6 MB), upsell box above every Question, countdown timers, "only 4 left" pressure, pinch-zoom blocked |
| **vairavimotestai.lt** | Mock exam, topic tests, KET lessons + study plan, teacher consultations, statistics | Claims AI that adapts to your pace and results (details UNCONFIRMED) | **No week plan.** You pay for answering time: 10 h = 9.49, 25 h = 17.99, 50 h = 24.49. Time runs only while answering. | Demo of 100 repeating Questions, no sign-up | **3**: fast first load. But a full-screen cookie wall, a "-51 %" countdown, a very long home page, and hour-based pricing is hard to understand. |
| **RoboKET** (Robo code MB). New and modern. | Mock exam with live "mistakes x/6" counter, 1700+ Questions, 800+ illustrated theory cards, community chat, rewards, LT + EN, no ads in app | **Pass-probability score** after each test ("safe to register at 90 %"). **Daily plan from your exam date** (10–20 min/day). Mistakes by topic. | **1 week: 5.99.** 2 weeks: 9.99. 1 month: 15.99. 3 months: 29.99. Money back if you reach 90 % and still fail. | Demo tests, no sign-up | **4**: lightest page (21 requests, about 370 KB). Start a real-format exam on the landing page. Instant red/green feedback with an inline explanation. But explanations mostly repeat the rule text. |
| **Autostart** (APPASTIC MB) | 1800+ Questions, explanations, all categories, 6 languages, statistics, web app + iOS + Android | Learning statistics only; nothing clearly adaptive | **1 week: 4.99 or 9.99** (two App Store prices, auto-renew). 1 month: 9.99–19.99. | 60 Questions | **UNCONFIRMED**: the website blocked my test browser. Reviews report the app not opening, an endless spinner, long tests restarting if the app closes, and grammar errors. |
| **Kettestai.lt** (APPASTIC MB, same company as Autostart). New app, Sept 2026. | Mock exam, topic tests, explanations, statistics, chat | Weak-topic statistics | **1 week: 7.99 or 9.99** (App Store). 1 month: 9.99–29.99. Web price needs login (UNCONFIRMED). | Demo test | **3 (partly UNCONFIRMED)**: light web page (29 requests, about 430 KB). Reviewers praise the design. The leaderboard shows the same name 5–6 times, which looks fake or broken. |
| **KET testai ir teorija** (RT Tech). App only. | 1350+ Questions, 730 theory cards, custom tests by topic, saved hard Questions, reminders | Pass-probability score, progress charts | **1 week: 3.99** (App Store list; its own description says 6.99). 1 month: 14.99. | 1 demo test | **UNCONFIRMED** (app only). The last update was Sept 2024, so it looks unmaintained. |

### Ratings (checked 2026-10-13)

| Product | App Store (Lithuania) | Google Play | Last app update |
|---|---|---|---|
| ketbilietai | 4.8 (about 1,000 ratings), #23 Education | 4.6 (1.4K reviews), 50K+ installs | Play: 2026-09-03 |
| eKET | 5.0 (1 rating, US storefront) | 4.5 (293 reviews), 10K+ installs | Play: 2026-08-28 |
| Autostart | 4.8 (about 2,000 ratings), #14 Education | 4.8 (1.29K reviews), 50K+ installs | Play: 2026-08-28 |
| RoboKET | 4.8 (312 ratings), top 50 Education | 4.6 (236 reviews), 10K+ installs | Play: 2026-10-06 |
| Kettestai.lt | 4.6 (53 ratings), #9 Education | not checked | iOS: 2026-09-28 |
| KET testai ir teorija | 4.6 (277 ratings) | not checked | iOS: 2024-09-21 |
| vairavimotestai.lt | no app found | no app found | n/a |

Chart positions change daily. Two listings both showed "#45", so treat ranks as rough.

---

## 2. Where KETGO can win

1. **Free means free, with explanations.** Everyone charges about 4–10 € per week. eKET locks explanations in its free demo, and Autostart gives only 60 Questions free. A free beta with full explanations and no trial-to-subscription trap is the strongest pull we have.
2. **No pressure tricks, no billing surprises.** Several common complaints are about money: auto-renew without asking (RoboKET, eKET), "can't stop the subscription" (eKET), "paid and got nothing" (ketbilietai, Autostart). eKET and vairavimotestai also use fake-urgency countdowns and "only 4 left". KETGO can be the calm, honest one. When paid plans come later, a one-off week pass with no auto-renew fits what learners want.
3. **Be honest about "like Regitra".** The number 1 complaint across ketbilietai, eKET and Autostart is: "I scored 95–100 % in the app and failed, because the real Questions were different." Every competitor promises "Questions like Regitra". KETGO serves only Own Questions, so we should not promise that. We should promise understanding of the rules, and build a readiness score on topic coverage, not on memorised repeats.
4. **Explanations that teach "why", in short plain Lithuanian.** Learners praise good explanations and attack bad ones. Autostart pastes a long KET paragraph, and RoboKET mostly repeats the rule. A short "why" plus the KET point number, free for everyone, is a clear gap.
5. **A question screen better than RoboKET's.** RoboKET sets the bar: no sign-up, instant red/green feedback, inline explanation, a "mistakes 1/6" counter. Beat it with nothing above the Question (no upsell banners like eKET), answers reachable with one thumb, a sticky "Next" button, a smaller page, and progress saved instantly. ketbilietai and Autostart users lose progress or cannot see past answers.
6. **Real spaced repetition plus a plan to the exam date.** Today's "smart" features are simple. ketbilietai retires a Question after 2 correct answers in a row. eKET weights weak topics. Only RoboKET builds a daily plan from the exam date. No competitor advertises true review over days and weeks (UNCONFIRMED that none does it inside the app).
7. **Let learners look back.** A ketbilietai reviewer asks to see answers from an earlier test after closing the app. Keep a full history of every test and mistake.
8. **Maybe no cookie banner at all.** ketbilietai and vairavimotestai show cookie walls that fill most of a phone screen. If KETGO uses only essential cookies and cookie-free analytics, it may not need a banner. This is UNCONFIRMED legally; check it in the privacy ticket.

---

## 3. What learners complain about (all products)

Grouped from recent Google Play and App Store reviews. Each line names the products where I saw it.

- **"Not like the real exam" / scored high, still failed**: ketbilietai (1★, 2026-09-08; 1★, 2025-09-18), eKET (1★, 2026-03-11, 03-14, 03-17), Autostart (1★ Play 2025-11-03; iOS review "totally different patterns").
- **Wrong, illogical or badly written Questions**: eKET ("full of mistakes", 2026-04-04), Autostart ("about 70 % fine, the rest silly", 2025-09-15; "many grammar errors", 2026-06-17), ketbilietai ("wrong tests", 2025-11-09; "4 identical Options", 2026-06-22).
- **Weak explanations**: Autostart ("just a very long KET point; could be short and clear like EKET", 2026-06-17).
- **Billing and subscriptions**: eKET ("won't let me stop the subscription", 2026-10-08; "charged without confirmation", 2026-10-06; "no weekly plan, about 18 €/month", 2026-10-07), RoboKET ("renewed without asking", 2026-07-17; "charged 3 times", 2026-04-18), ketbilietai ("bought 14 days, got nothing", 2025-07-15), Autostart ("charged, nothing works", 2025-11-14).
- **App bugs / won't open**: ketbilietai ("everything broke after I bought credits", 2026-07-22; "solved Questions not saved, learning mode doesn't work", 2026-06-22), Autostart ("spinner, never loads", 2026-06-18; "app is stuck", 2026-08-13), eKET ("freezes", 2025-10-31; "can't see teacher's answer", 2026-04-10).
- **Ads and marketing fatigue**: eKET ("your ads spam the whole internet", 2026-06-10; "cringe AI ads", 2025-11-08), Autostart ("TikTok ads say it's the best, it isn't", iOS review).
- **Lost progress**: Autostart (a long test restarts if you close the app), ketbilietai (can't see an earlier test's answers after closing).
- **"It's paid"**: Autostart (several 1★), ketbilietai ("could be free").

---

## 4. Per-competitor details

### 4.1 ketbilietai.lt: market leader

- **Owner**: UAB "DrivingEd", Kaunas ([site footer](https://www.ketbilietai.lt/nemokamas-ket-testas/)). Running since 2008. Claims "513,000+ drivers prepared here" and "1,484 registered in the last 10 days" ([home, EN](https://www.ketbilietai.lt/en/ketbilietai-tests)).
- **Linked sites (probably same network, owner UNCONFIRMED)**: [ketonline.lt](https://www.ketonline.lt/) (KET rules text, PDF, "Ask AI" box; its "test" link goes to ketbilietai) and [ketkursai.lt](https://ketkursai.lt/) (online theory course: B category 29 € for 60 days, audio-only 19 €). The ketbilietai driving-school page sends teachers to log in at ketkursai.lt ([source](https://www.ketbilietai.lt/mokykla/ket-testai-vairavimo-mokykloms/)), and ketbilietai's explanations link to ketkursai.
- **Features**: mock exam (30 min timer, number grid, finish screen with "review mistakes"), free test, road-signs test, situations test, new-rules test, bicycle/e-scooter test, explanations with KET point, "ask a teacher", daily "best results" leaderboard, asks for your exam date after a test, LT/EN/RU/UK/DE/PL on web. The app is Lithuanian only. ([home, EN](https://www.ketbilietai.lt/en/ketbilietai-tests), [English page](https://www.ketbilietai.lt/testai/driving-theory-test), [free test](https://www.ketbilietai.lt/nemokamas-ket-testas/))
- **Smart features**: app says "AI analyses your results, progress and learned topics; a chart shows your readiness and when to go to Regitra" ([App Store](https://apps.apple.com/lt/app/ketbilietai/id1571290796)). "If you answer a Question correctly at least twice in a row, you will not be asked it again"; "test from unlearned Questions only"; light/dark theme ([Google Play](https://play.google.com/store/apps/details?id=lt.ketbilietai.bendras&hl=en)).
- **Pricing** ([payments page](https://www.ketbilietai.lt/mokejimai/)): monthly subscription **15.50 €/month** (shown as reduced from 29 €), auto-renews every 30 days, cancel any time. Or day credits: **1 day 2 €**, **7 days 1.29 €/day (= 9.03 €)**, **14 days 1.07 €/day (= 14.98 €)**. "1 credit = 24 hours; you pay only for days you actually solve tests; unused credits stay valid." All categories and languages are included. App prices: 1 day 1.99 €, 7 days 8.99 €, 14 days 14.99 € ([App Store](https://apps.apple.com/lt/app/ketbilietai/id1571290796)). Driving schools buy credits or codes at **1/5 of the learner price** and may resell them ([schools page](https://www.ketbilietai.lt/mokykla/ket-testai-vairavimo-mokykloms/)).
- **Free**: about 200 Questions "with explanations, without registration" ([free test](https://www.ketbilietai.lt/nemokamas-ket-testas/)). I confirmed that the explanation shows in the mistake review after a free test.
- **Mobile (my test)**: the home page is light (59 requests, about 170 KB measured, load about 2.2 s). The cookie banner covers about 2/3 of the phone screen on first visit. It loads a Google ads script (pagead2.googlesyndication.com). The question screen is clean: big image, pill-shaped Options, timer, 30-number grid, sticky prev/next bar. In exam mode there is **no feedback until you finish**, and explanations are on a separate "mistakes" screen. Some page titles have broken Lithuanian letters (an SEO detail).
- **Recent additions**: new app version 2.x (App Store "What's new": version 2.0.14, a few hours before my check). Reviewers in June–July 2026 report bugs "after the recent update". Facebook login removed (an earlier Google Play "What's new" note, date UNCONFIRMED; [Google Play](https://play.google.com/store/apps/details?id=lt.ketbilietai.bendras&hl=en)). AI readiness chart (praised in a 2026-05-19 iOS review). More web languages (DE, PL, UK in menu). Content "updated 2026-09-30".
- **Ratings and complaints**: see the tables above. Main complaints: mismatch with the real exam, bugs after the update, a purchase not delivered, can't review old tests, English missing in the app ([iOS reviews](https://apps.apple.com/lt/app/ketbilietai/id1571290796)). Google Play reviews were pulled through SerpApi (Google Play product engine), sorted by newest.

### 4.2 eket.lt (eKET)

- **Owner**: UAB 4MARK, Vilnius ([Google Play](https://play.google.com/store/apps/details?id=com.eket.eket&hl=en)). Site since 2021. Claims "2800 Questions" ([home](https://eket.lt/)) and "9/10 pass first time" ([B plans](https://eket.lt/planai/tests/B,%20B1/)).
- **Features**: Regitra-style mock exam, situation Questions, choose by topic / difficulty / mistakes / unseen, study mode, "detailed explanations for each Question and each Option with the exact KET point", live online lectures, teacher Q&A, KET course, first-aid certificate, "Regitra exam acceleration" (get a date faster), driving-school catalogue with paid reservations ([App Store](https://apps.apple.com/us/app/eket-bilietai-2026-ket-testai/id6747953300), [terms](https://eket.lt/naudojimosi-taisykles/)).
- **Smart features**: "Learning wizard: a smart algorithm that builds tasks from your progress and fills knowledge gaps". The FAQ says weak topics are repeated more often ([B plans FAQ](https://eket.lt/planai/tests/B,%20B1/)). In a review reply, eKET says learners should reach at least 90 % "progress" before the Theory Exam ([Play review reply, 2026-03-17](https://play.google.com/store/apps/details?id=com.eket.eket)).
- **Pricing** ([B plans](https://eket.lt/planai/tests/B,%20B1/)): **7 days 1.31 €/day (≈ 9.17 €)**, struck-through 1.70 €/day. **31 days 0.56 €/day (≈ 17.36 €)**. **62 days 0.48 €/day (≈ 29.76 €)**, labelled "most popular", with a free e-book "worth 25 €". "Extra administration fees depending on payment method." Contradiction: the plan card lists lectures and consultations in the 7-day plan, but the FAQ says the 7-day plan has **tests only**. A 30-day money-back guarantee is shown. The FAQ promises a refund if you fail the first Theory Exam, "see the terms", but I could **not find the conditions** in the [terms page](https://eket.lt/naudojimosi-taisykles/) (UNCONFIRMED). App subscriptions auto-renew ([terms 3.7](https://eket.lt/naudojimosi-taisykles/)). App prices (US storefront, USD): 7 days 6.95–8.95, 31 days 12.95–14.99, 62 days 24.90–24.95, course + tests 39.90–49.99 ([App Store](https://apps.apple.com/us/app/eket-bilietai-2026-ket-testai/id6747953300)).
- **Free**: "200 free Questions" demo. Pressing "Explanation" opens a pop-up: "this feature is only for EKET members" (my test).
- **Mobile (my test)**: the heaviest site. Home page: 251 requests, about 2.6 MB, about 24,000 px tall on a phone. Many trackers: TikTok, Facebook, Google Ads, Sentry, Elfsight, OpenAI. It sets `user-scalable=no`, so you **cannot pinch-zoom**. Every page has a top "SPECIAL OFFER" countdown (about 18 days left). The pricing page shows "Only 4 left" and "7 people buying now" for a digital product. In the free test, an upsell box fills the top quarter of the screen above the Question, and the page under the Question goes on for about 8,000 px (reviews, pricing). No instant feedback.
- **Recent additions**: iOS app (version 1.0.49 on Aug 30; launch date UNCONFIRMED, probably 2025), "learning wizard", live lectures, exam-acceleration service, driving-school catalogue and reservations, AI-generated summary of Google reviews on the pricing page. Content "updated 2026-10-12".
- **Ratings and complaints**: Play 4.5 (293 reviews). Site claims Google rating 5.0 from 1,744 or 1,872 reviews (the number differs between pages). Complaints: subscription can't be stopped / charged without confirmation / no refund, "not like Regitra", logic errors in Questions, too many ads, freezes ([Google Play](https://play.google.com/store/apps/details?id=com.eket.eket)).

### 4.3 vairavimotestai.lt

- **Owner**: not stated on the pages I read (UNCONFIRMED). Web only; no app found.
- **Features**: A, AM, B, C, D, T and topic tests, "3800+ Questions", KET lessons and a study plan ("tests check knowledge, they don't give it; learn the theory first"), private teacher consultations (50 or 100 per month in bigger plans), instructor test (SEAKĮ 2026), detailed statistics ([home](https://vairavimotestai.lt/), [pricing](https://vairavimotestai.lt/kainos), [EN home](https://vairavimotestai.lt/?lang=en)).
- **Smart features**: "AI adapts to each learner's pace and results"; "chooses the most effective strategy and the most relevant Questions and topics". Details UNCONFIRMED (I did not log in).
- **Pricing** ([pricing](https://vairavimotestai.lt/kainos)): you buy a "solving code" with hours of answering time, valid until used up. **10 h: 9.49 €**. **25 h + lessons + 50 consultations: 17.99 €** (struck-through 29.99). **50 h + lessons + 100 consultations: 24.49 €** (struck-through 49.99). "Time counts only while answering." There is a "-51 %" sale countdown (about 3–6 hours left when checked). 30-day money-back guarantee (conditions UNCONFIRMED). No account needed: you log in with the code.
- **Free**: demo with "100 repeating Questions", no registration.
- **Mobile (my test)**: fast first paint (DOMContentLoaded about 0.3 s) but about 1.9 MB in total. A full-screen cookie wall on first visit, and the home page is about 17,700 px long. The question screen is readable: centred text, checkbox Options, timer, "finish test" button.
- **Recent additions / marketing**: shows "Regitra statistics": first-attempt B Theory Exam pass rate fell from 55.8 % (2015) to 38.3 % (2025). This is their claim and I did not check it against Regitra (UNCONFIRMED). "Live activity" widget ("111 learners solving now"). Google 5/5 from 264 reviews (self-reported).

### 4.4 RoboKET: the most modern rival

- **Owner**: Robo code MB. The same developer makes driving-theory apps for Spain (TraficoTest) and Italy (SuperQuizPatente) ([App Store](https://apps.apple.com/lt/app/roboket-ket-tests-lithuania/id6479808767)).
- **Features**: 1700+ "Regitra-style" Questions, "official illustrated theory" in 800+ cards, mock exam (30 Questions / 30 min / max 6 mistakes), community chat, rewards, LT and EN, "no ads", dark mode, EV calculator ([site](https://roboket.lt/)).
- **Smart features** ([App Store](https://apps.apple.com/lt/app/roboket-ket-tests-lithuania/id6479808767)): **pass probability** recalculated after every test ("at a stable 90 % it's safe to register"). **Daily plan**: enter your exam date and it spreads 10–20 min of study per day. Mistake statistics by topic.
- **Pricing** ([site](https://roboket.lt/)): **1 week 5.99 € (0.86 €/day)**, 2 weeks 9.99 €, 1 month 15.99 €, 3 months 29.99 € (0.33 €/day, "one of the best prices in Lithuania"). Site says "no commitment". The App Store lists them as subscriptions (5.99 / 15.99 / 29.99). **Money-back**: "if you reached 90 %+ pass probability and failed the first Theory Exam".
- **Free**: demo tests without registration. The landing page itself contains a working mock exam.
- **Mobile (my test)**: the lightest site (21 requests, about 370 KB). Modest cookie bar. You can start a real-format exam straight on the landing page. Answering gives **instant red/green feedback, an inline explanation, and the "Mistakes 1/6" counter updates**, then a big "Next" button. Downside: the explanation I saw mostly repeats the rule text instead of saying why. Emoji-heavy copy. The site loads a Google ads script even though the app says "no ads" (whether ads appear on the web is UNCONFIRMED).
- **Recent additions**: app version 7.2.3 three days before my check; Play updated 2026-10-06. Content "updated 2026-10-12".
- **Ratings and complaints**: iOS 4.8 (312), Play 4.6 (236 reviews, 10K+). Complaints: auto-renewal without asking, charged several times, sign-up email not arriving ([Google Play](https://play.google.com/store/apps/details?id=com.robocodemb.roboket)). Praise: the daily plan and rewards.

### 4.5 Autostart and Kettestai.lt (both APPASTIC MB)

- **Autostart**: [site](https://autostart.lt/), web app at app.autostart.lt, [App Store](https://apps.apple.com/lt/app/ket-bilietai-2026-autostart/id6670372956), [Google Play](https://play.google.com/store/apps/details?id=com.appastic.autostart&hl=en).
  - Features: 1800+ Questions with explanations, all categories, LT/EN/RU/PL/FR/ES, learning statistics, first-aid certificate info. Site claims "110,400+ users".
  - Pricing: weekly and monthly subscriptions that auto-renew. App Store lists **1 week 4.99 € and 9.99 €**, 1 month 9.99 / 14.99 / 19.99 €. Several prices probably means price tests (UNCONFIRMED).
  - Free: "60 Questions and basic features" ([site FAQ](https://autostart.lt/)).
  - Mobile: **UNCONFIRMED**, because the site showed a bot check ("Checking your browser") to my test browser. The app is 90 MB.
  - Complaints: app won't open or spins forever, a long test restarts if you leave, wrong or silly Questions, grammar errors, poor RU translation, explanations are just long KET text, "it's paid", TikTok ads overpromise.
  - Recent: version 3.9 (Aug 10) "updated to 2026 KET". Strong TikTok presence (@autostart_ket_testai).
- **Kettestai.lt**: [site](https://kettestai.lt/), [App Store](https://apps.apple.com/lt/app/kettestai-lt-ket-bilietai/id6801686291).
  - The **same company** (APPASTIC MB, same address and phone) launched this second brand. The iOS app's first reviews are from 2026-09-11, and it reached **#9 Education**. The page title includes "KETbilietai", which looks like it targets the market leader's name in search.
  - Features: mock and topic tests, explanations, statistics, chat.
  - Pricing: 1 week 7.99 or 9.99 €; 1 month 9.99–29.99 € (App Store). Web prices need login (UNCONFIRMED).
  - Mobile: light web home (29 requests, about 430 KB, about 5,500 px). The "best results" list shows the same first name 5–6 times.

### 4.6 KET testai ir teorija (RT Tech): app only

- [App Store](https://apps.apple.com/lt/app/ket-testai-ir-teorija/id6444296388). 1350+ Questions, 730 theory cards with photos, build your own test per topic with the same topic mix as Regitra, saved hard Questions, pass probability, reminders, sounds.
- Pricing: 1 week 3.99 € (list) or 6.99 € (its description), 1 month 14.99 €, auto-renew.
- **Last update 2024-09-21**, so it looks unmaintained. All visible reviews are from Dec 2022. A good early example of the "theory cards + probability" idea that RoboKET later polished.

### 4.7 Other players (short)

- **ketonline.lt**: KET rules text, road-sign pages, PDF, translations, "Ask AI" box ([site](https://www.ketonline.lt/), [ask page](https://www.ketonline.lt/klausti/)). Not a test site; it links to ketbilietai for tests.
- **ketkursai.lt**: online theory course with video and audio lessons, 100+ lessons, 60-day access. B category 29 €, A 35 €, A+B 39 €, audio only 19 € ([site](https://ketkursai.lt/)).
- **Alsket (alsket.lt)** and **ARV testai (arvtestai.lt)**: tests sold mainly through driving schools as access codes ([alsket](https://www.alsket.lt/), [arvtestai](https://arvtestai.lt/)). Prices UNCONFIRMED. These matter for our Partner offer: driving schools already have code systems, and ketbilietai lets schools resell its codes at a 5× margin.
- **Regitra's own free trial test**: linked from Regitra's [theory test page](https://www.regitra.lt/en/services/examination/theory-test). It is free and official, and some learners use it to compare apps (an Autostart reviewer suggests it).
- **EasyKET (easyket.lt)**: the site did not respond. It is probably inactive (UNCONFIRMED).

### 4.8 Market facts from Regitra

- Regitra held **136,676 theory exams in 2024**, 11 % more than in 2023 ([Regitra news, 2025-09-29](https://www.regitra.lt/en/news/regitra-nuo-sausio-1-d-teorijos-egzamina-bus-galima-laikyti-papildomomis-es-kalbomis)).
- From 2026-01-01 the Theory Exam is offered in Lithuanian, English, Polish, Spanish and French. **Russian was dropped**, and German is planned ([Regitra theory test page](https://www.regitra.lt/en/services/examination/theory-test), [news 2025-12-08](https://www.regitra.lt/naujienos/regitra-kviecia-teorijos-egzamina-laikyti-naujomis-kalbomis)). ketbilietai and Autostart still advertise Russian. Not relevant to KETGO now (Lithuanian only).

---

## 5. Notes for other tickets on the map

- **#9 What "smart" means at launch**: these are now table stakes: topic practice, mistakes-only practice, "learned" retirement (ketbilietai: 2 correct in a row), and a readiness or pass-probability score (ketbilietai, RoboKET, RT Tech). Differentiators still open: true spaced repetition over days, and a daily plan from the exam date (only RoboKET has one). Warning: a readiness score that says "ready" and then the learner fails is the number 1 source of 1★ reviews. Ours must be cautious and explain itself.
- **#11 Question screen on a phone**: the benchmark is RoboKET's flow: instant feedback in practice, inline explanation, a "mistakes x/6" counter in exam mode, a big Next button, no sign-up to start. Avoid eKET's upsell above the Question and ketbilietai's separate "review mistakes" step. Practice mode should give feedback at once; exam mode only at the end, like the Theory Exam.
- **#12 Look and feel**: the market looks like this: ketbilietai is clean blue, eKET is dark navy + yellow with countdown banners, RoboKET is teal with many emoji, vairavimotestai is red/blue. Room exists for calm, fast and honest: no fake urgency, no cookie wall if we can avoid it, allow pinch-zoom.

## 6. New open questions found

1. **Cookie banner**: can KETGO run without non-essential cookies (and so with no banner)? This affects the analytics choice in "How we know the beta works" and the GDPR work.
2. **Readiness score calibration**: in the beta we have no real pass/fail data. Should we ask learners to report their Theory Exam result, to calibrate later? (Competitors use "pass rates" heavily in marketing.)
3. **Later pricing model** (out of scope now, recorded for later): day-credit one-off passes (ketbilietai), hour-based codes (vairavimotestai), or auto-renew subscriptions (RoboKET, Autostart, eKET). Auto-renew drives many 1★ reviews. Money-back promises are common (RoboKET, eKET, vairavimotestai).
4. **Partner competition**: ketbilietai sells school codes at 1/5 of the learner price for resale, and Alsket/ARV are school-code systems. A free personal link may not be enough motivation for driving schools. Check this when the Partner ticket is opened.
