# Getting started

The handover pack runs at the **end** of an engagement, but the biggest
leverage move is starting it on day one.

## 1. Open both templates on day one of the build

```bash
cp handover-guide-template.md handover-<client>.md
cp runbook-template.md runbook-<client>.md
```

Fill them in **as you build**, not at the end. "Where it lives" gets
filled the moment you create the flow. "Common changes" gets filled
when you parameterize the recipient list. The finished docs become a
by-product of the build, not a separate end-of-engagement chore.

## 2. Record the Loom walkthrough

Open [`loom-script.md`](../loom-script.md), fill the bracketed `<…>`
placeholders, read it through once before recording. The worked
examples
([Greenfield Logistics](../examples/loom-script-greenfield-logistics.md) /
[Whitford Legal](../examples/loom-script-whitford-legal.md))
show what a filled-in script looks like — note the inline `*[show
this]*` stage directions.

Tips that materially improve the final video:
- Rehearse once start-to-finish before recording. Cuts most ums.
- Pause recording while you navigate tabs.
- Trim the first 4 seconds of dead air.
- Drop the Loom share link into the **top** of the handover guide.

## 3. Validate before delivering

```bash
python validate.py
```

Checks every file under `examples/` (and any path you pass explicitly)
for leftover `<…>` placeholders. A handover with a leftover
`<client>` is the single most preventable bad last impression.

## 4. Deliver all three together

The pack only works as a set:

- **Handover guide** answers "what did you build and where is it?"
- **Runbook** answers "what do I do when X breaks?"
- **Loom walkthrough** answers "can a non-technical owner see how to
  manage this?"

Delivering only the first two is what *every* freelancer does. The
Loom is what gets the five-star review.

## See it end-to-end on a worked example

[`examples/handover-greenfield-logistics.md`](../examples/handover-greenfield-logistics.md)
shows the finished form of a typical small-engagement handover.
[`examples/handover-whitford-legal.md`](../examples/handover-whitford-legal.md)
shows what a more complex (Copilot Studio rollout) handover looks like.

## What to read next

- [Usage](usage.md) · [Diagrams](diagrams.md) · [FAQ](faq.md)
