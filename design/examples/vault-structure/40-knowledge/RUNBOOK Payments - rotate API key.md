---
type: runbook
status: verified
created: 2026-03-02
updated: 2026-11-01
author: human
related: ["[[Payments platform]]"]
---
# RUNBOOK Payments - rotate API key

> **TL;DR** Rotate the gateway API key with zero downtime: add new key, deploy, remove old key.

## Steps
1. Create the new key in the gateway console (secret stays in the vault manager — never here)
2. Deploy with both keys enabled
3. Remove the old key after 24 h

<!-- Example: runbooks outlive projects → 40-knowledge/, linked from the area hub (D10). No secrets in notes. -->
