---
name: vault-capture
description: File anything (pasted text, meeting transcript, link, idea, decision, bug, incident) into this Obsidian vault as the right note type. Use when the user says capture, save, note down, file this, log this, or pastes content to keep.
---

Follow AGENTS.md. Steps:

1. Classify the input against `_system/schema.json` types (meeting, decision, note, howto, reference, debug-log, incident, story, …). If unsure or it mixes several things, use `inbox`.
2. Search for an existing note first (`grep -ril "<key term>" --include=*.md .`). Prefer appending to an existing note over creating a duplicate.
3. Create with `python3 _system/scripts/new_note.py <type> "<Title>" [--project "<P>"] --author agent:claude`, then fill the template sections from the input. Keep the user's facts; don't invent. Mark unknowns as `TODO`.
4. Split out side-products: decisions → `decision` records, action items → `- [ ]` tasks with @owner, reusable lessons → `note`/`howto`. Link everything to its project/area hub via `related`.
5. Append a line to `_system/agent-log.md`, run `python3 _system/scripts/lint.py`, fix errors.
6. Reply with the list of notes created/updated as `[[links]]`.
