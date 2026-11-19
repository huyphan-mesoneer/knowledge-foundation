# Research 4/6: Agent retrieval in a Markdown vault (second brain)

Scope: how agents find and retrieve knowledge in an Obsidian/Markdown vault. Feeds ROADMAP 1.2, 1.4, 1.7 and success criterion S4 (5 "where is X / what did we decide about Y" answers in < 2 min each).

## Executive summary

- **Use agentic search (rg/glob/read) as the v1 retrieval mechanism.** It is the only option that needs no index, no plugin, no sync, and works identically for any agent. Claude Code itself moved from RAG to glob/grep for the same reasons (secondary source, see E1).
- **Retrieval reliability comes from the vault's shape, not the tool.** Four things matter most: one-line summaries that grep can return in bulk, type/status in single-line frontmatter, plain-Markdown hubs that list their children, and unique, stable filenames.
- **Two defects in the current prototype hurt agents directly:** (a) `Home.md` and the other hubs are Bases embeds (`![[projects.base]]`), so an agent reading them sees no list; (b) `tpl-decision` has no TL;DR line and uses properties (`deciders`, `supersedes`, `superseded_by`) that are not in `schema.json`, which breaks AGENTS.md section 4.
- **Do not build an index, embeddings or an MCP server for v1.** Add an LLM-maintained index (Karpathy pattern) only when the vault passes ~300 notes or grep misses in the pilot. Embeddings are a Phase 3 option at most.
- **Ranked retrieval stack for v1:** (1) agentic search over frontmatter + TL;DR + filenames, (2) plain-Markdown hubs/MOCs, (3) LLM-maintained index + log, (4) Obsidian MCP server, (5) embeddings.

## Key findings

### F1. Agentic search beats pre-built retrieval for small-to-medium personal corpora (medium-high confidence)
- Anthropic describes Claude Code's approach: "primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time" (E1).
- Anthropic recommends a hybrid: small always-loaded instruction files, everything else on demand. "The hybrid strategy might be better suited for contexts with less dynamic content" (E1). A personal vault is dynamic, so on-demand search fits better than pre-loading.
- Anthropic's RAG article says that if the knowledge base is under ~200k tokens, put all of it in the prompt (E2). A personal vault will likely exceed this by 1-3 years of use (my estimate: 500 notes x ~600 tokens is ~300k). So agents need search, not full loading, and the 200k threshold is a planning marker, not a v1 need.
- Exact-identifier matching is where BM25/grep beats embeddings. Anthropic reports hybrid embeddings + BM25 beats embeddings alone, and BM25 handles exact technical strings (E2). Personal-note queries are often exact names ("Checkout revamp", "DEC Postgres"), which favors grep.
- Limit: the Claude Code evidence is a code corpus, interview-sourced (E3). No public benchmark compares grep and embeddings on prose notes. Treat as a reasoned default, not proof. S4 pilot is the test.

### F2. Anthropic's context guidance names the exact signals this vault already uses (high confidence, primary source)
- "Folder hierarchies, naming conventions, and timestamps all provide important signals" and timestamps "can be a proxy for relevance" (E1).
- Structured note-taking: the agent "regularly writes notes persisted to memory outside of the context window" and pulls them back later (E1). This is the mechanism behind `agent-log.md` and any owner-context file (F7).

### F3. Karpathy's LLM Wiki: index file first, search later (high confidence on pattern, medium on scale claims)
- Three layers: immutable raw sources, LLM-owned wiki pages, schema file (AGENTS.md/CLAUDE.md). Two special files: `index.md` (catalog: link + one-line summary per page, updated on every ingest) and `log.md` (append-only, greppable prefixes) (E4).
- At query time the agent reads `index.md`, picks pages, reads them. Karpathy says this "works surprisingly well at moderate scale" and avoids embedding RAG; search is added "as the wiki grows" (E4).
- Costs: every ingest must touch the index (a 10-15 page fan-out per source in his example). That is the drift risk. For a personal vault with humans editing, a hand-maintained global index goes stale quickly. Hub notes (F4) get most of the benefit with less upkeep.
- Lint step (orphans, stale claims, missing links) maps onto this vault's weekly review and `lint.py`.

