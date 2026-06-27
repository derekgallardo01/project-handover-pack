# Runbook — <project name>

The "edit it later" guide. Written so a non-developer owner can make safe changes
and recover from common problems.

## Common changes (how-to)
| I want to… | Do this |
|------------|---------|
| Add a field to the output | <Open flow > the "Map fields" step > add the column> |
| Change the schedule | <Open flow > Recurrence trigger > edit interval> |
| Add a recipient to notifications | <Open flow > "Send email" step > add address> |
| Pause it temporarily | <Power Automate > flow > Turn off> |

## Troubleshooting
| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| No new rows today | source had no data, or run failed | check run history; check source |
| "Connection not authorized" | token expired | re-authenticate the connector |
| Duplicate rows | run executed twice / key not unique | check for double trigger; dedupe on <key> |
| Wrong values | source format changed | check the "Map fields" step against new format |

## Recovery
- **Re-run a failed run:** Power Automate > flow > Run history > select run > Resubmit.
- **Backfill a missed day:** <manual trigger steps / set date parameter>.
- **Roll back a change:** flows keep version history under … (or restore from the
  exported solution package delivered with this project).

## Health checklist (monthly)
- [ ] Run history is mostly green over the last 30 days.
- [ ] Connections are still authorized.
- [ ] Output destination isn't near a storage/row limit.
- [ ] Licenses/connectors used are still active.
