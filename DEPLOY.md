# DEPLOY.md — Brick & Basil (brick-basil-apex)

Built 2026-11-24 by the websites desk. Template v2 multi-page (9 core pages + menu + privacy + 404/thanks = 12 pages), demo host, noindex. Card t_a4dde0e9.

## Live
- Preview: https://brick-basil-apex-demo.up.railway.app (meta noindex per page + X-Robots-Tag `noindex, nofollow` header verified via curl -I)
- Railway: carrier project the-plain-bar `604a72a9-09eb-4169-920d-e64619651640` (co-hosted — account project cap, dead-shell precedent), service `brick-basil-apex-demo` id `9905797e-f1b0-4e87-9371-d6a7ff4f7d84`, deployment `bd8b5a06-d86c-4c86-aa9a-1b1c0a55e824` (SUCCESS 30s)
- Domain id `885dd128-b8d1-47e4-a8d3-95cbf8556148` → brick-basil-apex-demo.up.railway.app (generated post-healthy, renamed via domain update)
- GitHub: https://github.com/gnaritas/brick-basil-apex (public, no secrets)
- Forms → Brevo HTTP API v3 (BREVO_API_KEY set xkeysib-onward via `railway variable set --stdin`), server.js from salty/tidys funnel-format lineage: OPEN/CONTACT/MAILSENT JSON lines

## Gotchas learned this build (2026-11-24)
- First `railway api 'mutation{serviceCreate(...)}'` attempt returned an id that resolved to **Not Authorized** on direct query and was absent from a full 61-project service sweep minutes later — while a domain walk had briefly served 200s. Lesson: after ANY serviceCreate, re-prove the service by GraphQL project→services sweep + host walk before bookkeeping; do not trust a one-shot create output in a co-host project. Second create (9905797e) verified end-to-end instead.
- `railway api` GraphQL on this account: root `projects(first:N)` returns Not Authorized (workspace-scoped) — use CLI `railway project list --json` for the sweep; `service(id:)` direct also Not Authorized for co-hosted services; scope everything through `project(id:...){services(first:N)}`.
- Co-host siblings unaffected: after all domain surgery, salty/finders/capitol hosts re-probed 200 + own brand titles ✓ (multi-service project teardown/dogma unchanged: serviceDelete only, never project delete).

## Verified
- `_verify.py` local gate: PASS, 0 fails, 12 pages, noindex per page.
- Live curl walk: 10/10 content routes 200 + correct content-type; /nope-route 404 branded; /healthz 200; /open 200 image/gif sha == public/pixel.gif; og.png 200 56KB; X-Robots-Tag via curl -I ✓.
- Form relay end-to-end on the LIVE host: POST /contact → 303 → /thanks; service logs CONTACT + MAILSENT (2026-11-24 22:22Z); OPEN log with t-token proven (t=brick-basil-apex-t1 pre-test).
- Render sweep (mandatory): 24 full-page captures (12 pages × 1280/390) via real Chrome — DOM gates RESULT PASS, overflow_px=0 everywhere, console errors clean (404's expected status line aside), titles/h1s from rendered DOM match served bytes.
- Vision battery: 24 scale-1 shots via threaded OpenRouter gemini-2.5-flash — 24/24 VERDICT: CLEAN (results: sites/brick-basil-apex/vision-results.json).
- Map embed: container rects 558px desktop / 352px mobile (≥200px gate ✓), embed resource curl -L 200 → google.com/maps/embed pb-string carries the published Suite-4 address.
- Copy is evidence-traced: sites/brick-basil-apex/evidence.json claims ledger (press Business Debut 2026-11-24 + owner FB intro); zero invented facts — no hours, no opening date beyond "opening early 2027".

## Pitch
- Script: `~/.hermes/projects/websites/_pitch_brick-basil-apex.send.py` (salty-lineage clone: envelope-resume guard, no-redirect brand∧town liveness, physical-line events mirror; trap greps clean: no v4 wrapper, no line_no=pitches). check-only PASS words=99 links=2 guard=homonym_guard-only mx=ok liveness=claims-hold (301s = parked).
- Recipient: info@brickandbasilnc.com — self-published on shop's own FB Page intro (provenance on card); inbox on Google infra (domain MX = smtp.google.com); RCPT probe inconclusive (Google throttles probe conns) — same class as 3 delivered Gmail sends 11-24.
- Offer: founder bundle $249 + $39/mo, 31-day trial. Token brick-basil-apex-t1 on both links + pixel; arm coin sha256(slug)%2=1 → v7 subject "Website demo for Brick & Basil"; shop_tz America/New_York seeded; t2 2026-12-03, mature 2026-12-10.
- Send state: parked 2026-11-24 14:3x PST — owner-local 17:32 EST out of 07:00–17:00 window; SCHEDULED_UNTIL 2026-11-25T07:30:00-05:00.
