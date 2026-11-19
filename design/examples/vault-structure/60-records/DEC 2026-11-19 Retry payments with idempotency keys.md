---
type: decision
status: accepted
created: 2026-11-19
author: human
related: ["[[Checkout revamp]]", "[[Payments platform]]"]
---
# DEC 2026-11-19 Retry payments with idempotency keys

> **TL;DR** We retry failed payments up to 3 times, always with the checkout ID as idempotency key.

## Context
Gateway timeouts cause failed checkouts; blind retries caused [[INC 2026-11-12 Duplicate charges after gateway timeout]].

## Options
1. No retries — simple, keeps failures
2. Retries without keys — risk of double charge
3. Retries with idempotency keys — chosen

## Outcome
Option 3. Decided in [[2026-11-19 Checkout retry design review]].

<!-- Example: record name is TYPE FIRST (D12). Body never edited once accepted; to change it, write a new DEC with supersedes. -->
