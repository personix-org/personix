---
title: "Glosar"
part: "Appendix"
lang: en
version: v6
---

# Glosar

| Termen | Română | Semnificație |
|------|-------|---------|
| **Authority** | Autoritate | O entitate de încredere (persoană, organizație) care verifică informații și își pune reputația în joc pentru ele. Poate fi specializată (de investigație, juridică, tehnică). |
| **Claim** | Afirmație | În general: orice enunț verificabil. Aici: o înregistrare publicată în rețeaua de reputație — o aserțiune despre un eveniment, o proprietate sau o relație, semnată criptografic și verificată. De ex. „Sunt rezident al localității X” sau „această persoană a încălcat un contract”. |
| **Compartmentalization** | Compartimentare | În general: separarea informației în unități izolate, astfel încât expunerea unei unități să nu le compromită pe celelalte. Un principiu cunoscut din serviciile de informații. Aici: identități DID paralele în dictaturi — compromiterea uneia nu le dezvăluie pe celelalte. |
| **Consistent Hash Ring** | Inel de hash consistent | Un mecanism algoritmic pentru selecția verificatorilor — o poziție pe inel este determinată de hash-ul documentului DID din cadrul grafului social. Asigură o selecție nedeterministă, dar verificabilă. |
| **DID** | DID (identitate descentralizată) | O identitate digitală pe care o creezi și o controlezi tu însuți, fără o autoritate centrală. Semnată criptografic cu cheia ta privată — nimeni nu o poate revoca sau falsifica. |
| **DID Document** | Document DID | Un fișier de date accesibil public care descrie identitatea ta DID — conține chei publice, adrese de rețea și metadate. Servește la verificarea identității tale în rețea. |
| **Due Diligence** | Due diligence | În general: verificarea aprofundată a unei părți adverse înainte de a intra într-o relație comercială sau juridică — verificarea istoricului, finanțelor, reputației și riscurilor ei. Aici: în rețeaua de reputație se produce mai repede și mai automat datorită disponibilității înregistrărilor verificate. |
| **Economic Neutrality Principle** | Principiul neutralității economice | Comportamentul onest în rețea este economic apropiat de zero — costurile de publicare se întorc ca recompense pentru verificare. Comportamentul necinstit este o pierdere netă. |
| **Emergent** | Emergent | Ivindu-se spontan din interacțiunile unor părți mai simple, fără ca cineva să-l proiecteze sau să-l dirijeze. Un stol de păsări zboară în formație fără un plan — formația se ivește din reguli simple urmate de fiecare individ. |
| **Emergent Social Contract** | Contract social emergent | Reguli de comportament care se nasc nu de sus (lege), ci de jos — din interacțiuni repetate și consens în cadrul unei comunități. |
| **ESR** | Registrul electronic al cheltuielilor | Un sistem propus pentru urmărirea transparentă a cheltuielilor publice — fiecare cheltuială realizată a statului este potrivită cu o plată planificată. Inspirat de EET-ul ceh, dar întors împotriva statului. |
| **Hash** | Hash (amprentă) | În general: o funcție matematică unidirecțională care produce o „amprentă” unică, de lungime fixă, din orice intrare — ca amprenta unui document. Aceeași intrare produce mereu aceeași ieșire, dar intrarea nu poate fi derivată din ieșire. Aici: folosit pentru a determina o poziție pe inelul de hash și pentru a verifica integritatea documentului. |
| **Just-in-Time Funding** | Finanțare just-in-time | Finanțare a statului condiționată de transparență — banii curg doar când statul acceptă ESR și își potrivește cheltuielile. O pârghie pentru a sili cooperarea. |
| **Meritocracy** | Meritocrație | În general: un sistem în care poziția este determinată de meritul real și de capacitatea dovedită, nu de titluri formale, relații sau privilegii moștenite. Aici: rețeaua de reputație îi favorizează în mod firesc pe cei care contribuie demonstrabil la comunitate — vocea lor cântărește mai mult datorită istoricului, nu funcției. |
| **Onion Gateway** | Onion gateway | Adresa de rețea a unei identități DID pe rețeaua onion. Separată de documentul DID — poate fi schimbată fără a pierde identitatea (asemenea schimbării adresei IP din spatele unui domeniu). |
| **Onion Routing** | Onion routing (Tor) | Un protocol de comunicare care asigură necenzurabilitatea rețelei. Mesajele sunt criptate în straturi — fiecare nod desprinde un strat, dar nu cunoaște întregul traseu. |
| **Oracle Problem** | Problema oracolului | În general: cum să te asiguri că datele care intră într-un sistem digital corespund fidel cu ceea ce s-a întâmplat efectiv în lumea fizică. Termenul provine din domeniul blockchain. Aici: rezolvată prin autorități care își pun reputația în joc drept garanție că o înregistrare digitală corespunde realității fizice. |
| **Phenomenological** | Fenomenologic | În general: o abordare care studiază fenomenele așa cum se manifestă ele în experiența directă, observând ce decurge din ele, fără teorii prestabilite. Aici: libertatea, contractul social și normele de comportament sunt fenomene observate — consecințe ale miilor de microinteracțiuni dintre oameni, nu principii definite de sus. |
| **Policy** | Policy (politică) | În general: un set de reguli sau principii care guvernează comportamentul într-un context dat. Aici: fiecare participant la rețeaua DID își declară politica — cum reacționează la comportamentul concret al celorlalți, ce reguli respectă și ce pedepse consideră proporționate. Agregatul politicilor formează contractul social emergent. |
| **Proxy** | Proxy | În general: un înlocuitor sau intermediar — un sistem sau o entitate care acționează în numele alteia. Folosit aici în două contexte: (1) ESR ca proxy care potrivește cheltuielile publice cu plățile planificate; (2) observatorii ca proxy între editor și verificator, în trucul observatorilor. |
| **Publisher** | Editor | Un participant la rețea care creează și publică o înregistrare (o afirmație despre o nedreptate, o remediere și așa mai departe). Suportă costul publicării. |
| **Reputation-Based Social Network (RSN)** | Rețea de reputație | O rețea socială descentralizată în care participanții fac schimb de feedback despre comportamentul din lumea reală. Înregistrările sunt costisitoare de creat, ieftine de citit. |
| **Reputation Signal** | Semnal de reputație | O înregistrare individuală din rețea — pozitivă (remedierea unui prejudiciu, îndeplinirea unei obligații) sau negativă (nedreptate, încălcare de contract). Cumulativ, semnalele formează un profil de reputație. |
| **Social Graph** | Graf social | Rețeaua contactelor tale și a contactelor contactelor tale. Algoritmul caută verificatori la o adâncime configurabilă (de exemplu 3 niveluri). Fără blockchain global — rețeaua formează în mod firesc comunități cu suprapuneri. |
| **Tax Allocation** | Alocarea taxelor | Un mecanism prin care contribuabilul decide unde merge o parte din taxele lui. Procentul alocabil crește de la an la an. |
| **Track Record** | Track record (istoric) | În general: istoricul rezultatelor, succeselor și eșecurilor trecute ale unei persoane sau organizații. Aici: suma tuturor interacțiunilor trecute ale unei identități DID date în rețea — afirmații verificate, înregistrări acceptate și respinse — din care se derivă reputația ei. |
| **Verifier** | Verificator | Un participant selectat algoritmic pentru a verifica și publica o înregistrare. Își pune numele bun în joc pentru veridicitatea informației. |
