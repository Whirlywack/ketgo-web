# Tech stack options for the beta

Ticket: [#26 Tech stack options: evidence for the beta](https://github.com/Whirlywack/ketgo-web/issues/26) · Map: [#1](https://github.com/Whirlywack/ketgo-web/issues/1) · Feeds: [#7 Tech stack and hosting](https://github.com/Whirlywack/ketgo-web/issues/7)

**Checked on 2026-10-14.**

**How I checked.** I started from what the stack must carry: the closed tickets [#5](https://github.com/Whirlywack/ketgo-web/issues/5), [#6](https://github.com/Whirlywack/ketgo-web/issues/6), [#15](https://github.com/Whirlywack/ketgo-web/issues/15), [#17](https://github.com/Whirlywack/ketgo-web/issues/17), [#21](https://github.com/Whirlywack/ketgo-web/issues/21), [#22](https://github.com/Whirlywack/ketgo-web/issues/22) and [#23](https://github.com/Whirlywack/ketgo-web/issues/23). The May 2026 plan (SvelteKit + Supabase + Cloudflare) and the 2025 Expo app were inputs only. Sources are official docs, pricing pages, legal pages and source code. For field speed data I used HTTP Archive's Core Web Vitals Technology Report. Four research helpers gathered most vendor facts in parallel. I re-checked the facts that decide the choice myself: the WebKit source code, the Supabase and Better Auth package code, HTTP Archive numbers, Hetzner's status page, and Scaleway's product pages.

I also ran four tests of my own, all on 2026-10-14:

1. **Bundle and speed test.** I built the same "first Question" screen in six setups and measured the bytes and speed (section B).
2. **Sign-in test.** I ran the full "anonymous Learner → 6-digit email code → Account" flow on SvelteKit 3 with Better Auth (section C).
3. **Network round trips from Lithuania.** This computer is in Lithuania: Cloudflare reports `colo=VNO, loc=LT`. I timed connections to every candidate region (section D).
4. **Field data.** I queried the HTTP Archive API directly for pass rates by framework (section B).

**UNVERIFIED** marks anything I could not trace to a primary source.

**Evidence strength used in this file:**

- **Measured.** My own test on 2026-10-14. The method is given where the test is described.
- **Data.** Field data from many real sites or networks: HTTP Archive + Chrome UX Report, WonderNetwork pings, npm download counts.
- **Docs.** Official docs, pricing pages, legal pages, status pages or source code of the product itself.
- **Vendor claim.** A company says it about itself: marketing, its own blog or its own benchmark.
- **Community report.** Third-party blogs, forum posts and news stories.
- **Design guess.** My judgement from the evidence. Test it.

**Words used** (one line each):

- **JS bundle:** the JavaScript the phone must download and run before the page works.
- **gzip:** the normal way servers shrink files in transit. Sizes in this file are after gzip, with 1 KB = 1,000 bytes.
- **LCP:** the time until the main content is shown.
- **INP:** the time from a tap to the next screen update.
- **CWV:** Google's three Core Web Vitals: LCP, INP and CLS (layout jumps).
- **Server-rendered:** the server sends ready HTML, so text shows before any JavaScript runs.
- **Hydration:** the JavaScript that then wakes the page up so taps work.
- **Managed database:** the provider runs, backs up and patches the database for us.
- **ORM:** a library that writes SQL for us from typed code (here: Drizzle).
- **Serverless container:** our app packed as a Docker image; the provider runs and scales it, with no server to patch.
- **Cold start:** the delay when a stopped app has to start again for a request.
- **Cron:** a job that runs on a timer, for example every minute.
- **VAPID:** the keys a server uses to sign web push messages.
- **MoR (merchant of record):** a seller that handles VAT and invoices for us.
- **PITR:** point-in-time recovery, which restores the database to any minute in a window.

---

## A. Short answer

**Recommended stack:** SvelteKit 3 as one Node server, Better Auth, Drizzle and PostgreSQL. It runs on **Scaleway in Warsaw**, with a Serverless Container for the app and Managed PostgreSQL for the data, and Scaleway Transactional Email sends the codes. Every part with personal data is run by one EU company, about 16 ms from Vilnius.

| Layer | Choice | Why (short) | 500 learners | 5,000 | 30,000 |
|---|---|---|---|---|---|
| App framework | **SvelteKit 3** (Svelte 5), adapter-node, one server for pages and API | Smallest JS of the full app frameworks I built: **34.5 KB**, against 107–136 KB for React Router and Next.js. Cookies are httpOnly by default. Service worker built in. (Measured + Docs) | €0 | €0 | €0 |
| Auth | **Better Auth 1.7**, with the `anonymous` and `emailOTP` plugins, inside our own server | My test passed end to end. An anonymous Learner gets an httpOnly cookie from our host. A 6-digit code makes an Account, and the "link" hook fires so progress can move over. (Measured) | €0 | €0 | €0 |
| Database | **PostgreSQL** on **Scaleway Managed Database**, Warsaw, + **Drizzle** ORM | Plain SQL for the answer log and later AI work. Backups and failover are managed. French company (Iliad group). (Docs) | ~€13 | ~€17–33 | ~€75–95 |
| Hosting | **Scaleway Serverless Containers**, Warsaw (`pl-waw`) | 16 ms from Vilnius (Measured). Pages and API on one host. Cron triggers. Private network to the database. A max-scale setting caps the bill. EU company. (Docs) | ~€6 | ~€16 | ~€60 |
| Daily reminders | Scaleway CRON trigger → our `/internal/reminders` endpoint, every minute | No extra service; standard UNIX cron format. (Docs) | incl. | incl. | incl. |
| Web push | `web-push` library (Node) with VAPID keys + SvelteKit's own service worker | Runs as-is on a Node server. (Docs) | €0 | €0 | €0 |
| Email codes | **Scaleway Transactional Email (TEM)** | "All data is hosted and processed entirely within the European Union." 300 emails/month free, then €0.25 per 1,000. (Docs) | €0 | ~€1 | ~€5 |
| Pictures | Static files inside the app, hashed names, cached "forever" | ~300 files × ≤ 50 KB ≈ 15 MB. No extra service needed. (Design guess) | €0 | €0 | €0 |
| Analytics + A/B tests | Own Postgres events + server-side A/B assignment from the Learner ID. **Plausible** (Estonia) only if traffic-source charts are wanted | The answer log already holds the learning data. No analytics cookies. (Design guess + Vendor claim) | ($9) | ($9) | (~$39) |
| Payments (later) | **Stripe Managed Payments** (Stripe as MoR, Lithuania supported, +3.5 %) or **Paddle** (5 % + $0.50) | Both handle EU VAT. A small "entitlement" table + webhook means no rebuild. (Docs) | — | — | — |
| **Total** (without Plausible) | | | **~€19** | **~€35–50** | **~€140–160** |

How the costs were worked out:

- They assume every learner is active every day with ~40 answers (~60 requests). That is an upper bound.
- Scaleway prices are the Paris list prices; **Warsaw prices are UNVERIFIED**.
- The formulas are in sections C and D.

**Runner-up: the same app code on Vercel Pro (fra1) + Neon Postgres (Frankfurt).** SvelteKit, Better Auth and Drizzle stay the same; only the host and the database change.

- **Strengths:** it has the least ops and built-in preview deploys, and Neon can give each preview its own copy of the database. AI agents know this platform best.
- **Costs:** about **$40 / $80–105 / $330–610** a month at 500 / 5k / 30k (estimates; formulas in sections C and D).
- **Ownership:** Vercel and Neon (owned by Databricks) are both US companies.

**What would flip the choice to the runner-up:**

1. The Scaleway first-week checks fail. The checks are: custom domain + TLS, private network to the database, the cron trigger every minute, and cold starts.
2. The owner values per-branch previews and the most familiar platform for AI agents more than EU ownership and the bill at 30k.
3. The lawyer check finds no issue with US-parent processors.

**What would flip the host to Hetzner:**

- **When:** Hetzner can sell cloud servers again, and the owner accepts running Postgres backups ourselves. Hetzner is the cheapest at about €6–20 a month at all three sizes.
- **Today:** Hetzner shows "Limited availability of cloud instances" (open since 2026-06-26), and every cloud plan reads "This product is currently unavailable" (Docs).

**One thing that is the same in every option:** keep the app a plain Node server + plain Postgres. Then the host can be changed in a day, and the choice above stays reversible. (Design guess)

---

## B. App framework and rendering

### B1. My bundle and speed test (Measured)

I built the same screen in each setup. It has one Question with a picture box, 4 Options, and instant feedback with a short "why" after a tap. The page reads the learner cookie on the server and saves the answer in the background with one POST. The setups used each framework's normal pattern (Next.js server component + client component; SvelteKit `load` + runes; React Router `loader`; Astro page + island). Each was scaffolded with the official CLI, given a production build, and served by its own production server.

- **Bytes.** A Playwright Chromium browser loaded each page and saved every response it fetched. I re-compressed each body with gzip level 6 (the usual server default) and with brotli 11. "JS" is every script file; "whole page" adds the HTML and CSS. Nothing was cached.
- **Speed.** Lighthouse 13.5.0 ran its default mobile test, 3 runs each, median shown. It simulates a Moto G Power: 150 ms round trip, 1.6 Mbit/s and a 4× slower CPU ([Lighthouse throttling](https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md)). All servers sat behind the same gzip proxy so compression was equal.
- **Tap → feedback.** Playwright tapped a wrong Option with the CPU slowed 4×. I timed from `pointerdown` to the frame after the feedback box appeared, median of 5 runs. The test page has no real picture and no web font. So these numbers show the **framework's own cost**, not the final page.

| Setup (version) | JS to first Question (gzip) | Brotli | JS files | Whole page (gzip) | Lighthouse LCP | Lighthouse TBT | Tap → feedback |
|---|---|---|---|---|---|---|---|
| Astro 7.3, no framework (inline script) | 0.6 KB (inside the HTML) | — | 0 | 1.2 KB | 0.75 s | 0 ms | 32 ms |
| **Astro 7.3 + Svelte 5 island** | **14.5 KB** | 13.1 KB | 3 | 17.5 KB | 1.21 s | 0 ms | 33 ms |
| Hono 4.13 + htmx 2.0 (server sends the feedback) | 16.9 KB | 15.3 KB | 1 | 17.8 KB | 1.05 s | 0 ms | **199 ms** (waits for the server) |
| **SvelteKit 3.0.1 (Svelte 5.57)** | **34.5 KB** | 31.2 KB | 10 | 36.0 KB | 1.35 s | 0 ms | 32 ms |
| React Router 8.4 (framework mode, React 19.3) | 106.7 KB | 93.3 KB | 5 | 108.9 KB | 1.81 s | 0 ms | 31 ms |
| **Next.js 16.4 (App Router, React 19.3)** | **135.9 KB** | 115.8 KB | 6 | 139.4 KB | 1.93 s | 41 ms | 31 ms |

What this shows:

- **The budget from #21 is ≤ 170 KB for landing + first Question, of which JS ≤ 100 KB.**
  - Next.js and React Router already break the JS part on an empty screen, before any KETGO code, font or picture. Next.js alone uses 136 of the 170 KB. Its two biggest files are React DOM (72 KB gzip) and the Next.js router runtime (50 KB gzip), judged from the code inside them.
  - SvelteKit leaves about 130 KB free; Astro leaves about 150 KB.
- **Tap → feedback is the same (≈ 2 screen frames) for every setup that decides on the phone.** On a small screen like this, the framework does not slow the tap. A server round trip does: htmx waited 199 ms with a 150 ms round trip, so it would miss the ≤ 100 ms target on a weak mobile network. KETGO should decide right/wrong on the phone and save the answer in the background.
- **Lighthouse LCP is under 2.5 s for all of them** on this tiny page. SvelteKit's first paint (1.35 s) was later than Next.js's first paint (0.76 s) in the simulation, because SvelteKit tells the browser to preload its 10 small files early. Its LCP is still better than Next.js's (1.93 s). The real LCP will be the scene picture, which is why the byte budget matters.
- **Limits:** the test ran on a Mac with a slowed CPU, not a real phone. Repeat it on a mid-range Android in week 1 (section H).

### B2. Comparison of the candidates

Field pass rate = the share of real sites using that technology whose mobile visitors get "good" on all three Core Web Vitals. The data is for August 2026, from my own query of `cdn.httparchive.org/v1/cwv` (**Data**). These are whole sites with ads and heavy pictures, not clean tests, so they show a direction and do not prove the framework is the cause.

| Framework | Measured JS (B1) | Field: all 3 CWV good | Field: INP good | Sites in sample | httpOnly cookie by default | Service worker / push | Evidence on AI coding agents | Owner, latest major |
|---|---|---|---|---|---|---|---|---|
| **SvelteKit 3** | 34.5 KB | **50.6 %** | 74.8 % | 9,682 | **Yes**: "`httpOnly` is `true` by default, as is `secure`" (Docs) | **Built in**: "bundled and automatically registered" (Docs) | No public eval. Svelte 5 "runes" are a known weak spot (Community report). Official MCP server + `llms.txt` (Docs) | Open source; creator employed by Vercel since 2021 (Vendor claim). **3.0.0 on 2026-10-01** |
| Next.js 16 (App Router) | 135.9 KB | 38.3 % | 60.8 % | 248,526 | No: "The only option with a default value is `path`" (Docs) | Official PWA + push guide, hand-written service worker (Docs) | **Vercel's own eval: top models 97 % pass@4** (Vendor claim). Ships `AGENTS.md` + 472 doc files inside the package (Measured) | Vercel. 16.0 on 2025-10-22 |
| React Router 8 (framework mode) | 106.7 KB | 24.3 % (includes many single-page apps) | 53.8 % | 188,752 | No, must be set (Docs, partly UNVERIFIED) | Not built in (UNVERIFIED) | None found. Old Remix tutorials in training data (UNVERIFIED) | Shopify. 8.0 on 2026-06-17 |
| Astro 7 (+ islands) | 14.5 KB with a Svelte island | **71.0 %** | 85.7 % | 43,850 | `Astro.cookies`; defaults not documented (UNVERIFIED) | Not built in (Docs: none mentioned) | None found | **Cloudflare** since 2026-01-16; "will remain open source" (Vendor claim). 7.0 on 2026-06-22 |
| htmx (+ Hono) | 16.9 KB | 55.5 % | 95.3 % | 26,623 | Hono `setCookie`; set flags yourself | Not built in | Plain HTML is easy for agents (Design guess) | Community |
| Nuxt 4 | not built | 28.6 % | 65.3 % | 94,069 | — | — | — | Vercel (NuxtLabs joined 2025) |
| Qwik | not built | 62.5 % | 76.5 % | 1,334 | — | — | — | Builder.io (UNVERIFIED). v2 still RC on 2026-10-13 |

Popularity (npm downloads, week to 2026-10-12, **Data**): next 67.5 M, react-router 56.8 M, astro 7.3 M, svelte 6.8 M, @sveltejs/kit 3.3 M, nuxt 2.3 M, htmx.org 0.29 M, @solidjs/start 0.13 M, @builder.io/qwik 0.06 M. Stack Overflow 2025: Next.js used by 20.8 % of respondents, Svelte 7.2 %, Astro 4.5 % (**Data**).

**Dropped fast:**

- **Nuxt:** Vue stack, weakest field data of the big ones (28.6 %), nothing gained over SvelteKit.
- **Qwik:** tiny ecosystem (0.06 M downloads a week), v2 not stable yet.
- **SolidStart:** only 9 sites in HTTP Archive, 0.13 M downloads a week.
- **Expo / React Native Web:** react-native-web alone is about 73 KB gzip, and a 2023 test found a fresh Expo Router web app near 400 KB gzip (Community report, stale). Web is its second target. This fits the owner's feeling that the 2025 app was slow. Only worth it if native store apps are planned.
- **TanStack Start:** not assessed.

### B3. Why SvelteKit

1. **It is the only full app framework I measured that fits the budget with room to spare** (34.5 KB vs 107–136 KB). (Measured)
2. **Field data points the same way:** 50.6 % of SvelteKit sites pass all three CWV on mobile, against 38.3 % for Next.js App Router and 24.3 % for React Router. (Data)
3. **It obeys the cookie rule by default** (httpOnly + Secure) and **bundles and registers the service worker** that web push needs. (Docs)
4. **It is a full app framework**, with routing, forms, server endpoints and client navigation between Questions. Astro is smaller and has better field data, but its strength is content pages. A Lesson is an app with state, so most of KETGO would end up inside one big island anyway. (Design guess)
5. **It also won in the May 2026 plan, but for other reasons.** This note keeps the framework and drops the rest of that plan (Supabase Auth, Cloudflare Pages, Edge Functions), for the cookie and latency reasons in sections C and F.

**The weak spot is AI coding agents:**

- **No public eval.** Next.js has a public agent eval (top models 97 %, Vendor claim); Svelte has none.
- **Svelte 5 "runes" are a known weak spot.** The Svelte community says "most AI models struggle with Svelte 5 code" (Community report, 2025).
- **SvelteKit 3.0.0 is two weeks old.** Most models were trained before it, and it moved several things:
  - `svelte.config.js` is gone; config now lives in `vite.config`.
  - `$lib` is now `#lib`.
  - `$app/environment` is now `$app/env`.
  - `$service-worker` was removed.
  - Node 22.17+ and Vite 8 are required.

  (Docs: [migration guide](https://svelte.dev/docs/kit/migrating-to-sveltekit-3))
- **Fixes:**
  - Always scaffold with the official `sv` CLI.
  - Add the Svelte MCP server and `llms.txt` docs to the agents' context.
  - Put the Kit 3 migration notes into `CLAUDE.md`.
  - Run `svelte-check` and a production build in CI.
- **Do not start on SvelteKit 2.** Its last release was 2.70.3 on 2026-08-18, and I found no support promise (Data + UNVERIFIED).

**If the 170 KB budget were dropped,** Next.js would win on AI-agent evidence. The budget came from #21 and is binding for this note.

---

## C. Database, backend and auth

### C1. My sign-in test (Measured)

On the SvelteKit 3.0.1 production build (adapter-node), I ran Better Auth 1.7.7 with the `anonymous` and `emailOTP` plugins and an in-memory test database. I drove the flow with `fetch` calls, like the app would:

```
POST /api/auth/sign-in/anonymous -> 200
  Set-Cookie: __Secure-better-auth.session_token=…; Max-Age=34560000; Path=/; HttpOnly; Secure; SameSite=Lax
  anonymous user: EKtR…hzmd  isAnonymous = true
POST /api/auth/email-otp/send-verification-otp -> 200
  code sent by email: 560346 (6 digits)
POST /api/auth/sign-in/email-otp -> 200
  Set-Cookie: __Secure-better-auth.session_token=…; Max-Age=34560000; Path=/; HttpOnly; Secure; SameSite=Lax
  account user: afIT…nI5C  isAnonymous = false
  onLinkAccount calls: [{"from":"EKtR…hzmd","to":"afIT…nI5C","fromAnonymous":true}]
wrong code -> 400
```

What this proves:

- **The anonymous Learner exists from the first Start.** The cookie is httpOnly and set by our own server on our own host. Max-Age is 400 days because I set it; the default is shorter (next list).
- **The 6-digit code creates the Account.** It works without links.
- **The `onLinkAccount` hook receives both users.** That is where KETGO moves the Learner's answers to the Account, or switches to the Account's existing progress, as #6 requires.

What I found that needs care:

- **Install:** `npm i better-auth` **fails with `ERESOLVE`** in a SvelteKit 3 project. Better Auth 1.7.7 declares `@sveltejs/kit "^2.0.0"` as an optional peer. It installs with `--legacy-peer-deps` (or an npm `overrides` entry), and then it works. (Measured)
- **The default session is only 7 days** (`expiresIn: 3600 * 24 * 7`, refreshed once a day when used; Docs: package code). For anonymous Learners that would lose progress after a week away. **Set `session.expiresIn` to 400 days**; Chrome caps cookies at 400 days anyway.
- **The account user gets a new ID**, and the anonymous user is deleted by default after linking (Docs). So **keep progress in our own `learner` table** and point the auth user at it. Do not key answers to the auth user's ID. (Design guess)
- **The rate limiter keeps its counts in memory by default**, which "is not suitable for serverless" (Docs). Store them in the database once there is more than one container. Set a generous limit on anonymous sign-ins: a driving-school class can share one IP. (Design guess)
- **Behind a proxy, the server must know its public `https://` address.** adapter-node 6 reported `https://` request URLs even with `ORIGIN=http://…`, and Better Auth's path check then failed until `baseURL` matched (Measured). Set the public URL in both places in week 1.

Better Auth defaults I checked in the published package code (**Docs**):

- 6-digit codes, valid 300 s, 3 tries.
- Code routes allow 3 requests per 60 s.
- Cookies are `httpOnly: true`.
- An email-code sign-in (`/sign-in/…` and `/email-otp/verify-email`) triggers the anonymous link.
- Deleting a user is built in but off by default.

**Ownership:** Vercel bought Better Auth on 2026-07-07. "The library remains free and open source under MIT" and "retains its name" (Vendor claim). It runs inside our server, so no data goes to Vercel. Auth.js joined Better Auth in Sept 2025 (Vendor claim).

### C2. Comparison

| Option | Anonymous Learner, cookie set by our host | 6-digit code that keeps progress | Answer log in SQL | Company / data location | Cost 500 / 5k / 30k per month | Ops for one owner | Verdict |
|---|---|---|---|---|---|---|---|
| **Postgres + Drizzle + Better Auth** (in our server) | **Yes** (Measured) | **Yes** (Measured) | Yes | Depends on the Postgres host | €0 for auth | Low | **Pick** |
| **Scaleway Managed PostgreSQL** (Warsaw) | — (database only) | — | Yes | French (Iliad); Paris, Amsterdam, Warsaw (Docs) | **~€13 / ~€17–33 / ~€75–95** | Low: managed backups, HA standby option | **Pick for the data** |
| Neon (Frankfurt) | — (database only) | — | Yes | Databricks (US); Frankfurt, London (Docs) | ~$20 / ~$40–51 / ~$150–230 | Lowest; branches for previews | **Runner-up** |
| Supabase (Auth + Postgres) | **Partly.** The default browser client writes session cookies with `document.cookie`, `httpOnly: false` (Docs: source). Safari caps such cookies after 7 days without a visit (Docs) | Yes: `updateUser({email})` + 6-digit `{{ .Token }}` (Docs) | Yes | Supabase Inc (US); EU regions incl. Stockholm and Frankfurt (Docs) | $25 / ~$30–34 / ~$76–101 | Low | Not for auth. As plain Postgres it gives nothing over Neon or Scaleway |
| Self-hosted Postgres on Hetzner | — | — | Yes | German | €6–16 (shared with the app) | **High**: our own backups, upgrades, restores | Fallback; cannot order servers now (section D) |
| Firebase (EU) | Anonymous auth yes | **No email-code sign-in found** (Docs, absence) | No (document store; export to BigQuery) | Google (US) | ~$0 / ~$5 / ~$65 | Low | Drop |
| Convex (Dublin) | Not verified | Not verified | Awkward (document store) | US; EU region costs +30 % (Docs) | ~$0–2 / ~$33 / ~$105 | Low | Drop |
| PocketBase | No anonymous user built in (UNVERIFIED) | OTP built in, 8 digits by default (Docs: source) | SQLite | Open source, self-hosted | Host cost | Medium; still pre-1.0 (v0.40.5) | Drop |
| Cloudflare D1 / Turso | Via our own code | Via our own code | SQLite; billed per row written, indexes count (Docs) | US | D1 $0 / $5 / $27–99 | Low, but **D1 caps a database at 10 GB** (Docs). At 30k learners the log grows ~18 GB/month | Drop |

**Supabase in detail** (it was the May plan's core):

- **Cookies.** `@supabase/ssr` 0.12.7 has `httpOnly: false` and writes `document.cookie = serialize(name, value, options)` in the browser. Its browser client says "the session is always persisted via cookies" (Docs: package code).
  - WebKit: "ITP deletes all cookies created in JavaScript … after 7 days of no user interaction" (Docs).
  - So an iPhone learner who uses KETGO in a Safari tab and takes a week off could lose the session. This combines two documented rules; I did not test it on a phone. It breaks the #6 rule "the ID is a cookie set by our server".
- **Anonymous sign-ins** are limited to "30 requests per hour" per IP by default. The limit can be changed in the dashboard (Docs). An anonymous user who loses the cookie "can't access their account" (Docs).
- **Missing access rules.** "A table in an exposed schema without RLS is readable and writable by any role with a grant on it" (Docs). A 2025 scan of apps built with an AI app builder found about 10 % open to anyone with the public key (CVE-2025-48757, Community report). Our design has no public database API at all, so this risk disappears.

**Delete my progress and the 12-month anonymisation** are plain SQL in every option. No vendor offers a ready helper (Docs, absence). Plan:

- **Delete:** delete the `learner` row; answers cascade; the totals table stays.
- **Anonymise:** a nightly job gives each Learner unseen for 12 months a new random ID on their answers, then deletes the Learner, the auth user, the sessions and the email.

**Answer log:** one append-only table, `answer_event`.

- **Columns:** Options shown in order, selected Options, response time, predicted P(correct), candidate set + selection probability, model version, mode and days to exam. Store the lists as `jsonb`.
- **Growth (Design guess):** 40 answers × 30 days ≈ 1,200 rows per learner per month, at about 0.5 KB per row with its index. That is ~0.3 / 3 / 18 GB per month at 500 / 5k / 30k learners, or ~3.6 / 36 / 216 GB after 12 months. Plan monthly partitions from the start.
- **Analysis:** export to DuckDB/Parquet for the later AI work.

**Cost formulas** (Docs, list prices on 2026-10-14):

- **Scaleway** (Paris prices; Warsaw UNVERIFIED): `730 h × node price + €0.0993 × GB storage + €0.03 × GB backups`.
  - 500: DB-DEV-S (2 vCPU, 2 GB) at €0.0156/h = €11.4, + ~€1.3 storage and backups.
  - 5k: DB-DEV-S or DB-DEV-M (€0.0382/h = €27.9), + ~€5 storage and backups.
  - 30k: DB-DEV-M or PLAY2-NANO (€0.0432/h) + a standby node (€0.0136–0.0376/h) + ~€32 for 250 GB plus backups.
- **Neon Launch:** `CU × 730 × $0.106 + $0.35 × GB`. That is 0.25 CU always on at 500, ~0.5 CU at 5k, and 1–2 CU at 30k, plus storage growth.
- **Supabase Pro:** `$25 + compute above the $10 credit + $0.125 × GB above 8 GB`.

---

## D. Hosting and runtime

### D1. Round trips from Vilnius (Measured)

These are TCP connect times from this computer in Lithuania, best of 7, to a public endpoint in each region (2026-10-14). One connect is about one network round trip. A phone on 4G adds its own radio delay on top.

| Region (endpoint used) | Best round trip |
|---|---|
| Cloudflare, Vilnius PoP (`colo=VNO`) | 7.6 ms |
| Vercel edge (answered from `arn1`, Stockholm) | 15.3 ms |
| **Scaleway Warsaw** (`s3.pl-waw.scw.cloud`) | **15.8 ms** |
| Hetzner Helsinki (`hel1-speed.hetzner.com`) | 25.1 ms |
| AWS Stockholm (`dynamodb.eu-north-1`) | 27.8 ms |
| AWS Frankfurt (`dynamodb.eu-central-1`), where Vercel fra1, Neon and Supabase Frankfurt sit | 33.3 ms |
| Scaleway Amsterdam / Hetzner Nuremberg / Hetzner Falkenstein | 33.6 / 34.2 / 34.4 ms |
| Scaleway Paris | 42.2 ms |
| AWS Ireland | 47.9 ms |

This matches WonderNetwork's server-to-server pings from Vilnius: Warsaw 7.8 ms, Helsinki 15.2 ms, Stockholm 15.8 ms, Frankfurt 31.7 ms (Data).

**What matters more than the region:** the app and the database must sit in the **same** data centre. A page that makes 5 database queries from Vilnius to Frankfurt pays 5 × ~30 ms. (Design guess from the numbers above.)

### D2. Comparison

| Host | Nearest region | One host for pages + API | Cron for reminders | Web push library | Cost 500 / 5k / 30k per month (app only) | Bill control | Company | Ops | Previews |
|---|---|---|---|---|---|---|---|---|---|
| **Scaleway Serverless Containers** | **Warsaw** | Yes | CRON triggers, UNIX format, time zone can be chosen (Docs); minimum interval UNVERIFIED | `web-push` on Node | **~€6 / ~€16 / ~€60** | **max-scale** caps instances; beyond it, requests get 503 (Docs) | French (Iliad) | Low: no OS to patch | DIY with GitHub Actions |
| Vercel Pro (fra1 or arn1) | Stockholm / Frankfurt | Yes | Pro: once per minute. **Hobby: once per day** (Docs) | `web-push` on Node functions | $20 / ~$40–55 / ~$175–375 | Spend Management can pause the site at a budget (Docs) | US | Lowest | **Built in** |
| Cloudflare Workers | Vilnius PoP | Yes | Cron Triggers, 1 minute, UTC (Docs) | **`web-push` fails on Workers** (issue #718, open; Community report). Needs a Web Crypto library | $5 / ~$6 / ~$26 | **No spend cap** (Community report). One public story of a $36,000 bill from a retry loop (Community report, unverified) | US | Low; edge runtime limits (128 MB, 6 connections) | Version previews |
| Hetzner Cloud (+ Docker) | Helsinki | Yes | System cron | `web-push` | ~€6 / ~€6–9 / ~€9–20, incl. a self-run DB | Fixed: "bill will never exceed its monthly price cap" (Docs) | German | **High**: OS, TLS, DB backups | DIY |
| Fly.io | Frankfurt / Stockholm; no Baltic or Polish region (Docs) | Yes | Process cron | `web-push` | ~$5 / ~$12 / ~$40–50 (estimate) | — | US | Medium | — |

Hetzner, in detail:

- **Prices.** They rose on 2026-06-15, for example CX23 from €3.99 to €5.49 a month.
- **Availability.** The status page shows **"Limited availability of cloud instances"**, open since 2026-06-26. All cost-optimised and regular cloud plans read "This product is currently unavailable. Please check back later." (Docs, fetched 2026-10-14). Third-party reports tie this to hardware shortages (Community report).

**Dropped fast:**

- **Vercel Hobby:** "restricted to non-commercial, personal use only", and cron runs once a day, so reminders at a chosen time cannot work (Docs).
- **Railway:** the only EU region is Amsterdam, and billing is by usage (Docs).
- **Render:** bandwidth costs $0.15/GB beyond 5–25 GB, and free services sleep (Docs + Community report).
- **Netlify:** credit pricing (~$120 at 900 GB), and scheduled functions have no documented per-minute interval (Docs).
- **DigitalOcean:** a US company and dearer than Hetzner for the same box (Docs).
- **Deno Deploy:** egress costs $0.20/GiB (Docs).
- **bunny.net Magic Containers:** EU company, but not researched deeply enough to rank.
- **Coolify / Dokploy** (self-hosting panels): both published many Critical and High security advisories in June–July 2026. A panel bug can mean "Authenticated RCE leading to host root" (Docs: GitHub advisories). If we self-host, use plain Docker Compose or Kamal.

### D3. Why Scaleway Warsaw

1. **Closest real region:** 16 ms measured, about half the round trip to Frankfurt. Database, app, email and object storage are all in the same region (Docs: product availability).
2. **One EU company for everything with personal data.** TEM: "no personal data is transferred outside the EU" (Docs). That removes the US-parent question from the lawyer check (#6) for hosting. The EU-US Data Privacy Framework is under appeal at the EU Court (C-703/25 P, Community report).
3. **Low ops without lock-in.**
   - The app is a normal Docker image and the database is normal Postgres; both move to any host.
   - Containers reach the database over a private network at no extra cost (Docs). Managed PostgreSQL "comes with high-availability mode, data replication, and automatic backups" (Docs).
4. **Predictable bill.** Compute is per second, with a `max-scale` cap, and there are no per-request fees (Docs). Keep **min-scale = 1**: at 0, instances stop "after 15 minutes of inactivity" and the next learner waits for a cold start (Docs).
5. **Costs** (Docs: €0.00001 per vCPU-second, €0.000002 per GB-second, free 200k vCPU-s + 400k GB-s per month):
   - 500: 1 container at 0.25 vCPU / 0.5 GB always on ≈ €6.
   - 5k: 0.5 vCPU / 1 GB ≈ €16.
   - 30k: 2 × 1 vCPU / 1 GB ≈ €60.
   - These sizes are a design guess; my load estimate is ~21 requests/s at 30k, which is small.
6. **Weak spots:**
   - No built-in preview deploys.
   - Fewer AI-agent examples than Vercel.
   - PITR is not documented (UNVERIFIED).

   These are the week-1 checks.

---

## E. Smaller layers

### E1. Email for 6-digit codes

Volumes assumed: ~300 / 3,000 / 20,000 emails per month (Design guess: most Learners never make an Account).

| Service | Company / data | Price at 300 / 3k / 20k | Notes |
|---|---|---|---|
| **Scaleway TEM** | French; "All data is hosted and processed entirely within the European Union" (Docs) | €0 / ~€0.7 / ~€4.9 | 300 free, then €0.25 per 1,000 (Docs). Shared IPs on the cheap plan; dedicated IP on the €80 Scale plan |
| Amazon SES (eu-central-1) | US | ~$0.03 / ~$0.3–0.5 / ~$2–3.2 | Pricing tiers changed; which tier applies is UNVERIFIED |
| Brevo | French | Free 300/day with Brevo branding; Starter ~$9 | Third-party prices disagree (Community report) |
| Mailjet | Sinch (Sweden), with a US group company; US or EU hosting | Free 6,000/month (200/day) | Privacy policy relies on the DPF (Docs) |
| Lettermint | "EU-based infrastructure" (Vendor claim) | Free 300; €10 for 10k | Company HQ UNVERIFIED |
| Resend | US; "your Resend account data still resides in the US" even with the EU region (Docs) | Free 3,000/month | Drop |
| Postmark | ActiveCampaign (US); data may go to the US (Docs) | 100 free; $15 for 10k | Drop |

**Pick Scaleway TEM.** Test delivery to Gmail, Outlook, iCloud and Lithuanian inboxes in week 1, with SPF, DKIM and DMARC set. Keep Lettermint or SES as fallback.

### E2. Analytics and A/B tests

- **Learning analytics live in our own Postgres.** Every answer is already logged (#15). Add a small `app_event` table for funnel steps (Start, first Question, Lesson 1 end, Account, push allowed).
- **A/B tests: assign the variant on the server from the Learner ID**, log it on every event, and analyse in SQL. This needs no analytics cookie. Lithuania needs consent for analytics cookies (#23). (Design guess)
- **Traffic sources:** Plausible is Estonian, its data stays in the EU, and it is cookieless (Vendor claim). $9/month for 10k pageviews; ~$39 at 100k (Community report). It has goals and funnels, no experiments.
- **If richer product analytics are wanted later:** PostHog EU Cloud. 1 M events and 1 M feature-flag requests are free each month, with experiments included (Docs). It is a US company, and how its cookieless mode works with experiments is UNVERIFIED.

### E3. Pictures

About 100 scenes and 200 sign drawings at ≤ 50 KB each come to ~15 MB. **Ship them as static files in the app**: SvelteKit gives imported files hashed names that can be cached forever. If they ever need their own home, use Scaleway Object Storage (same region) or bunny.net (Slovenia, $0.01/GB in Europe, $1 monthly minimum; Docs). Cloudflare R2 has zero egress fees and an EU-jurisdiction option, but it is a US company and custom-domain support for EU buckets is UNVERIFIED.

### E4. Payments later (fit check only)

| Option | Who handles EU VAT | Fee | Fit |
|---|---|---|---|
| **Stripe Managed Payments** | Stripe is the merchant of record; Lithuania is supported; "online courses" are an eligible category (Docs) | 3.5 % on top of normal Stripe fees (Docs) | Good. Only Checkout / Payment Links are supported (Docs) |
| Stripe Billing + Stripe Tax | **We are** the seller and file VAT (Docs) | Card fees + Tax fees | Fine while all buyers are in Lithuania |
| Paddle | Paddle is the merchant of record | 5 % + $0.50 (Docs) | The $0.50 hurts at €3–10 prices |
| Polar.sh / Lemon Squeezy | Merchant of record | 4–5 % + fixed fee (Docs) | Lemon Squeezy is moving to Stripe Managed Payments (Vendor claim) |

**Tax points to confirm with an accountant:**

- Lithuanian VAT registration starts at €45,000 (Community report; confirm with VMI).
- Cross-border B2C digital sales in the EU switch to the buyer's VAT rate above €10,000 a year (Docs: Your Europe).

**No rebuild needed.** A paid plan is an `entitlement` row (Account, plan, status, end date) kept up to date by a webhook. Any of these providers fits.

---

## F. How the pieces fit (combination checks)

1. **Safari and the learner cookie** (Docs: WebKit source, `NetworkTaskCocoa.mm`, main branch, read 2026-10-14):
   - **When the cap applies.** WebKit caps a server-set cookie at 7 days (`m_ageCapForCNAMECloakedCookies { 24_h * 7 }`) only when the response is "a same-site subresource but it resolves to a different CNAME or IP address range than the top site request".
   - **What "different IP range" means.** It is fewer than 16 matching bits for IPv4 and fewer than 64 for IPv6 (`matchingLength < 4 * sizeof(struct in_addr)`). The "top site" IP is the address of the page's own connection (`setFirstPartyHostIPAddress`).
   - **Page responses are never capped.** `if (request.isTopSite()) … _cookieTransformCallback = nil`: a cookie set in the HTML page response itself is never capped by this rule.
   - **For KETGO:**
     - Serve pages and `/api/auth` from **one hostname on one host**.
     - **Refresh the session cookie on page loads.** In SvelteKit that is `hooks.server.ts`, which runs before every page response.
     - Never put the auth API on a subdomain that points to another provider. That is exactly the case the May plan had with Supabase Auth.
     - This keeps the cookie safe even if a CDN hands out IPs from two ranges.
     - The Home Screen web app is exempt from the 7-day rule for script storage (Docs); a real iPhone test is still needed (#23).
2. **Better Auth on SvelteKit 3 on Node:** works, with three settings: `--legacy-peer-deps`, a 400-day session, and the public `https` `baseURL`. (Measured)
3. **Web push from the runtime.** On a Node container, `web-push` works as-is. It is old (last release 3.6.7 on 2024-01-16) but used everywhere (10.9 M downloads a week) (Data). If it ever fails with Apple's push service, `@block65/webcrypto-web-push` 2.0 and `@pushforge/builder` 2.0 use Web Crypto and claim Apple support (Vendor claim). On Cloudflare Workers, `web-push` is reported broken (issue #718).
4. **SvelteKit 3 service worker:**
   - Kit 3 registers the service worker as a module and removed `$service-worker` (Docs).
   - `@vite-pwa/sveltekit` 1.1.0 only lists Kit 1 and 2 as peers (Data: npm).
   - So **hand-write the service worker**: about 60 lines for `push`, `notificationclick` and a small offline page. Push does not need a PWA plugin. (Design guess)
5. **Reminders at each Learner's time:**
   - Store the chosen time as a UTC minute.
   - A Scaleway CRON trigger calls `POST /internal/reminders` every minute with a secret header.
   - The job picks Learners due now who have not studied today, and claims each one with `SELECT … FOR UPDATE SKIP LOCKED`, so two containers never send twice.
   - **If the trigger cannot run every minute,** run every 5 minutes; reminders are then up to 5 minutes late. (Design guess)
6. **The learning engine:** `ts-fsrs` 5.4.2 is plain TypeScript and runs in the Node server (Data: npm). Keep it behind one function so the later Python/AI work can replace it (as in the May plan's ADR).

---

## G. Facts the tech-stack decision (#7) needs

- A first-Question screen costs **34.5 KB** of gzipped JS in SvelteKit 3. It costs **106.7 KB** in React Router 8 and **135.9 KB** in Next.js 16, before any KETGO code. (Measured)
- Astro + a Svelte island costs **14.5 KB**; htmx costs **16.9 KB** but needs a server round trip per tap (199 ms at 150 ms network round trip). (Measured)
- Tap → feedback was ~32 ms (two frames) in every framework that decides on the phone. On a small screen, the framework does not slow the tap. (Measured, desktop with a 4× slower CPU)
- Mobile pass rate on all three Core Web Vitals, August 2026: Astro 71.0 %, SvelteKit 50.6 %, Next.js App Router 38.3 %, Nuxt 28.6 %, React Router 24.3 %. (Data; whole sites, not proof of cause)
- Vercel's own Next.js agent eval shows top models at 97 % pass@4 (2026-09-25). No such eval exists for SvelteKit. (Vendor claim)
- SvelteKit 3.0.0 shipped on 2026-10-01 and changed config, imports and the service worker. Most AI models predate it. (Docs + Data)
- SvelteKit sets cookies httpOnly + Secure by default; Next.js does not. (Docs)
- WebKit caps server-set cookies at 7 days only for background requests to a different CNAME or IP range. A cookie set on the page response itself is never capped. (Docs: source code)
- Supabase's default browser client writes non-httpOnly cookies from JavaScript. That clashes with "the learner ID is a cookie set by our server". (Docs: source code)
- Better Auth anonymous → 6-digit code → Account works on SvelteKit 3: httpOnly cookie from our host, and the link hook fires. (Measured)
- Better Auth needs `--legacy-peer-deps` on Kit 3, and its default session is 7 days. Change both. (Measured + Docs)
- Vercel bought Better Auth on 2026-07-07; it stays MIT. (Vendor claim)
- Round trip from Vilnius: Scaleway Warsaw 16 ms, Hetzner Helsinki 25 ms, AWS Stockholm 28 ms, AWS Frankfurt 33 ms. (Measured)
- Hetzner raised cloud prices on 2026-06-15 and has limited new cloud servers since 2026-06-26; every plan page reads "currently unavailable". (Docs)
- Scaleway Warsaw offers Managed PostgreSQL, Serverless Containers, Serverless Jobs and Object Storage, and TEM is global. (Docs)
- Scaleway containers: €0.00001 per vCPU-second, no request fees, max-scale caps instances, min-scale 0 sleeps after 15 minutes. (Docs)
- Vercel Hobby forbids commercial use and runs cron once a day. Vercel Pro runs cron every minute. (Docs)
- Neon is owned by Databricks; Launch costs $0.106 per CU-hour and $0.35 per GB-month, with EU regions in Frankfurt and London. (Docs)
- Cloudflare D1 caps a database at 10 GB and bills per row written. (Docs)
- `web-push` does not run on Cloudflare Workers (open issue) but runs on any Node server. (Community report + Docs)
- Scaleway TEM: 300 emails free, then €0.25 per 1,000, all data in the EU. (Docs)
- Stripe Managed Payments (merchant of record, +3.5 %) is available for a Lithuanian business. (Docs)
- Estimated monthly cost of the recommended stack: ~€19 at 500 learners, ~€35–50 at 5,000, ~€140–160 at 30,000. Runner-up: ~$40 / ~$80–105 / ~$330–610. (Docs prices + Design guess for usage)

---

## H. Risks and first build checks

Prove these in the first week, before much code depends on them:

1. **Real iPhone (iOS 26).**
   - Start in a Safari tab, wait 8+ days without visiting, and come back: is the Learner still there?
   - Add to Home Screen: does the cookie carry over?
   - Does push arrive from the Home Screen app? (#23 asked for the same.)
2. **Real mid-range Android** (a Samsung A-series or Moto G phone) with the real scene picture and font.
   - LCP ≤ 2.5 s on 4G.
   - Tap → feedback ≤ 100 ms.
   - Landing + first Question ≤ 170 KB.

   If SvelteKit's 10 small JS files hurt first paint, try its `bundleStrategy` option (Design guess; check the docs).
3. **Scaleway basics.**
   - Custom domain + TLS on a Serverless Container.
   - Private network to Managed PostgreSQL.
   - A CRON trigger every minute, and its time zone.
   - Cold start with min-scale 1 when a second instance starts.
   - Warsaw prices against Paris prices.
   - Backup retention, and whether PITR exists.
   - Billing alerts.
4. **Better Auth settings.**
   - Install with `--legacy-peer-deps` or `overrides`.
   - `session.expiresIn` = 400 days; the rate limit stored in the database.
   - `onLinkAccount` for both #6 cases. A new email keeps the device's progress. An existing Account replaces it, after the one-line warning.
   - Turn on `deleteUser` for "Delete my progress".
5. **Public URL behind the proxy.** Set the adapter-node origin and the Better Auth `baseURL` to the public `https://` address, and test the CSRF origin check.
6. **Service worker + push.** Hand-written module service worker on Kit 3. `web-push` with VAPID keys to Chrome on Android and Safari on iOS. Keep a Web Crypto library as plan B.
7. **AI agents on Svelte 5 / Kit 3.**
   - Add the Svelte MCP server, `llms.txt` and the Kit 3 migration notes to the agents' context.
   - CI runs `svelte-check`, the tests and a production build on every change.
   - Watch for Svelte 4 syntax (`export let`, `$:`) and for `$lib` / `$app/environment`.
8. **Email delivery.** TEM with SPF, DKIM and DMARC to Gmail, Outlook, iCloud and common Lithuanian inboxes. Measure how long the code takes to arrive.
9. **Answer log.**
   - Decide the `answer_event` columns (#15).
   - Set up monthly partitions.
   - Make the app role insert-only, so only the anonymisation job may update rows.
   - Run a dry run of delete and anonymise.
10. **Preview deploys.** A GitHub Action that deploys each pull request to a preview container with its own preview database. Budget one day.
11. **Lawyer check.** Scaleway and TEM data processing agreements, plus the cookie questions already listed in #6.
12. **Watch Hetzner.** If cloud capacity returns and the owner wants the lowest bill, the same Docker image moves to Helsinki. Postgres backups then become our job.

---

## Sources

### Earlier KETGO research
- First impression and mobile UI (#21): <https://github.com/Whirlywack/ketgo-web/blob/research/first-impression-ui/docs/research/first-impression-ui.md>
- Accounts, phone storage and privacy (#23): <https://github.com/Whirlywack/ketgo-web/blob/research/accounts-storage-privacy/docs/research/accounts-storage-privacy.md>
- May 2026 plan (input only): `~/Documents/ketgo-grilled/docs/adr/0004-tech-stack.md`

### Measurement tools and budgets
- Lighthouse throttling: <https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md>
- web.dev performance budgets: <https://web.dev/articles/performance-budgets-101>
- npm registry and downloads API: <https://registry.npmjs.org/>, <https://api.npmjs.org/downloads/point/last-week/next>
- Cloudflare trace (location check): <https://www.cloudflare.com/cdn-cgi/trace>
- WonderNetwork pings from Vilnius: <https://wondernetwork.com/pings/Vilnius>

### Layer 1: app framework
- HTTP Archive tech report: <https://httparchive.org/reports/techreport/tech>; API used: <https://cdn.httparchive.org/v1/cwv?technology=SvelteKit&geo=ALL&rank=ALL&start=latest> (same pattern for Astro, Svelte, Next.js, Next.js%20App%20Router, React%20Router, Nuxt.js, Htmx, Qwik, Remix, Vue.js, React, SolidStart)
- SvelteKit 3 migration guide: <https://svelte.dev/docs/kit/migrating-to-sveltekit-3>
- SvelteKit service workers: <https://svelte.dev/docs/kit/service-workers>
- SvelteKit cookies: <https://svelte.dev/docs/kit/@sveltejs-kit#Cookies>
- Svelte and AI (MCP, llms.txt): <https://svelte.dev/docs/ai>, <https://svelte.dev/docs/ai/mcp>
- Svelte 5 and AI models (community): <https://sveltesociety.dev/video/this-ai-model-writes-svelte-5-code-perfectly-3e4fd8c93a38753c>
- Vercel hires Svelte's creator: <https://vercel.com/blog/vercel-welcomes-rich-harris-creator-of-svelte>
- Next.js agent evals: <https://nextjs.org/evals>
- Next.js PWA guide: <https://nextjs.org/docs/app/guides/progressive-web-apps>
- Next.js cookies: <https://nextjs.org/docs/app/api-reference/functions/cookies>
- React Router v8: <https://remix.run/blog/react-router-v8>
- React Router createCookie: <https://reactrouter.com/api/utils/createCookie>
- Astro on-demand rendering: <https://docs.astro.build/en/guides/on-demand-rendering/>
- Cloudflare acquires Astro: <https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-astro-to-accelerate-the-future-of-high-performance-web-development/>
- NuxtLabs joins Vercel: <https://vercel.com/blog/nuxtlabs-joins-vercel>
- Qwik resumability: <https://qwik.dev/docs/concepts/resumable/>
- Expo static rendering: <https://docs.expo.dev/router/reference/static-rendering/>
- Expo Router bundle size (2023): <https://blog.theodo.com/2023/12/expo-router-visualizing-bundle-size>
- Stack Overflow Developer Survey 2025: <https://survey.stackoverflow.co/2025/technology>
- State of JS 2025, meta-frameworks: <https://2025.stateofjs.com/en-US/libraries/meta-frameworks/>
- @vite-pwa/sveltekit: <https://www.npmjs.com/package/@vite-pwa/sveltekit>

### Layer 2: database, backend and auth
- @supabase/ssr source: <https://github.com/supabase/ssr/blob/main/src/utils/constants.ts>, <https://github.com/supabase/ssr/blob/main/src/cookies.ts>, <https://github.com/supabase/ssr/blob/main/src/createBrowserClient.ts>
- Supabase anonymous sign-ins: <https://supabase.com/docs/guides/auth/auth-anonymous>
- Supabase rate limits: <https://supabase.com/docs/guides/auth/rate-limits>
- Supabase email OTP: <https://supabase.com/docs/guides/auth/passwordless-login/auth-email-otp>
- Supabase email templates: <https://supabase.com/docs/guides/auth/auth-email-templates>
- Supabase custom domains: <https://supabase.com/docs/guides/platform/custom-domains>
- Supabase pricing, compute, backups, regions, RLS: <https://supabase.com/pricing>, <https://supabase.com/docs/guides/platform/compute-and-disk>, <https://supabase.com/docs/guides/platform/backups>, <https://supabase.com/docs/guides/platform/regions>, <https://supabase.com/docs/guides/database/postgres/row-level-security>
- CVE-2025-48757 (community write-up): <https://cvemon.intruder.io/cves/CVE-2025-48757>
- Better Auth docs: <https://www.better-auth.com/docs/plugins/anonymous>, <https://www.better-auth.com/docs/plugins/email-otp>, <https://www.better-auth.com/docs/concepts/cookies>, <https://www.better-auth.com/docs/reference/security>, <https://www.better-auth.com/docs/concepts/rate-limit>, <https://www.better-auth.com/docs/installation>, <https://www.better-auth.com/docs/concepts/users-accounts>
- Better Auth source: <https://github.com/better-auth/better-auth> (published package `better-auth@1.7.7` read directly)
- Vercel acquires Better Auth: <https://vercel.com/blog/vercel-acquires-better-auth>
- Auth.js joins Better Auth: <https://www.better-auth.com/blog/authjs-joins-better-auth>
- Chrome 400-day cookie cap: <https://developer.chrome.com/blog/cookie-max-age-expires>
- Neon pricing, regions, Auth, Databricks: <https://neon.com/pricing>, <https://neon.com/docs/introduction/regions>, <https://neon.com/docs/auth/overview>, <https://neon.com/blog/neon-and-databricks>
- Scaleway Managed Databases pricing and FAQ: <https://www.scaleway.com/en/pricing/managed-databases/>, <https://www.scaleway.com/en/docs/managed-databases-for-postgresql-and-mysql/faq/>
- Aiven pricing: <https://www.aiven.io/pricing?product=pg>
- DigitalOcean managed databases: <https://www.digitalocean.com/pricing/managed-databases>
- Cloudflare D1 pricing and limits: <https://developers.cloudflare.com/d1/platform/pricing/>, <https://developers.cloudflare.com/d1/platform/limits/>
- Turso pricing: <https://turso.tech/pricing>
- Convex regions and plans: <https://docs.convex.dev/production/regions>, <https://www.convex.dev/plans>
- Firebase anonymous auth and pricing: <https://firebase.google.com/docs/auth/web/anonymous-auth>, <https://firebase.google.com/pricing>, <https://cloud.google.com/firestore/pricing>
- PocketBase: <https://github.com/pocketbase/pocketbase/blob/master/core/collection_model_auth_options.go>, <https://pocketbase.io/docs/authentication/>
- EU-US DPF appeal (community): <https://www.dataguidance.com/news/eu-cjeu-admits-microsoft-intervener-appeal-concerning>

### Layer 3: hosting and runtime
- Scaleway product availability: <https://www.scaleway.com/en/docs/account/reference-content/products-availability/>
- Scaleway serverless pricing: <https://www.scaleway.com/en/pricing/serverless/>
- Scaleway containers autoscaling: <https://www.scaleway.com/en/docs/serverless-containers/reference-content/containers-autoscaling.md>
- Scaleway containers on Private Networks: <https://www.scaleway.com/en/docs/serverless-containers/reference-content/containers-private-networks.md>
- Scaleway CRON triggers: <https://www.scaleway.com/en/docs/serverless-containers/how-to/add-trigger-to-a-container/>
- Scaleway instance pricing: <https://www.scaleway.com/en/pricing/virtual-instances/>
- Vercel regions, cron, Hobby, fair use, pricing, fra1 pricing, flat-rate CDN, spend management, Fluid compute, DPA: <https://vercel.com/docs/regions>, <https://vercel.com/docs/cron-jobs/usage-and-pricing>, <https://vercel.com/docs/plans/hobby>, <https://vercel.com/docs/limits/fair-use-guidelines>, <https://vercel.com/pricing>, <https://vercel.com/docs/pricing/regional-pricing/fra1>, <https://vercel.com/docs/pricing/flat-rate-cdn>, <https://vercel.com/docs/spend-management>, <https://vercel.com/docs/fluid-compute>, <https://vercel.com/legal/dpa>
- Cloudflare Workers pricing, limits, cron, static assets, Node.js compatibility, Hyperdrive, data localisation, network: <https://developers.cloudflare.com/workers/platform/pricing/>, <https://developers.cloudflare.com/workers/platform/limits/>, <https://developers.cloudflare.com/workers/configuration/cron-triggers/>, <https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/>, <https://developers.cloudflare.com/workers/runtime-apis/nodejs/>, <https://developers.cloudflare.com/hyperdrive/platform/pricing/>, <https://developers.cloudflare.com/data-localization/faq/>, <https://www.cloudflare.com/network>
- $36,000 Cloudflare bill story (community): <https://ppc.land/developer-faces-36-000-cloudflare-bill-after-queue-loop-post-says/>
- Hetzner: <https://www.hetzner.com/cloud/>, <https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/>, <https://status.hetzner.com/>, <https://www.hetzner.com/cloud/cost-optimized/>, <https://www.hetzner.com/cloud/regular-performance/>, <https://www.datacenterdynamics.com/en/news/german-cloud-firm-hetzner-hikes-prices-by-up-to-50-percent-due-to-drastic-component-price-increases>
- Fly.io pricing and regions: <https://docs.fly.io/about/pricing>, <https://docs.fly.io/reference/regions>
- Railway pricing, regions, limits: <https://railway.com/pricing>, <https://docs.railway.com/reference/regions>, <https://docs.railway.com/reference/usage-limits>
- Render pricing and cron: <https://render.com/pricing>, <https://render.com/docs/cronjobs>
- DigitalOcean pricing: <https://www.digitalocean.com/pricing/app-platform>, <https://www.digitalocean.com/pricing/droplets>
- Netlify pricing and scheduled functions: <https://www.netlify.com/pricing/>, <https://docs.netlify.com/build/functions/scheduled-functions/>
- Deno Deploy pricing: <https://deno.com/deploy/pricing>
- bunny.net Magic Containers: <https://bunny.net/docs/magic-containers/pricing>
- web-push: <https://www.npmjs.com/package/web-push>, <https://github.com/web-push-libs/web-push/issues/718>
- Web Crypto push libraries: <https://github.com/block65/webcrypto-web-push>, <https://cdn.jsdelivr.net/npm/@pushforge/builder@2.0.4/README.md>
- Coolify and Dokploy advisories: <https://github.com/coollabsio/coolify/security/advisories>, <https://github.com/Dokploy/dokploy/security/advisories>

### Safari and cookies (cross-cutting)
- WebKit tracking prevention policy: <https://webkit.org/tracking-prevention/>
- CNAME cloaking defence: <https://webkit.org/blog/11338/cname-cloaking-and-bounce-tracking-defense/>
- IP-address cloaking bug: <https://bugs.webkit.org/show_bug.cgi?id=246477>
- WebKit source: <https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/cocoa/NetworkTaskCocoa.mm>, <https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/cocoa/NetworkTaskCocoa.h>, <https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/cocoa/NetworkDataTaskCocoa.mm>, <https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/NetworkSession.cpp>

### Layer 4: smaller layers
- Scaleway TEM: <https://www.scaleway.com/en/pricing/managed-services/#transactional-email>, <https://www.scaleway.com/en/docs/transactional-email/faq>
- Amazon SES: <https://aws.amazon.com/ses/pricing/>
- Brevo: <https://www.brevo.com/pricing/>
- Mailjet: <https://www.mailjet.com/pricing/>, <https://www.mailjet.com/legal/privacy-policy-old>
- Resend: <https://resend.com/docs/dashboard/domains/regions>, <https://resend.com/pricing>
- Postmark: <https://postmarkapp.com/pricing>, <https://postmarkapp.com/privacy-policy>
- Lettermint: <https://lettermint.co/pricing>
- Plausible: <https://plausible.io/eu-hosted-web-analytics>, <https://plausible.io/>, <https://analytics-alternatives.com/tools/plausible>
- Umami: <https://umami.is/pricing>
- PostHog: <https://posthog.com/pricing>, <https://posthog.com/experiments/pricing>, <https://posthog.com/docs/privacy/data-collection>
- GrowthBook: <https://www.growthbook.io/pricing>, <https://www.growthbook.io/blog/introducing-eu-data-residency>
- Matomo (community pricing): <https://www.stackscored.com/pricing/analytics/matomo>
- Cloudflare R2: <https://developers.cloudflare.com/r2/pricing/>, <https://developers.cloudflare.com/r2/reference/data-location/>
- bunny.net CDN and storage: <https://bunny.net/pricing/cdn/>, <https://bunny.net/pricing/storage/>
- Stripe Managed Payments: <https://docs.stripe.com/payments/managed-payments>, <https://docs.stripe.com/payments/managed-payments/eligibility>, <https://support.stripe.com/questions/managed-payments-pricing>
- Paddle: <https://www.paddle.com/pricing>
- Lemon Squeezy: <https://www.lemonsqueezy.com/pricing>
- Polar.sh fees: <https://polar.sh/docs/merchant-of-record/fees>
- Lithuanian VAT threshold (community): <https://euroref.dev/lt/vat-registration-threshold>
- EU One-Stop Shop: <https://europa.eu/youreurope/business/finance-and-tax/vat/one-stop-shop/index_en.htm>
