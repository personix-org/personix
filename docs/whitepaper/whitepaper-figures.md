# Whitepaper Figures — Mermaid Diagrams

---

## Figure 1: RSN Architecture (Section 3.2)

Four-layer architecture of the Reputation Social Network showing component hierarchy and inter-layer communication.

```mermaid
flowchart TB
    subgraph AGG["Reputation Aggregation Layer"]
        direction LR
        A1["Interpretation\nServices"]
        A2["Risk\nSummaries"]
        A3["Service\nMarket"]
    end

    subgraph CLAIM["Claim Protocol"]
        direction LR
        C1["Claim\nComposition"]
        C2["Signing"]
        C3["Metadata"]
    end

    subgraph VERIF["Verification Network"]
        direction LR
        V1["Hash Ring"]
        V2["Verifier\nSelection"]
        V3["Accept /\nReject"]
    end

    subgraph DID["DID Layer"]
        direction LR
        D1["Identities"]
        D2["Declared\nRules"]
        D3["Reputation\nScores"]
        D4["Onion\nGateway"]
    end

    AGG <-->|"reputation queries & summaries"| CLAIM
    AGG <-->|"verified claim data"| VERIF
    CLAIM <-->|"claims submitted for verification"| VERIF
    CLAIM <-->|"identity & signing keys"| DID
    VERIF <-->|"DID positions on hash ring"| DID

    style AGG fill:#7b2d8e,color:#fff,stroke:#5a1d6b,stroke-width:2px
    style CLAIM fill:#27ae60,color:#fff,stroke:#1e8449,stroke-width:2px
    style VERIF fill:#e67e22,color:#fff,stroke:#ca6f1e,stroke-width:2px
    style DID fill:#2980b9,color:#fff,stroke:#1f6591,stroke-width:2px

    style A1 fill:#9b59b6,color:#fff,stroke:#7d3c98
    style A2 fill:#9b59b6,color:#fff,stroke:#7d3c98
    style A3 fill:#9b59b6,color:#fff,stroke:#7d3c98

    style C1 fill:#2ecc71,color:#fff,stroke:#27ae60
    style C2 fill:#2ecc71,color:#fff,stroke:#27ae60
    style C3 fill:#2ecc71,color:#fff,stroke:#27ae60

    style V1 fill:#f39c12,color:#fff,stroke:#d68910
    style V2 fill:#f39c12,color:#fff,stroke:#d68910
    style V3 fill:#f39c12,color:#fff,stroke:#d68910

    style D1 fill:#3498db,color:#fff,stroke:#2980b9
    style D2 fill:#3498db,color:#fff,stroke:#2980b9
    style D3 fill:#3498db,color:#fff,stroke:#2980b9
    style D4 fill:#3498db,color:#fff,stroke:#2980b9
```

---

## Figure 2: Four DID Roles (Section 4.2)

Interaction model between the four DID roles. Roles are not mutually exclusive -- a single DID can play multiple roles simultaneously.

```mermaid
flowchart TB
    H["<b>Holder</b>\nManages identity\nAccumulates reputation"]
    E["<b>Executor</b>\nActs on behalf\nof Holder"]
    A["<b>Authority</b>\nEndorses claims for fee\nStakes reputation"]
    V["<b>Verifier</b>\nAlgorithmically selected\nPublishes claims"]
    N[("RSN\nNetwork")]

    E -->|"authorized by\n(power of attorney)"| H
    H -->|"submits claim\nfor endorsement"| A
    A -->|"co-signs claim\n(stakes reputation)"| H
    A -->|"endorsed claim enters\nverification pipeline"| V
    V -->|"selected by\nprotocol (hash ring)"| H
    V -->|"publishes\nverified claim"| N

    E -.->|"can publish claims\non behalf of Holder"| A

    note1["Roles are NOT mutually exclusive.\nOne DID can play multiple roles."]

    style H fill:#3498db,color:#fff,stroke:#1f6591,stroke-width:3px
    style E fill:#2ecc71,color:#fff,stroke:#1fa355,stroke-width:2px
    style A fill:#9b59b6,color:#fff,stroke:#7d3c98,stroke-width:2px
    style V fill:#e67e22,color:#fff,stroke:#ca6f1e,stroke-width:2px
    style N fill:#34495e,color:#fff,stroke:#2c3e50,stroke-width:2px
    style note1 fill:#f9f9c5,color:#333,stroke:#ccc,stroke-dasharray:5 5
```

---

## Figure 3: Verifier Selection Protocol (Section 5.2)

