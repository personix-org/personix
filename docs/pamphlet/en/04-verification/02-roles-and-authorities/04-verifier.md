---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifier

Any DID can act as a verifier, either directly or through verification rights delegated to a third DID. For me — or my delegate — to be able to verify, I should be reachable on the network (online). Not everyone will want to commit to that, which is why a DID record can list, in priority order, the substitutes who will perform the function on its behalf while it is offline.

Every DID active in the network publicly declares its own policy. Through the rules defined in that policy it judges, during the verification process, the reputation of the counterparty and the content and form of the claim that the issuer has flagged for publication into the reputation network. Part of the policy is the calculation formula used to compute fees for verification services. Once that is in place, then across a statistically large number of claims flowing through the network I wait for the network’s algorithm to draw me on the issuer’s side and assign me, in a given iteration, to verify the information being issued. The issuer can compute in advance how a correctly behaving verifier would react, but cannot avoid actually contacting them (or their substitutes); the iteration with the selected verifier has to be carried out by the issuer even when they know in advance it will not pass.

How do we know that the issuer runs the verifier-selection algorithm over the correct set of candidate verifier DIDs? Together with its publicly declared policy, every DID also publishes the current list of identifiers of its social network within the reputation network. If an issuer defines its social network as a social bubble that merely echoes and reinforces its own views, information published through it will hardly be received more widely by other communities. The fact that I manage, at high cost, to push a radical claim into the network does not imply that, when judging the counterparty’s reputation, I will give it any weight. Some claims I am pushed by my community to take into account (sentences and restrictions imposed on offenders); others are entirely up to me — I decide for myself the economic value of including or excluding a given piece of information.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
