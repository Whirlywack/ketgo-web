# Accounts: phone storage, sign-up friction and privacy rules (2026)

Research for issue [#23](https://github.com/Whirlywack/ketgo-web/issues/23). It feeds the decision in [#6 Accounts and saving progress](https://github.com/Whirlywack/ketgo-web/issues/6). Checked on 2026-10-14.

Words like **Lesson**, **Theory Exam** and **Mock Exam** mean what `GLOSSARY.md` says.

This is research, not legal advice. Before launch, a lawyer should check the privacy part (section 5).

## How to read the evidence labels

| Label | Meaning |
|---|---|
| **strong** | An official primary source says it directly (law text, Apple/WebKit, Google/Chrome, MDN, the court). Or a good randomised study in a setting close to ours. |
| **moderate** | A primary source, but indirect, old, or one study / one company. Or a clear step of reasoning from strong facts. |
| **weak** | Industry or vendor numbers without a clear method, news reports, or our own guess. |
| **none** | We found nothing. |

**How we searched.** Browser facts come from WebKit, Apple, Chrome, web.dev and MDN pages. Law comes from e-seimas.lrs.lt, e-tar.lt, VDAI, EDPB and the EU Court. For peer-reviewed work on sign-up we tried the Consensus MCP first, but its monthly quota was used up ("You've used all 30 searches this month; resets on November 1st"). So we searched Google Scholar (through SerpApi), OpenAlex and Semantic Scholar instead.

## Short answer

| Question | Answer | Evidence |
|---|---|---|
| Does Safari delete localStorage/IndexedDB after 7 days? | **Yes.** After **7 days of Safari use** with no tap, click or typing on the site, Safari deletes localStorage, IndexedDB, service-worker data and cookies made by JavaScript. Any tap on KETGO starts the 7 days again. Cookies set by our **server** are not deleted by this rule. | strong |
| Does it hit a site the learner opens often? | **No**, as long as the learner taps something at least once in every 7 days of Safari use. A learner who takes a two-week break while still using Safari for other things **loses** local-only progress. | strong |
| Does it hit Home Screen web apps? | **No.** Home Screen web apps are exempt. | strong |
| Safari → Home Screen: does progress carry over? | **Only cookies carry over.** Since iOS 17.2, cookies are copied **once**, at the moment of "Add to Home Screen". localStorage and IndexedDB are **not** copied. After that, nothing is shared. Since iOS 26, every site added to the Home Screen opens as a web app by default. | strong |
| Android Chrome: when does it delete? | Only when the phone or browser is **running out of space**. It deletes the least recently used site first. We found no inactivity rule like Safari's. | strong (no inactivity rule: moderate) |
| Does `navigator.storage.persist()` stop that? | **Yes on Chrome**, if granted. Chrome grants it **silently** based on use (installed, bookmarked, much used, or notifications allowed). After that, only the user can delete the data. On Safari it is granted mainly to Home Screen web apps. | strong |
| Web push | **iPhone: only from a Home Screen web app** (iOS 16.4+), and only after a tap. **Android: works in the browser.** Chrome data: about **23 %** of notification prompts on Android were accepted (study published 2021). | strong / moderate |
| iOS vs Android in Lithuania | **Android 70.4 %, iOS 29.6 %** of mobile web page views (StatCounter, September 2026). | moderate |
| Sign-in that survives "email opens elsewhere" | A **6-digit email code** works everywhere, because the learner types it where they started. A **magic link** breaks in the iPhone Home Screen web app: it opens in Safari, which has separate storage. | moderate |
| Published completion rates | Passkeys: 93 % vs 63 % for other methods (FIDO Alliance, 2025). **No neutral numbers exist for email code vs magic link.** | moderate / none |
| Required vs later sign-up | Forced sign-up loses people (Baymard: 18 % of shoppers who gave up said "the site wanted me to create an account"). Duolingo says letting people do a Lesson before sign-up raised daily users by about 20 %. **No peer-reviewed study in learning apps.** One large e-commerce experiment found an **optional** early sign-up request raised sign-ups by 58 % with no loss of buyers. | weak–moderate |
| Is a random learner ID + answer log personal data? | **Yes.** Treat it as personal data (pseudonymous). GDPR applies from day one, even without an email. | strong |
| Does keeping the ID on the phone need cookie consent? | **Probably not**, if the ID is used **only** to save the progress the learner asked for. That fits the "strictly necessary" exemption in Lithuanian law (ERĮ Art. 73(4)). Using it for analytics would need consent. VDAI reads "necessary" narrowly, so tell the learner clearly. | moderate |
| What changes when an email is added? | A direct identifier is added. We need a legal basis (contract or consent), a privacy notice, a retention period and a delete option. Marketing or "come back" emails need opt-in. Lithuania's consent age is **14**, but it only matters if consent is our legal basis. | strong (text) / moderate (how it applies) |
| Minimum age for the category-B Theory Exam | Licence at **18**. In practice the Theory Exam is from **17**: the driving-school course must end at 17 or older, and you need the course to sit the exam. **Nobody under 14 sits it. Under 16 is very unlikely.** Many learners will be 16–17, so minors. | strong (law) / moderate (the "from 17" step) |

---

## 1. Browser storage on phones

### 1.1 Safari's 7-day rule (Intelligent Tracking Prevention, ITP)

**What it deletes, and when.** WebKit's tracking-prevention page [S1]:

> "ITP deletes all cookies created in JavaScript and all other script-writeable storage after 7 days of no user interaction with the website. The latter storage forms are: IndexedDB, LocalStorage, Media keys, SessionStorage, Service Worker registrations and cache"

The 2020 announcement [S2] says it counts **days of Safari use**, not calendar days: "after seven days of Safari use without user interaction on the site."

**What counts as a visit.** "User interaction is a user click, tap, or keyboard entry on a website ... Scrolling is not considered user interaction." [S1]

- So a learner who opens KETGO and answers one Question keeps their data. The 7 days start again. **strong**
- A learner who stops using KETGO for 7 days of Safari use loses all local-only progress. **strong**
- Days when Safari is not opened at all do not count. **strong** [S2]

**Server-set cookies survive.** The rule names "cookies created in JavaScript", not cookies set by the server. A WebKit engineer confirmed this for web apps in WebKit bug 237350: "Non CNAME-cloaked server-set cookies and HTML storage should not be deleted" [S3]. **strong**

- **One trap:** ITP caps cookies at 7 days if they come from a server that looks like a third party hiding behind our domain ("CNAME cloaking" or "third-party IP address cloaking") [S1]. So the cookie should be set by KETGO's own host, not by an auth service on another provider's domain. WebKit does not publish how it detects the IP case. **moderate**

**Still in force?** Yes. The rule is on WebKit's current tracking-prevention page [S1]. The Safari 26.0 and 27.0 release notes (Sept 2025 and Oct 2026) list no change to it [S4][S5]. **strong** (that it is in force) / **moderate** (that nothing changed: we read the notes' relevant parts, not every line)

