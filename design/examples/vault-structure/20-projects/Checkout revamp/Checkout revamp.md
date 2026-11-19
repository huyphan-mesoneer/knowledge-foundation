---
type: project
status: active
created: 2026-10-01
updated: 2026-11-19
author: human
due: 2026-12-15
tags: []
related: ["[[Payments platform]]"]
---
# Checkout revamp

> **TL;DR** Cut failed checkouts by 30% with safe automatic payment retries, by 2026-12-15.

## Contents
- [[PRD Checkout retry flow]] — what the user experiences
- [[SPEC Payment retries]] — how we build it
- [[2026-11-19 Checkout retry design review]] — design review meeting

## Decisions
- [[DEC 2026-11-19 Retry payments with idempotency keys]]

## Key knowledge
- [[Retries need idempotency keys]]

## Next actions
- [ ] Get spec approved — @me — 📅 2026-11-26
- [ ] Evaluate retry budget per merchant (from inbox)

<!-- Example: PROJECT HUB. Folder = project. Deliverable docs (PRD, SPEC) live next to it; knowledge is linked, never stored here. When done: status done → whole folder moves to 90-archive/20-projects/. -->