Detailed flowchart of the nondeterministic verifier selection protocol based on consistent hashing. This is the core mechanism that prices radical claims through escalating iteration costs.

```mermaid
flowchart TB
    PUB["<b>Publisher</b>\ncreates claim"]
    CLAIM["<b>Claim Document</b>\n(structured assertion\nabout real-world event)"]
    PREV["<b>Previous Hash</b>\n(null on first iteration)"]
    HASH["<b>Hash Function f_h</b>\nf_h(claim || prev_hash)"]
    RING["<b>Map to Hash Ring</b>\nPosition in DID\nIdentifier Space"]
    SEARCH["<b>Clockwise Search</b>\nFind nearest DID\non the ring"]
    CANDIDATE["<b>Nearest DID =</b>\n<b>Verifier Candidate</b>"]
    POLICY{"<b>Verifier Policy</b>\n<b>Check</b>\nClaim compatible\nwith Verifier's\ndeclared policies?"}
    ACCEPT(["<b>Claim Published</b>\nto RSN"])
    REJECT["<b>Rejection Recorded</b>\nRejection hash added\nto claim metadata"]
    COST["<b>Cost Increases</b>\n- iteration++\n- document grows\n- fees escalate"]

    PUB --> CLAIM
    CLAIM --> HASH
    PREV --> HASH
    HASH --> RING
    RING --> SEARCH
    SEARCH --> CANDIDATE
    CANDIDATE --> POLICY

    POLICY -->|"<b>ACCEPT</b>\nVerifier stakes\nreputation"| ACCEPT
    POLICY -->|"<b>REJECT</b>\nPolicies incompatible\nor risk too high"| REJECT

    REJECT --> COST
    COST -->|"rejection hash\nbecomes new input\n(next iteration)"| HASH

    ITER["Each iteration:\n- New hash = new ring position\n- New Verifier candidate\n- Document bloat grows\n- Verifier risk premium rises\n- Total cost compounds"]

    style PUB fill:#4a90d9,color:#fff,stroke:#2c5f8a,stroke-width:2px
    style CLAIM fill:#4a90d9,color:#fff,stroke:#2c5f8a,stroke-width:2px
    style PREV fill:#95a5a6,color:#fff,stroke:#7f8c8d,stroke-width:1px
    style HASH fill:#f5a623,color:#fff,stroke:#c47d12,stroke-width:3px
    style RING fill:#7b68ee,color:#fff,stroke:#5a48cc,stroke-width:2px
    style SEARCH fill:#7b68ee,color:#fff,stroke:#5a48cc,stroke-width:2px
    style CANDIDATE fill:#7b68ee,color:#fff,stroke:#5a48cc,stroke-width:2px
    style POLICY fill:#e67e22,color:#fff,stroke:#ca6f1e,stroke-width:3px
    style ACCEPT fill:#2ecc71,color:#fff,stroke:#1fa355,stroke-width:4px
    style REJECT fill:#e74c3c,color:#fff,stroke:#c0392b,stroke-width:2px
    style COST fill:#e74c3c,color:#fff,stroke:#c0392b,stroke-width:2px
    style ITER fill:#fef9e7,color:#333,stroke:#f0c040,stroke-width:2px,stroke-dasharray:5 5
```

---

## Figure 4: Expensive Radicalism — Cost Escalation (Section 5.4)

Three cost channels that compound to make radical claims expensive — not censored, but priced.

