# Runbook — Whitford Legal: Copilot Studio knowledge agent

The "edit it later" guide. Written so the KM partner and IT lead can make
safe changes and recover from common problems without contacting the builder.

## Common changes (how-to)

| I want to… | Do this |
|------------|---------|
| Add a new client name to the sensitive-topics list | Open SharePoint → "WLF Sensitive Topics" list → New item. Use exact-name and known variants (e.g. "Acme Inc.", "Acme"). Save. No agent restart needed; the topic re-reads on next request. |
| Add a new precedent to the agent's knowledge | Save to `/sites/precedents`. Wait up to 1 hour for the Copilot Studio indexer to pick it up. To force, open Copilot Studio → Agents → WLF Knowledge Agent → Knowledge → re-index. |
| Rotate the on-call senior associate | Open SharePoint → "WLF KM On-call" list → edit the row for the current/next ISO week. Save. The escalation flow re-reads on next escalation. |
| Add an eval case (a question that was answered wrong) | Open `wlf-copilot-pilot` repo → `evals/golden.json` → add the case. Open a PR. CI runs the full eval set and gates merge. |
| Update the agent's system instruction | Copilot Studio → Agents → WLF Knowledge Agent → Settings → Instructions. Change, save, publish. The eval set will catch most regressions. |
| Pause the agent | Copilot Studio → Agents → WLF Knowledge Agent → Publish → Channels → Teams → toggle off. |
| Add a fourth SharePoint site to the knowledge | This is a CHANGE REQUEST under SOW §7. The §2 scope locked in three sites and the privacy/compliance scope was reviewed against those three only. |

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Lawyer says the agent answered a question about an active client | Sensitive-topic list missing the client name | Add the name + variants to the SharePoint list. Add the question as a new eval case so it can't regress. |
| Eval set CI is red | A recent change to topics / instructions / knowledge regressed at least one case | Open the PR → see the failing case IDs → revert OR add docs/keywords to fix → re-run. Don't merge a red CI. |
| No escalation DMs delivered | Escalation service principal token expired OR on-call row missing | Azure portal → app registration `wlf-rag-pilot-escalation` → certificates & secrets. Also check the "WLF KM On-call" list has a row for the current ISO week. |
| Citation links return 404 | Document was moved/renamed | Re-index the affected site (Copilot Studio → Knowledge → re-index). If repeated, fix the link in the document. |
| Slow responses (>10s) | Azure OpenAI quota strain or peak hour | Check Azure portal metrics for the deployment. Quota was provisioned above projected use; if exceeded, request a temporary increase. |
| "I don't have information on that" for a question the docs clearly cover | New doc hasn't been indexed yet OR sensitive-topic regex caught a benign client-name substring | Trigger a re-index. If sensitivity, look at the sensitive-topic list for over-broad keywords and refine. |

## Recovery

- **Roll back a Copilot Studio change:** the agent keeps a publish history.
  Copilot Studio → Agents → WLF Knowledge Agent → Publish → Versions →
  restore the last green version.
- **Roll back a knowledge change:** the SharePoint site keeps version
  history on every document. Restore the prior version from the document
  context menu.
- **Roll back an eval-set change:** revert the PR in `wlf-copilot-pilot`.
  Squash-merge keeps history clean.
- **Emergency disable:** turn off the Teams channel under the agent's
  publish settings. Lawyers will see "this agent is not available".
  Re-enable once the issue is fixed.

## Health checklist (monthly — first Monday)

- [ ] Eval pass rate on `wlf-copilot-pilot` main is 100%.
- [ ] Last 30 days of Copilot Studio analytics show a healthy daily curve
      (no zero-traffic days).
- [ ] "WLF KM Escalations" list has been triaged (no stale items).
- [ ] Sensitive-topic list reviewed; any new clients onboarded in the
      last month have been added.
- [ ] Azure OpenAI quota utilization < 70% of approved throughput.
- [ ] Azure OpenAI privacy settings unchanged (no-retention, no abuse-
      monitoring) — re-confirm from the privacy-config checklist.

If any item trips, see Troubleshooting; if still stuck during the 30-day
support window, email the builder.