### F4. Hubs/MOCs that list children are the cheapest index (high confidence, convergent)
- llms.txt: an H1, a one-line summary blockquote, H2 sections of `- [name](link): note`, optional section for secondary items; designed so agents read one small file and follow links only when needed (E5). Same design principle as hub notes.
- Karpathy's index and this vault's roadmap draft both say: hubs list key children explicitly (E4; design/linking.md section 4).
- Gap: the prototype hubs are Bases embeds. In `Home.md` an agent sees `![[projects.base]]`, not the projects. Bases are queryable for humans and need Obsidian to render; agents see only the view definition (E6 documents Bases as frontmatter-driven views). Fix: each hub keeps a plain list of `[[links]]` (can be generated or hand-written), with Bases as the human view on top.

### F5. Frontmatter is a query surface only if it is one-line and typed (high confidence, local evidence)
- `rg -l "^type: decision"` and `rg -l "^status: active"` work only when each property is on one line. Multi-line YAML lists break line-based search. The current templates use one-line flow arrays (`related: []`, `tags: [decision]`), which is correct; keep this as a rule.
- Bases and Dataview read the same properties (E6), so the frontmatter serves humans and agents with no duplicate data.
- `aliases` is a real Obsidian property (E7). It is the cheapest answer to synonyms ("Dashboard" for Home, "AI" for "Artificial intelligence"). Obsidian does not document how aliases affect search (E7), so do not rely on Obsidian search for aliases; agents must grep `^aliases:` explicitly.

### F6. Summary lines: one standard, grep-able across the vault (high confidence, local evidence)
- Every knowledge note has `> **TL;DR**` (tpl-note) and that line is designed to be "relied on without reading further." One `rg -n "TL;DR"` call returns a summary of every knowledge note. This is the cheapest "index" available.
- Gap: `tpl-decision` has `> **Decision:** one sentence` instead. Same purpose, different marker, so the search misses decisions. Fix: one marker (`> **TL;DR**`) in all knowledge and record templates.
- Do not add a second `summary:` frontmatter field. It duplicates the TL;DR (DRY), and two summaries drift apart.

### F7. Memory about the owner: a small, owner-curated file (medium confidence)
- Agents need owner context that is not in notes: abbreviations, synonyms, role, active focus, output preferences. Claude Code auto memory loads only the first 200 lines or 25 KB at session start, and "the more specific and concise your instructions, the more consistently Claude follows them" (E8). Keep the always-loaded layer small.
- Recommend one owner-maintained file, e.g. `_system/owner-context.md` (<= 100 lines): glossary (term -> canonical note), synonyms, current focus, preferences. Owner edits it; agents may append suggestions under a heading, never rewrite. This fits the existing `_system` rule ("change only when asked") and avoids an agent-written memory store that nobody reviews.
- Keep this file out of any team/shared context. The vault is private (ROADMAP D4), so this is acceptable.

### F8. Folder moves and renames break path-based retrieval, not wikilinks (high confidence, from linking.md and Obsidian behavior)
- Obsidian resolves `[[Name]]` by filename across the vault, so moving a file keeps wikilinks working as long as names are unique. Obsidian updates links on in-app renames; renames by agents or scripts do not (design/linking.md section 1).
- Path-based retrieval breaks on moves: `grep ... 20-projects` misses archived items; a hub that lists `20-projects/X/spec.md` as a path goes dead. AGENTS.md section 8 commands are folder-scoped, which is right for "active projects" and wrong for "where is X".
- Rule: "where is X" and "what did we decide" searches run over the whole vault, including `90-archive/`. Folder only narrows when the question is about one lifecycle stage.
- Archive status: on archive, set `status` to its final value (`done`, `cancelled`, `superseded`) so a property filter finds it regardless of path.

### F9. Embeddings and plugins: real cost, unclear value for v1 (medium confidence)
- Smart Connections uses local embeddings, and its README warns that a note with the exact query text may not appear if it is not semantically similar (E9). Exact-string lookup still needs ordinary search.
- Secondary sources report a license change in early 2026 and an MCP bridge that exposes the index at block level. Unverified; check directly before any use (E9).
- Plugin budget S6 is <= 5 in the default stack. A semantic plugin takes one slot and adds a sync/privacy question for no proven gain on a personal vault.
- Obsidian MCP servers (MCPVault, cyanheads, getglad) add property search and write tools (E10). Currency is unverified (search results show no 2026 dates). They are per-tool, so they break agent-agnosticism (ROADMAP D5). Phase 3 optional.

