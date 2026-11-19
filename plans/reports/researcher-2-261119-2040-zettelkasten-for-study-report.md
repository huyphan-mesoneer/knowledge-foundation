---
created: 2026-11-19
angle: 2 of 6 — Zettelkasten / evergreen notes for study
status: research input for Phase 1.2 (no decision made)
---
# Zettelkasten for study: note types, titles, IDs, linking

## Executive summary

- Study layer needs **no new method**. Ahrens' three note tiers map onto types the schema already has: fleeting → `00-inbox`, literature → `reference`, permanent → `note`, structure → `moc`. Add nothing for v1.
- **Claim-style titles for `note` only** (complete phrase, one idea). Topic titles for `moc`, `reference`, `person`, `howto`. Fill the findability gap with `aliases` and a TL;DR.
- **No Zettelkasten IDs or Folgezettel.** Readable unique names + links do the job. IDs add lookup friction and no retrieval gain in Obsidian.
- **Linking minimum: 1 hub, plus 1 concept link when a real one exists.** "Densely linked" (Matuschak) is an aspiration, not a creation-time rule for busy professionals. Enforce "no orphans" via lint, not "dense links".
- **Collector's fallacy** is the main failure risk. Mitigate with a "my take / extracted notes" gate on `reference`, not with more types.
- **AI retrieval:** atomic + claim-titled notes are a good retrieval unit (title scan is cheap; in-note TL;DR works as context prefix). Cost: answers spanning several notes need link traversal, and sentence titles match topic-word queries poorly. Evidence is analogical; no controlled study of Zettelkasten notes vs chunked RAG found.

## Key findings

### 1. Ahrens' tiers map cleanly to the existing schema

| Ahrens (2017) | Function | Vault equivalent (already in `_system/schema.json`) |
|---|---|---|
| Fleeting note | Disposable capture | `inbox` (process ≤ 7 days, per AGENTS.md §7) |
| Literature note | Summary of a source, own words, bib details | `reference` (status `to-read/reading/done`) |
| Permanent note | Own-words idea, understandable out of context, linked into the box | `note` (status `seedling/growing/evergreen`) |
| Structure / index note | Entry points into the box | `moc` |
| Project note | Output-bound | `project` (PARA, see angle 1) |

Caveat: secondary sources say Ahrens uses "literature" and "permanent" inconsistently; the book itself was not read in full. Schema mapping stands on its own logic, not on Ahrens' exact wording.

### 2. Evergreen-note principles (Matuschak)

- **Atomic** and **concept-oriented**: "It's best to factor Evergreen notes by concept (rather than by author, book, event, project, topic, etc)." Source-bound notes "don't combine with the old ones", so no accumulation. This argues against one note per book. The `reference` note stays source-bound; ideas go to `note` files keyed by concept.
- **Titles as APIs**: "When Evergreen notes are factored and titled well, those titles become an abstraction for the note itself." Three rules: separation of concerns (atomicity), complete-phrase titles "to sharpen claims", positive framing ("Prefer positive note titles to promote systematic theory").
- **Exception Matuschak himself uses**: lexical titles for coined terms and outline notes. Propositional titles are the default for evergreen notes, not a universal rule.
- **Dense linking**: "lots of links", fine-grained associations, tags are "an ineffective association structure". Gives no number. Links are described as review mechanism and a cost the author accepts. Matuschak also says you can link to a stub before writing it.
- Ahrens' question shift: "Under which topic do I store this note?" → "In which context will I want to stumble upon it again?" This is the argument for concept files over source files.

### 3. Collector's fallacy

- Ahrens' term for saving information and feeling it is learned. Forum consensus: "to know about something" ≠ "knowing something".
- Risk in this vault: `reference` notes (status `to-read`) pile up with no extracted notes. The template already has "My take" and "Follow-ups" with an unchecked box, which helps.
- Abandonment: "most people abandon by month three" appears only in an unsourced HN thread. Adobe's guide says many abandon before seeing benefit. Treat abandonment as plausible, not measured.

### 4. Folgezettel / IDs

- Forum consensus: Luhmann IDs are "no more meaningful than date IDs" unless every new note is filed behind its closest relative. Digital archives that use IDs usually replace them with real links ("for a digital note archive it is best to realize note sequences via actual links rather than Folgezettel-style IDs").
- Folgezettel "strips meaning from hierarchy" (one forum view); structure is better carried by links and MOCs.
- For an Obsidian vault, `[[Title]]` already is a stable, readable ID. Filename uniqueness (linking.md §4 rule 2) is the only constraint needed.

### 5. AI-agent retrieval: pro / con

