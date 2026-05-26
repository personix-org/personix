---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observer

The observer role removes the verifier’s incentive to bend the rules. In situations where a verifier doesn’t like the issuer’s or the authority’s request, they could simply stay silent — not respond, and block the algorithmic sequence. The observer — or a set of observers — stakes their reputation on documenting how the verifier was queried. If the verifier stays silent despite a declared policy that says otherwise, they can be convicted of violating the protocol.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## The mechanism: timestamp and challenge code

Before you send a claim to the verifier, you route it through observers — people you trust, or specialised observer-service providers who charge a small fee. Each observer receives your submission, time-stamps it, signs that they saw it go out, and generates a challenge code — a cryptographic hash of their signature. The codes are appended to your request. The verifier sees them but has no idea who the observers are, or whether the codes are even real. Observers thus act as proxies between the issuer and the verifier, holding an independent record that the claim was submitted and what it contained. There can be zero to N of them.

When the verifier behaves honestly — accepting or rejecting in line with their declared policy — the codes stay opaque. Nobody is exposed.

But if the verifier stays silent despite an accommodating policy, or responds in a way that contradicts what they published, you hold the original observer signatures. You can publish them as proxy testimony that the claim was submitted and that the verifier did not follow the protocol. Anyone can verify that the signatures match the challenge codes.

## The punchline: you don’t need real observers

And here is the most elegant part: **you do not need real observers at all.** You can generate random numbers that look exactly like challenge codes. The verifier cannot tell the difference — they have to roll the dice on whether to risk their reputation. Behind every request they receive there could be a respected observer watching incognito — or it could be pure noise. The verifier does not know. And that uncertainty is the mechanism.

The cost of maintaining honest pressure: nearly zero (random numbers are free). The potential cost of dishonesty for the verifier: catastrophic. Honest behaviour is incentivised even when nobody is actually watching.

The system works because everyone is a little paranoid. Uncertainty is cheaper than surveillance.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Multiple verifiers in a single iteration
> A reinforcing companion rule for verifier availability can be an algorithmic extension that returns, in a single iteration, a set of candidate verifiers rather than just one.