### F10. Decision records: findable if the status chain is explicit (high confidence, local evidence)
- Questions like "what did we decide about Y" need: type filter -> term match -> prefer `status: accepted` -> follow `superseded_by`.
- Gap: `supersedes` and `superseded_by` are in tpl-decision but not in `schema.json` (optional list: status, updated, author, tags, related, aliases, source, roles, visibility). `deciders` is also not in the schema. This violates AGENTS.md section 4 ("never invent properties" in ROADMAP 1.7) and means lint.py may flag them. Fix: add them to the schema, or drop them and use `related`.
- `supersedes: ` with an empty value parses as null in YAML. Fine for grep, but use `[]` or a quoted link to match the flow style.

## Evidence (URLs)

- E1. Anthropic, "Effective context engineering for AI agents": https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (primary; glob/grep just-in-time, hybrid strategy, folder/naming/timestamps as signals, structured note-taking).
- E2. Anthropic, "Contextual Retrieval": https://www.anthropic.com/engineering/contextual-retrieval (primary; failure-rate numbers on a document corpus: contextual embeddings -35%, + contextual BM25 -49%, + reranking -67%; hybrid beats embeddings alone; under ~200k tokens include whole KB). Numbers are for document chunks, not personal notes.
- E3. Claude Code agentic search origin, secondary: Pragmatic Engineer newsletter with Boris Cherny: https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny?open=false (states agentic search "is really just glob and grep, and it outperformed RAG"). Analysis: https://yage.ai/share/why-coding-agents-still-use-grep-en-20260327.html (AI-generated, labeled as such; cites Cursor's observation that rg can exceed 15 s in very large monorepos, which does not apply to a personal vault).
- E4. Karpathy, "LLM Wiki" gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (primary; index.md, log.md, ingest/query/lint, search added at scale). Secondary summaries: https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/ . A commenter cites studies that LLM-only-maintained markdown degrades quality; unverified.
- E5. llms.txt proposal: https://llmstxt.org/ (format: H1, blockquote summary, H2 link lists with one-line notes, optional section).
- E6. Obsidian Bases syntax: https://help.obsidian.md/bases/syntax (frontmatter values read as note properties; views are definitions, not lists).
- E7. Obsidian aliases: https://obsidian.md/help/aliases (aliases are a YAML list property; search behavior not documented).
- E8. Claude Code memory (CLAUDE.md, auto memory, 200 lines / 25 KB load limit, "more specific and concise... more consistently"): https://code.claude.com/docs/en/memory
- E9. Smart Connections README: https://cdn.jsdelivr.net/gh/brianpetro/obsidian-smart-connections@main/README.md (local embeddings; exact-match caveat). License/MCP claims come from secondary reviews only.
- E10. Obsidian MCP servers (search results, not fetched individually): https://glama.ai/mcp/servers/getglad/obsidian_mcp/tools/search_by_property ; https://github.com/mcp-research/cyanheads__obsidian-mcp-server
- Local: `AGENTS.md`, `_system/schema.json`, `_system/templates/tpl-decision.md`, `_system/templates/tpl-note.md`, `Home.md`, `design/linking.md`, `ROADMAP.md` (sections 1.2, 1.4, 1.7).

## Trade-off matrix (retrieval options for v1)

| Option | Setup cost | Maintenance | Exact-name lookup | Synonym/semantic lookup | Staleness | Agent-agnostic | Fit for v1 |
|---|---|---|---|---|---|---|---|
| A. Agentic search (rg + frontmatter + TL;DR) | none | none | strong | weak (needs aliases/glossary) | none (reads disk) | yes (plain text) | high |
| B. Plain-Markdown hubs/MOCs | low | medium (append on create) | strong (one read) | medium (human-curated) | drifts if not updated | yes | high (with A) |
| C. LLM-maintained index.md + log.md | low | high (touches many pages per ingest) | strong | medium | high risk | yes | defer (>300 notes) |
| D. Obsidian MCP server | medium (install, Local REST or FS) | low | strong (property search) | weak | none | no (per-tool) | Phase 3 optional |
| E. Embeddings (Smart Connections etc.) | medium (plugin, model) | medium (re-index, model change) | weak (can miss exact text) | strong | low-medium | no (Obsidian-only) | defer; plugin budget |

