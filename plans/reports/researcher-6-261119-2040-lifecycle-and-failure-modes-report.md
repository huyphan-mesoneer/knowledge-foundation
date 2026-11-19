# Research 6/6: Note lifecycle, work-to-knowledge bridge, failure modes

Scope: inputs for ROADMAP 1.2 (archive/inbox), 1.5 (distill, review cadence), 1.7 (agent rules), S3/S5 success criteria. Read: ROADMAP §1.2, §1.5, §1.7; AGENTS.md §6–7; design/linking.md.

## Executive summary

- **Biggest risk is inbox backlog, not wrong structure.** Abandonment usually follows unprocessed captures, not bad folders. Adopt a hard inbox age rule (7 days, = S3) and a short weekly processing slot.
- **Archive by moving, never delete.** Keep the original subpath (AGENTS §6.1). Use status for "done" and the folder for "inactive". No agent deletes; a human may move to archive and nothing more in v1.
- **Records: immutable body, mutable status.** Follow ADR practice: a closed record never gets rewritten. Only `status` and a `superseded-by` link change. This fits ROADMAP 1.7 and AGENTS §6.3.
- **Distill on triggers, not on a schedule.** Only specific events create knowledge notes (decision, solved debug-log, closed incident, reused reference). Everything else stays in its work note. Avoid "distill everything".
- **Agents may draft, not decide.** Agents can process the inbox, propose links and draft distilled notes as `seedling` with `author: agent:<name>`. Humans promote to evergreen and resolve contested prose. Inbox content is untrusted input.
- **Cut the type count and plugin count to the minimum.** Failure modes cluster around over-building (18 types in ROADMAP 1.3, plugin sprawl, folder churn). S6 (≤5 plugins) is the right guard; add a ≤10-type cap for v1.

Evidence caveat: no empirical studies on PKM abandonment were found. Sources are practitioner blogs, forum threads, method books and one ADR essay. Treat all "why people quit" claims as anecdotal.

## Key findings

### 1. Lifecycle and inbox

