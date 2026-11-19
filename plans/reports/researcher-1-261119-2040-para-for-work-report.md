# Researcher 1: PARA for work knowledge

**Status:** DONE_WITH_CONCERNS
**Scope:** ROADMAP §1.2 (note-taking method and vault structure), angle "PARA for work".
**Concerns:** No controlled evidence for PARA exists. CODE definitions come from secondary sources only (Forte Labs CODE page returned 404). Obsidian path-break behaviour outside the app rests on a forum thread, not official docs. Both need a pilot check.

---

## 1. Executive summary

- PARA is an actionability lens, not a complete system. Forte defines Projects (short-term, goal-driven), Areas (ongoing, no end date), Resources (topics of interest) and Archives (inactive items from the other three). The rule is to organize "according to the projects and goals you are committed to right now." [S1][S2]
- PARA does not classify record types (decision, incident, meeting, debug log). Those need a second axis: our `type` property plus typed folders.
- PARA's "Resources" bucket is its known failure point; material filed there is rarely revisited. `40-knowledge/` should replace it with linked notes plus MOCs, not a second dump folder. [S3][S4]
- Recommended method: **D, refined** (the prototype hybrid). Lifecycle folders, typed folders, `type`/`status` as properties, tags for topic only, hubs as the only navigation.
- Moving notes is low risk when links use bare names (`[[Name]]`). Path-qualified links break when files move outside Obsidian. Enforce bare names. [S6][S7]

## 2. Key findings

**F1. PARA categories are defined by lifecycle and actionability.** Projects: "short-term efforts... that you take on with a certain goal in mind." Areas: "require ongoing attention." Resources: "topics you're interested in and learning about." Archives: "no longer active, but you might want to save for future reference." No formal decision procedure beyond these definitions. [S1]

**F2. Forte's create/archive rules.** Create folders only when there is something to put in them, except when setup friction would block capture. Archive completed or inactive projects (the most common case), areas whose responsibility has ended, and resources whose interest has gone dormant. Never delete. Before archiving a finished project, scan it for reusable intermediate material. Forte argues against scheduled reorganizing: organize "opportunistically, as opportunities arise." [S2][S8]

**F3. CODE and Progressive Summarization.** CODE = Capture, Organize, Distill, Express. Capture has no filter ("anything that feels insightful, interesting, or useful"). Progressive summarization adds layers (bold, highlight, highlight-of-highlights, executive summary, remix); deeper layers are reserved for notes that earn them and happen during reviews already under way. [S9][S10] CODE stage definitions here are from secondary sources only. [S11]

**F4. Failure modes documented by practitioners and by Forte.**
- Resources dump: "almost everything sent into an Area or Resources folder was never seen again." [S4] A bookmark dump of 400 unsorted links is harder to use than a bookmark manager. [S3][S12]
- Archive as graveyard: used for things people feel guilty discarding. [S3][S12]
- Areas degrading into topic folders, filled with interest-based notes instead of accountabilities. [S12]
- Folder churn: moving notes is friction; one user stopped moving things and folders became cluttered. [S5]
- Broken clustering: related projects split across folders when some finish and others don't. [S5]
- Neglect: organizing never gets scheduled and the system decays. [S8][S12]
- An overcrowded Projects folder is worse than an underused Archive. [S12]

**F5. Property-based alternative.** In Obsidian, category and status can be set with properties and archived notes hidden with one Bases filter, so nothing moves. [S5][S13] Counter-argument: folders are simpler, visible at a glance and portable across apps; properties need Bases familiarity and consistent metadata. [S5] A hybrid (folders for top-level buckets, properties for status) is a common middle path. [S13]

**F6. PARA and Zettelkasten are complementary.** One author: PARA is "resource management," Zettelkasten is "a method for working with ideas." [S14] That author's combined model puts Resources and Archive under Zettelkasten; this is the author's model, not Forte's. [S14] Another practitioner keeps PARA for work notes and merges targeted Zettelkasten-style insights; Area/Resource material was rarely revisited. [S4]

**F7. Engineering mapping (secondary, partly inferred).** Projects: a migration, an ADR for a redesign. Areas: on-call, architecture standards, infrastructure reliability. Resources: benchmarks, cheat sheets, talks. Archives: completed or deprecated material. Test that separates project from area: "could I close a ticket on it?" The article does not cover PRDs, specs, incidents or meetings. [S12]