**Does `persist()` save a Safari tab?** Probably not. Safari 17 says an origin "might be excluded from eviction if ... its storage is in persistent mode". But WebKit "grants a request based on heuristics like whether the website is opened as a Home Screen Web App" [S6]. Those are already exempt. We found no source saying a normal Safari tab gets `persist()` granted, or that it beats the 7-day rule. **weak** (unconfirmed)

### 1.2 Home Screen web apps on iPhone

**Exempt from the 7-day rule.** "The first-party domain of home screen web applications is exempt from ITP's 7-day cap on all script-writeable storage" [S1]. **strong**

- Small exception: cookies made by JavaScript are still capped at 7 days inside web apps. localStorage and IndexedDB are not deleted [S3]. **strong**

**Storage is separate from Safari.** Apple, WWDC23: "Home Screen web apps have a standalone, app-like experience on iOS, with separate cookies and storage from the browser." [S7] **strong**

**What is copied when the learner taps "Add to Home Screen" (iOS 17.2 and later).** WebKit, Safari 17.2 release notes [S8]:

> "Whether a user is in Safari, Safari View Controller, or another browser on iPhone or iPad, when they tap 'Add to Home Screen' and create a web app, the cookies are copied over, including the information about login state. This will only work if the authentication state is stored within cookies. No other kind of local storage is copied over. After a user adds a web app to the Home Screen or Dock, no other website data is shared"

So, for a learner who starts in Safari and then adds KETGO to the Home Screen:

| Where KETGO keeps the learner ID / progress | Carries over? |
|---|---|
| Only in localStorage or IndexedDB | **No.** The web app starts empty. The learner sees a fresh start. **strong** |
| ID in a cookie, progress on our server | **Yes, once.** The web app gets a copy of the cookie, so it finds the same progress on the server. **strong** (mechanism) / **moderate** (we did not test it on a phone) |
| Anything changed after the moment of adding | **No.** From then on Safari and the web app are two separate worlds. If the learner keeps using both, they split into two learners unless they sign in. **strong** |

**iOS 26 change.** "By default, every website added to the Home Screen opens as a web app." The learner can switch off "Open as Web App" to get a plain bookmark [S4]. So in 2026 almost every learner who adds KETGO to the Home Screen gets the separate web-app storage, even without a manifest file. **strong**

**EU note.** In the iOS 17.4 beta (Feb 2024) Apple stopped Home Screen web apps in the EU, then reversed this before release [S9]. We found nothing newer that removes them in the EU. **moderate** (Apple's own statement was quoted by news sites; we could not open Apple's page)

### 1.3 Android Chrome

