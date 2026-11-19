---
type: note
status: evergreen
created: 2026-11-19
updated: 2026-11-19
author: human
aliases: [Idempotency, Idempotency key, Exactly-once payments]
related: ["[[MOC Distributed systems]]"]
---
# Retries need idempotency keys

> **TL;DR** Retrying a non-idempotent call (like a payment) can repeat its effect; sending a unique idempotency key lets the server ignore duplicates.

## Explanation
A timeout does not tell you whether the server did the work. Retrying blindly can charge twice. With a key, the server stores the first result and returns it for repeats.

## Where I used it
- [[Checkout revamp]] — [[SPEC Payment retries]]
- Lesson from [[DBG 2026-11-10 Duplicate charge on retry]]

## Sources
- [[Designing Data-Intensive Applications]], ch. 11

<!-- Example: Zettelkasten permanent note with a CLAIM title (D12): the title states the lesson. aliases catch topic searches like "idempotency". -->
