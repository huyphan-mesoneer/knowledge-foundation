# AGENTS.md — operating manual for AI agents in this vault

This is an Obsidian vault used by **humans and AI agents together**. Humans read and write it in Obsidian; agents read and write the same Markdown files directly. Everything you need is plain text: Markdown + YAML frontmatter + `[[wikilinks]]`.

Follow these rules exactly. When a rule conflicts with a direct instruction from the vault owner, the owner wins.

## 1. Orient first

1. Read `_system/vault.json` — owner, roles (product, engineering, devops, …) and mode (`personal` or `team`).
2. Read `_system/schema.json` — the note types, their folders, filenames, templates and allowed `status` values. It is the single source of truth; this file only explains it.
3. Skim `Home.md` and the last ~20 lines of `_system/agent-log.md` to see what happened recently.

## 2. Folder map

| Folder | What lives here | Lifecycle |
|---|---|---|
| `00-inbox/` | Unprocessed captures | Processed within 7 days, then moved/merged/archived |
| `10-journal/daily`, `/weekly` | Daily notes, weekly reviews | Append-only log |
| `20-projects/<Project>/` | One folder per project. Hub note `<Project>.md` + project docs (PRD, stories, specs) | Moves to `90-archive/` when done |
| `30-areas/` | Ongoing responsibilities (no end date) | Long-lived |
| `40-knowledge/` | Atomic notes, how-tos, runbooks, references, MOCs | Evergreen; keep updated |
| `50-meetings/` | Meeting notes | Immutable after the day, except action-item checkboxes |
| `60-records/` | Decisions (DEC), incidents (INC), debug logs (DBG) | Immutable once closed; supersede, don't rewrite |
| `70-people/` | People and teams | Long-lived |
| `90-archive/` | Anything no longer active (keep its original subfolder) | Read-only |
| `_attachments/` | Images, PDFs, exports | — |
| `_private/` | Owner's private notes. Git-ignored. | **Off-limits to agents unless explicitly asked** |
| `_system/` | Schema, templates, views (`.base`), scripts, agent log | Change only when asked |

## 3. Creating notes

**Always create notes with the script** — it picks the right folder, filename and template, fills dates, and is idempotent:

```bash
python3 _system/scripts/new_note.py <type> "<Title>" [--project "<Project>"] [--author agent:<your-name>]
# examples
python3 _system/scripts/new_note.py daily --author agent:claude
python3 _system/scripts/new_note.py meeting "Sprint 42 planning" --project "Checkout revamp" --author agent:claude
python3 _system/scripts/new_note.py decision "Use Postgres for event store" --author agent:claude
```

It prints the path of the created (or already existing) note. Then edit that file to fill in the sections.

If you cannot run scripts, copy the template from `_system/templates/tpl-<type>.md`, replace `{{title}}`/`{{date:…}}` yourself, and save it at the folder/filename given in `schema.json`.

## 4. Frontmatter contract

Every note in a numbered folder starts with YAML frontmatter:

```yaml
---
type: note              # required, one of schema.json types
created: 2026-11-13     # required, YYYY-MM-DD
updated: 2026-11-14     # set whenever you change content
status: seedling        # if the type defines statuses, use only those values
author: human           # or agent:<name> for notes an agent created
tags: [topic/kafka]     # lowercase, kebab-case, nested with /
related: ["[[Checkout revamp]]", "[[Payments]]"]   # links to hubs (project/area/moc)
---
```

- Filename **is** the title. No `title:` field. Don't use `/ \ : * ? " < > | # ^ [ ]` in names.
- Every note (except daily/weekly/inbox) must link to at least one hub — a project, area or MOC — via `related` or the body. Orphans are lost knowledge.
- Never store secrets, credentials, tokens or customer personal data. Link to the secure system instead.

## 5. Writing style

- **One idea per knowledge note.** Split when a note covers two things.
- Start knowledge notes with a `> **TL;DR**` line that stands on its own.
- Link generously with `[[wikilinks]]`; create the target note if it deserves to exist.
- Prefer updating an existing note over creating a near-duplicate. Search first (`grep -ril "<term>" --include=*.md .`).
- Dates are ISO `YYYY-MM-DD`. Tasks are `- [ ] what — @owner — 📅 YYYY-MM-DD`.

## 6. Safety rules for agents

1. **Never delete.** Move to `90-archive/` keeping the original subpath. Obsidian links keep working.
2. **Don't rewrite human prose.** On notes with `author: human`, append (e.g. under `## Agent notes` or the section's end) or add a clearly marked suggestion `> [!agent] …`. Fix only obvious typos/links/frontmatter.
3. **Don't edit closed records.** Accepted decisions, resolved incidents and past meetings: create a new record that supersedes/links instead (action-item checkboxes may be ticked).
4. **Don't touch** `.obsidian/`, `_private/`, `_system/` (other than appending to `agent-log.md`) unless asked.
5. **Log your changes.** Append one line per session to `_system/agent-log.md`:
   `- 2026-11-13 14:05 · agent:claude · created [[2026-11-13 Sprint 42 planning]], updated [[Checkout revamp]] · why: owner asked to file meeting notes`
6. **Validate before finishing:** `python3 _system/scripts/lint.py` must report 0 errors.

## 7. Standard workflows

**Capture** (any input: chat, paste, transcript, link) → if the destination is obvious, create the typed note directly; otherwise `new_note.py inbox "<short title>"` and dump the content.

**Process inbox** (`00-inbox/`) → for each item: (a) merge into an existing note, (b) turn into a typed note via `new_note.py`, (c) extract tasks into the relevant project/daily note, or (d) archive if worthless. Then move the inbox file to `90-archive/00-inbox/`. Report what went where.

**Start of day** → create today's daily note; carry over unchecked tasks from the previous daily note; list active projects (`status: active`) and due tasks.

**Meeting notes** → `meeting` note linked to project/people; decisions become `decision` records (link both ways); action items stay as tasks in the meeting and are referenced in the project's hub.

**Decision** → `decision` record with context, options, outcome; add it to the project/area hub under `## Decisions`. To change an accepted decision, create a new one with `supersedes: "[[old]]"` and set the old one's status to `superseded`.

**Debug → knowledge** → when a `debug-log` is solved, extract the reusable lesson into a `howto` or `note` and link it from the log.

**Incident** → `incident` record during/after; afterwards update or create the `runbook`; action items go to the owning project/area.

**Weekly review** → create the `weekly` note; process the inbox; summarize the week's daily notes; update project statuses; list stale notes (`status: seedling` older than 30 days, runbooks not verified in 90 days); propose next week's priorities.

**Close a project** → set `status: done`, write the outcome + lessons in the hub, move the whole folder to `90-archive/20-projects/`.

## 8. Useful commands

```bash
python3 _system/scripts/lint.py              # validate frontmatter, folders, links, stale inbox
python3 _system/scripts/lint.py --json       # machine-readable
grep -rl "^type: project" --include=*.md 20-projects | xargs grep -l "^status: active"   # active projects
grep -rn -- "- \[ \]" --include=*.md 20-projects 30-areas 10-journal | head            # open tasks
```