**Default is "best effort".** MDN: "Best-effort data persists as long as the origin is below its quota, the device has enough storage space, and the user doesn't choose to delete the data via their browser's settings." [S10] **strong**

**When Chrome deletes.** When the device is low on space, or all browser data is over the browser's limit. "The data from the least recently used origin is deleted" first [S10]. web.dev: "Chromium-based browsers will begin to evict data when the browser runs out of space." [S11] **strong**

**No inactivity rule.** MDN lists "proactively, for origins that aren't used regularly" as a trigger "which happens only in Safari" [S10]. We found no Chrome page that says "never". **moderate**

**Space.** A site can use up to 60 % of the disk in Chrome [S10][S11]. Not a concern for KETGO. **strong**

**`navigator.storage.persist()`.**

- Chrome gives no pop-up. It decides from the user's history with the site: "Safari and most Chromium-based browsers ... automatically approve or deny the request based on the user's history of interaction with the site and do not show any prompts to the user." [S10] **strong**
- The signals Chrome uses: site engagement, "Has the site been installed or bookmarked?", "Has the site been granted permission to show notifications?" [S12] **strong** (the page is from 2020, but MDN agrees)
- Once granted, data is "only evicted, or deleted, if the user chooses to" [S10]. **strong**
- Firefox shows a pop-up asking the user [S10]. Samsung Internet: no documentation found. **none**

**Installed web app vs Chrome tab on Android.** We did not find a primary page saying whether an installed KETGO web app shares storage with the same site in a Chrome tab. **none** (test on a device)

### 1.4 What this means for saving progress (facts, not a decision)

- Progress kept **only on the phone** is lost on iPhone Safari after a 7-day break, and does not move into the Home Screen web app. **strong**
- A **server-set, first-party cookie** with a random learner ID survives Safari's 7-day rule, and is copied into the Home Screen web app when it is added. Progress stored on the server under that ID follows it. **strong** (mechanism) / **moderate** (not tested)
- The learner can still lose the ID: by clearing browser data, by using a second browser or phone, or by using Safari and the web app side by side after adding it. Only some kind of sign-in fixes those cases. **strong**

---

## 2. Web push in 2026

### iPhone

- **Only Home Screen web apps.** Apple: "Add web push to Home Screen web apps in iOS 16.4 or later and Webpages in Safari 16 for macOS 13 or later." [S13] There is no web push in a Safari tab on iPhone. **strong**
- **Only after a tap.** The web app "can request permission to receive push notifications as long as that request is in response to direct user interaction — such as tapping on a 'subscribe' button" [S14]. **strong**
- Declarative Web Push (no service worker needed) arrived in iOS 18.4 "for web apps added to the Home Screen" [S15]. **strong**
- We found no change in Safari 26 or 27 that brings push to Safari tabs [S4][S5]. **moderate**
- So on iPhone a learner must (1) add KETGO to the Home Screen, (2) open it from there, (3) tap a button, (4) say yes. We found no published data on how many iPhone users do all four. **none**

### Android

- Web push works in the normal browser. It needs an active service worker, not an install. MDN lists the Push API as available in all main browsers since March 2023 [S16]. **strong** (that it works in the browser tab is standard; no page states "no install needed" in those words)
- From Chrome 155 (announced July 2026), Chrome changes the Android prompt to a lighter, non-blocking one that "will time out when the non-blocking prompt expires". A timed-out prompt returns `default`, not `granted`. Users can turn notifications on later from Site Controls [S17]. **strong**
- Chrome automatically puts sites with very low accept rates into a quieter prompt [S18], and since October 2025 it removes the notification permission of sites that send many notifications the user ignores ("Less than 1% of all notifications receive any interaction"). "This feature does not revoke notifications for any installed web apps." [S19] **strong**

### How many people turn push on

- **Chrome's own data** (peer-reviewed, USENIX Security 2021, more than 40 million users and 100 million prompts): notification prompts had "only a 12% grant rate on desktop and 23% grant rate on Android" [S20]. The data is from about 2020. **moderate** (strong study, old data)
- Vendor numbers say about 5–10 % of web visitors subscribe (OneSignal, PushOwl, etracker). We did not see their methods. **weak**

### iOS vs Android in Lithuania

StatCounter, mobile operating system share in Lithuania, **September 2026: Android 70.4 %, iOS 29.59 %** [S21]. StatCounter counts page views on sites that use its tracker, not people. **moderate**

So about 3 in 10 KETGO learners are likely on iPhone, where push needs the Home Screen step.

---

## 3. Signing in on a phone

### Which methods survive "the email opens somewhere else"

The problem: the learner asks to sign in inside the Home Screen web app (or in Chrome), then opens the email in the Mail or Gmail app. Tapping a link there opens the **default browser**, not the web app.

