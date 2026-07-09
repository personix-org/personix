---
title: "Privire de ansamblu asupra rolurilor"
chapter: 3
part: "Cum funcționează verificarea"
lang: en
version: v6
---

# Privire de ansamblu asupra rolurilor

Am atins deja pe scurt unele dintre aceste roluri în capitolul despre rețea și proprietățile ei de bază. Acum e momentul să le privim din nou în detaliu și să le adăugăm pe cele suplimentare de care avem nevoie pentru a face rețeaua mai robustă. Fiecare tranzacție de verificare implică mai multe roluri — să vedem cum se comportă.

> [!note] Rolurile într-o tranzacție de verificare
> Fiecare verificare implică până la șase roluri distincte, rezumate în tabelul de mai jos. Toate pot avea propriul DID în rețeaua de reputație descentralizată.

| Rol | Descriere |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Emitentul (Issuer)** | Persoana care publică informație în rețea — afirmă că s-a întâmplat ceva (un DID a fost creat, editat sau dizolvat, o afirmație, politica unui DID dat etc.) |
| **Subiectul (Subject)** | Persoana despre care este informația — destinatarul afirmației |
| **Autoritatea (Authority)** | O entitate de încredere care își pune numele în joc pentru calitatea afirmației investigând-o și fie examinând dovezile prezentate, fie strângându-le activ |
| **Observatorul (Observer)** | O terță parte independentă care ține evidența felului în care verificatorul tratează afirmația — asigurându-se că verificatorul nici nu tace, nici nu se abate de la politica declarată |
| **Verificatorul (Verifier)** | Un participant selectat algoritmic care procesează tranzacția |
| **Delegatul (Delegate)** | O persoană care acționează în numele altui participant |
