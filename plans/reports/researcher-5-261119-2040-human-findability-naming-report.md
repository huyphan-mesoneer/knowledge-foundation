# Researcher 5: Human findability (folders vs properties vs tags vs links, naming)

> Saved by the team lead from researcher-5's messages (the researcher returns findings in messages instead of writing files). Section 2.1 was truncated in transit; the rows that arrived are kept.

Scope: angle 5 of 6. Reads: ROADMAP §1.2, §1.4, §1.6; `design/linking.md`; `AGENTS.md`; `Home.md`; `_system/views/*.base`; `_system/schema.json`.

## 1. Executive summary

- **Give each mechanism one job.** Obsidian's owner (Kepano) and the official docs point the same way: few folders, kind and state in properties, links for relationships, search or Bases for retrieval.
- **Bases reads frontmatter and link properties.** `file.links` includes frontmatter links, so `related: ["[[Hub]]"]` works in views. This contradicts one forum opinion ("don't put links in properties"), but the official docs support it.
- **Search has no `property:` operator.** Use `[type:decision]`, `[status:open]`, `[status:null]`. Write this down for S4.
- **Property types are vault-wide.** `status`, `type`, `created` must keep one type everywhere.
- **Filenames: readable title, plus a date or short kind code only where it helps.** Type prefixes only where many kinds share one folder (`20-projects/<Project>/`, `60-records/`).
- **Home: short dashboard plus a "where things live" table.** Practitioners navigate by quick switcher, backlinks and hubs. Max 4–5 widgets.

## 2. Key findings

### 2.1 Official Obsidian behavior (verified; partially truncated)

