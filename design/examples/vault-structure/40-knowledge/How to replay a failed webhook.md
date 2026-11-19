---
type: howto
status: verified
created: 2026-11-12
updated: 2026-11-12
author: human
related: ["[[Payments platform]]"]
---
# How to replay a failed webhook

> **TL;DR** Find the event ID in the gateway log, then call the replay endpoint once; it is safe because handlers are idempotent.

## Steps
1. Search the gateway log for the order ID
2. Replay the event from the console

<!-- Example: repeatable procedure, distilled from the incident [[INC 2026-11-12 Duplicate charges after gateway timeout]]. -->
