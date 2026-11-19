---
type: prd
status: approved
created: 2026-10-05
updated: 2026-11-01
author: human
related: ["[[Checkout revamp]]"]
---
# PRD Checkout retry flow

> **TL;DR** When a payment fails for a temporary reason, the shopper sees "retrying…" and is charged at most once.

## Problem
4% of checkouts fail on gateway timeouts; shoppers abandon.

## Requirements
- Retry automatically up to 3 times for temporary errors
- Never charge twice

<!-- Example: project-bound doc (D10). Lives in the project folder because it ends with the deliverable. Type prefix PRD because several kinds share this folder. -->
