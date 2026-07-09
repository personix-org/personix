---
title: "Rețea socială bazată pe reputație"
chapter: 2
part: "Instrumentul"
lang: en
version: v6
source: v1
---

# Rețea socială bazată pe reputație

Pentru a produce schimbarea, avem nevoie de un instrument proiectat cu grijă. Mai întâi îl vom schița pe scurt; în capitolele următoare vom examina fiecare parte în detaliu și vom adăuga mai multe. Imaginează-ți o rețea socială necenzurabilă, globală, descentralizată, în care ți-ai putea crea și administra în siguranță identitatea-proxy — o așa-numită Identitate Descentralizată (DID). Un DID este o identitate digitală pe care o creezi și o controlezi tu însuți, fără dependență de vreo autoritate centrală. Nimeni nu ți-o poate lua sau falsifica, pentru că este semnată criptografic cu cheia ta privată (sau cu mai multe chei, prin multisig).

> [!note] Notă
> O implicație este că o astfel de identitate ar putea înlocui treptat actele de identitate emise de stat — dar despre asta mai multe în capitolul despre tranziție.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Într-o astfel de rețea, ai putea raporta prin identitatea ta că cineva ți-a produs un prejudiciu (și, mai târziu, eventual, că l-a remediat sau a fost silit s-o facă). Pentru ca acest feedback — îndreptat spre cel care a produs prejudiciul — să aibă valoare ca sursă relevantă, introducerea informației în rețea trebuie să coste timp, energie și bani — iar pe deasupra trebuie produsă și o dovadă verificabilă pentru ceilalți că nu este vorbă în vânt.

Citirea informației ar fi ușoară și relativ ieftină, dar crearea unei înregistrări individuale ar fi costisitoare și pretențioasă. Scrierea ar urma un protocol clar, în care calculul conform algoritmului ales determină strict cărui DID să i se ceară verificarea informației transmise și cum să se procedeze astfel încât participantul selectat să prelucreze informația în numele tău, s-o publice și să devină verificatorul ei.

> [!note] Algoritm vs radicalism
> Selecția algoritmică a verificatorilor asigură că editorii de informație neradicali vor menține în timp un echilibru aproape neutru între costurile informației publicate și recompensele pentru verificare.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Să vedem cum selectează algoritmul un verificator.

