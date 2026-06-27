# Runbook — Greenfield Logistics: Asana → SharePoint daily sync

The "edit it later" guide. Written so Cara (non-developer) can make safe
changes and recover from common problems without calling the builder.

## Common changes (how-to)

| I want to… | Do this |
|------------|---------|
| Add a new column to the output | Open the flow → "Map fields (Select)" step → add a row mapping the Asana field name → the SharePoint column. Also add the column to the "Deliveries" list first. |
| Change the schedule | Open the flow → "Recurrence" trigger at the top → edit the time / weekdays. Save. Test with the manual "Run flow" button. |
| Add a recipient to the alert email | Open the flow → "Send email (V2)" step → add the address to the To field. Or edit the `ops-alerts@…` distribution list directly in Outlook (preferred — it survives flow edits). |
| Pause the sync temporarily | Power Automate → My flows → "Greenfield — Asana to SharePoint daily sync" → Turn off. Remember to turn it back on. |
| Change the notification distribution list | Edit `ops-alerts@greenfieldlogistics.com.au` in Outlook (Admin Center → Groups). The flow reads the address from a flow variable named `ALERT_RECIPIENTS` so you can also change it there if needed. |

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| No new rows today, but Asana had approved jobs | Run didn't execute or failed early | Power Automate → Run history. If no run for today, check the trigger is enabled. If failed, open the run to see which step. |
| "Connection not authorized" / 401 from Asana | OAuth token expired (90-day window) | Power Automate → Connections → Asana → Fix connection. Re-auth with Cara's account. Re-run the failed run via Resubmit. |
| Duplicate rows in "Deliveries" | Same Job ID coming through twice OR dedup column was renamed | Filter the Deliveries list by Job ID to confirm. If the column was renamed, restore it; if Asana is genuinely sending dups, check the Dispatch board for double-approvals. |
| Wrong values in Customer/Pickup/Drop fields | Asana field rename or new column type | Open the latest failed run → Map step → compare against the current Asana columns. Contact builder if a remap is needed. |
| Sync Log row shows `status = "skipped: no Job ID"` | A job was approved without a Job ID set | Find the offending job in Asana, set its Job ID, then manually trigger the flow once (Run now) to pull it. |
| Email alert never arrives but Sync Log shows failure | `ops-alerts@…` distribution list misrouted | Send a test email to the alias directly. If that fails, fix the alias in Outlook (Admin Center). |

## Recovery

- **Re-run a failed run:** Power Automate → flow → Run history → select the
  failed run → Resubmit. The flow is idempotent (dedupes on Job ID), so it's
  safe to re-run.
- **Backfill a missed day:** open the flow → click "Run now" — by default
  this pulls *yesterday's* approved jobs. To backfill an older day, edit the
  `lookback_days` flow variable to the number of days back (e.g. `3`),
  run once, then reset to `1`.
- **Roll back a change to the flow:** Power Automate keeps version history
  under flow → Settings → Versions. Restore the prior version if a recent
  edit broke something.

## Health checklist (monthly — first Monday)

- [ ] Run history shows ~20 green runs in the last 30 days (one per
      business day, allowing for holidays).
- [ ] Asana connection still authorized (no "Fix connection" prompt).
- [ ] "Deliveries" list row count grew roughly in line with sales (~500–1200
      rows in a typical month).
- [ ] "Sync Log" has no rows with `status = "failed"` in the last 30 days.
      Any present → investigate.
- [ ] Licenses still active: Cara's Power Automate per-user plan, M365 E3,
      Asana Business.

If anything in the checklist trips, see Troubleshooting above; if still
stuck during the support window, email the builder.
