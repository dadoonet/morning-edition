# Morning Edition — daily spec

Owner: DJ Elky (Java developer, DJ). Timezone Europe/Paris. Runs daily at 07:00.

## Curation (HN front page https://news.ycombinator.com/, top 10)
- Lean into: AI tools, creative software, dev tools, privacy/security, weird science, anything actionable.
  Also: Java/JVM/Spring, DJ software and audio, search/Elasticsearch/vector databases.
- Skip: business/funding/ads/marketing, job posts, pure politics, Ask HN fluff.
- WebFetch each chosen story before writing about it. Only state facts you actually retrieved;
  if a page is blocked or JS-only, say so on the spread instead of guessing. Paraphrase, no long quotes.
- Flag stories that directly apply to him with a ".foryou" box: a "For you" tag + one concrete action.
  Be honest about conditions ("if you run Ubuntu...").

## Format
- One self-contained file `magazines/YYYY-MM-DD.html` (Paris date). Style reference: the newest file in `magazines/`
  (copy its CSS system, but vary colours/layout each day; keep fonts Fraunces + Inter via Google Fonts).
- Cover/masthead with the 10 cover lines, then 10 spreads, each with a distinct background, layout and numeral
  treatment (hero outline numeral, rose alert stamp, terminal, midnight, academic drop-cap, specimen, timeline,
  cards, grid, big-stat finish — rotate/reinvent). Each links to the original and to the HN thread.
- NO small fonts: nothing below 19px computed. Verify with a headless-Chrome check.
- Then run `python3 scripts/build_index.py`, commit (`Morning Edition YYYY-MM-DD`), push to `main`.

## URL
https://dadoonet.github.io/morning-edition/magazines/YYYY-MM-DD.html