| Method | Works when the email opens in another browser or outside the web app? | Why | Evidence |
|---|---|---|---|
| **6-digit code by email** | **Yes.** | The learner reads the code and types it where they started. No link is opened. Code-in-email is also safe from email scanners that "click" links. | moderate (it follows from how it works; Supabase recommends codes for this reason [S22]) |
| **Magic link by email** | **Often no.** | On iPhone the web app has separate storage from Safari [S7], so the link signs the learner in to Safari, not the web app. With the PKCE method, "the code exchange must be initiated on the same browser and device where the flow was started" [S23], so it can fail outright. Some email scanners open links first and use up the one-time link [S22]. | strong (each part) / moderate (the combined effect; not tested) |
| Magic link on **Android** with KETGO installed | **Maybe.** | An installed web app registers "intent filters for all URLs within the scope of the app", so links can open the app [S24]. That page is from 2017. Gmail often opens links in its own in-app browser. | weak (test on a device) |
| **Google / Apple sign-in** | **No email step**, so the problem does not arise. | But on iPhone, a Home Screen web app opens outside pages (like the Google sign-in page) in an in-app Safari view [S7]. We found no Apple page on whether the sign-in result returns to the web app. | weak (test on a device) |
| **Passkeys** | **No email step.** | Synced by iCloud Keychain or Google Password Manager. We found no primary source on passkeys inside iPhone Home Screen web apps. A first-time sign-up and a lost phone still need a fallback, usually email. | weak |

**Code autofill.** iOS 17 can fill codes from Apple Mail into Safari, according to Apple's feature list as reported by news sites. Developers report it does not always work, and we found no Apple developer documentation for email codes [S25]. `autocomplete="one-time-code"` is the standard field hint [S8]. **weak**

### Published completion rates

| Method | Number | Who published it | Evidence |
|---|---|---|---|
| Passkeys | 93 % sign-in success, vs 63 % for "other methods" (which mixes social login, MFA and one-time codes) | FIDO Alliance Passkey Index, Oct 2025; survey of 9 member companies (Amazon, Google, Microsoft, PayPal, TikTok and others) [S26] | moderate (industry) |
| Passkeys vs passwords | 98 % vs 32 % success | Microsoft, Dec 2024; no definition or sample given [S27] | weak–moderate (vendor) |
| Google sign-in / One Tap | Reddit: sign-ups +50 % with the Google button, one-tap added more | Google case studies, picked by Google [S28] | weak (vendor) |
| **Email code vs magic link** | **No neutral published numbers.** | Only vendor blogs, which admit there is no shared benchmark | **none** |

So we will have to measure our own sign-in funnel.

---

## 4. Sign-up friction

**What we looked for:** studies comparing "sign up first" with "sign up later" or "sign up optional", ideally in learning apps, measuring activation and retention.

### Peer-reviewed

- **Huang, Mojumder, Sun, Lv and Golden (2021), *Information Systems Research* 32(3):914–931** [S29]. A large randomised field experiment with a US online shop. New visitors were randomly split. One group got a sign-up **request** at the start of their visit, on top of the usual one at checkout. The other group got only the checkout one. The authors set their request apart from a hard wall, where users must leave if they do not register.
  - Result: "users in the treatment group, on average, are 58.08% relatively more likely to register". The early request "does not impact customer conversion in the short-term".
  - People who signed up because of the early request later bought more: 10.89 % more likely to buy, 13.22 % more revenue.
  - Meaning for us: an **early, skippable** ask can get more sign-ups without losing people. It says nothing about a **forced** wall.
  - Evidence: **moderate** (strong design, but shopping, not learning)
- **Learning apps:** we found **no** peer-reviewed study on sign-up timing. **none**
- **"Ask after the first win costs less":** no direct peer-reviewed test found. **none** (direct)
  - There is related lab and field evidence that people who already have some progress try harder to finish, the "endowed progress effect" [S30]. It is indirect. **weak**

### Industry (labelled as industry)

- **Baymard Institute** (US online shoppers, list updated Sept 2025): **18 %** of shoppers who gave up at checkout said "The site wanted me to create an account" [S31]. **moderate** (big survey, but shopping and self-reported)
- **Duolingo**, Gina Gotthilf (then VP of Growth), First Round Review, 2017 [S32]:
  - "by allowing users to experience Duolingo *without* signing up — do a lesson, see the set of skills that you can run through — we could increase those sign-up metrics significantly ... Simply moving the sign-up screen back a few steps led to about a 20% increase in DAUs."
  - Later they added three optional "soft walls" (with a "Later" button) and a "hard wall, after several lessons". "Without those soft walls priming a sign-up as they're ignored, those hard walls perform significantly worse." Those changes added 8.2 % more daily users.
  - Evidence: **weak–moderate** (first-hand and in a learning app, but one company, no published method)

### Bottom line

