# Handover guide — <project name>

**Delivered to:** <client> · **By:** Derek G. · **Date:** <date>

## What was built
<Plain-English description of the solution and the outcome it delivers.>

**Walkthrough video:** <Loom link>

## How it works (at a glance)
<Insert architecture diagram (your architecture/HLD diagram) or a numbered flow.>
1. <Trigger> → 2. <Pull data> → 3. <Transform> → 4. <Write> → 5. <Notify>

## Where it lives
| Thing | Location |
|-------|----------|
| The flow / app / report | <Power Automate > My flows > "Name"> |
| Source data | <Asana workspace / mailbox / form> |
| Output | <SharePoint site > library > file> |
| Service account | <name, owner> |

## How to monitor it
- **Is it running?** <Power Automate > flow > Run history. Green = success.>
- **Where do failures show up?** <email alert to <address> / run-log file>
- **Normal schedule:** <e.g. daily 6:00 AM ET, ~30s per run>

## If something looks wrong
See the **runbook** (`runbook-template.md`) for common fixes. Quick checks:
- [ ] Did the source have data today?
- [ ] Is the connection still authorized? (re-auth if expired)
- [ ] Any failed runs in history? Open one to see the step that failed.

## Who to contact
- Day-to-day owner: <name>
- Builder (me): <contact> — support window: <e.g. 14 days post-handover included>
