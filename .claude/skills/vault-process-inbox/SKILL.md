---
name: vault-process-inbox
description: Empty the vault's 00-inbox by turning each capture into a typed note, merging it into existing notes, extracting tasks, or archiving it. Use when the user asks to process, triage, clean up or sort the inbox.
---

Follow AGENTS.md. For each file in `00-inbox/` (oldest first):

1. Read it and decide one outcome:
   - **Merge** into an existing note (search first), or
   - **Promote** to a typed note via `new_note.py <type> "<Title>" --author agent:claude`, or
   - **Extract tasks** into the relevant project hub / today's daily note, or
   - **Discard** (no lasting value).
2. Move the processed inbox file to `90-archive/00-inbox/` (never delete).
3. If an item's destination is genuinely ambiguous (e.g. which project), leave it in the inbox and ask.

Finish: one agent-log line, `lint.py` with 0 errors, and a table for the user: inbox item → outcome → [[destination]].
