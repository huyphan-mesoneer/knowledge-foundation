---
name: vault-weekly-review
description: Run the weekly review of this vault — process the inbox, summarize the week, update project statuses, flag stale knowledge, propose next week's priorities. Use for "weekly review", "plan next week", "what happened this week".
---

Follow AGENTS.md.

1. `python3 _system/scripts/new_note.py weekly --author agent:claude`.
2. Run the vault-process-inbox procedure (ask before discarding anything that isn't obviously noise).
3. Read this week's daily notes, meetings, records and changed notes (`find . -name "*.md" -mtime -7 -not -path "./.git/*"`). Fill **Wins / shipped**, **Learned** (link notes), **Blockers / risks**.
4. For each active project: check `## Next actions` and the log; propose status changes (don't silently change `status` on human-authored hubs — suggest in a `> [!agent]` callout or ask).
5. Flag stale items: `seedling` notes > 30 days, `runbook` with `last_verified` > 90 days or empty, `decision` stuck in `proposed`, `incident` not `reviewed`, inbox items > 7 days.
6. Propose top 3 priorities for next week; tick the review checklist items you actually completed.
7. Agent-log line, `lint.py` 0 errors, and a concise summary to the user.
