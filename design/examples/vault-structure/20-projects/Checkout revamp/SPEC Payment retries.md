---
type: spec
status: review
created: 2026-11-10
updated: 2026-11-19
author: human
related: ["[[Checkout revamp]]"]
---
# SPEC Payment retries

> **TL;DR** Exponential backoff (3 tries) with an idempotency key per checkout, stored in Postgres.

## Design
- Key = checkout ID, sent on every gateway call → see [[Retries need idempotency keys]]
- Decision: [[DEC 2026-11-19 Retry payments with idempotency keys]]

<!-- Example: spec for a deliverable → project folder. A spec describing a long-lived system would go to 40-knowledge/ instead (D10). -->
