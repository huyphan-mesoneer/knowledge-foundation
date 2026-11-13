---
status: draft
created: 2026-11-13
updated: 2026-11-13
owner: Huy Phan
roadmap: "[[ROADMAP#1.7 Rules for AI agents]]"
---
# Linking guidelines (draft)

> **TL;DR** — Link to whole notes by default, to a standard template heading when only one section matters, and almost never to blocks. Every note links to at least one hub. Backlinks and the graph are computed by Obsidian from those links, so humans and agents only ever write **outgoing** links — correctly named, to notes that exist.

Status: draft from the Phase 1 discussion on 2026-11-13. Feeds roadmap items 1.2 (structure), 1.5 (human workflow) and 1.7 (agent rules). Nothing here is decided until it is in the roadmap's decision log.

## 1. How linking works in Obsidian

- A link is plain text in a file: `[[Note name]]`. Nothing else is stored.
- **Backlinks are computed, not written.** If note A contains `[[B]]`, Obsidian shows A in B's backlinks pane. Nobody "creates" a backlink.
- **Links in properties count.** `related: ["[[Checkout revamp]]"]` shows up in backlinks and the graph like a body link.
- **Unlinked mentions:** Obsidian also lists notes that contain a note's name as plain text, so they can be turned into links.
- **Renaming inside Obsidian updates every link** to the renamed note. Renaming the file outside Obsidian (terminal, script, agent) does **not**.

## 2. Seeing the knowledge graph (humans)

| Tool | Use it for |
|---|---|
| Backlinks pane (incl. unlinked mentions) | "What refers to this note?" — daily use |
| Outgoing links pane | "What does this note depend on?" |
| Local graph | Neighbourhood of the current note, 1–2 hops |
| Global graph (filtered, coloured by `type`) | Exploring, spotting clusters, orphans and gaps — not daily navigation |
| Hub notes (project, area, MOC) | Primary navigation |
| Bases views | Lists by property; can show link counts to find orphans |

The graph is only as useful as the linking discipline behind it — hubs matter more than the graph.

Optional later (not v1): plugins for typed relations such as parent/child or supersedes (e.g. Breadcrumbs, ExcaliBrain).

## 3. Granularity: what to link to

| Level | Syntax | When | Share |
|---|---|---|---|
| Note | `[[Checkout revamp]]` | Default | ~90% |
| Heading | `[[Checkout revamp#Decisions]]` | Target is long and only one section matters. Only to **standard template headings** (stable across notes) | occasional |
| Block | `[[Checkout revamp#^r1]]` | One exact line (requirement, action item). Requires adding `^id` to the target note | rare |
| Embed | `![[Spec#API]]` | Show the target content inline instead of just linking | rare |

**Rule of thumb:** if you keep needing to link to a specific item inside a note, that item deserves its own note — a decision in meeting notes → a `decision` record; a lesson in a debug log → a `howto`/`note`. Then a plain note link is enough (one idea per note).

Caveats:
- Heading links can break when a heading is renamed → fixed template headings keep them stable.
- Block links modify the target note (they add `^id`) → restricted for agents (see §5).

## 4. Linking rules (everyone)

1. **Every note links to at least one hub** (project, area or MOC) via `related` or the body. Exceptions: daily, weekly, inbox.
2. **File name = title, and names are unique**, so `[[Name]]` always resolves to exactly one note. No `title` property.
3. **Link to the exact file name**; use `[[Name|other wording]]` for display text.
4. **Hubs list their key children explicitly** (a project lists its decisions, specs, PRDs) even though backlinks would show them — readers and agents can then read one note instead of searching.
5. **Link generously, but only to notes that exist** — or create the target if it deserves to be a note. Don't leave dangling links as placeholders.
6. **Prefer extending an existing note to creating a near-duplicate**; search before creating.
7. **Rename inside Obsidian** so links are updated.

## 5. Rules for AI agents

Agents never load the whole vault and cannot see Obsidian's panes. They work on plain text:

**Before writing a link — discover what exists**
1. List note names (file names are titles — cheap).
2. Search keywords and `aliases`.
3. Check the relevant hub notes.
4. Link if a matching note exists; otherwise create it (if it deserves to exist) or leave plain text. **Never invent a link to a non-existent note.**

**Reading backlinks** — search the vault for `[[Note name` (plus its aliases). This returns what Obsidian's backlinks pane shows. Searching the bare name finds unlinked mentions, which the agent may **suggest** linking.

**Granularity**
- Note links by default.
- `#Heading` only to standard template headings.
- **Don't add block IDs (`^id`) to human-written notes.** If precise linking is needed, propose extracting the item into its own note.

**Renaming** — agents don't rename notes. If a rename is required, the agent must find and update every `[[Old name…]]` (including `#heading` and `|alias` forms) in the same change, and log it.

**Hubs** — when an agent creates a note under a project/area, it also adds the link to the hub's relevant section (e.g. `## Decisions`), appending only.

## 6. How agents find information (search strategy)

Agents use on-demand search, not full loading:

- **Always loaded:** a short `AGENTS.md` (core rules only).
- **Loaded when relevant:** skills (Markdown instructions, no code) — candidates:
  - `vault-search`: hubs first → filter by properties (`type`, `status`) → full-text search → follow links 1–2 hops → read only matching notes.
  - `vault-write`: right template, search before create, fill properties, link to a hub, don't rewrite human prose.
  - Workflow skills: capture, process inbox, weekly review, meeting → decisions/tasks.
- **Runtime tools:** the agent's built-in file search; plain text + consistent properties scale to a few thousand notes.
- **Later (Phase 3, only if needed):** an Obsidian MCP server or generated index (direct backlinks/queries), semantic search (e.g. Smart Connections) when keyword search misses.

## 7. Open questions

- [ ] Is "every note links to a hub" mandatory, or a warning only?
- [ ] Are heading links allowed only to template headings, or any heading?
- [ ] Do we allow block references at all in v1?
- [ ] Should agents be allowed to convert unlinked mentions into links automatically, or only suggest?
- [ ] Typed relations (supersedes, depends-on, parent) as properties now, or later?
- [ ] When (vault size / pain) do we add an index or MCP layer for agents?
