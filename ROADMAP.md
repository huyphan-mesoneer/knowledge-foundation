---
created: 2026-11-13
updated: 2026-11-19
owner: Huy Phan
---
# 🗺️ Roadmap — knowledge-foundation

Goal: an Obsidian vault template that anyone (PO, engineer, DevOps, QA, designer, manager) can bootstrap and keep using for **personal knowledge** (one private vault per person; shared team vaults are out of scope for v1, see D2), written and maintained by **humans and AI agents** with the same result.

**How to use this file:** it is the single progress overview. Tick `[x]` when an item is agreed/done, write the outcome in the [[#Decision log]], and bump `updated`. Agents may tick items only when the owner confirmed the decision in conversation.

Status legend: ⬜ not started · 🟡 in progress · ✅ done · ⏸️ parked

## Overview

| Phase | Goal | Code? | Status |
|---|---|---|---|
| 0. Prototype | Quick end-to-end draft to have something concrete to discuss | yes | ⏸️ parked (reference only) |
| 1. Design discussion | Agree on templates, note-taking method, agent rules, community plugins | **no** | 🟡 in progress |
| 2. Template authoring | Write the final templates, property schema, AGENTS.md, plugin settings (Markdown/JSON only) | no | ⬜ |
| 3. Tooling & automation | Bootstrap, validation, agent skills, CI | yes | ⬜ |
| 4. Pilot | Real use by 1 PO + 1 engineer + 1 DevOps for 2–3 weeks, plus personal use | no | ⬜ |
| 5. Release v1 | Publish template repo, onboarding guide, maintenance process | — | ⬜ |

---

## Phase 0 — Prototype ⏸️

A first draft exists in this repo (folders, 18 templates in `_system/templates/`, `AGENTS.md`, Bases views, Python scripts, Claude skills). It is **input for the Phase 1 discussion, not a decision**. Nothing in it is final; scripts/skills are parked until Phase 3.

- [ ] Decide: keep the prototype in `main` as reference, or move it to a `prototype` branch so `main` only contains agreed work

---

## Phase 1 — Design discussion (no code) 🟡

Output of this phase: a written decision for every item below (in the [[#Decision log]]). Items are ordered; later ones depend on earlier ones.

### 1.1 Principles & scope
- [x] Who is the primary user for v1: individual (personal vault) / team (shared repo) / both → **individual only** (D2)
- [x] Same template for personal and team, or one core + two profiles? → **one template, no team profile** (D3)
- [x] What must stay private in team mode (journal, 1:1s, people notes)? → **n/a — the whole vault is private to its owner** (D4)
- [x] Agent-agnostic (any AI tool via `AGENTS.md`) vs. optimized for one tool (Claude Code) → **agnostic, Claude extras optional** (D5)
- [x] Desktop only, or must it work on mobile too (affects plugin choice) → **desktop for writing, mobile read-only** (D6)
- [x] Success criteria for v1 → **S1–S6 below** (D7)

**v1 success criteria (D7)** — measured in the Phase 2 review and the Phase 4 pilot:

| # | Criterion | How it's measured |
|---|---|---|
| S1 | A new user creates 3 correctly typed notes within 15 min of cloning, without help | Pilot onboarding session |
| S2 | The same 5 note types, created by a human and by an agent, have identical structure (same properties, same headings) | Phase 2 conformance review |
| S3 | Pilot users still use it in week 3: ≥ 5 notes/week each, nothing in the inbox older than 7 days | Count notes in the vault |
| S4 | A person or agent answers 5 "where is X / what did we decide about Y" questions in < 2 min each | Pilot exercise |
| S5 | No agent safety violations (no deletes, no rewrites of human prose, no secrets written) | Review the agent log and git diff |
| S6 | No more than **5** community plugins in the default stack | Plugin count |

### 1.2 Note-taking method & vault structure
Options to compare:
- **A. PARA** (Projects / Areas / Resources / Archive) — organizes by actionability; good for work.
- **B. Zettelkasten / evergreen notes** — atomic, densely linked ideas; good for learning.
- **C. Type-based** (folder per note type: meetings, decisions, …) — predictable for agents.
- **D. Hybrid (prototype):** folders express *lifecycle* (inbox → projects/areas → knowledge → archive), the `type` property expresses *kind*.

Questions:
- [ ] Which method (A–D)?
- [ ] Folders vs. properties vs. tags: what is each one used for (one job each)?
- [ ] Where do role-specific docs live (PRD, spec, runbook, incident): inside the project, in knowledge, in records?
- [ ] Hubs: project notes, area notes, MOCs — which are mandatory, and must every note link to one?
  - Draft proposal: [[design/linking|Linking guidelines]] §4
- [ ] Naming conventions: date prefixes, type prefixes (`DEC`, `INC`, `RUNBOOK`), allowed characters, language (EN only?)
- [ ] Inbox policy: everything lands in inbox first? Max age before processing?
- [ ] Archive policy: when and how notes are archived; is deleting ever allowed?

### 1.3 Template catalogue
Decide which note types ship in v1. For each accepted type agree on: purpose · folder · filename pattern · required properties · section headings · status values.

| Type | For | Candidate role pack | v1? |
|---|---|---|---|
| inbox | quick capture | everyone | ⬜ |
| daily / weekly | journal, review | everyone | ⬜ |
| project | time-bound outcome (hub) | everyone | ⬜ |
| area | ongoing responsibility (hub) | everyone | ⬜ |
| note | one idea / concept | everyone | ⬜ |
| howto | repeatable procedure | everyone | ⬜ |
| reference | summary of article/book/talk | everyone | ⬜ |
| moc | map of content | everyone | ⬜ |
| meeting | notes + decisions + action items | everyone | ⬜ |
| decision | ADR-style record | everyone | ⬜ |
| person | person / team | everyone | ⬜ |
| prd | product requirements | product, design | ⬜ |
| story | user story + acceptance criteria | product, qa | ⬜ |
| spec | technical design / RFC | engineering | ⬜ |
| debug-log | bug investigation diary | engineering, qa | ⬜ |
| runbook | operational response | devops | ⬜ |
| incident | incident + postmortem | devops | ⬜ |

- [ ] Accept / drop / merge types (fewer is easier to adopt — is 17 too many for v1?)
- [ ] Missing types? (e.g. OKR, retro, interview, release notes, learning log, 1:1)
- [ ] Section headings per template are **fixed contracts** (agents and humans rely on them) — agree the list per type
- [ ] Template language for placeholders: core `{{date}}` syntax vs. Templater `<% %>` (see 1.6) — affects how agents fill them

### 1.4 Properties (frontmatter) schema
- [ ] Common properties for every note (prototype: `type`, `created`, `updated`, `status`, `author`, `tags`, `related`)
- [ ] Per-type required properties and allowed `status` values
- [ ] Value formats: dates (`YYYY-MM-DD`), links in properties (`"[[Note]]"`), lists, people (`[[Person]]` vs text)
- [ ] Tags: taxonomy (e.g. `topic/…`, `role/…`), or tags kept minimal and properties used instead?
- [ ] Provenance: how to mark who wrote a note (`author: human` / `agent:<name>`) and who last changed it
- [ ] Where the schema is documented as the single source of truth (Markdown doc? fileClass notes? JSON?) — depends on 1.6

### 1.5 How humans take notes (workflow)
- [ ] Capture: hotkey/mobile/quick-add flow; "capture fast, organize later"
- [ ] Process: who processes the inbox and how often (human, agent, both)
- [ ] Distill: when a meeting/debug log becomes a reusable knowledge note
- [ ] Review cadence: daily (5 min), weekly (30 min), monthly area review — what is the checklist
- [ ] Tasks: inside notes (`- [ ]`) or in an external tool (Jira, etc.) linked from notes?
- [ ] Linking habits: minimum one hub link; when to create a new note vs. extend an existing one

### 1.6 Community plugins — human notes must match the templates
Principle to agree on: **one schema, two paths** — humans get the template through plugins, agents get it through written rules; both must produce identical structure.

| Need | Candidate plugins | Notes / trade-offs |
|---|---|---|
| Create a note from the right template | **Templater** (folder templates), **QuickAdd** (choice menu: type → template → folder → filename), core Templates + Auto Template Trigger | Templater syntax `<% %>` is powerful but agents can't execute it — they must write the *rendered* result. QuickAdd doesn't auto-apply by folder; it's an explicit "new X" command |
| Put the note in the right folder with the right name | QuickAdd, Templater (`tp.file.move`), Auto Note Mover | Moving by property/tag vs. creating in place |
| Typed, validated properties (dropdowns for `status`, required fields) | **Fileclass** (successor of Metadata Menu, frontmatter-only, Bases-based), Metadata Menu | Gives humans guided input matching the schema; fileClass notes could *be* the schema agents read |
| Keep formatting consistent (property order, `updated` timestamp, headings) | **Linter** | Auto-fixes on save; agents' output passes through the same rules when opened |
| Dashboards / queries | core **Bases** (prefer), Dataview | Bases only reads frontmatter → everything queryable must be a property |
| Tasks across notes | Tasks plugin, or core only | Only if 1.5 keeps tasks in the vault |
| Daily/weekly notes | core Daily notes, Periodic Notes | Weekly needs a plugin or a QuickAdd choice |
| Sync / version control | Obsidian Git, Obsidian Sync, iCloud | Personal only (D2); mobile is read-only (D6) — sync just needs to deliver notes to the phone |

- [ ] Minimal set of plugins (every extra plugin = onboarding + maintenance cost); candidate stacks:
  - **Lean:** core only (Templates, Daily notes, Properties, Bases) + Linter
  - **Guided (candidate recommendation):** Templater + QuickAdd + Fileclass + Linter + Bases
  - **Power:** Guided + Dataview + Tasks + Periodic Notes + Obsidian Git
- [ ] Check each chosen plugin: maintained in 2026, mobile support, license, data stays local
- [ ] Ship plugin settings in the template (`.obsidian/plugins/*/data.json`) or document manual setup?
- [ ] How do we prove human-created and agent-created notes match? (manual review checklist in Phase 2, automated check in Phase 3)

### 1.7 Rules for AI agents
- [ ] Read order before acting (vault profile → schema → AGENTS.md → recent log)
- [ ] Creating notes: must start from the template file and keep every heading; never invent properties
- [ ] Editing human notes: append-only / suggestion callouts (`> [!agent]`) / free edit?
- [ ] Immutable records: decisions, incidents, past meetings — supersede instead of edit
- [ ] Never delete — archive; off-limits areas (`_private/`, `.obsidian/`)
- [ ] Provenance and audit: `author`, `updated`, an append-only agent log
- [ ] Quality bar: TL;DR line, one idea per note, link to a hub, no secrets / personal data
- [ ] Standard agent workflows to support: capture, process inbox, daily start, meeting → decisions/tasks, weekly review, debug-log → how-to, close project
- [ ] How rules are delivered: `AGENTS.md` only, plus tool-specific skills (Claude), plus rules inside each template (comments)?
- [ ] Linking rules for humans and agents — see draft [[design/linking|Linking guidelines]] (granularity, hub rule, backlink discovery, renaming, search strategy)

### 1.8 Exit criteria for Phase 1
- [ ] All items above have a decision in the log
- [ ] Owner sign-off; Phase 2 task list derived from decisions

---

## Phase 2 — Template authoring (no code) ⬜
- [ ] Final templates for every accepted type (in the chosen placeholder syntax)
- [ ] Schema document (properties, statuses, naming, folders)
- [ ] `AGENTS.md` v1 (+ `CLAUDE.md` pointer)
- [ ] Plugin list + settings (Templater/QuickAdd choices, Fileclass definitions, Linter rules)
- [ ] Home dashboard and Bases views
- [ ] Human onboarding guide (README) and per-role quick-start pages
- [ ] Conformance review: one person + one agent create the same 5 note types → compare

## Phase 3 — Tooling & automation (code) ⬜
- [ ] Bootstrap (new vault from template, choose roles/mode)
- [ ] Validator (properties, folders, links, stale inbox) usable by agents and CI
- [ ] Agent skills/commands for the standard workflows
- [ ] ~~CI for team vaults~~ — dropped, no team vaults in v1 (D2)
- [ ] Re-evaluate the parked Phase 0 scripts against Phase 1–2 decisions

## Phase 4 — Pilot ⬜
- [ ] Pilot users: PO, engineer, DevOps — each with their own personal vault (D2)
- [ ] 2–3 weeks real use with an agent; collect friction log
- [ ] Adjust templates/rules; measure success criteria from 1.1

## Phase 5 — Release v1 ⬜
- [ ] Tag v1, publish as GitHub template repo
- [ ] Changelog + process for changing the schema (who approves, migration of existing notes)

---

## Decision log
| # | Date | Topic | Decision | Why |
|---|---|---|---|---|
| D1 | 2026-11-13 | Process | Phase 1 is discussion only — no code/scripts until templates and rules are agreed | Avoid building tooling around unagreed structure |
| D2 | 2026-11-19 | 1.1 Primary user | v1 targets individuals only: one personal vault per person, nothing shared | Personal habit comes first; sharing adds Git, privacy and convention overhead that v1 doesn't need |
| D3 | 2026-11-19 | 1.1 Profiles | One template, no team profile (the prototype's `mode: personal\|team` goes away) | Follows from D2; fewer variants to maintain |
| D4 | 2026-11-19 | 1.1 Privacy | The whole vault is private to its owner; no team/private split | Follows from D2. Whether a separate `_private/` area (off-limits to agents) is still needed is moved to 1.2/1.7 |
| D5 | 2026-11-19 | 1.1 Agents | Agent-agnostic: `AGENTS.md` is the only source of rules; tool-specific skills (Claude) are thin wrappers that add no rules. Every rule must be followable with plain Markdown read/write, no scripts | Works with any AI tool; scripts are optional speed-ups (Phase 3) |
| D6 | 2026-11-19 | 1.1 Platform | Desktop is the only place notes are written; mobile is read-only (no mobile capture) | Plugins don't need mobile support, which widens the choice in 1.6 |
| D7 | 2026-11-19 | 1.1 Success criteria | Adopt S1–S6 (see 1.1), with S6 = max 5 community plugins | Measurable and checked in the Phase 2 review / Phase 4 pilot; keeps adoption cost low |

## Open questions / parking lot
- Should the vault support multiple languages (e.g. EN + VI notes)?
- Integration with Jira/Confluence: link only, or sync?
- ~~Team vault size: one vault per team or per organization?~~ — moot after D2
- Prototype `AGENTS.md` says "always create notes with the script", which conflicts with D1/D5 — rewrite in Phase 2
- How (if at all) people share a note from their personal vault with others later (export, copy to Confluence, …) — post-v1