## Ranked recommendation

1. **Agentic search over the vault as the default** (option A). Zero infra, matches the one production evidence point, works for any agent.
2. **Plain-Markdown hubs listing children** (option B). Biggest gain per unit of effort. Every hub gets a visible `## Contents` list of `[[links]]`, Bases views stay below it.
3. **Owner-context file** (F7) for synonyms and glossary, because agentic search fails on vocabulary, not on structure.
4. **LLM-maintained index + log** (option C), but only after the pilot shows hubs are not enough, or at ~300 notes.
5. **MCP server** (option D) as an optional Phase 3 add-on, never a requirement.
6. **Embeddings** (option E): drop from v1. Revisit only if the S4 pilot fails on synonym-type questions after the glossary is in place.

## Recommendations

### R1. Required retrieval properties (all knowledge and record types)
- `type`, `created`, `status` (where the type defines statuses), `related` (one hub link), `tags` (flow list).
- `updated` for any note an agent edits.
- `aliases` (optional, but recommended for project, person, and any note with a codename or acronym).
- Single-line values only. No multi-line YAML lists.
- Summary: body `> **TL;DR**` line, one standalone sentence, <= ~200 characters, first thing after the H1. Required in tpl-note, tpl-decision, tpl-incident, tpl-runbook, tpl-howto, tpl-spec, tpl-prd, tpl-reference, tpl-debug-log.

### R2. Hub and index conventions
- Every hub (project, area, MOC) has a `## Contents` section listing children as `- [[Note]] — TL;DR-style one-liner` (hand-written or agent-appended). Bases views go below it, never instead of it.
- Home.md gets the same: a plain list of active projects and areas, not only embeds. Update in the same change as project status changes.
- `MOC` notes are topic hubs; a note with no hub is an orphan and fails lint (AGENTS.md section 4). Keep the rule; the lint check should look for `[[` links in `related` or body.
- Do not build a global `index.md` in v1 (YAGNI, drift risk). Revisit at ~300 notes.
- `_system/owner-context.md`: glossary (term -> `[[canonical note]]`), synonyms, current focus, preferences. Owner-edited; agents append suggestions only.

### R3. Naming rules
- Filename = title = unique across the whole vault, including `90-archive/`. Check uniqueness before `new_note.py` creates a file; reject duplicates.
- Type prefixes (`DEC`, `INC`, `DBG`, `RUNBOOK`, `SPEC`, `PRD`, `STORY`, `MOC`) are allowed because `ls | rg " DEC "` finds all decisions in one call. Do not add prefixes to plain notes.
- Date prefix (`YYYY-MM-DD`) only for time-stamped records and meetings; it gives chronological `ls` and "latest decision" queries for free.
- Use stable names. Agents never rename. If a rename is unavoidable, rg for the old name across the vault in the same change, and use `aliases` to keep the old name findable.
- Avoid generic titles ("Notes", "Meeting", "Decision") that collide across folders.

### R4. Search strategy for agents (ordered; stop when answered)
1. Orient: read `_system/vault.json`, `_system/schema.json`, `owner-context.md`, last 20 lines of `agent-log.md`. (Matches AGENTS.md section 1; add owner-context.)
2. Exact name and alias: `ls -R` or glob for the term in filenames; `rg -il "^aliases:.*<term>" --include=*.md .`
3. Type and status filter: `rg -l "^type: decision" .` intersected with `rg -l "^status: accepted"`, and with a term: `rg -il "<term>"` on that list.
4. Summary scan: `rg -n "TL;DR" --include=*.md .` returns one-line summaries for all knowledge notes in one call; pick at most 5 candidates.
5. Keyword fallback: expand the term with owner-context synonyms, then `rg -il "<term1>|<term2>" .` (search whole vault, including `90-archive/`).
6. Hub walk: open the relevant hub's `## Contents`, follow 1-2 `[[links]]` hops.
7. Read the full candidate notes only now. For decisions read `## Outcome`; if `status: superseded`, follow `superseded_by` to the current one.
8. Answer with the file path, its `updated` date, and the TL;DR. If nothing matches after steps 2-6, say "not found" and list the searched terms. Never invent a note or a link.
- Target: 5 questions in < 2 min for an agent means at most ~6 tool calls per question. Steps 2-4 should resolve most questions in 2-3 calls.