**F8. Obsidian link mechanics.** Obsidian updates links automatically when a file is renamed or moved inside the app. [S6] Plain `[[Name]]` links resolve by filename: when the name is unique the link is the bare name, otherwise it is the full path from the vault root. [S7] Moves made outside Obsidian (agent, git, Finder) are not covered by official docs; community reports say path-qualified links break. [S7] Verify in pilot.

## 3. Evidence

| # | Source | Type | Used for |
|---|---|---|---|
| S1 | https://fortelabs.com/para/ | Primary (Forte Labs) | Category definitions, actionability |
| S2 | https://fortelabs.com/blog/para/ | Primary (Forte Labs) | Origin, project-first setup, archive rules |
| S8 | https://every.to/forte-labs/para-part-2-just-in-time-organization-850888 | Primary-adjacent (Forte series on Every) | Opportunistic organizing, archive rules, neglect |
| S9 | https://fortelabs.com/blog/progressive-summarization-a-practical-technique-for-designing-discoverable-notes/ | Primary (Forte Labs) | Progressive summarization layers |
| S11 | https://web-highlights.com/blog/master-your-second-brain-how-to-use-the-code-technique/ ; https://thevicmontano.substack.com/p/codes-distill-phase-your-ultimate | Secondary | CODE stages (Forte CODE page returned 404) |
| S3 | https://www.zainrizvi.io/blog/para-vs-zettelkasten-the-false-binary/ | Practitioner blog | Resources dump, Zettelkasten pairing |
| S4 | https://www.zainrizvi.io/blog/remembering-what-you-read-zettelkasten-vs-para | Practitioner blog (search snippet, not fetched in full) | Area/Resource material rarely revisited |
| S5 | https://forum.obsidian.md/t/challenging-paras-traditional-folder-approach/110515 | Community forum | Properties vs folders, friction, broken clustering |
| S6 | https://obsidian.md/help/links | Official docs | Auto-update on in-app rename |
| S7 | https://forum.obsidian.md/t/renaming-file-removes-path-from-links-to-it-when-new-link-format-is-shortest/106794 | Community forum, developer replies | Unique-name vs full-path link rule |
| S12 | https://dev.to/rosgluk/para-method-for-engineers-organize-knowledge-by-action-1npg | Practitioner article | Engineering mapping, failure modes, archive rules |
| S13 | https://forum.obsidian.md/t/grouping-notes-into-folders-through-bases-or-properties/105200 | Community forum (search snippet, not fetched) | Folders vs Bases/properties |
| S14 | https://zettelkasten.de/posts/building-a-second-brain-and-zettelkasten/ | Practitioner blog | BASB vs ZKM purpose; combined model |

Credibility: Forte's primary pages are the authority on definitions. Forums and practitioner blogs are useful for failure modes but anecdotal. No controlled studies of PARA were found. Confidence: high on Forte's definitions; medium on Obsidian behaviour outside the app.

## 4. Trade-off matrix (ROADMAP §1.2 options)

Scale: ++ strong, + ok, 0 neutral, − weak, −− poor.

| Dimension | A. PARA (pure) | B. Zettelkasten (pure) | C. Type-based folders | D. Hybrid (prototype, refined) |
|---|---|---|---|---|
| Fit for work (deadlines, deliverables) | ++ | − | 0 | ++ |
| Fit for study / evergreen knowledge | − (Resources dump) | ++ | − | + |
| Role docs with no single home (runbook, spec) | −− (must pick one bucket) | + | + | + (owner-lifetime rule) |
| Records, meetings, people | −− (no home) | − | ++ | ++ |
| Archive / lifecycle semantics | ++ | − | −− (none) | ++ |
| Agent predictability (where to write) | 0 | 0 | ++ | + (rules table) |
| Maintenance cost | 0 (moves) | + | + | + (few moves: inbox→bucket, project→archive) |
| Adoption risk | Medium (Resources dump) | Medium (linking discipline) | Low | Low–medium (more rules) |
| Fit with `_system/schema.json` | − (contradicts `40-knowledge`, `60-records`) | − | ++ | ++ (already built) |