| Fact | Source | Design impact |
|---|---|---|
| Bases shows files as rows and properties as columns. Views: Table, List, Cards, Kanban, Map. Data lives in local Markdown properties. | [Bases help](https://obsidian.md/help/bases) | Anything to be queried must be a property. |
| Bare names in Bases are note properties; `file.*` is file metadata (`file.name`, `file.folder`, `file.path`, `file.tags`, `file.links`, `file.backlinks`, `file.ctime`, `file.mtime`). `file.hasLink()`, `file.hasTag()`, `file.inFolder()` are functions. | [Bases syntax](https://obsidian.md/help/bases/syntax) | Views can filter by folder and by hub link. |
| Wikilinks in frontmatter are Link objects; `file.links` includes them. | [Bases syntax](https://obsidian.md/help/bases/syntax) | `related` links can drive hub views. |
| `file.backlinks` is performance-heavy; reverse the lookup with `file.links` when possible. | [Bases syntax](https://obsidian.md/help/bases/syntax) | Use `related` on the child note. |
| Search operators: `tag:`, `path:`, `file:`, `content:`, `line:`, `section:`, `task:`, regex, `OR`, `-`. Properties: `[property]`, `[property:value]`, `[property:null]`. No `property:` operator. | [Search](https://obsidian.md/help/plugins/search) | Document the bracket syntax. |
| _(remaining rows truncated in transit)_ | | |

### 2.2 Practitioner positions (ranked by credibility)

| Rank | Source | Position | Credibility |
|---|---|---|---|
| 1 | stephango.com/vault (Kepano, Obsidian CEO) | Few folders ("many of my entries belong to more than one area of thought"). Properties (`categories`) main organizer. Links used profusely. Navigates via quick switcher, backlinks, in-note links; mostly skips file explorer. `YYYY-MM-DD` dates everywhere. | Product owner; personal practice, not a spec. |
| 2 | Forum, ryadaj — [opinionated reflection](https://forum.obsidian.md/t/an-opinionated-reflection-on-using-folders-links-tags-and-properties/78548) | Folders by file type. Links for navigation. Tags: 1–3 word topics, controlled vocabulary. Properties for minutiae. "Don't put links in properties." Knowledge notes named as statements. | 3 yrs practice; link-in-properties advice conflicts with Bases docs. |
| 3 | Forum, MitchWagner — [folders vs linking vs tags](https://forum.obsidian.md/t/folders-vs-linking-vs-tags-the-definitive-guide-extremely-short-read-this/78468) | Many folders for projects, few for PKM. Links as main map. Tags sparingly. | Community opinion; disputed. |
| 4 | [dsebastien](https://www.dsebastien.net/structure-a-findable-obsidian-vault-folders-links-dates-and-daily-notes/) | Folders by what a note is, not what it's about. Max 3–4 levels. Type prefixes. Aliases for abbreviations. ISO dates for chronological notes. One index note. MOCs at ~50+ notes. | Concrete but promotional. |
| 5 | [Atlas](https://laoujin.github.io/Atlas/research/2026-05-30-beginner-intermediate-obsidian-a-roadmap-for-a-developer-with-a-1-200-note-vault/properties-tagging-for-queryable-notes/) | Typed properties for sortable values. Closed sets in properties, not tags. Start with type, status, topic only. | Secondary checklist. |

Agree: folders = kind/lifecycle not topic; properties = sortable closed sets; links = relationships; tags optional topic search; dates in filenames only for chronological notes.
Disagree: links in properties (follow docs: yes); tags (keep optional, topic-only); folders (keep lifecycle folders, not kind folders).

### 2.3 Fit with this repo

- Consistent with D2–D7; core Bases + search cover findability without plugins.
- `visibility` redundant under D4 → remove (owner confirm).
- `source` and `related` both carry links → `related` is the single relationship property; `source` becomes text/URL.
- `PRD`/`STORY`/`SPEC` prefixes justified (shared project folder).
- S4 needs a written query recipe on Home and in AGENTS.md.

## 3. Recommendations

### 3.1 One job each

| Mechanism | One job | Example | Not for | Who sets it |
|---|---|---|---|---|
| Folder | Lifecycle and location | `20-projects/<P>/`, `40-knowledge/`, `90-archive/` | Kind, topic, status | Moved only on lifecycle change |
| `type` | Kind | `type: decision` | Location, state | At creation, never changed |
| `status` | State within a kind | `status: open` | Kind, topic | Owner/workflow |
| `related` | Hub membership + relationships | `related: ["[[Checkout revamp]]"]` | Kind, state | At creation; appended |
| Body links | Relationships in text | `[[Payments API]]` | Structural metadata | In text |
| `tags` (optional) | Topic search, `topic/*` only, max 3 | `tags: [topic/kafka]` | Kind, state, role | Optional |
| `aliases` | Synonyms, abbreviations, translations, old names | `aliases: [PSP]` | Separate notes | Optional |
| Filename | Identity and recall | `DEC 2026-11-19 Use Postgres for event store` | Status | Fixed after creation |
| Bases views | Retrieval by property | `records.base` | Storage | Shipped in `_system/views/` |
| Bookmarks | Personal pins | pinned hub | Shared structure | Personal |
| Graph | Exploration, orphan spotting | Local graph | Daily navigation | Human only |

Rule: a property never repeats what a folder says; a tag never repeats `type` or `status`. Remove `visibility`; `source` = text/URL; keep `roles` only if a view needs it.

### 3.2 Naming per note kind

General: filename = title, unique; forbidden `/ \ : * ? " < > | # ^ [ ]` (use ` - ` for `:`); English filenames and property names; one property-name style; ISO dates.

| Kind | Folder | Pattern | Example |
|---|---|---|---|
| inbox | `00-inbox/` | `YYYY-MM-DD <short title>` | `2026-11-19 Kafka retry idea` |
| daily | `10-journal/daily/` | `YYYY-MM-DD` | `2026-11-19` |
| weekly | `10-journal/weekly/` | `YYYY-[W]WW` | `2026-W47` |
| meeting | `50-meetings/` | `YYYY-MM-DD <Title>` | `2026-11-19 Sprint 42 planning` |
| decision | `60-records/` | `DEC YYYY-MM-DD <Title>` | `DEC 2026-11-19 Use Postgres for event store` |
| incident | `60-records/` | `INC YYYY-MM-DD <Title>` | `INC 2026-11-20 Checkout 500s during deploy` |
| debug-log | `60-records/` | `DBG YYYY-MM-DD <Title>` | `DBG 2026-11-18 Flaky login test` |
| project hub | `20-projects/<Project>/` | `<Project>` | `Checkout revamp` |
| PRD/story/spec | `20-projects/<Project>/` | `PRD <Title>` / `STORY <Title>` / `SPEC <Title>` | `SPEC Payment retries` |
| area hub | `30-areas/` | `<Area>` | `Platform on-call` |
| note | `40-knowledge/` | Statement title | `Idempotency keys prevent duplicate charges` |
| howto/runbook | `40-knowledge/` | `<Service> - <task>` (no RUNBOOK prefix) | `Payments - rotate API key` |
| reference | `40-knowledge/` | Source title | `Designing Data-Intensive Applications` |
| moc | `40-knowledge/` | `MOC <Topic>` | `MOC Payments` |
| person/team | `70-people/` | `<First Last>` / `<Team>` | `Ada Lovelace` |

Prefix only where several kinds share a folder. Date IDs beat sequential numbers (no counter, no collisions).

### 3.3 Home dashboard

1. One capture line.
2. "Where things live" table (≤8 rows): in progress → active projects; what we decided → decisions view; what is broken → open incidents; how to do X → `[type:howto] X`; who is X → `[type:person] X`; a day → daily note; unsure → open debug logs; old work → `90-archive/`.
3. Four Bases embeds, ≤10 rows each: Inbox (alert >7 days), Active projects, Open records, Recently changed.
4. Move Meetings/Knowledge/Areas embeds to their own hub notes.

Pilot measure: Home opens vs quick-switcher use; if unused by week 2, cut to table only.

### 3.4 Search recipes (Home + AGENTS.md)

- Kind: `[type:decision] Postgres` · State: `[type:incident] [status:open]` · Hub: `file.hasLink` in Bases or search `[[Checkout revamp]]` · Topic: `tag:#topic/kafka` · Title: quick switcher (`DEC 2026`) · Alias: quick switcher (verify).

## 4. Trade-offs

| Option | Upside | Downside | Verdict |
|---|---|---|---|
| Type prefix everywhere | Typeable | Hurts readability; redundant with `type` | Only in shared folders |
| Date prefix everywhere | Sorts | Noise for knowledge | Dated kinds only |
| Tags as primary index | Cross-cutting | Fragments; duplicates properties | Optional, topic-only |
| Links as primary index | Strong relationships | Needs hub discipline | Required for hubs |
| Many topic folders | Familiar | Notes fit one folder | No |
| Many Home widgets | Looks complete | Unused | Max 4 |

## 5. Limitations and open questions

Unverified: quick switcher ranking/alias search; mobile rendering of Bases embeds; kepano repo mechanics; scale (expected hundreds of notes — fine).

Open: non-English titles? RUNBOOK prefix wanted? keep `roles`/`source`? date ID vs sequential for DEC/INC/DBG (date recommended)? per-kind status values (recommended) vs merged?

## Sources

- https://obsidian.md/help/bases · https://obsidian.md/help/bases/syntax · https://obsidian.md/help/plugins/search · https://obsidian.md/help/tags · https://obsidian.md/help/properties · https://obsidian.md/help/aliases
- https://stephango.com/vault
- https://forum.obsidian.md/t/an-opinionated-reflection-on-using-folders-links-tags-and-properties/78548
- https://forum.obsidian.md/t/folders-vs-linking-vs-tags-the-definitive-guide-extremely-short-read-this/78468
- https://www.dsebastien.net/structure-a-findable-obsidian-vault-folders-links-dates-and-daily-notes/
- https://laoujin.github.io/Atlas/research/2026-05-30-beginner-intermediate-obsidian-a-roadmap-for-a-developer-with-a-1-200-note-vault/properties-tagging-for-queryable-notes/

**Status:** DONE_WITH_CONCERNS