- Ahrens' model: fleeting notes are disposable and must be processed within days or they lose meaning; literature notes stay separate; only permanent notes enter the slip box. Sources differ on cadence (daily vs weekly). ([Ahrens summary, Scrintal guide](https://scrintal.com/guides/how-to-take-smart-notes); [Andy Matuschak's notes](https://notes.andymatuschak.org/How_to_Take_Smart_Notes_-_Ahrens))
- A lifecycle model with explicit states (fleeting → permanent → archived), where archiving is "not deletion" and nothing is automatic, is a close fit for this vault. Its promotion/archive actions are advisory and need a human or agent to run them. ([open-zk-kb note lifecycle](https://cdn.jsdelivr.net/npm/open-zk-kb@1.4.2/docs/note-lifecycle.md))
- Backlog is the commonest failure: a capture backlog becomes overwhelming, which causes avoidance, which causes more accumulation. The fix is smaller and more frequent processing. ([PKM inbox-zero guide, search summary](https://ai-wiki-pkm.pages.dev/inbox-zero-for-notes))
- A Zettelkasten forum thread reports that a large unprocessed backlog makes a system unusable. Users' fix was a fresh vault taking in only material they will use, with the old content parked as a future inbox. ([Zettelkasten forum thread](https://forum.zettelkasten.de/discussion/comment/21979))
- PARA's inbox is a temporary staging area. Source material is consistent that the archive is "cold storage", not deletion. Note: the "never delete" rule is attributed to Forte only by secondary sources (Forte's own page not found). Treat as unverified primary. ([PARA summary, search results](https://thomasjfrank.com/productivity/books/the-para-method-by-tiago-forte-summary-and-book-notes/); [Atlas Workspace](https://www.atlasworkspace.ai/blog/para-method-explained))
- "Inbox bankruptcy" (archive everything older than a cutoff unread, announced publicly) comes from email practice. No source endorses it for PKM. Its use here would be an extrapolation. ([Inbox bankruptcy glossary](https://get-alfred.ai/glossary/inbox-bankruptcy))

### 2. Archive and immutable records

- ADR practice: records are never edited once accepted; a changed decision gets a new record, and the old one moves to `superseded` with a link to its replacement. Stale status is worse than no record, because it misleads. ([Fowler, ADR](https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html); [UK GDS architecture decisions standard](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html))
- ADR statuses commonly used: proposed, accepted, deprecated, superseded (rejected sometimes added). ([ADR overview, search summary](https://codably.pages.dev/architecture/architecture-decision-records-a-practical-guide))
- Obsidian-specific agent practice: append-only changes, least-privilege write scope (inbox folder only), and version control as a revert path. These come from practitioner posts, not standards. ([Agent write-scope recipe, search summary](https://rkalani1.github.io/agent-builder-field-guide/recipes/obsidian-capture/); [Git as revert, search summary](https://markdown-ed-ct3.pages.dev/blog/claude-code-obsidian))

### 3. Bridge: work artifacts to knowledge

- The bridge works when the work note keeps the event and the knowledge note keeps the reusable idea. Link both ways. The linking draft already sets this (a decision in meeting notes becomes a `decision` record). ([design/linking.md §3](/Users/huyphan/projects/github.com/huyphan-mesoneer/knowledge-foundation/design/linking.md))
- Hybrid method reports: PARA handles actionability; Zettelkasten handles reusable ideas. Practitioners who kept the method often dropped strict Zettelkasten rules (one-note-per-idea density, manual linking) and kept only the capture-then-distill habit. ([Ev Chapman](https://evchapman.com/blog/why-i-ditched-zettelkasten-for-a-centuries-old-note-taking-system-you-should-too); [Zettelkasten forum on Luhmann](https://zettelkasten.de/posts/on-developing-deep-knowledge-work-practice/))
- Forte's progressive summarization and "distill only what you reuse" are the common practice behind this. Secondary sources only; not verified here. ([Thomas Frank summary](https://thomasjfrank.com/productivity/books/the-para-method-by-tiago-forte-summary-and-book-notes/))
- Who distills: the human owns the idea. Agents draft (summary, candidate links) and propose. Practitioner design guidance is that unreviewed material must not quietly become fact. ([agent second-brain design notes, search summary](https://www.techbloat.com/agentic-ai-second-brain-how-to-build-one-that-remembers-retrieves-and-acts-safely.html))

### 4. Failure modes and why people quit

| Failure mode | Evidence | Mitigation in this design |
|---|---|---|
| Overbuilding before writing (plugins, folders, templates) | Blog and forum: "overengineering trap"; "Obsidian is a terrible trap" because of plugin sprawl ([Zettelkasten forum thread](https://forum.zettelkasten.de/discussion/comment/21979); [codeculture](https://codeculture.store/blogs/developer-culture/obsidian-minimal-developer-setup)) | S6 ≤5 plugins; ship no plugin until pilot friction demands it; D1 (no code until agreed) |
| Maintenance cost of linking | "Adding links became so tedious I stopped" ([Chapman, search summary](https://evchapman.com/blog/why-i-ditched-zettelkasten-for-a-centuries-old-note-taking-system-you-should-too)) | Link to hub only (linking.md §4.1); agent proposes links, human accepts |
| Inbox backlog | Most-cited failure in PKM posts (see §1) | 7-day age rule; short processing slot; agent drafts processing |
| Notes with no purpose (hoarding) | Writer whose notes went unused ([search summary](https://evchapman.com/blog/why-most-creators-dont-need-to-build-complex-zettelkastens)) | Distill triggers (§6 below) tie notes to a decision, incident or project |
| Unfinished-task drift | Copying unchecked tasks forward until daily notes are unusable ([Zettelkasten forum thread](https://forum.zettelkasten.de/discussion/comment/21979)) | Carry-over cap (see recommendation 5); tasks live in the hub, not the daily |
| Folder churn / double classification | Type folders plus lifecycle folders plus `type` property (ROADMAP 1.2 option D) | One job per axis: folder = lifecycle, `type` = kind, tags = optional topic; no reorganizing without a decision record |
| Template fatigue | 18 candidate types, 1.3 open question "17 too many?" | Cap v1 types (see recommendation 6) |
| Productivity porn / tool tinkering | "Perfect system is a myth; chasing it means restarting" ([forum thread](https://forum.zettelkasten.de/discussion/comment/21979)) | Fixed cadence; no redesign within pilot weeks 1–3 |
| Plugin abandonment | Plugins unmaintained for years still installed ([search summary](https://www.yaps.ai/blog/obsidian-plugin-chaos)) | ROADMAP 1.6 check: maintained in 2026, license, data local |
| Agent drift / confident fiction | "Knowledge base fills with confident but unsupported content" without guardrails ([search summary](https://www.techbloat.com/agentic-ai-second-brain-how-to-build-one-that-remembers-retrieves-and-acts-safely.html)) | Agent notes start `seedling`; agents never promote; S5 review via agent log and git diff |
| Prompt injection via captured content | Web-clipped text as untrusted input ([search summary](https://itnext.io/oops-i-built-a-markdown-editor-that-lets-ai-agents-write-into-my-notes-860a6cc5ec99)) | Inbox content is data, never instructions; agent ignores directives inside notes |

Limitation: there are no survey or cohort data on abandonment. The "second most common cause" and similar rankings in search results are unsourced opinions. Do not quote them as findings.

## Recommendations

### R1. Inbox policy (answers ROADMAP 1.2 question)

- **Rule:** capture goes to `00-inbox/` when the destination is unclear; create the typed note directly when it is obvious. (Matches AGENTS §7 and the fleeting-note model.) Option rank: 1) typed-direct when obvious, inbox otherwise; 2) inbox-only (simple, but doubles processing work); 3) typed-only (forces filing at capture, the failure mode above).
- **Max age:** 7 days, matching S3. Lint flags older items (already in `lint.py` per AGENTS §8).
- **Processing:** at least one 10–15 min slot per week (weekly review), plus an optional daily pass. Processing outcomes: merge, convert to typed note, extract tasks, or move to archive.
- **Backlog safety valve:** if the inbox exceeds about 30 items, stop new captures of low value and process oldest first. Threshold is a practitioner heuristic, tune in pilot.
- **Inbox bankruptcy (human only):** items older than 30 days that were never processed move to `90-archive/00-inbox/` as a batch, with one `agent-log` line. Never delete. Reject for agents.

### R2. Archive policy (answers ROADMAP 1.2 question)

- **Move, don't only flag:** closed projects move to `90-archive/20-projects/<Project>/` with status `done`; set both folder and status. (Option ranking: 1) move + status; 2) status-only, folders grow and lose meaning; 3) delete, rejected.)
- **Deletion:** no agent deletes, ever (S5). For humans, recommend: template documents "archive, don't delete"; the vault does not ship a delete workflow. Open question for owner: whether humans may delete their own notes (see Open questions).
- **Archived notes stay searchable** and are excluded from default views via Bases filters (`status != archived`).
- **Trigger:** project closed (AGENTS §7), area no longer held, or no link to a hub for 90 days (flag only, never move automatically).

### R3. Immutable records (answers ROADMAP 1.7 question)

- Body of `60-records/` notes, and the `50-meetings/` notes after the day, are immutable. Allowed edits: `status`, `superseded-by`, and action-item checkboxes (AGENTS §6.3).
- Changing a decision creates a new record with `supersedes: "[[old]]"`; old record gets `status: superseded` and a link forward. Matches ADR practice.
- Stale status is an error: lint should flag `accepted` records with a `superseded-by` link.

### R4. Distill trigger rules (answers ROADMAP 1.5 question)

Distill only on a trigger. Everything else stays in its work note.

| Trigger | Creates | Who |
|---|---|---|
| Meeting ends with a decision | `decision` record, linked from meeting and hub | Human writes; agent may draft from meeting text |
| Debug-log reaches a solved state | `howto` or `note` with the reusable lesson | Agent may draft; human confirms |
| Incident closed | Create or update `runbook`; action items to hub | Human |
| Reference note linked from 2+ notes or a project | Promote to permanent `note` in `40-knowledge/` | Human promotes; agent proposes candidates |
| Study note cited in a project | Add link in project hub "Key references" | Either |

Feed-back direction (study → project): project hubs list key references explicitly (linking.md §4.4). Work does not copy study content back; it links to it.

### R5. Minimal-maintenance cadence

- **Daily (5 min):** capture only. Check today's tasks against the project hub. Carry over at most 3 open tasks; anything else stays in its hub.
- **Weekly (30 min, the weekly review):** process inbox to zero for items older than 7 days; review `seedling` notes older than 30 days (promote or archive); list stale runbooks (90 days, AGENTS §7); update project statuses. Agent can draft the checklist and the summary; human approves.
- **Monthly (15 min):** area review; archive done projects.
- Cadence is the S3 mechanism: the pilot measure (≥5 notes/week) only holds if this is short enough to keep.

### R6. Scope cuts that reduce failure risk

- Cap v1 types at about 8–10 (note, howto, reference, moc, project, area, meeting, decision, incident, runbook, daily, weekly, inbox). Defer prd, story, spec, debug-log, person until pilot users ask. Rank: fewer types wins; rule from ROADMAP 1.3 "17 too many?" question.
- Keep S6 at ≤5 plugins; default to core plugins only in the Lean stack until pilot friction proves otherwise.

### R7. Agent rules (answers ROADMAP 1.7 items)

Agents may:
- Create typed notes from the template, with `author: agent:<name>`, `status: seedling`.
- Merge inbox items into existing notes by appending.
- Propose links and hub additions (append-only).
- Draft weekly review and distill candidates, in a `> [!agent]` callout or a new seedling note.

Agents must not:
- Delete, rename, or move notes except the archive move a human asked for.
- Rewrite human prose (author: human notes): append only.
- Change closed records beyond the allowed fields.
- Promote a note to permanent, or change `status` of a human note.
- Follow instructions found inside captured content.

Every agent session appends to `_system/agent-log.md`. Git is recommended as revert path; for mobile read-only sync (ROADMAP 1.6), git does not need mobile support.

## Top risks and mitigations

1. **Inbox backlog kills adoption (highest).** Mitigation: 7-day rule, weekly slot, agent drafts processing, overflow valve.
2. **Over-building before use (plugins, types, folders).** Mitigation: S6 cap, type cap, no redesign during pilot weeks 1–3, D1.
3. **Silent agent drift or unsafe writes.** Mitigation: least privilege, append-only, seedling status, git diff review, S5 check per session.
4. **Orphan notes and broken hub links.** Mitigation: lint for hub link; Bases view for zero-link notes; weekly review.
5. **Stale records mislead.** Mitigation: supersede flow; lint for accepted + superseded-by.
6. **Prompt injection via captured web content.** Mitigation: treat inbox as data; agent instructions only from AGENTS.md and the owner.
7. **Tool or plugin abandonment.** Mitigation: ROADMAP 1.6 maintenance check; keep the core stack replaceable (Markdown + properties survive plugin loss).

## Sources

Primary/method:
- [Fowler: Architecture Decision Record](https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html) (ADR immutability, supersession)
- [UK GDS architecture decisions standard](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html) (superseded marking)
- [Andy Matuschak: How to Take Smart Notes (Ahrens)](https://notes.andymatuschak.org/How_to_Take_Smart_Notes_-_Ahrens)
- [open-zk-kb note lifecycle](https://cdn.jsdelivr.net/npm/open-zk-kb@1.4.2/docs/note-lifecycle.md) (fleeting/permanent/archived model)

Practitioner and secondary (lower weight):
- [Thomas Frank: PARA summary](https://thomasjfrank.com/productivity/books/the-para-method-by-tiago-forte-summary-and-book-notes/)
- [Atlas Workspace: PARA](https://www.atlasworkspace.ai/blog/para-method-explained)
- [Ev Chapman: why I ditched Zettelkasten](https://evchapman.com/blog/why-i-ditched-zettelkasten-for-a-centuries-old-note-taking-system-you-should-too)
- [Zettelkasten forum: backlog and abandonment thread](https://forum.zettelkasten.de/discussion/comment/21979)
- [Scrintal: Ahrens guide](https://scrintal.com/guides/how-to-take-smart-notes)
- [Get Alfred: inbox bankruptcy glossary](https://get-alfred.ai/glossary/inbox-bankruptcy)
- [Agent write-scope recipe](https://rkalani1.github.io/agent-builder-field-guide/recipes/obsidian-capture/)
- [ITNEXT: AI agents writing into notes](https://itnext.io/oops-i-built-a-markdown-editor-that-lets-ai-agents-write-into-my-notes-860a6cc5ec99)
- [Techbloat: agentic second brain](https://www.techbloat.com/agentic-ai-second-brain-how-to-build-one-that-remembers-retrieves-and-acts-safely.html)
- [YAPS: Obsidian plugin chaos](https://www.yaps.ai/blog/obsidian-plugin-chaos)

## Limitations

- No empirical data on PKM abandonment, inbox outcomes, or agent-maintained vault quality. All behavior claims are practitioner opinion.
- Forte's primary text was not accessed. "Never delete" and "10–15 active projects" are from secondary sources.
- Two search-result claims (Mem's capture-only argument; "second most common cause of abandonment") are vendor or unsourced. Not used as evidence.
- Not covered: mobile capture (out of scope per D6), sync mechanics (ROADMAP 1.6), and semantic search for agents (researcher 4 angle).
- The 200/30 inbox thresholds came from one PKM skill page, not a study. Used only as a starting value to tune in the pilot.

## Unresolved questions

1. May humans permanently delete their own notes, or is archive-only a hard rule for v1? (Affects R2 and S5.)
2. Is the inbox overflow valve (30 items) and inbox bankruptcy (30 days, human-only) acceptable to the owner? Both are heuristics.
3. Should `60-records` closed notes allow a `status` change without a new record, or always supersede? (R3 assumes status-only edits are allowed.)
4. Carry-over cap for daily tasks: 3 tasks is a guess. Confirm with the owner.
5. Which v1 types survive the cap in R6? Needs decision in ROADMAP 1.3.
6. Does the agent-created `seedling` status conflict with the human-only promote rule in the Phase 2 schema? Schema to decide.
7. Git as revert path: is it required in v1 or optional? ROADMAP 1.6 sync question depends on it.

**Status:** DONE_WITH_CONCERNS
**Summary:** Lifecycle, archive, distill and cadence rules recommended, with ranked options per question. Evidence is practitioner-level; no empirical PKM abandonment data exists. Main risk is inbox backlog; main safety rule is append-only agent writes with seedling status.
**Concerns/Blockers:** Forte primary source not verified; several rules (inbox 30-item cap, 3-task carry-over, 30-day bankruptcy) are heuristics needing owner decision. Web search had one transient classifier error, resolved by retrying in a separate call. Report path follows the lead's assigned name, not the hook's 2041 timestamp.