**Ranking**
1. **D, refined.** Covers all four needs at moderate rule cost; most structure already exists in the prototype.
2. **A, pure PARA.** Good for work, but no home for study notes, records or role docs that outlive projects.
3. **C, type-based.** Simplest for agents, but no active/archived signal.
4. **B, pure Zettelkasten.** Excellent for ideas, but no deadlines, no project hubs, no archive.

## 5. Recommendations for ROADMAP §1.2

**Q1. Method: D, refined.**
- Lifecycle folders: `00-inbox/` (capture), `20-projects/` (active work), `30-areas/` (accountabilities), `40-knowledge/` (evergreen; replaces PARA Resources), `90-archive/` (inactive).
- Typed folders outside PARA: `10-journal/`, `50-meetings/`, `60-records/`, `70-people/`.
- Drop "Resources" as a folder concept. Knowledge is organized by MOCs and links, not by a second container.

**Q2. Folders vs properties vs tags: one job each.**
- Folder = where it lives now (location and lifecycle). Encodes kind only in fixed record folders.
- `type` property = what it is. Lets Bases and agents filter by kind regardless of folder.
- `status` property = state within its type (project: planned/active/done/cancelled). Authoritative for state.
- Archive rule: archived when status is done/cancelled or the responsibility ends. Lint checks that folder and status agree.
- `tags` = topic only (`topic/kafka`). Never lifecycle or type.
- `roles` (already in schema) = property, not tag.
- Links = relationships (`project`, `area`, `related`). Hubs are the navigation.

**Q3. Role-specific docs: "where will it be maintained?"**

| Doc | Lifetime | Home | Why |
|---|---|---|---|
| PRD, story, spec for a deliverable | ends with the deliverable | `20-projects/<Project>/` | Project-bound (schema already does this) |
| Spec describing a live system | no end date | `40-knowledge/` (type `spec`), linked from Area hub | Survives project archiving; findable by name |
| Runbook | no end date | `40-knowledge/`, linked from Area hub (e.g. On-call) | Evergreen; no folder churn when ownership moves |
| Incident / postmortem | closed once reviewed | `60-records/` | Immutable record; link to system Area and project |
| Decision (ADR) | immutable | `60-records/` | Supersede, don't edit |
| Debug log | solved or abandoned | `60-records/` | Investigation diary; distill lessons to `howto` |
| Meeting | immutable after the day | `50-meetings/` | Action items become project/area tasks |
| Person / team | long-lived | `70-people/` | Not PARA |

Consequence: the prototype's `runbook` in `40-knowledge/` is correct, provided the Area hub links it. Area folders should hold hub notes only, not documents, to avoid churn.

**Q4. Hubs.**
- Work notes (PRD, story, spec, decision, incident, debug log, meeting) link to a project or area.
- Knowledge notes (note, howto, runbook, reference) link to a MOC or area at creation. This prevents the Resources dump.
- Exempt: inbox, daily, weekly. Person may link to a team.
- Enforcement: lint warning in v1, error later. Resolves the open question in `design/linking.md` §7.
- Periodic orphan report: knowledge notes with zero inbound links after 90 days. Measures S3/S4.

**Q5. Naming (provisional; weak PARA guidance).**
- Keep type prefixes (`DEC`, `INC`, `DBG`, `RUNBOOK`, `How to`) in flat folders (`40-knowledge/`, `60-records/`), where they help humans and agents scan filenames.
- Inside a project folder, prefixes (`PRD`, `SPEC`, `STORY`) are optional. Decide by an agent-search test.
- Names must be unique and bare for links (see Q7).

**Q6. Inbox.**
- Capture anything; no filter at capture (CODE; Progressive Summarization layer 1).
- The 7-day processing rule is not from Forte; it is an owner choice. Keep it (matches S3 and schema `inbox_max_age_days`). Owner to confirm.
- Reconcile with Forte's "no scheduled reorg": inbox triage moves items into buckets; it does not re-fold the structure. Weekly review covers triage and project status, not re-foldering.

