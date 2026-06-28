# FAQ

## Why fill the handover guide DURING the build, not after?

Because at the end of the engagement you've forgotten the things a new
owner needs to know — which decisions were intentional vs accidental,
why this connector and not another, which secret lives where. Capturing
as you go is cheap. Capturing in retrospect is lossy.

## Is the Loom video really necessary?

Yes. Fewer than 10% of freelancers send a walkthrough video; it's a
review magnet. Three to five minutes is enough. The script in
[`loom-script.md`](../loom-script.md) is the structure that works for
non-technical owners.

## What if the client says they don't want a video?

Make it anyway. They'll watch it once and then forward it to whoever
inherits the system when they leave. The video is a future-proofing
artefact, not an immediate-consumption one.

## How long is the support window?

Whatever you put in the handover guide's "Who to contact" section. The
defaults in the worked examples are 14 days (small engagement) and 30
days (larger engagement). Don't include indefinite support — set a
date.

## What if the client asks for support after the window closes?

Quote it. The runbook covers the changes they can make themselves;
anything beyond that is a change request per the SOW. Replying "happy
to help, that's a 1-hour change request at <rate>" is normal.

## How do I add screenshots / GIFs to the handover guide?

Drop them in a `screenshots/` folder next to the handover guide and
reference them with `![](screenshots/name.png)`. The kit doesn't
include any (because the screenshot of *your* engagement is what's
relevant). For inspiration, the runnable demos in this portfolio use a
Playwright workflow to auto-capture — same pattern could work for a
real engagement's UI.

## What goes in the runbook vs the handover guide?

- **Handover guide**: identity + location + monitoring + escalation.
  "What it is, where it lives, who to contact."
- **Runbook**: operations + troubleshooting + recovery. "How to fix
  X. What to do when Y."

A common rule: if it's a one-time question ("who built this?"),
handover. If it's a recurring how-to ("how do I add a recipient?"),
runbook.

## Why a "monthly health checklist" in the runbook?

So the owner has a structured monthly review that catches drift early.
Templates without one tend to result in "nobody checked in 6 months,
something silently broke 4 months ago." A 10-minute monthly review
prevents the 4-week emergency.

## Can I use this pack outside of Microsoft engagements?

Yes. The templates are platform-agnostic — "monitoring", "common
changes", "troubleshooting" apply to any system. The examples happen to
be M365 because that's my focus, but the structure works anywhere.
