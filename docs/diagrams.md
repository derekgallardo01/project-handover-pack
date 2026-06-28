# Diagrams

This is a templates kit — the diagrams here are about how the handover
fits into an engagement, not about a runnable system.

## 1. Where the handover sits in the engagement lifecycle

```mermaid
flowchart LR
    SOW["Signed SOW<br/>(discovery kit)"] --> HLD["HLD<br/>(architecture kit)"]
    HLD --> BUILD["Build phase"]
    BUILD --> FILL["Fill handover guide + runbook<br/>AS YOU BUILD"]
    FILL --> BUILD
    BUILD --> ACC["Acceptance"]
    ACC --> LOOM["Record Loom walkthrough"]
    LOOM --> VAL["python validate.py<br/>(catches leftover placeholders)"]
    VAL --> DELIVER["Deliver all 3 to client"]
    DELIVER --> SUPPORT["Support window<br/>(14 or 30 days)"]
    SUPPORT --> CLOSED["Engagement closed"]
    CLOSED --> REPEAT["Repeat business / referral?<br/>(handover quality decides)"]
```

The diagram makes one point: the handover is where repeat business and
five-star reviews are won or lost. Treat it as the deliverable, not the
afterthought.

## 2. The three artefacts — what each answers

```mermaid
flowchart TB
    OWNER["Day-to-day owner (non-developer)"] --> H["Handover guide:<br/>'What is it, where is it, who do I call?'"]
    OWNER --> R["Runbook:<br/>'What do I do when X breaks?<br/>How do I make change Y?'"]
    OWNER --> L["Loom walkthrough:<br/>'Can I SEE how this works?'"]

    H --> READ_ONCE["Read once, reference later"]
    R --> READ_ON_NEED["Read on need (per situation)"]
    L --> READ_ON_INHERIT["Watched when someone new inherits the system"]
```

## 3. The "fill as you build" workflow (the leverage move)

```mermaid
stateDiagram-v2
    [*] --> Build_Day1: handover-X.md + runbook-X.md created
    Build_Day1 --> Build_Mid: "Where it lives" section gets filled as components land
    Build_Mid --> Build_Late: "Common changes" rows filled as parameters get wired
    Build_Late --> Build_Late: "Troubleshooting" rows added per real bug hit
    Build_Late --> Acceptance: handover docs are ~90% done by acceptance
    Acceptance --> Loom_Recording: script.md filled + recorded
    Loom_Recording --> Validate: python validate.py
    Validate --> Loom_Recording: leftover placeholder found
    Validate --> Deliver: all clean
    Deliver --> [*]
```

Compared to the alternative ("docs at the end"):

```mermaid
stateDiagram-v2
    [*] --> Build_All
    Build_All --> Build_All: code, code, code
    Build_All --> Acceptance: code's done!
    Acceptance --> Panic: now write the docs from memory
    Panic --> Panic: forgot why I made this choice
    Panic --> Mediocre_Deliver: incomplete docs, no Loom, missed details
    Mediocre_Deliver --> [*]
```

## 4. Two worked engagements at a glance

```mermaid
flowchart TB
    subgraph GL["Greenfield Logistics handover"]
      G1["Build: Power Automate flow"]
      G2["3 artefacts: handover + runbook + loom"]
      G3["14-day support window"]
      G4["Monthly health check baked into runbook"]
    end
    subgraph WL["Whitford Legal handover"]
      W1["Build: Copilot Studio agent + Azure OpenAI"]
      W2["3 artefacts (same shape)"]
      W3["30-day support window"]
      W4["Monthly health check incl. AOAI quota review"]
    end
```

Same pack structure; different scale of engagement.