```mermaid
flowchart TB
    subgraph ITER["Iteration Cost"]
        I1["Each rejection =\nnew hash = new verifier"]
        I2["Linear growth:\nn × c_time"]
        I1 --> I2
    end

    subgraph BLOAT["Document Bloat"]
        B1["Every request & response\nadds metadata"]
        B2["Linear growth:\nS_doc × c_storage"]
        B1 --> B2
    end

    subgraph RISK["Verifier Risk Premium"]
        R1["Willing verifiers charge\nmore for risky content"]
        R2["Exponential growth:\nα · e^(β · r)"]
        R1 --> R2
    end

    I2 --> TOTAL
    B2 --> TOTAL
    R2 --> TOTAL
    TOTAL["Total Cost = Iteration + Bloat + Premium"]

    TOTAL --> STRIP

    subgraph STRIP["Cost by Claim Type"]
        direction LR
        L1["Credible\n1–2 iter | small doc | base fee"]
        L2["Controversial\n5–10 iter | medium doc | 3× fee"]
        L3["Radical\n15–30 iter | large doc | 10× fee"]
        L4["Fraudulent\n∞ iter | unpublishable"]
        L1 ~~~ L2 ~~~ L3 ~~~ L4
    end

    MSG["Not censorship — pricing.\nNo claim is banned. Risk is priced."]
    STRIP --> MSG

    style I1 fill:#4a90d9,color:#fff,stroke:#2c5f8a
    style I2 fill:#4a90d9,color:#fff,stroke:#2c5f8a
    style B1 fill:#f5a623,color:#fff,stroke:#c47d12
    style B2 fill:#f5a623,color:#fff,stroke:#c47d12
    style R1 fill:#7b68ee,color:#fff,stroke:#5a48cc
    style R2 fill:#7b68ee,color:#fff,stroke:#5a48cc
    style TOTAL fill:#34495e,color:#fff,stroke:#2c3e50,stroke-width:3px
    style L1 fill:#2ecc71,color:#fff,stroke:#1fa355
    style L2 fill:#f1c40f,color:#333,stroke:#d4ac0d
    style L3 fill:#e74c3c,color:#fff,stroke:#c0392b
    style L4 fill:#7b241c,color:#fff,stroke:#512e1c,stroke-width:3px
    style MSG fill:#ecf0f1,color:#2c3e50,stroke:#bdc3c7,stroke-width:2px
    style ITER fill:#e8f4fd,stroke:#4a90d9,color:#333
    style BLOAT fill:#fef3e0,stroke:#f5a623,color:#333
    style RISK fill:#ede7f6,stroke:#7b68ee,color:#333
    style STRIP fill:#f9f9f9,stroke:#95a5a6,color:#333
```

---

## Figure 5: Reputable Authority — Reputation at Stake (Section 6.2)

Authority vouching process with asymmetric consequences: slow gain vs. instant loss.

```mermaid
flowchart TB
    EXAM["Authority examines claim\nReputation: 85%"]

    EXAM -->|"Claim was TRUE"| TRUE_PATH
    EXAM -->|"Claim was a LIE"| FALSE_PATH

    subgraph TRUE_PATH["Honest Vouch"]
        direction TB
        T1["Reputation rises to 87%\n+2%"]
        T2["More clients, higher fees"]
        T3["12 years reinforced"]
        T1 --> T2 --> T3
    end

    subgraph FALSE_PATH["False Vouch"]
        direction TB
        F1["Reputation crashes to 15%\n-70%"]
        F2["Clients leave, no income"]
        F3["12 years destroyed\nin one act"]
        F1 --> F2 --> F3
    end

    INSIGHT["Gaining reputation: slow (+2% per honest vouch)\nLosing it: instant (-70% per false vouch)"]
    TRUE_PATH --> INSIGHT
    FALSE_PATH --> INSIGHT

    style EXAM fill:#4a90d9,color:#fff,stroke:#2c5f8a,stroke-width:3px
    style T1 fill:#2ecc71,color:#fff,stroke:#1fa355
    style T2 fill:#27ae60,color:#fff,stroke:#1e8449
    style T3 fill:#1fa355,color:#fff,stroke:#178042
    style F1 fill:#e74c3c,color:#fff,stroke:#c0392b
    style F2 fill:#c0392b,color:#fff,stroke:#96281b
    style F3 fill:#96281b,color:#fff,stroke:#7b241c
    style TRUE_PATH fill:#eafaf1,stroke:#2ecc71,color:#333
    style FALSE_PATH fill:#fdedec,stroke:#e74c3c,color:#333
    style INSIGHT fill:#ecf0f1,color:#2c3e50,stroke:#bdc3c7,stroke-width:2px
```

---

## Figure 6: Migration Phases (Section 9.3)

Three-phase state diagram of voluntary migration from state systems to RSN. Reversible at every stage.

```mermaid
stateDiagram-v2
    direction LR

    state "Phase 1: Overlay\n━━━━━━━━━━━━━━━━━━━━\nRSN as informational layer\nState is sole provider" as P1
    state "Phase 2: Competition\n━━━━━━━━━━━━━━━━━━━━\nRSN provides functional alternatives\nDual-system use" as P2
    state "Phase 3: Transition\n━━━━━━━━━━━━━━━━━━━━\nRSN outperforms state\nVoluntary migration" as P3

    [*] --> P1
    P1 --> P2 : Reputation data gains\nreal-world value
    P2 --> P3 : RSN services outperform\nstate equivalents
    P3 --> P2 : Edge cases require\nstate fallback

    note right of P3
        Reversible at every stage
    end note
```
