# Loom walkthrough script — Whitford Legal: Copilot Studio knowledge agent

A worked version of `loom-script.md` for the Whitford Legal engagement.
Target length 5 min (slightly longer than the default because there are two
audiences: KM partner + IT lead). The actual recorded video is linked from
[handover-whitford-legal.md](handover-whitford-legal.md).

---

**0:00 — Intro (20s)**
> "Hi J. and D., this is a quick walkthrough of the Copilot Studio knowledge
> agent I built for Whitford Legal. I'll show you what it does in Teams,
> how the sensitive-topic escalation works, where to monitor it, and how to
> make the changes I expect you to make week-to-week. The written guide
> and runbook cover everything too."

**0:20 — What it does for a lawyer (60s)**
> "Here's the agent in Teams. *[ask a benign question — 'what's our standard
> NDA carve-out for IP?']* You can see the answer comes back with a citation
> to the source document. *[click citation]* And it opens the doc in
> SharePoint at the right section. Now let's try a follow-up — *[ask 'and
> for confidentiality?']* — the agent has the context from the previous
> turn, so it knows we're still on NDA carve-outs."

**1:20 — The sensitive-topic escalation (60s)**
> "Now let's see what happens with something the agent shouldn't answer.
> *[ask 'what should I tell Acme Inc. about their pending motion?']*
> No retrieval, no generated answer — just a Teams DM to the on-call
> senior associate. *[switch to the senior associate's Teams view]* —
> there's the DM. The on-call rotation is the SharePoint list I'll show
> you in a moment."

**2:20 — Where to monitor it (60s, mostly for D.)**
> "Three places you'll look. First, Copilot Studio analytics — daily
> session counts, top intents, escalation rate. *[show analytics page]*.
> Second, the WLF KM Escalations SharePoint list — every escalation lands
> here with the question, the matched keyword, and the on-call who was
> DMed. Third, the eval pass rate on the `wlf-copilot-pilot` repo —
> there's the green CI badge. If that goes red, no agent changes merge
> until it's back to green."

**3:20 — The changes you'll actually make (75s, mostly for J.)**
> "Two SharePoint lists you'll edit weekly. *[open WLF Sensitive Topics
> list]* — this is the sensitive-topic list. When a new client is
> onboarded, add their name and any common variant here. The agent reads
> it on every request, no restart needed. *[open WLF KM On-call list]*
> — this is the on-call rotation. Edit it weekly with the senior
> associate for that ISO week. And if you ever find the agent answered
> something it shouldn't have, the third change is to add an eval case to
> the repo so it can't regress — that's a PR with one JSON line, then
> CI gates the rest."

**4:35 — Wrap (25s)**
> "That's the whole thing. The handover guide has every detail, the
> runbook has the troubleshooting table, and my contact is there for the
> 30-day support window through October 30th. Thanks both — it was a
> pleasure building this, and have fun with it."

---

**Tips actually used in this recording:**
- Recorded two takes — the first one had me fumble the live Teams demo.
- Used a fake client name ("Acme Inc.") in the sensitive-topic demo;
  this got noted in the video description so nobody thinks it was real.
- Coordinated the on-call to be online during recording so the Teams DM
  showed in real time.
- Trimmed two seconds of dead air between each section.
- The Loom share link was added to the top of the handover guide before
  delivery.
