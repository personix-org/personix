---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputation-Based Social Network

To bring about change, we need a carefully designed tool. First we will sketch it briefly; in later chapters we will examine each piece in greater detail and add more. Imagine an uncensorable, global, decentralized social network where you could safely create and manage your proxy identity — a so-called Decentralized Identity (DID). A DID is a digital identity that you create and control yourself, without dependence on any central authority. Nobody can take it away or forge it, because it is cryptographically signed with your private key (or keys, via multisig).

> [!note] Note
> One implication is that such an identity could gradually replace state-issued identification documents — but more on that in the chapter on transition.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

In such a network, you could report through your identity that someone has caused you harm (and later, potentially, that they have remedied it or been compelled to do so). For this feedback — directed at the originator of the harm — to have value as a relevant source, entering information into the network must cost time, energy, and money — and on top of that, verifiable proof must be produced for others that this is not idle chatter.

Reading information would be easy and relatively cheap, but creating an individual record would be costly and demanding. Writing would follow a clear protocol, in which computation according to the chosen algorithm strictly determines which DID to ask for verification of the submitted information and how to proceed so that the selected participant processes the information on your behalf, publishes it, and becomes its verifier.

> [!note] Algorithm vs radicalism
> Algorithmic selection of verifiers ensures that non-radical information publishers will, over time, maintain a nearly neutral balance between the costs of published information and rewards for verification.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Let us look at how the algorithm selects a verifier.

> [!note] Algorithm
> Algorithmic selection non-deterministically chooses a different verifier (or a set of possible verifiers) for different pieces of information. A hash (a one-way mathematical function that produces a unique “fingerprint” from any input — like a fingerprint of a document) of the complete DID document determines the position on a consistent hash ring and selects verifier candidates.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> In plain language: the algorithm takes your entire DID document, computes a fingerprint from it, and that fingerprint determines your verifier.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

With the first verifier the algorithm selects, you as the publisher may not succeed — your reputation or declared settings may not meet their requirements. You would algorithmically continue the search for the next one by performing another recursive iteration, which assigns you a further verifier. With each step the “distance” to the target verifier grows, and so does the accompanying metadata that must be published. As the data grows, costs naturally rise (not only because of the initial size of the claim, but also because of the metadata accumulating with each rejection). Credible information passes far more easily than nonsensical whims. It is up to each person how high a price they are willing to bear and how much the record matters to them — radicalism is guaranteed to get expensive.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Whatever the verifier decides in response to your verification request, the ball is back in the publisher's court: they can accept the verifier's offer for verification services, fold the response into the chronology and try again (more expensively), or walk away and swallow the sunk cost.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

To give your information greater weight and a better chance of acceptance with verifiers, you — as a publisher with a stake in the information being issued — could use the services of a **trusted authority**. The authority either rejects the submitted information or accepts it and stakes its good name (reputation) on it. The authority typically requests real-world evidence, verifies it, and classifies it. The output is a protocol of its assessment of the given case at the given time. Think of an authority as a specialist in a certain type of service in both the real and digital world — for example an investigator, an auditor, an insurer, a supplier of a certain class of goods (in essence, any economic actor on the market).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

By the time you try to publish information into the network, it will likely already contain information about its actors — these are reputation signals. Navigating how to read reputation signals — what they mean for you in different situations and what risks they carry — may not be trivial. Each participant can look at reputation records differently through their DID, depending on the situation they are dealing with regarding the counterparty. Is the counterparty a reliable payer, or do I need to demand money upfront for a business transaction? Does the offered product carry reviews about hidden fraud or defects? Are they trying to wriggle out of contractual responsibility when something goes wrong? Sometimes a more complex view of the counterparty's overall consistency comes in handy — it depends on the preferences of whoever requests the overview. The market could offer products and services that simplify, process, and clarify the reading of reputation in the context of the situation at hand. Various authorities and their offered services can serve this purpose as well.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Examples
> Typical information of interest to publishers — and valuable to others — concerns events beyond ordinary interpersonal communication in the real or virtual world.
>
> Negative examples:
> - evidence of criminal acts (e.g., audited by a trusted investigative body)
> - indirect evidence (weak on its own, but statistically cumulative) — e.g., repeated presence near multiple thefts in a short time → still coincidence?
> - breach of contract
>
> Positive examples:
> - remedied harm (voluntarily or under pressure from the community as punishment)
> - acceptance and serving of a penalty proposed by authority X
> - authority X revoked recognition of the perpetrator's property rights to a certain extent
>
> It is up to each person to gather available information about the counterparty and assess the risks according to their preferences.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Whether information about you appears in the network depends exclusively on your own behavior.
> You never have to join such a network, yet information about you may still appear in it. It depends exclusively on your actions and the impact they have on others.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

What I have just briefly sketched is how a social network inspired by Decentralized Identity (DID) could work. The primary purpose of DID concepts is to strengthen privacy and freedom through the principle of subscribing to the rules I will follow and live by — giving users the ability to decide what information to share and under what conditions.

I propose to further connect DIDs into a communication network where their holders exchange feedback even beyond situations where something has happened to someone and the community or an individual needs to react. Such preventive comparison of the rules we have signed up to — with the option to compute the economic and other consequences of mutual deviations in expectations about how the other side ought to operate — could be considered a motivation for finding consensus. Instead of freedom, such a system would emphasize voluntary decision-making combined with responsibility for real-world behavior.

An individual cannot break the system alone — a group of people stands a greater chance, and a group of people with negotiated consensus and motivations to pull together on many issues stands an even greater chance of resisting authoritarian tendencies. The organization prerequisite from the first chapter will be fulfilled once two conditions are met: the DID reputation network covers communities representatively enough that its use ceases to be exotic. And at the same time, this community segment becomes an economically significant minority that can assertively negotiate with the rest of society.

> [!note] Voluntariness vs freedom
> Freedom — in the positive sense — would be a secondary effect of balancing two factors: voluntariness and the pressure of one's surroundings toward responsibility.

> [!note] The AI Era and the Value of Reputation
> In the era of artificial intelligence, everything connected to cognitive thinking is being automated — and it may go even further. What then remains in human activity as a competitive advantage? The answer is hard, and something will surely be found, but one thing we can say with certainty: reputation will decide. A verifiable history of your behavior, your commitments and their fulfillment — that is something AI will not build for you.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
