---
type: incident
status: reviewed
created: 2026-11-12
author: human
related: ["[[Payments platform]]"]
---
# INC 2026-11-12 Duplicate charges after gateway timeout

> **TL;DR** 37 shoppers were charged twice for 40 min after a gateway slowdown; refunded, root cause fixed by idempotency keys.

## Timeline
- 14:02 gateway latency spike
- 14:42 retries disabled, refunds started

## Follow-ups
- [x] Runbook: [[How to replay a failed webhook]]
- [x] Decision: [[DEC 2026-11-19 Retry payments with idempotency keys]]

<!-- Example: incident record. Closed → body immutable; lessons go to 40-knowledge/. -->
