# Usage

How to actually use the handover pack on a live engagement.

## Step 1 — Fill the templates as you build, not at the end

This is the biggest leverage point. Open `handover-guide-template.md` and
`runbook-template.md` on day one and fill them in as you make decisions.
"Where it lives" gets filled when you create the flow. "Common changes"
gets filled when you parameterize the recipient list. The finished docs
become the by-product of the build, not a separate end-of-engagement
chore.

The worked examples
([handover-greenfield-logistics.md](../examples/handover-greenfield-logistics.md),
[runbook-greenfield-logistics.md](../examples/runbook-greenfield-logistics.md))
show what "good" looks like:

- **Specific over generic.** "Power Automate → My flows → Greenfield —
  Asana to SharePoint daily sync" beats "the flow".
- **Concrete troubleshooting.** Each symptom names the actual table /
  filter / step to look at, not "investigate the error".
- **Visible support window.** "Through 2026-08-19" beats "14 days" —
  the client knows the exact date the included support ends.

## Step 2 — Record the Loom walkthrough

Open `loom-script.md`, fill the bracketed `<…>` placeholders, and read it
through once before recording. The example
[loom-script-greenfield-logistics.md](../examples/loom-script-greenfield-logistics.md)
is what a filled-in script looks like — note the inline `*[show this]*`
stage directions for what to do on screen.

Tips that materially improve the final video:

- Rehearse once start-to-finish before hitting record. Cuts most of the
  ums.
- Pause recording while you navigate tabs — the viewer doesn't need to
  watch you click.
- Trim the first 4 seconds of dead air at the start.
- Drop the Loom share link into the handover guide at the top, not the
  bottom.

## Step 3 — Validate before delivering

```bash
python validate.py examples/handover-greenfield-logistics.md   # check a specific file
python validate.py                                             # check every file under examples/
```

The linter flags angle-bracket placeholders that slipped through. Run it
on every handover document before delivery — a handover with a leftover
`<client>` is the single most preventable bad last impression.

The validator deliberately **ignores fenced code blocks** so Mermaid
diagrams in the handover guide don't trigger false positives.

## Step 4 — Deliver all three together

The pack only works as a set:

- **Handover guide** answers "what did you build and where is it?"
- **Runbook** answers "what do I do when X breaks?"
- **Loom walkthrough** answers "can a non-technical owner see how to
  manage this?"

Delivering only the first two is what *every* freelancer does. Adding the
Loom is what gets the five-star review.

## Customizing the kit

### Adding a section to the handover guide

Edit `handover-guide-template.md`. Common additions per engagement type:

- **§Security model** — who has what access, where credentials live.
- **§Cost expectations** — for anything on Azure consumption tiers, what
  monthly spend looks like at expected volume.
- **§Future enhancements deferred** — the "we discussed this but didn't
  build it" list, so future-them remembers why.

### Adding a runbook entry

Edit `runbook-template.md`. The two tables (Common changes / Troubleshooting)
are the meat. Every symptom you actually hit in testing is a new
Troubleshooting row — capture them as you go, while the diagnostic steps
are fresh.

### Adding a new worked example

Copy your engagement's pack into `examples/` under a non-real client name.
Run validate — it should pass clean. Add the new files to
`tests/test_validate.py` so the new example is regression-tested.

## What this pack is not

- **Not a maintenance contract.** The 14-day post-handover support window
  is for defect fixes and questions on documented usage — not for new
  features.
- **Not a substitute for actually training the user.** The walkthrough
  + docs do most of the work, but for complex builds a 30-min live
  Q&A after the client has watched the video catches the questions the
  docs didn't anticipate.
- **Not exhaustive.** The runbook covers expected failure modes; novel
  failures still need a human (you) for the first 14 days.