- Forcing sign-up **before** any value loses people. **moderate** (industry only, but it all points one way)
- Letting people do a Lesson first, then asking, worked for Duolingo. **weak–moderate**
- An **optional** ask can still be shown early without harm. **moderate** (one e-commerce RCT)
- Nobody has published this for driving-theory or learning web apps. **none**

---

## 5. Privacy (GDPR and Lithuania)

### 5.1 Is a random learner ID + answer log on our server personal data?

**Yes. Treat it as personal data (pseudonymous data).** **strong**

- GDPR Art. 4(1): a person is "identifiable" if they "can be identified, directly or indirectly, in particular by reference to an identifier such as ... an online identifier" [S33].
- Recital 30 names "cookie identifiers" and says they leave traces which, "when combined with unique identifiers and other information received by the servers, may be used to create profiles ... and identify them" [S33]. Our server also receives the IP address with every request.
- Recital 26: pseudonymised data that "could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person" [S33].
- EU Court, *EDPS v SRB* (C-413/23 P, 4 Sept 2025): pseudonymised data may stop being personal data **for a recipient** who cannot re-identify anyone. But "the identifiable nature of the data subject must be assessed at the time of collection of the data and from the point of view of the controller" [S34]. KETGO is the controller, so for us it is personal data.

Even without an email, GDPR applies: we need a legal basis, a short privacy notice, a retention period, and a way to delete a learner's data.

### 5.2 Does keeping the ID in the browser need cookie consent?

**The rule.** Storing or reading anything on the learner's phone needs consent, unless it is strictly necessary for a service the learner asked for. In Lithuania this is the Law on Electronic Communications (ERĮ, IX-2135, new wording from 1 Dec 2021), **Art. 73(4)** [S35]. It ends with the exemption for storage that is needed "būtinais atvejais teikti informacinės visuomenės paslaugas, kurias užsako abonentas ar faktinis viešųjų elektroninių ryšių paslaugų gavėjas" (*where necessary to provide an information society service the user asked for*). **strong**

- The old "Art. 61(3)" no longer applies. **strong** [S35]
- **VDAI** (the State Data Protection Inspectorate) supervises this article, not RRT [S35]. **strong**

**localStorage counts, not just cookies.** The EDPB says the rule covers information stored in the browser "(such as cookies, local storage, WebSQL ...)" once it, "or any derivation of this information", leaves the device. Sending a unique identifier from the browser to us is a "gaining of access", so the rule applies [S36]. **strong**

**Does the learner ID fit the exemption?** Probably yes, if it is used only for saving progress. **moderate**

- The EU's 2012 guidance (WP29 Opinion 04/2012) gives two tests: the storage is needed for a feature, and the user explicitly asked for that feature. It says "the user may explicitly ask the service to remember some information from one session to another, which requires the use of persistent cookies" [S37]. Saving your progress in a practice app fits that.
- **Caution 1:** the same opinion says long-lived login cookies and long-lived preference cookies are **not** exempt unless the user is told and chooses (e.g. "remember me (uses cookies)") [S37]. So be explicit: tell learners on screen that KETGO saves their progress on this phone.
- **Caution 2:** VDAI reads "necessary" narrowly. Its 2025 cookie review warns against sites calling cookies "necessary" ("kaip „būtinieji“ yra klasifikuojami slapukai, kurių diegimui iš tikrųjų reikalingas atskiras ... sutikimas"). It puts "functional" cookies (language, appearance) in a separate group from necessary ones, and does not say they are exempt [S38]. **strong** (what VDAI wrote) / **moderate** (how it applies to us)
- **Not exempt:** using the same ID for analytics, A/B tests or ads. Those need opt-in consent. VDAI: "Teisėtas interesas nėra tinkamas teisinis pagrindas" (*legitimate interest is not a valid basis*) for non-necessary trackers. Accept and Reject must be equally easy [S39]. **strong**
- We found **no** VDAI text that mentions localStorage by name [S38]. **none**

### 5.3 What changes when an email is added

**strong** (law text) / **moderate** (how it applies to KETGO)

- **New direct identifier.** An email usually names the person. A leak now hurts more, so security and breach handling matter more.
- **Legal basis.** Two realistic options:
  - **Contract** (GDPR Art. 6(1)(b)): the account is the service the learner signs up for. For learners aged 14–17, the Civil Code says minors "sandorius sudaro, turėdami tėvų arba rūpintojų sutikimą" (*make contracts with their parents' or guardians' consent*). Contracts made without consent are valid if a parent agrees later. They may make "smulkius buitinius sandorius" (*small everyday deals*) alone. Whether a free app account counts as a small everyday deal is **untested** [S40].
  - **Consent** (GDPR Art. 6(1)(a)): in Lithuania a child of **14 or older** can give it alone for online services (ADTAĮ Art. 6) [S41]. Under 14, a parent must consent.
  - **Age 14 matters only if consent is the basis.** All realistic Theory Exam learners are 16 or older (see 5.4), so both are above 14.
