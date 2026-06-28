# Project handover & enablement pack

[![CI](https://github.com/derekgallardo01/project-handover-pack/actions/workflows/ci.yml/badge.svg)](https://github.com/derekgallardo01/project-handover-pack/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#)

**Docs:** [Getting started](docs/getting-started.md) · [Usage](docs/usage.md) · [Diagrams](docs/diagrams.md) · [FAQ](docs/faq.md)

Templates that make the end of an engagement as professional as the start:
a **handover guide**, an operational **runbook**, and a short
**walkthrough-video script** so a non-technical owner can run and maintain
what you built. Ships with a fully worked example set and a placeholder
linter so half-finished handovers don't reach a client.

```bash
python validate.py                                            # check examples/ are fully filled in
python validate.py handover-greenfield-logistics.md           # check your draft before delivering
python -m pytest -q                                           # 2 tests gating the kit
```

## Why it exists

The handover is where repeat business and five-star reviews are won or
lost. A client who is left with clear documentation and a walkthrough
trusts you with the next project; one who's left guessing how to maintain
the solution does not. These templates make a thorough handover quick to
produce every time.

## What's inside

| File | Purpose |
|------|---------|
| [handover-guide-template.md](handover-guide-template.md) | What was built, how it's configured, accounts/permissions, where things live, and how to get support. |
| [runbook-template.md](runbook-template.md) | Day-to-day operations: routine tasks, monitoring, common issues and fixes, and escalation. |
| [loom-script.md](loom-script.md) | A 3–5 min script for recording a walkthrough video — the single cheapest thing that makes a handover feel premium. |
| [examples/handover-greenfield-logistics.md](examples/handover-greenfield-logistics.md) | A completed handover guide (Asana → SharePoint sync, threads with the discovery / SOW / HLD examples). |
| [examples/runbook-greenfield-logistics.md](examples/runbook-greenfield-logistics.md) | The matching runbook with concrete troubleshooting rows. |
| [examples/loom-script-greenfield-logistics.md](examples/loom-script-greenfield-logistics.md) | The matching Loom script with inline stage directions. |
| [validate.py](validate.py) | Placeholder linter — flags unfilled `<…>` markers; skips fenced code so Mermaid diagrams don't trigger. |
| [tests/](tests/) | Self-tests: examples validate clean; bare templates still look like templates. |
| [docs/usage.md](docs/usage.md) | Step-by-step usage + how to customize the pack. |

## How to use it

1. Fill [handover-guide-template.md](handover-guide-template.md) and
   [runbook-template.md](runbook-template.md) **as you build**, not at the
   end. The finished docs become the by-product, not a separate chore.
2. Record a 3–5 minute walkthrough from [loom-script.md](loom-script.md).
3. Run `python validate.py` on the filled-in files to catch any leftover
   `<…>` placeholders.
4. Deliver all three at close-out. This is the difference between "done"
   and "done and maintainable."

[docs/usage.md](docs/usage.md) walks the process end-to-end with the worked
examples, including tips that materially improve the final walkthrough
video.
