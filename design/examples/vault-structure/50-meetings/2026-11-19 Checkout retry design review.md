---
type: meeting
created: 2026-11-19
author: human
related: ["[[Checkout revamp]]"]
---
# 2026-11-19 Checkout retry design review

> **TL;DR** Agreed on idempotency keys for retries; spec to be updated by next week.

## Attendees
[[Ada Lovelace]], [[Payments squad]]

## Notes
- Gateway supports an Idempotency-Key header
- Store keys in Postgres for 24 h

## Decisions
- [[DEC 2026-11-19 Retry payments with idempotency keys]]

## Action items
- [ ] Update [[SPEC Payment retries]] — @me — 📅 2026-11-26

<!-- Example: meeting is immutable after the day (except checkboxes). The decision got its own record so it can be found and linked. -->
