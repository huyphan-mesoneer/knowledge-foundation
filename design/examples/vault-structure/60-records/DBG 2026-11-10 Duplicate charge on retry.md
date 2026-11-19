---
type: debug-log
status: solved
created: 2026-11-10
author: human
related: ["[[Checkout revamp]]"]
---
# DBG 2026-11-10 Duplicate charge on retry

> **TL;DR** Duplicate charge reproduced: the client retried after a timeout and the gateway had already captured the first call.

## Log
- 10:15 reproduced in staging with 5 s gateway delay
- 11:40 confirmed: no idempotency key sent

## Lesson
→ [[Retries need idempotency keys]]

<!-- Example: debug diary. When solved, the reusable lesson is distilled into a knowledge note (distill trigger). -->
