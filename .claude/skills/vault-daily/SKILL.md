---
name: vault-daily
description: Start or wrap up the day in the vault — create today's daily note, carry over unfinished tasks, surface active projects and due items, or log what happened. Use for "start my day", "daily note", "what's on today", "end of day log".
---

Follow AGENTS.md.

**Start of day**
1. `python3 _system/scripts/new_note.py daily --author agent:claude` (idempotent).
2. Find the previous daily note in `10-journal/daily/`; copy its unchecked `- [ ]` tasks into today's `## 🔁 Carried over` (don't remove them from the old note).
3. List active projects (`type: project`, `status: active`) with their `## Next actions`, open action items with 📅 dates ≤ today, and inbox count. Put a short summary in the reply; suggest up to 3 focus items but let the user choose.

**End of day**
Append to `## 📝 Log` what the user tells you (or summarize from notes changed today: `find . -name "*.md" -newermt "$(date +%F)"`). Route anything durable to typed notes as in vault-capture.

Log to `_system/agent-log.md`; run `lint.py`.