### R5. Keep the always-loaded layer small
- AGENTS.md is the rule source. Keep it under ~150 lines; move examples and per-type detail into `_system/` files that agents open on demand.
- `owner-context.md` <= 100 lines. Hub `## Contents` lists stay under ~30 items; split the hub (sub-MOC) past that.

### R6. Schema hygiene (fixes found in this review)
- Add `supersedes`, `superseded_by`, `deciders` to `schema.json` optional list, or remove them from tpl-decision and use `related`. Pick one; recommend adding `supersedes` and `superseded_by` (needed for the status chain), dropping `deciders` (YAGNI for personal vault).
- Unify the decision marker: `> **TL;DR**` replaces `> **Decision:**`, or keep both if the decision line is needed for humans, but the TL;DR must exist.

## What to avoid

- Bases-only hubs with no plain-text list (agents see empty embeds).
- Folder-scoped search for "where is X" or "what did we decide" (misses `90-archive/`).
- Multi-line YAML lists, nested frontmatter, or values that span lines (break `rg -l`).
- A second summary field next to the TL;DR (drifts).
- Path-based links in hubs (`20-projects/...`). Use `[[Name]]`.
- Renaming files outside Obsidian, or agents renaming at all.
- Global index.md maintained by agents on every ingest in v1 (drift, high upkeep).
- Embeddings or a semantic plugin as a v1 dependency (plugin budget, exact-match misses, sync/privacy).
- An agent-written memory store that the owner does not review. Keep owner context owner-curated.
- Unprefixed, generic, or duplicate titles.

## Limitations

- No retrieval benchmark run on this vault. Ranking is from source evidence and reasoning; the S4 pilot (5 questions, timed) is the real test. Suggest recording: which step of R4 answered each question, and tool calls used.
- Claude Code grep-over-RAG evidence comes from an interview as relayed by secondary sources. Anthropic's primary docs confirm the approach but give no comparative numbers.
- Anthropic's Contextual Retrieval numbers are for document chunks, not personal notes.
- Karpathy's gist is primary; its scale claims ("moderate scale") are unquantified. Lint and fan-out costs are from his description, not measured.
- Not verified: Basic Memory (fetch returned 404), Anthropic memory tool docs (redirect not followed), Khoj, Copilot for Obsidian. Did not evaluate them; they are not in the ranking.
- Obsidian MCP and Smart Connections currency and licensing are unverified (search results only; no 2026 release dates seen).
- Did not read every template (only tpl-decision and tpl-note). Other templates may have the same marker and schema gaps; check before implementing R1 and R6.
- Tool note: a Bash call was blocked by an auto-mode hook during this research. I used Read for file access; results are unaffected.

## Unresolved questions

1. Should the TL;DR be mandatory for `meeting`, `person`, `project` and `area` hubs too? Current drafting: knowledge and record types only.
2. Is `_system/owner-context.md` acceptable under the `_system` rule ("change only when asked")? Proposal: owner-created, agents append only under a heading.
3. Should hub `## Contents` be hand-written or agent-maintained, given the "append only" rule for human-authored notes (AGENTS.md section 6.2)?
4. Keep `deciders` in tpl-decision or drop it? Recommendation: drop (YAGNI), but owner decides.
5. What counts as "answered" for S4: a path plus TL;DR, or the specific fact? Affects how strict the pilot is.
6. Does lint.py check for orphans via body `[[links]]` or only `related`? Needs a read of lint.py before R2 changes.

**Status:** DONE_WITH_CONCERNS
**Summary:** Agentic search (rg over frontmatter, TL;DR lines, filenames) with plain-Markdown hubs is the ranked v1 retrieval stack; embeddings, MCP servers and a global LLM-maintained index are deferred. Prototype defects found: Bases-only hubs are opaque to agents, tpl-decision lacks TL;DR and uses properties missing from schema.json.
**Concerns/Blockers:** Claude Code grep-over-RAG evidence is secondary (interview relayed by blogs); no retrieval benchmark run on this vault; Basic Memory and Anthropic memory-tool docs not verified; plugin currency and licenses unverified. Report: /Users/huyphan/projects/github.com/huyphan-mesoneer/knowledge-foundation/plans/reports/researcher-4-261119-2040-agent-retrieval-second-brain-report.md
