---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Roles Overview

We already touched briefly on some of these roles in the chapter about the network and its basic properties. Now is the time to look at them again in more detail and add the additional ones we need to make the network more robust. Every verification transaction involves several roles — let’s see how they behave.

> [!note] Roles in a Verification Transaction
> Each verification involves up to six distinct roles, summarised in the table below. All of them can have their own DID in the decentralized reputation network.

| Role | Description |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Issuer** | The person who publishes information to the network — claims that something happened (a DID was created, edited or dissolved, a claim, the policy of a given DID, etc.) |
| **Subject** | The person the information is about — the addressee of the claim |
| **Authority** | A trusted entity that stakes its name on the quality of the claim by investigating it and either reviewing the evidence presented or actively gathering it |
| **Observer** | An independent third party who keeps a record of how the verifier handles the claim — making sure the verifier neither stays silent nor deviates from the policy they declared |
| **Verifier** | An algorithmically selected participant who processes the transaction |
| **Delegate** | A person acting on behalf of another participant |
