# Loom walkthrough script — Greenfield Logistics: Asana → SharePoint daily sync

A worked version of `loom-script.md` for the Greenfield engagement. Target
length 3–5 min; the actual recorded video is linked from
[handover-greenfield-logistics.md](handover-greenfield-logistics.md).

---

**0:00 — Intro (15s)**
> "Hi Cara, this is a quick walkthrough of the Asana-to-SharePoint sync I
> built for you. I'll show you what it does, how to check it's working,
> and how to make small changes. The written guide covers everything too —
> the link is in the handover doc I sent."

**0:15 — What it does (45s)**
> "At a high level: every weekday at 6 AM Sydney time, the flow pulls every
> job approved in the Asana Dispatch board the previous business day, and
> writes them as rows in your Deliveries list here on SharePoint, deduped
> by Job ID so re-runs don't duplicate. Here's the result — *[show the
> SharePoint Deliveries list filtered to today; point at 3–4 rows]* — these
> all landed automatically this morning."

**1:00 — Where it lives + how to check it's healthy (90s)**
> "This is the flow, in Power Automate, called 'Greenfield — Asana to
> SharePoint daily sync'. Here's the run history — *[scroll the last 7
> days]* — every weekday should be green. If anything fails you'll get
> an email at `ops-alerts@greenfieldlogistics.com.au`, and the failure
> also shows up in this Sync Log list on SharePoint — *[show the Sync Log
> list]* — one row per run, with the row counts and status. Filter for
> `status = failed` if you ever want to look at just the bad runs."

**2:30 — Making a common change (60s)**
> "Two changes you might want to make. First, the schedule — open the flow,
> click the Recurrence trigger at the top, and change the time or weekdays
> there. Just hit Save when you're done and you're good. Second, adding an
> email recipient to alerts — easiest way is to add them to the
> `ops-alerts@…` distribution list directly in Outlook so the flow doesn't
> need editing. The runbook lists the rest of the common changes —
> adding a column, pausing the flow, that kind of thing."

**3:30 — Wrap (20s)**
> "That's the whole thing. The handover guide has every detail and my
> contact for the 14-day support window through August 19th. Thanks Cara
> — it was a pleasure building this. Happy syncing."

---

**Tips actually used in this recording:**
- Rehearsed once start-to-finish before hitting record (cut 90 seconds of
  ums).
- Paused recording while navigating to a new tab so the video stays tight.
- Trimmed the first 4 seconds of dead air at the start.
- Put the Loom share link at the top of the handover guide so Cara doesn't
  have to hunt for it.
