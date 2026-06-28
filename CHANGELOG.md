# Changelog

Notable changes to the project handover & enablement pack. Dates are when the
change landed on `main`.

## 2026-06-27 — Second worked engagement (Whitford Legal)
- `examples/handover-whitford-legal.md` — completed handover guide for the
  Copilot Studio rollout
- `examples/runbook-whitford-legal.md` — matching runbook with concrete
  edits (sensitive-topic list, on-call rotation, eval cases) and recovery
- `examples/loom-script-whitford-legal.md` — matching 5-min walkthrough
  script with stage directions
- `tests/test_validate.py` extended to cover the 3 new examples

## 2026-06-27 — GitHub Actions CI
- `.github/workflows/ci.yml` running pytest + validate on Python 3.11
- CI status badge added to README

## 2026-06-27 — Build-out: worked examples + linter + tests + usage doc
- `examples/handover-greenfield-logistics.md` + `runbook-greenfield-logistics.md`
  + `loom-script-greenfield-logistics.md` — completed handover trio for the
  fictional Asana → SharePoint sync engagement
- `validate.py` placeholder linter; skips fenced code blocks
- 2 tests covering examples validate clean and bare templates still look
  like templates
- `docs/usage.md` — step-by-step usage including "fill as you build" workflow
  and Loom recording tips
- README expanded with usage steps, file index, link to docs/usage.md

## 2026-06-27 — Initial public release
- `handover-guide-template.md` — what was built, where it lives, how to
  monitor, how to get support
- `runbook-template.md` — common changes, troubleshooting, recovery, monthly
  health checklist
- `loom-script.md` — 3–5 min walkthrough video script