**Pro**
- Atomic notes ≈ pre-chunked retrieval units. Chroma's chunking study: "RecursiveCharacterTextSplitter at 200 tokens with no overlap performs well"; recursive 400 tokens no overlap scores 89.5 recall at k=5. Typical atomic note sits in this range, so the unit is already sized correctly. Chroma also notes "some strategies outperform others by up to 9% in recall", so chunk boundaries matter more than size alone.
- Claim titles let an agent judge relevance from the file list (linking.md §5 step 1 already relies on listing names). A sentence title says what the note concludes, which an agent can use without opening it.
- Anthropic's contextual retrieval: chunks without context fail more. Prepending a 50–100 token situating context cut top-20 failure from 5.7% to 3.7% (embeddings alone) and 2.9% (with contextual BM25). A note with `# Title` + TL;DR gives the same context for free, written by the human.
- A-Mem (NeurIPS 2025) builds Zettelkasten-style linked memory for LLM agents and reports gains over baselines. Relevant as direction, but it generates its own links and attributes, so it does not validate hand-written vault notes.

**Con**
- Answers that span several atomic notes need traversal (MOC → note → link → note). An agent that stops after the first hit gives a partial answer. Hubs/MOCs must list children explicitly (linking.md §4 rule 4).
- Sentence titles have low lexical overlap with topic queries ("what do we think about X" vs "Retries should be idempotent by default"). Keyword search on titles misses; full-text search on body works. Mitigate: `aliases` + a TL;DR with the topic keywords.
- Filename rules in AGENTS.md (`/ \ : * ? " < > | # ^ [ ]` forbidden) constrain claim titles. Claims often want `:` or `?`. Needs a rewording convention or the rule must be checked against the title style.
- Over-atomization: too-small notes lose context that chunking research flags ("recall can peak before relevant information gets diluted" applies in both directions).
- Evidence gap: no controlled test of Zettelkasten-style vault notes vs chunked RAG on personal notes. Practitioner reports are mixed ("alright, but not good enough" for RAG over zettelkasten cards).

### 6. Options compared (ranked)

**Title style (for `note` type)**

| Rank | Option | Performance (retrieval) | Complexity | Maintenance | Human findability | Fit |
|---|---|---|---|---|---|---|
| 1 | Claim titles + `aliases` + TL;DR with topic keywords | High for agent scan; medium for human search | Low (rule + one property) | Low | Medium (aliases fix most) | Best fit: reuse signal, matches schema |
| 2 | Topic titles + mandatory claim TL;DR | Medium (keyword hits; claim in body) | Lowest | Low | High | Fallback if pilot S4 fails |
| 3 | Zettelkasten IDs + topic/claim title | Neutral (IDs not searched by people) | Medium (ID generation, lookup) | Medium | Low | Reject |

**Linking minimum for `note`**

| Rank | Rule | Pros | Cons |
|---|---|---|---|
| 1 | ≥1 hub (MOC/project/area) mandatory; ≥1 concept link if one exists; lint flags zero-link notes | Matches linking.md §4; cheap; avoids orphans | Weaker "emergent" graph early |
| 2 | Dense linking target (e.g. ≥3 outgoing) | Richer graph, more review value (Matuschak) | Friction → abandonment; links created to satisfy a count |
| 3 | No linking rule (hub optional) | Zero friction | Orphans; agents cannot traverse |

**Study note type set**

| Rank | Set | Verdict |
|---|---|---|
| 1 | Existing: `note`, `reference`, `moc` (+ inbox) | Enough. Adds no types. |
| 2 | Add `learning-log` type | Only if pilot shows daily notes can't hold study progress (YAGNI now) |
| 3 | Separate `fleeting`/`literature`/`permanent` folders | Duplicates inbox/reference/note; breaks PARA lifecycle folders. Reject. |

### 7. How study notes connect to PARA work notes

- **Concept notes live in `40-knowledge/` regardless of trigger.** A concept learned for a project still goes to `note`, not into `20-projects/<X>/`. Keeps concept-oriented accumulation (Matuschak).
- **Project notes link to concepts**; concepts do not link to project status. Project-specific application (the "how we use it here") goes in the project note, linked to the concept.
- **Area hub `Learning`** (roles: `everyone` → `Career and growth`, `Learning`) is the hub for study MOCs. Each study topic MOC links to the area hub. Satisfies the one-hub rule.
- **Work decisions** (`decision`) cite concept notes in `related`; concept notes do not need to backlink.
- Trigger rule for agents: when a work note cites an idea twice or more, propose a `note` (suggest only; no auto-creation).

## Concrete recommendations for this vault

