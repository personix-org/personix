---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Consensus and the Verification Process

To build consensus on which rules a society should, on average, uphold and enforce, the following mechanism can help. As a DID participant, I declare the rules I subscribe to and will live by, and I publish them. (Think of it as the by-laws and statutes that, in my view, make up my ideal world — a world where I do not feel restricted, but safe.)

I can estimate in advance how my DID contacts would react — and assess how strongly, and by whom, I would be sanctioned in ordinary social or business interactions, should they hypothetically occur.

The definitive evaluation happens when you request information from another DID, or ask them to verify a claim (or ask an authority for a service, and so on) that you want to publish to the reputation network. It should turn out the same way as it does when you run the evaluation yourself, in dry run, against the counterparty’s declared policy — and if it doesn’t, something is wrong on the counterparty’s side: they are trying to play a dishonest game.

The outcome is either acceptance, with a quoted price for verification (in the case of verifier or authority services), or rejection. Both sanctions and bonuses for deviation from the evaluator’s policy are folded into the quoted price. The requester then decides whether to accept the terms, or move on to the next round of verification in the allocation algorithm — repeating the process until satisfied, or until the economics make it pointless to continue.

> [!note] The Social Graph
> The reputation network is, first and foremost, a social network. You add contacts — people who consent to the connection. They have contacts, and those contacts have contacts. The algorithm searches for verifiers within a configurable depth (e.g., three levels: your direct contacts, their contacts, and one level beyond). No global blockchain is needed — the network naturally forms communities with overlaps into other communities.
>
> The algorithm is nondeterministic: it hashes your claim document, maps the hash to a position on a ring of known identities within this circle, and selects the nearest one as the candidate verifier. You cannot predict or influence who will verify your claim.

Each verifier’s rejection enlarges your document and increases its processing cost — that is the first cost channel (document growth). Each new verifier charges a fee based on data volume, your reputation, and how far the content of your claim deviates from their declared verification policy — that is the second cost channel (risk premium). And each iteration costs time and energy — the third cost channel.

> [!note] What the Verifier Checks, in Order
> Once selected, a verifier evaluates a claim in roughly four ordered steps — cheapest filters first, expensive content checks last:
>
> 1. **Policy gating.** Does this kind of claim fall within what the verifier publicly verifies at all? If not, the request is rejected outright.
> 2. **Authority trust.** Is the authority that endorsed the claim trusted enough under the verifier’s own declared policy? An authority below the verifier’s trust threshold is grounds for rejection regardless of the claim’s content.
> 3. **Issuer reputation.** Does the issuer meet the reputation thresholds the verifier has declared for this type of claim? Low reputation may either raise the fee or trigger rejection.
> 4. **Content check.** Only when the first three gates pass does the verifier evaluate the claim itself — signatures, internal consistency, formal correctness, and how far it deviates from the verifier’s policy. The fee charged for this last step reflects the actual risk taken.
>
> The verifier publishes the policy that governs each of these gates, so the steps are not at their discretion — they are bound by what they have already declared. Deviation from the published policy is itself a publishable claim against them, and they pay for it with their reputation.

The result: publishing a credible and useful claim costs almost nothing. Publishing a radical claim costs more. Publishing a lie becomes prohibitively expensive — you must iterate through verifier after verifier, and every one who rejects you adds costs. The market prices your claim, and the price tells you where you stand in relation to the communities you move in.

It is not enough to declare that you adhere to a rule when in reality you do not. In that case, your DID risks the publication of a negative record exposing the hypocrisy — which turns you into a risk for everyone else. The outcome should be fewer but more consistently followed rules, and a clearing of that jungle of laws and regulations that even legal professionals can barely navigate.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consensus vs Accountability
> For the network to serve as a valuable source of information, a DID should not be too radical — otherwise the others will reject it. Social pressure will seek equilibrium, and attempts to destabilise it will likely be punished.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] The Number of Votes Is Not the Same as the Weight of a Voice
> Juraj Karpiš says that "money is the memory of good deeds." I would add that reputation is the memory of the bad ones.
>
> It follows that, meritocratically, whoever contributes more and has no bad reputation deserves a greater weight of voice in the community. Looked at through the lens of bilateral relationships: when I weigh which consensus pressures to accommodate, the greatest weight goes to the relationships from which I derive the largest economic benefit. Ten people with whom I have no active trade will influence me far less than one permanent business partner. This paradigm is not limited to commerce — it extends to social, political and other relationships.