**Q7. Archive mechanics.**
- Trigger: project status set to done or cancelled. Move the whole project folder to `90-archive/20-projects/<Project>/`, keeping the subpath (AGENTS.md §6.1).
- Before archiving, scan for reusable material and promote it to `40-knowledge/` (Forte's step).
- Areas: archive only when the responsibility ends. Knowledge notes: set `status` to outdated/retired; move only when the topic is dead.
- Never delete. Archive is the only exit.
- Links: use bare names (`[[Name]]`), never paths. Moves then don't break links. Lint flags any `[[folder/...]]`.
- Agents: default search skips `90-archive/` unless the question is historical.
- If an index or MCP cache is added later (`design/linking.md` §6), archive moves must invalidate it.

**Q8. Failure-mode guardrails (from the criticisms).**
- Cap Areas. Role-based areas are fine; avoid topic areas. "Learning" (schema `roles.everyone`) is a topic risk; consider an accountability name (e.g. "Skill development").
- Resources dump: knowledge notes link a MOC at creation; orphan report.
- Archive graveyard: archive only on project close, not as a discard pile.
- Neglect: weekly checklist includes "active projects with no update in 14 days" and "inbox older than 7 days".
- Overcrowded Projects: owner sets a cap on active projects (suggest ≤ 5; a preference, not a researched value).

## 6. Adoption risk and architectural fit

- Maturity: PARA dates from 2017, in wide use; Forte's book (2023) is current. No breaking changes in the method. Obsidian Bases is newer and may change.
- Abandonment risk: low; PARA is a method, not a tool.
- Community: large in PKM; few rigorous evaluations.
- Fit: D matches `_system/schema.json` (folders by type and lifecycle, per-type `status`, `roles`). The change is mostly documentation: drop "Resources" wording, add the owner-lifetime rule and hub rules.
- Constraints: solo owner (D2); rules must be followable by a human in Obsidian and by an agent with plain Markdown read/write (D5).

## 7. Limitations

- No controlled or longitudinal studies of PARA were found; evidence is Forte's claims and practitioner anecdote.
- CODE evidence is secondary; the Forte Labs CODE page returned 404.
- Obsidian path-break behaviour outside the app is from forum reports. Verify: move a note with `mv`, check links, confirm the bare-name rule holds.
- Not covered here: Zettelkasten mechanics in depth (angle 2), existing hybrid systems (angle 3), agent retrieval quality (angle 4), human findability (angle 5), lifecycle failure modes beyond PARA (angle 6).
- Naming was only lightly covered; treat Q5 as provisional.

## 8. Unresolved questions

1. Is `40-knowledge/` one flat folder or topic subfolders? Flat is simpler for agents; subfolders help humans browse. Decide with angle 4/5 evidence.
2. Can areas contain documents, or only hub notes? Recommendation: hubs only. Owner to confirm.
3. Should project status "done" trigger archiving via an agent workflow, or wait for owner confirmation? Given friction (S5) and "never delete" (AGENTS.md §6), agent-proposed and owner-confirmed looks safest.
4. Does the owner want a cap on active projects? The number is a preference, not researched.
5. Is "Learning" acceptable as an Area, given the topic-folder failure mode? Owner decision.
6. Is the 7-day inbox age right for a single person? Owner to confirm; test in pilot.
7. Pilot test of moves outside Obsidian (agent `mv`, then link check) is needed before "bare names only" becomes a lint error.

## 9. Sources

- [S1] https://fortelabs.com/para/
- [S2] https://fortelabs.com/blog/para/
- [S3] https://www.zainrizvi.io/blog/para-vs-zettelkasten-the-false-binary/
- [S4] https://www.zainrizvi.io/blog/remembering-what-you-read-zettelkasten-vs-para
- [S5] https://forum.obsidian.md/t/challenging-paras-traditional-folder-approach/110515
- [S6] https://obsidian.md/help/links
- [S7] https://forum.obsidian.md/t/renaming-file-removes-path-from-links-to-it-when-new-link-format-is-shortest/106794
- [S8] https://every.to/forte-labs/para-part-2-just-in-time-organization-850888
- [S9] https://fortelabs.com/blog/progressive-summarization-a-practical-technique-for-designing-discoverable-notes/
- [S11] https://web-highlights.com/blog/master-your-second-brain-how-to-use-the-code-technique/
- [S12] https://dev.to/rosgluk/para-method-for-engineers-organize-knowledge-by-action-1npg
- [S13] https://forum.obsidian.md/t/grouping-notes-into-folders-through-bases-or-properties/105200
- [S14] https://zettelkasten.de/posts/building-a-second-brain-and-zettelkasten/