> [!note] Algoritm
> Selecția algoritmică alege în mod nedeterminist un verificator diferit (sau un set de verificatori posibili) pentru informații diferite. Un hash (o funcție matematică unidirecțională care produce o „amprentă” unică din orice intrare — ca amprenta unui document) al documentului DID complet determină poziția pe un inel de hash consistent și selectează candidații de verificatori.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Pe scurt: algoritmul îți ia întregul document DID, calculează din el o amprentă, iar acea amprentă îți determină verificatorul.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Cu primul verificator pe care îl selectează algoritmul, tu, ca editor, s-ar putea să nu reușești — reputația ta sau setările declarate s-ar putea să nu îndeplinească cerințele lui. Ai continua algoritmic căutarea următorului, efectuând o nouă iterație recursivă, care îți atribuie un alt verificator. Cu fiecare pas, „distanța” până la verificatorul-țintă crește, la fel și metadatele însoțitoare care trebuie publicate. Pe măsură ce datele cresc, costurile urcă în mod firesc (nu doar din cauza dimensiunii inițiale a afirmației, ci și din cauza metadatelor care se acumulează la fiecare respingere). Informația credibilă trece mult mai ușor decât capriciile fără sens. Depinde de fiecare cât de mare este prețul pe care e dispus să-l suporte și cât de mult contează înregistrarea pentru el — radicalismul e garantat că devine scump.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Orice ar decide verificatorul ca răspuns la cererea ta de verificare, mingea revine în terenul editorului: el poate accepta oferta verificatorului pentru serviciile de verificare, poate include răspunsul în cronologie și poate încerca din nou (mai scump) sau se poate retrage și înghiți costul irecuperabil.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Pentru a da informației tale o greutate mai mare și o șansă mai bună de acceptare la verificatori, tu — ca editor cu miză în informația emisă — ai putea folosi serviciile unei **autorități de încredere**. Autoritatea fie respinge informația transmisă, fie o acceptă și își pune numele bun (reputația) în joc pentru ea. Autoritatea cere de regulă dovezi din lumea reală, le verifică și le clasifică. Rezultatul este un protocol al evaluării ei pentru cazul dat, la momentul dat. Gândește-te la o autoritate ca la un specialist într-un anumit tip de serviciu, atât în lumea reală, cât și în cea digitală — de pildă un investigator, un auditor, un asigurător, un furnizor al unei anumite clase de bunuri (în esență, orice actor economic de pe piață).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Până să încerci să publici informație în rețea, aceasta va conține deja, probabil, informații despre actorii ei — acestea sunt semnale de reputație. Orientarea în felul în care se citesc semnalele de reputație — ce înseamnă ele pentru tine în situații diferite și ce riscuri poartă — poate să nu fie banală. Fiecare participant poate privi înregistrările de reputație altfel, prin DID-ul său, în funcție de situația cu care se confruntă în raport cu partea adversă. Este partea adversă un plătitor de încredere sau trebuie să cer banii înainte pentru o tranzacție comercială? Produsul oferit poartă recenzii despre fraude sau defecte ascunse? Încearcă să se sustragă responsabilității contractuale atunci când ceva merge prost? Uneori este utilă o privire mai complexă asupra consecvenței generale a părții adverse — depinde de preferințele celui care solicită prezentarea de ansamblu. Piața ar putea oferi produse și servicii care simplifică, prelucrează și clarifică citirea reputației în contextul situației date. Diverse autorități și serviciile pe care le oferă pot servi la fel acestui scop.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Exemple
> Informația tipică ce interesează editorii — și valoroasă pentru ceilalți — privește evenimente ce depășesc comunicarea interpersonală obișnuită din lumea reală sau virtuală.
>
> Exemple negative:
> - dovezi ale unor fapte penale (de ex. auditate de un organ de investigație de încredere)
> - dovezi indirecte (slabe în sine, dar cumulative statistic) — de ex. prezența repetată în apropierea mai multor furturi într-un timp scurt → tot coincidență?
> - încălcarea contractului
>
> Exemple pozitive:
> - prejudiciu remediat (de bunăvoie sau sub presiunea comunității, ca pedeapsă)
> - acceptarea și executarea unei pedepse propuse de autoritatea X
> - autoritatea X a retras recunoașterea drepturilor de proprietate ale făptașului într-o anumită măsură
>
> Depinde de fiecare să adune informațiile disponibile despre partea adversă și să evalueze riscurile după preferințele sale.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Dacă informația despre tine apare în rețea depinde exclusiv de propriul tău comportament.
> Nu ești niciodată obligat să te alături unei astfel de rețele, și totuși informația despre tine poate apărea în ea. Depinde exclusiv de faptele tale și de impactul lor asupra celorlalți.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Ceea ce tocmai am schițat pe scurt este felul în care ar putea funcționa o rețea socială inspirată de Identitatea Descentralizată (DID). Scopul principal al conceptelor DID este întărirea intimității și a libertății prin principiul abonării la regulile pe care le voi urma și după care voi trăi — dându-le utilizatorilor puterea de a decide ce informații să împărtășească și în ce condiții.

Propun conectarea în continuare a DID-urilor într-o rețea de comunicare în care deținătorii lor fac schimb de feedback chiar dincolo de situațiile în care i s-a întâmplat ceva cuiva și comunitatea sau un individ trebuie să reacționeze. O astfel de comparare preventivă a regulilor la care ne-am abonat — cu opțiunea de a calcula consecințele economice și de altă natură ale abaterilor reciproce în așteptările despre cum ar trebui să funcționeze cealaltă parte — ar putea fi considerată o motivație pentru găsirea consensului. În locul libertății, un asemenea sistem ar sublinia decizia voluntară combinată cu responsabilitatea pentru comportamentul din lumea reală.

Un individ nu poate sparge singur sistemul — un grup de oameni are șanse mai mari, iar un grup de oameni cu consens negociat și motivații de a trage împreună la multe chestiuni are șanse și mai mari de a rezista tendințelor autoritare. Premisa organizării din primul capitol va fi îndeplinită odată ce sunt satisfăcute două condiții: rețeaua de reputație DID acoperă comunitățile suficient de reprezentativ încât folosirea ei să înceteze a mai fi exotică. Și, în același timp, acest segment de comunitate devine o minoritate semnificativă economic, care poate negocia asertiv cu restul societății.

> [!note] Caracterul voluntar vs libertatea
> Libertatea — în sens pozitiv — ar fi un efect secundar al echilibrării a doi factori: caracterul voluntar și presiunea mediului spre responsabilitate.

> [!note] Era IA și valoarea reputației
> În era inteligenței artificiale, tot ce ține de gândirea cognitivă se automatizează — și s-ar putea merge chiar mai departe. Ce rămâne atunci în activitatea umană ca avantaj competitiv? Răspunsul e greu, și cu siguranță se va găsi ceva, dar un lucru îl putem spune cu certitudine: reputația va decide. Un istoric verificabil al comportamentului tău, al angajamentelor tale și al împlinirii lor — asta e ceva ce IA nu ți-l va construi.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
