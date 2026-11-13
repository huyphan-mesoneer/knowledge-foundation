# knowledge-foundation

An Obsidian vault template for **personal and team knowledge** that works for any role — product owner, engineer, DevOps, QA, designer, manager — and is designed to be **maintained by humans and AI agents together**.

- Plain Markdown + YAML frontmatter, core Obsidian only (no community plugins required).
- One schema (`_system/schema.json`) defines every note type, its folder, filename and template — humans, scripts and agents all follow the same contract.
- Agents get an operating manual (`AGENTS.md`, also loaded via `CLAUDE.md`), a note-creation script, a linter, and an append-only change log.

## Quick start

```bash
# 1. Get a copy (GitHub "Use this template", or clone)
git clone <this-repo> my-vault && cd my-vault

# 2. Bootstrap for yourself (or your team)
python3 _system/scripts/bootstrap.py --owner "Your Name" --roles engineering,devops --mode personal
#   roles: product, engineering, devops, qa, design, management (comma-separated, any mix)
#   mode:  personal (everything in git)  |  team (journal kept out of git)

# 3. Open the folder as a vault in Obsidian (1.9+ for Bases dashboards) and start at Home.
```

Bootstrap creates your area notes for the chosen roles, today's daily note, and `_system/vault.json` (which agents read to learn who you are).

## Structure

```
00-inbox/          capture anything; process weekly
10-journal/        daily/ and weekly/ notes
20-projects/       one folder per project: hub note + PRDs, stories, specs
30-areas/          ongoing responsibilities (role areas, systems, domains)
40-knowledge/      atomic notes, how-tos, runbooks, references, MOCs
50-meetings/       meeting notes
60-records/        decisions (DEC), incidents (INC), debug logs (DBG)
70-people/         people and teams
90-archive/        finished/inactive, original subpath kept
_attachments/      images and files
_private/          git-ignored personal notes (agents stay out)
_system/           schema, templates, views (.base), scripts, agent log
Home.md            dashboard
AGENTS.md          rules for AI agents (CLAUDE.md points here)
```

The idea: **folders express lifecycle** (inbox → active → evergreen → archive), **frontmatter `type` expresses kind**. Projects end; areas don't; knowledge outlives both.

## Note types

| Type | For | Folder | Role pack |
|---|---|---|---|
| inbox | quick capture | 00-inbox | everyone |
| daily / weekly | log, focus, review | 10-journal | everyone |
| project | time-bound outcome (hub) | 20-projects/&lt;P&gt; | everyone |
| area | ongoing responsibility | 30-areas | everyone |
| note | one idea / concept | 40-knowledge | everyone |
| howto | repeatable procedure | 40-knowledge | everyone |
| reference | summary of an article/book/talk | 40-knowledge | everyone |
| moc | map of content for a topic | 40-knowledge | everyone |
| meeting | notes, decisions, action items | 50-meetings | everyone |
| decision | ADR-style decision record | 60-records | everyone |
| person | person or team | 70-people | everyone |
| prd | product requirements | 20-projects/&lt;P&gt; | product, design |
| story | user story + acceptance criteria | 20-projects/&lt;P&gt; | product, qa |
| spec | technical design / RFC | 20-projects/&lt;P&gt; | engineering |
| debug-log | bug investigation diary | 60-records | engineering, qa |
| runbook | operational response | 40-knowledge | devops |
| incident | incident + postmortem | 60-records | devops |

All templates are available to everyone; the role packs only decide which areas bootstrap creates and which templates are suggested.

## Daily use (humans)

- **Capture:** `Cmd/Ctrl+N` creates a note in the inbox. Don't organize while capturing.
- **Typed note:** create a note, then *Templates: Insert template* → pick `tpl-…`. Move it to the folder from the table above (or use the script below).
- **Today:** *Daily notes: Open today's daily note*.
- **Weekly (30 min):** create the weekly note and follow its checklist — empty the inbox, update projects, promote good ideas into knowledge notes.
- **From a terminal:** `python3 _system/scripts/new_note.py meeting "Sprint 42 planning" --project "Checkout revamp"` puts the note in the right place with the right name.

## Working with AI agents

Point any coding/AI agent (Claude Code, Cursor, Copilot, Codex, …) at the vault folder. They read `AGENTS.md`, which tells them to:

- create notes only through `new_note.py` (correct folder, name, template),
- never delete (archive instead) and not rewrite human prose (append or add `> [!agent]` callouts),
- mark their notes `author: agent:<name>` and append to `_system/agent-log.md`,
- run `lint.py` before finishing.

Claude Code also gets ready-made skills in `.claude/skills/`: **vault-capture**, **vault-process-inbox**, **vault-daily**, **vault-weekly-review**. Try: *"process my inbox"*, *"file these meeting notes"*, *"do my weekly review"*.

## Personal vs team

- **Personal:** one vault per person; sync via git, iCloud or Obsidian Sync.
- **Team:** one shared git repo. Run bootstrap with `--mode team` so `10-journal/` stays local, keep private notes in `_private/` (git-ignored), and let CI run the linter (`.github/workflows/vault-lint.yml`). Each person can still keep a separate personal vault from the same template.

## Maintenance

```bash
python3 _system/scripts/lint.py         # frontmatter, folders, broken links, stale inbox
```

To add a note type: add it to `_system/schema.json`, add `_system/templates/tpl-<type>.md`, done — the script and linter pick it up.
