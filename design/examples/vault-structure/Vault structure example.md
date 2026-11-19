---
status: draft
created: 2026-11-19
roadmap: "[[ROADMAP#1.2 Note-taking method & vault structure]]"
---
# Vault structure: worked example

> **TL;DR** One small, connected example vault showing what goes in each folder (decisions D8–D14). Frontmatter and headings are illustrative only; the final templates and properties are decided in roadmap 1.3/1.4.

**The story:** an engineer owns the payments service (area), runs a checkout project, has an incident and a design review, and studies distributed systems on the side. Start from [[Payments platform]] or [[Skill development]] and follow the links.

| Folder | Example | What it shows |
|---|---|---|
| `00-inbox/` | [[2026-11-19 Retry budget per merchant]] | Quick capture with no clear home yet |
| `10-journal/daily/` | [[2026-11-19]] | Daily log, links to the work |
| `10-journal/weekly/` | [[2026-W47]] | Weekly review: inbox processed, status, plan |
| `20-projects/<P>/` | [[Checkout revamp]] (hub), [[PRD Checkout retry flow]], [[SPEC Payment retries]] | Project hub + deliverable docs next to it |
| `30-areas/` | [[Payments platform]], [[Skill development]] | Hub-only notes: purpose, standards, `## Contents`, recurring duties |
| `40-knowledge/` | [[Retries need idempotency keys]] (claim title), [[Bounded context]] (term title), [[MOC Distributed systems]], [[RUNBOOK Payments - rotate API key]], [[How to replay a failed webhook]], [[Designing Data-Intensive Applications]] (reference) | Zettelkasten layer: atomic notes, MOC, procedures, sources |
| `50-meetings/` | [[2026-11-19 Checkout retry design review]] | Meeting → decision extracted into its own record |
| `60-records/` | [[DEC 2026-11-19 Retry payments with idempotency keys]], [[INC 2026-11-12 Duplicate charges after gateway timeout]], [[DBG 2026-11-10 Duplicate charge on retry]] | Type-first record names; immutable once closed |
| `70-people/` | [[Ada Lovelace]], [[Payments squad]] | Person and team |
| `90-archive/` | [[Card vault migration]] | Closed project moved with its original subpath |

**Flows to trace:**
- **Work → knowledge:** [[DBG 2026-11-10 Duplicate charge on retry]] → lesson [[Retries need idempotency keys]] → used in [[SPEC Payment retries]].
- **Meeting → decision:** [[2026-11-19 Checkout retry design review]] → [[DEC 2026-11-19 Retry payments with idempotency keys]] → listed in the [[Checkout revamp]] hub.
- **Study:** [[Skill development]] → [[MOC Distributed systems]] → notes ← [[Designing Data-Intensive Applications]].
- **Agent question "what did we decide about retries?":** filename prefix `DEC` + TL;DR line → answer in 1–2 searches.

Each example ends with an HTML comment (`<!-- Example: … -->`) explaining why it sits where it does.