- **Privacy notice at sign-up** (GDPR Art. 13): who we are, why we keep the email, how long, the learner's rights, and any processors (e.g. the email-sending service).
- **Retention** (GDPR Art. 5(1)(e)): GDPR sets no number. We must choose one and say it. A useful fact: a Theory Exam pass is valid at most **1 year** [S42]. So a rule like "delete accounts after N months without use" is easy to justify.
- **Delete and export.** Learners can ask to delete or get their data (Art. 15, 17, 20). Build a "delete my account" button.
- **Emails we send:**
  - The sign-in code itself is a service message. It needs no extra consent.
  - Marketing or "come back and practise" emails are direct marketing under the ePrivacy Directive Art. 13, so they need **opt-in**. **moderate** (we did not check the Lithuanian article number)
- **Children.** GDPR Recital 38 says children "merit specific protection". Many of our learners are 16–17, so the notice should be in plain words. **strong**

### 5.4 Minimum age for the category-B Theory Exam

- **Licence: 18.** Road Traffic Safety Law (SEAKĮ) Art. 23(2): "B kategorija – 18 metų" [S43]. **strong**
- **Driving on roads while learning: from 17.** "Mokinys neturi būti jaunesnis daugiau kaip vienais metais negu nustatytas amžius" (*the learner must not be more than one year younger than the driving age*) (SEAKĮ Art. 21(5)) [S43]. **strong**
- **Driving-school course: must end at 17 or older.** The driver-training procedure (order 2B-84): "mokymosi pabaigoje sulaukęs nustatyto amžiaus (B kategorijos – ne jaunesnis kaip 17 metų)" (*at the end of training, has reached the set age; category B: not younger than 17*). Learning with a family instructor is also from 17, after passing the Theory Exam [S44]. **strong**
- **The Theory Exam needs a finished course.** Order 1V-329 point 6 says candidates must have finished a training course. The Theory Exam comes first, the driving test second. A pass is valid for at most 1 year [S42]. 1V-329 sets **no age** for the Theory Exam itself, only for the driving test. **strong**
- **So, in practice: from 17.** No age is written for the Theory Exam, but you need a finished course, and the course must end at 17 or older. Regitra said "Teorijos egzaminą galima laikyti nuo 17 metų" (*the Theory Exam can be taken from 17*) in a 2010 news item [S45]. **moderate** (two strong facts joined by reasoning, plus an old Regitra statement)
- **Under 14 or 16?**
  - **Under 14: no** Theory Exam candidates. **strong**
  - **Under 16: very unlikely.** Someone may start the course or use KETGO early, out of curiosity or for moped (AM, 15) or B1 (16), but they cannot sit the B exam until about 17. **moderate**
  - **Many learners are 17 and still minors.** **strong**
- **Watch:** new consolidated versions of SEAKĮ and the training procedure start on **1 Nov 2026**. Re-check Art. 21 and 23 after that date [S43][S44].

---

## Facts the accounts grilling needs

- iPhone Safari deletes local-only progress after 7 days of Safari use without a tap on KETGO (strong).
- Cookies set by our own server survive that 7-day rule (strong).
- iPhone Home Screen web apps have no 7-day rule, but their storage is separate from Safari (strong).
- When a learner adds KETGO to the Home Screen, only cookies are copied, once; localStorage and IndexedDB are not (iOS 17.2+, strong).
- Since iOS 26, every site added to the Home Screen opens as a separate web app by default (strong).
- Android Chrome deletes site data only when the phone is short of space, and `persist()` can stop even that (strong).
- Lithuanian mobile web is about 70 % Android and 30 % iPhone (moderate).
- iPhone web push only works after Add to Home Screen plus a tap; Android push works in the browser (strong).
- About 1 in 4 Chrome notification prompts on Android were accepted (2021 study, moderate).
- A 6-digit email code works across browsers and apps; a magic link breaks in the iPhone web app (moderate).
- Nobody has published neutral completion rates for email code vs magic link (none).
- Forcing sign-up before any value loses people; Duolingo's "Lesson first, ask later" gave about 20 % more daily users (weak–moderate, industry).
- An optional early sign-up request raised sign-ups 58 % without losing buyers in one large e-commerce experiment (moderate).
- There is no published sign-up-timing study for learning apps (none).
- A random learner ID plus answers on our server is personal data under GDPR, even without an email (strong).
- Keeping that ID on the phone likely needs no cookie banner if it only saves progress the learner asked for; analytics needs opt-in (moderate).
- Adding email means a legal basis, privacy notice, retention period, delete button, and opt-in for any non-sign-in emails (strong).
- Lithuania's digital-consent age is 14, and it only matters if consent is our legal basis (strong).
- The licence is at 18, the Theory Exam is in practice from 17, nobody under 14 sits it, and many learners are minors (strong/moderate).
- A Theory Exam pass is valid for at most 1 year, which gives a natural data-retention horizon (strong).