1. **No new note types for v1.** Map fleeting/literature/permanent/structure to `inbox`/`reference`/`note`/`moc`. Add to the roadmap §1.2 decision log.
2. **`note` titles are claims**, complete phrase, ≤ ~10 words, no forbidden filename characters (rewrite `:`/`?` forms). Example: "Retries need idempotency keys" not "Retries" or "Retry: idempotency".
3. **`moc`, `reference`, `person`, `howto`, `runbook` keep topic/name titles.** `howto`/`runbook` keep their existing prefixes.
4. **Add `aliases: []` to `tpl-note.md` and `tpl-reference.md`** (native Obsidian property). Use it for the topic term a human would search for. Small change; re-check against the design doc before implementing.
5. **TL;DR must contain the topic keyword(s)** as well as the claim. Gives both lexical and semantic hooks for agents.
6. **No IDs, no Folgezettel.** Unique readable filenames only (linking.md §4 rule 2 is sufficient).
7. **Linking minimum:** `note` must have 1 hub link (required) and should have ≥1 concept link. Lint warns on zero outbound links; no count target.
8. **Collector's fallacy gate:** a `reference` moves from `reading` → `done` only when it has ≥1 linked `note` or a filled "My take". Weekly review (AGENTS.md §7) lists `reference` notes in `to-read` older than 90 days.
9. **Concept-first placement:** study concepts in `40-knowledge/`, never duplicated per source. One `reference` per source; concepts extracted once, linked from many.
10. **Pilot metric** (add to S4 test): time to find 5 study concepts by title and by topic keyword. If topic-keyword search fails, fall back to rank-2 title option.

## Limitations

- Ahrens' book not read in full; its terminology cross-checked only via secondary summaries and forum threads. The collector's-fallacy attribution rests on secondary sources.
- zettelkasten.de pages were summarized via a fetch tool, not read verbatim. Several Luhmann-specific claims are forum-sourced.
- A-Mem: venue and abstract confirmed (NeurIPS 2025); arXiv ID not verified.
- Chroma numbers: primary page fetched; some secondary blogs quote different figures. Only primary numbers used here.
- No empirical data on Zettelkasten abandonment rates or on retrieval quality of personal vaults vs RAG. Recommendations on linking count and title style are judgment plus analogy, not measured.
- Did not evaluate Obsidian plugins (out of scope; Phase 1.x).

## Sources

- Matuschak, "Evergreen notes" (principles incl. atomic, concept-oriented, densely linked): https://notes.andymatuschak.org/Evergreen_notes
- Matuschak, "Evergreen notes should be concept-oriented": https://notes.andymatuschak.org/Evergreen_notes_should_be_concept-oriented
- Matuschak, "Evergreen notes should be densely linked": https://notes.andymatuschak.org/Evergreen_notes_should_be_densely_linked
- Matuschak, "Evergreen note titles are like APIs": https://notes.andymatuschak.org/Evergreen_note_titles_are_like_APIs
- Matuschak, "Prefer note titles with complete phrases to sharpen claims": https://notes.andymatuschak.org/Prefer_note_titles_with_complete_phrases_to_sharpen_claims
- Matuschak, "Prefer positive note titles to promote systematic theory": https://notes.andymatuschak.org/z63PA5ATVi8oyhyLgeGvL3p
- Zettelkasten.de overview (summary via fetch, principles of identity and connectivity): https://zettelkasten.de/posts/overview/
- Zettelkasten forum, Ahrens note types / collector's fallacy: https://forum.zettelkasten.de/discussion/comment/14175/ and https://forum.zettelkasten.de/discussion/comment/14298
- Zettelkasten forum, IDs vs date IDs: https://forum.zettelkasten.de/discussion/comment/15009
- Ahrens, "How to Take Smart Notes" (secondary summary): https://notes.andymatuschak.org/How_to_Take_Smart_Notes_-_Ahrens
- Anthropic, Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval
- Chroma, Evaluating Chunking Strategies: https://www.trychroma.com/research/evaluating-chunking
- A-Mem: Agentic Memory for LLM Agents (NeurIPS 2025): https://proceedings.neurips.cc/paper_files/paper/2025/hash/19909c36f51abc4856b4560aff3d36d6-Abstract-Conference.html
- Adobe, Zettelkasten overview (abandonment note, non-academic): https://www.adobe.com/acrobat/resources/zettelkasten-method.html

## Unresolved questions

1. Should `aliases` be mandatory on `note` or optional? (Affects S1 onboarding time.)
2. Do we allow lexical titles for coined terms (Matuschak's exception), or force claim form for all `note`s?
3. Is the filename character rule (AGENTS.md §4) compatible with claim titles, or do we allow a title/filename split (breaks "filename is title")?
4. Lint for zero outbound links: warning or error? (Relates to linking.md §7 open question 1.)
5. Learning-log need: does the pilot need a dedicated type, or do daily notes suffice?
6. Who owns the area hub `Learning` per role — one per person (personal vault) is assumed; confirm.

**Status:** DONE_WITH_CONCERNS
**Summary:** Zettelkasten tiers map onto existing types (inbox/reference/note/moc), so no new study types for v1. Claim-style titles for `note` only, plus `aliases`; no IDs/Folgezettel; linking minimum is 1 hub + optional concept link with lint on orphans. Main risk is collector's fallacy (mitigate with a reference gate). Atomic notes suit agent retrieval analogically (Chroma, Anthropic contextual retrieval), but no controlled study of vault notes vs RAG was found.
**Concerns/Blockers:** Ahrens book and zettelkasten.de read via secondary summaries; A-Mem arXiv ID unverified; retrieval and abandonment claims rest on analogy and opinion, not measurement. Six unresolved questions above need owner input.
