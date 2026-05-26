# Whitepaper — Extra Figures (F7, F8, F9)

---

## Figure 7: Claim Lifecycle (Section 4.3)

```mermaid
sequenceDiagram
    participant Publisher
    participant Authority
    participant HashFn as Hash Function
    participant Ring as Hash Ring
    participant Verifier
    participant Network

    Note over Publisher: F7 — Claim Lifecycle

    Publisher->>Publisher: Compose claim document

    rect rgba(200, 200, 255, 0.15)
        Note over Publisher,Authority: Optional endorsement
        Publisher->>Authority: Submit for endorsement
        Authority->>Authority: Review claim, assess risk
        Authority-->>Publisher: Co-sign + fee quote
    end

    Publisher->>HashFn: claim_doc + previous_hash
    HashFn->>Ring: Mapped position on ring

    Ring->>Verifier: Nearest DID clockwise = candidate

    Verifier->>Verifier: Check against own policies

    alt Accept
        Verifier->>Network: Publish claim
        Network-->>Publisher: Confirmation + reputation update
    else Reject
        Verifier->>HashFn: Rejection hash -> new iteration
        Note over Verifier,HashFn: Cost increases with each iteration
    end
```

---

## Figure 8: Emergent Consensus — Satisfaction Averaging (Section 7.2)

```mermaid
flowchart TB
    subgraph individuals ["Individual Satisfaction Thresholds"]
        direction LR
        A["<b>Person A</b><br/>Strict<br/>Full compensation +<br/>public acknowledgment<br/><i>Dial: HIGH</i>"]
        B["<b>Person B</b><br/>Pragmatic<br/>Compensation only<br/>&nbsp;<br/><i>Dial: MEDIUM</i>"]
        C["<b>Person C</b><br/>Forgiving<br/>Apology suffices<br/>&nbsp;<br/><i>Dial: LOW</i>"]
    end

    A --> consensus
    B --> consensus
    C --> consensus

    consensus["<b>Network Consensus</b><br/>= statistical average of<br/>bilateral negotiations"]

    consensus --> pricing["<b>Verifier Pricing</b>"]

    pricing --> expensive_high["Response FAR ABOVE consensus<br/><i>(barbaric)</i><br/>Expensive to publish"]
    pricing --> cheap["Response NEAR consensus<br/><i>(proportional)</i><br/>Cheap to publish"]
    pricing --> expensive_low["Response FAR BELOW consensus<br/><i>(negligent)</i><br/>Also expensive"]

    footer["No law sets this. No authority enforces it.<br/><b>Price = consensus mechanism.</b>"]
    expensive_high ~~~ footer
    cheap ~~~ footer
    expensive_low ~~~ footer

    style A fill:#e74c3c,color:#fff,stroke:#c0392b
    style B fill:#f5a623,color:#fff,stroke:#c47d12
    style C fill:#2ecc71,color:#fff,stroke:#1fa355

    style consensus fill:#7b68ee,color:#fff,stroke:#5a48cc,stroke-width:3px
    style pricing fill:#4a90d9,color:#fff,stroke:#2c5f8a

    style expensive_high fill:#ff6b6b,color:#fff,stroke:#cc4444
    style cheap fill:#50c878,color:#fff,stroke:#36a85e,stroke-width:3px
    style expensive_low fill:#ff6b6b,color:#fff,stroke:#cc4444

    style footer fill:none,stroke:none,color:#555
```

---

## Figure 9: Citizen Tax Allocation Over Time (Section 8.3)

```mermaid
flowchart LR
    subgraph timeline ["Tax Allocation Timeline"]
        direction LR
        Y1["<b>Year 1</b>"]
        Y3["<b>Year 3</b>"]
        Y5["<b>Year 5</b>"]
        Y7["<b>Year 7</b>"]
        Y10["<b>Year 10</b>"]

        Y1 --> Y3 --> Y5 --> Y7 --> Y10
    end

    subgraph citizen_pct ["Citizen-Directed"]
        direction LR
        C1["5%"]
        C3["10%"]
        C5["15%"]
        C7["25%"]
        C10["40%"]
    end

    subgraph state_pct ["State-Managed"]
        direction LR
        S1["95%"]
        S3["90%"]
        S5["85%"]
        S7["75%"]
        S10["60%"]
    end

    Y1 --- C1
    Y3 --- C3
    Y5 --- C5
    Y7 --- C7
    Y10 --- C10

    Y1 --- S1
    Y3 --- S3
    Y5 --- S5
    Y7 --- S7
    Y10 --- S10

    prereq["<b>Prerequisites</b><br/>DID with verified citizenship<br/>+ residency + reputation"]
    note["Citizen DIRECTS tax — not avoids it.<br/>State portion shrinks but <b>never reaches zero</b>."]

    Y10 ~~~ prereq
    prereq ~~~ note

    style C1 fill:#2ecc71,color:#fff,stroke:#1fa355
    style C3 fill:#27ae60,color:#fff,stroke:#1e8449
    style C5 fill:#1abc9c,color:#fff,stroke:#148f77
    style C7 fill:#16a085,color:#fff,stroke:#117a65,stroke-width:2px
    style C10 fill:#0e6655,color:#fff,stroke:#0b5345,stroke-width:3px

    style S1 fill:#e74c3c,color:#fff,stroke:#c0392b,stroke-width:3px
    style S3 fill:#e67e22,color:#fff,stroke:#d35400
    style S5 fill:#f39c12,color:#fff,stroke:#d68910
    style S7 fill:#f5b041,color:#333,stroke:#d4ac0d
    style S10 fill:#f9e79f,color:#333,stroke:#d4ac0d

    style prereq fill:#4a90d9,color:#fff,stroke:#2c5f8a
    style note fill:none,stroke:none,color:#555

    style Y1 fill:#34495e,color:#fff,stroke:#2c3e50
    style Y3 fill:#34495e,color:#fff,stroke:#2c3e50
    style Y5 fill:#34495e,color:#fff,stroke:#2c3e50
    style Y7 fill:#34495e,color:#fff,stroke:#2c3e50
    style Y10 fill:#34495e,color:#fff,stroke:#2c3e50
```