## Open / unconfirmed (test on real phones or ask a lawyer)

1. On a real iPhone (iOS 26/27): does a server-set login cookie really carry into the Home Screen web app? Does Google sign-in inside the web app return the session to the web app? Do passkeys work inside it?
2. On a real Android phone: do links in Gmail open an installed KETGO web app? Does the installed web app share storage with Chrome?
3. Does `persist()` granted in a Safari tab (if ever) protect against the 7-day rule? No WebKit page says.
4. Would VDAI accept a progress-saving learner ID as "strictly necessary"? No VDAI text mentions localStorage. Lawyer question.
5. Is a free app account a "small everyday deal" a 14–17-year-old can make alone under Civil Code Art. 2.8(2)? Lawyer question.
6. The Lithuanian article for the email-marketing opt-in rule (ePrivacy Art. 13). We did not check it.
7. How many iPhone users add a web app to the Home Screen. We found no data.

## Sources

Browser and platform:

- [S1] WebKit, *Tracking Prevention in WebKit* (page dated 2023-04-27, current): <https://webkit.org/tracking-prevention/>
- [S2] WebKit blog, *Full Third-Party Cookie Blocking and More* (2020-03-24): <https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/>
- [S3] WebKit bug 237350, *Web App Added to Home Screen Cookies Deleted After 7 Days* (WebKit engineer's reply): <https://bugs.webkit.org/show_bug.cgi?id=237350>
- [S4] WebKit blog, *WebKit Features in Safari 26.0* (2025): <https://webkit.org/blog/17333/webkit-features-in-safari-26-0/>
- [S5] WebKit blog, *WebKit Features for Safari 27.0* (2026-10-07): <https://webkit.org/blog/18325/webkit-features-for-safari-27-0/>
- [S6] WebKit blog, *Updates to Storage Policy* (2023-08-10): <https://webkit.org/blog/14403/updates-to-storage-policy/>
- [S7] Apple, WWDC23 *What's new in web apps*: <https://developer.apple.com/videos/play/wwdc2023/10120/>
- [S8] WebKit blog, *WebKit Features in Safari 17.2* (2023-12-11), sections "Login cookies" and "One time codes": <https://webkit.org/blog/14787/webkit-features-in-safari-17-2/>
- [S9] WebKit bug 268643 (iOS 17.4 beta, EU web apps) and TechCrunch, *Apple reverses decision about blocking web apps on iPhones in the EU* (2024-03-01): <https://bugs.webkit.org/show_bug.cgi?id=268643>, <https://techcrunch.com/2024/03/01/apple-reverses-decision-about-blocking-web-apps-on-iphones-in-the-eu/>
- [S10] MDN, *Storage quotas and eviction criteria*: <https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria>
- [S11] web.dev, *Storage for the web* (2024-09-23): <https://web.dev/articles/storage-for-the-web>
- [S12] web.dev, *Persistent storage* (2020): <https://web.dev/articles/persistent-storage>
- [S13] Apple Developer, *Sending web push notifications in web apps and browsers*: <https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers>
- [S14] WebKit blog, *Web Push for Web Apps on iOS and iPadOS* (2023-02-16): <https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/>
- [S15] WebKit blog, *WebKit Features in Safari 18.4* (2025-03-31): <https://webkit.org/blog/16574/webkit-features-in-safari-18-4/>
- [S16] MDN, *Push API*: <https://developer.mozilla.org/en-US/docs/Web/API/Push_API>
- [S17] Chrome for Developers, *Notification prompts on Android* (2026-07-22): <https://developer.chrome.com/blog/notification-prompts-android>
- [S18] Chrome for Developers, *Notification permission data in CrUX* (2020-02-11): <https://developer.chrome.com/blog/notification-permission-data-in-crux/>
- [S19] Google, *Automatic notification permission revocation* (Oct 2025): <https://blog.google/chromium/automatic-notification-permission/>
- [S20] Bilogrevic et al., *"Shhh...be quiet!" Reducing the Unwanted Interruptions of Notification Permission Prompts on Chrome*, USENIX Security 2021: <https://www.usenix.org/conference/usenixsecurity21/presentation/bilogrevic>
- [S21] StatCounter, *Mobile Operating System Market Share Lithuania* (September 2026): <https://gs.statcounter.com/os-market-share/mobile/lithuania>

Sign-in:

- [S22] Supabase docs, *Email Templates* (link prefetching by email scanners) and *Passwordless email sign-in*: <https://supabase.com/docs/guides/auth/auth-email-templates>, <https://supabase.com/docs/guides/auth/auth-email-passwordless>
- [S23] Supabase docs, *PKCE flow*: <https://supabase.com/docs/guides/auth/sessions/pkce-flow>
- [S24] web.dev, *WebAPKs on Android* (2017): <https://web.dev/articles/webapks>
- [S25] Apple Developer Forums thread on Mail code autofill (2023): <https://developer.apple.com/forums/thread/738690>
- [S26] FIDO Alliance, *Passkey Index* (Oct 2025): <https://fidoalliance.org/wp-content/uploads/2025/10/FIDO-Passkey-Index-October-2025.pdf>
- [S27] Microsoft Security blog, *Convincing a billion users to love passkeys* (2024-12-12): <https://www.microsoft.com/en-us/security/blog/2024/12/12/convincing-a-billion-users-to-love-passkeys-ux-design-insights-from-microsoft-to-boost-adoption-and-security/>
- [S28] Google Identity, *Reddit case study*: <https://developers.google.com/identity/sign-in/case-studies/reddit>

Sign-up friction:

- [S29] Huang, N., Mojumder, P., Sun, T., Lv, J., Golden, J. M. (2021). *Not Registered? Please Sign Up First: A Randomized Field Experiment on the Ex Ante Registration Request*. Information Systems Research 32(3):914–931. <https://doi.org/10.1287/isre.2021.0999>
- [S30] Nunes, J. C., Drèze, X. (2006). *The Endowed Progress Effect: How Artificial Advancement Increases Effort*. Journal of Consumer Research 32(4). <https://doi.org/10.1086/500480>
- [S31] Baymard Institute, *Cart Abandonment Rate Statistics* (updated 2025-09-22), industry: <https://baymard.com/lists/cart-abandonment-rate>
- [S32] First Round Review, *The Tenets of A/B Testing from Duolingo's Master Growth Hacker* (2017), industry: <https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker/>

Privacy and law:

- [S33] GDPR, Regulation (EU) 2016/679, Art. 4(1), 5, 6, 8, 13, 15, 17, 20 and Recitals 26, 30, 38: <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- [S34] Court of Justice of the EU, Press release 107/25, *EDPS v SRB* (C-413/23 P), 4 Sept 2025: <https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-09/cp250107en.pdf>
- [S35] Lietuvos Respublikos elektroninių ryšių įstatymas IX-2135 (new wording XIV-635, in force 2021-12-01; consolidated from 2026-07-01), Art. 5(2) and 73(4): <https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.232036/asr>
- [S36] EDPB, *Guidelines 2/2023 on the Technical Scope of Art. 5(3) of the ePrivacy Directive*, v2.0, adopted 2024-10-07, paras 44 and 61–63: <https://www.edpb.europa.eu/system/files/documents/2024-10/edpb_guidelines_202302_technical_scope_art_53_eprivacydirective_v2_en_0.pdf>
- [S37] Article 29 Working Party, *Opinion 04/2012 on Cookie Consent Exemption* (WP194), adopted 2012-06-07, sections 2.2, 2.3, 3.1, 3.2, 3.6: <https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2012/wp194_en.pdf>
- [S38] VDAI, *Slapukų naudojimo praktikos apibendrinimas* (2025): <https://vdai.lrv.lt/public/canonical/1765784968/1188/2025-04-02_Slapuku%CC%A8%20naudojimo%20praktikos%20apibendrinimas_new_galutinis.pdf>
- [S39] VDAI news, *VDAI primena: būtina užtikrinti tinkamą slapukų ir kitų sekimo technologijų naudojimą* (updated 2026-07-23): <https://vdai.lrv.lt/lt/naujienos/vdai-primena-butina-uztikrinti-tinkama-slapuku-ir-kitu-sekimo-technologiju-naudojima-Xad/>
- [S40] Lietuvos Respublikos civilinis kodeksas, Art. 2.8 (consolidated 2026-09-27): <https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.107687/asr>
- [S41] Asmens duomenų teisinės apsaugos įstatymas I-1374, Art. 6 (consolidated from 2026-06-30): <https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.29193/asr>
- [S42] Ministry of the Interior order 1V-329, *Motorinių transporto priemonių vairuotojų egzaminavimo sąlygų ir tvarkos aprašas* (consolidated from 2026-02-09), points 6–7 and the 1-year validity rule: <https://www.e-tar.lt/portal/lt/legalAct/TAR.C5B4B2AF50A4/asr>
- [S43] Saugaus eismo automobilių keliais įstatymas VIII-2043, Art. 21(5), 22(10), 23(2) (consolidated 2026-01-01 to 2026-10-31): <https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.111999/asr>
- [S44] Driver-training procedure, order 2B-84 (consolidated 2021-09-17 to 2026-10-31), points 7 and 18: <https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/fbab3c40d26511e39bf688e133d06adf/asr>
- [S45] Regitra news, *Teorijos egzaminą galima laikyti nuo 17 metų* (2010-09-10): <https://www.regitra.lt/naujienos/teorijos_egzamina_galima_laikyti_nuo_17_metu/>
