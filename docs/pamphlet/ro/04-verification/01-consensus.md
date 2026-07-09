---
title: "Consensul și procesul de verificare"
chapter: 3
part: "Cum funcționează verificarea"
lang: en
version: v6
source: v1
---

# Consensul și procesul de verificare

Pentru a construi consens asupra regulilor pe care o societate ar trebui, în medie, să le respecte și să le impună, poate ajuta mecanismul următor. Ca participant DID, îmi declar regulile la care mă abonez și după care voi trăi, și le public. (Gândește-te la ele ca la regulamentele și statutele care, în viziunea mea, alcătuiesc lumea mea ideală — o lume în care nu mă simt îngrădit, ci în siguranță.)

Pot estima dinainte cum ar reacționa contactele mele DID — și pot evalua cât de puternic și de către cine aș fi sancționat în interacțiuni sociale sau de afaceri obișnuite, dacă acestea ar avea loc ipotetic.

Evaluarea definitivă se produce când ceri informație de la un alt DID sau îi ceri să verifice o afirmație (ori ceri unei autorități un serviciu și așa mai departe) pe care vrei s-o publici în rețeaua de reputație. Ar trebui să iasă la fel cum iese când rulezi tu însuți evaluarea, în probă (dry run), pe politica declarată a părții adverse — iar dacă nu iese, ceva e în neregulă de partea adversă: încearcă un joc necinstit.

Rezultatul este fie acceptare, cu un preț cotat pentru verificare (în cazul serviciilor de verificator sau autoritate), fie respingere. Atât sancțiunile, cât și bonusurile pentru abaterea de la politica evaluatorului sunt incluse în prețul cotat. Solicitantul decide apoi dacă acceptă condițiile sau trece la runda următoare de verificare din algoritmul de alocare — repetând procesul până este mulțumit sau până când economia face inutilă continuarea.

> [!note] Graful social
> Rețeaua de reputație este, în primul rând, o rețea socială. Adaugi contacte — oameni care consimt la legătură. Ei au contacte, iar acele contacte au contacte. Algoritmul caută verificatori până la o adâncime configurabilă (de ex. trei niveluri: contactele tale directe, contactele lor și încă un nivel mai departe). Nu este nevoie de un blockchain global — rețeaua formează în mod firesc comunități cu suprapuneri în alte comunități.
>
> Algoritmul este nedeterminist: face hash documentului afirmației tale, mapează hash-ul pe o poziție de pe un inel al identităților cunoscute din acest cerc și o selectează pe cea mai apropiată drept candidat verificator. Nu poți prezice sau influența cine îți va verifica afirmația.

Fiecare respingere a unui verificator îți mărește documentul și îi crește costul de prelucrare — acesta este primul canal de cost (creșterea documentului). Fiecare verificator nou percepe o taxă bazată pe volumul de date, pe reputația ta și pe cât de departe se abate conținutul afirmației tale de la politica lui de verificare declarată — acesta este al doilea canal de cost (prima de risc). Iar fiecare iterație costă timp și energie — al treilea canal de cost.

> [!note] Ce verifică verificatorul, în ordine
> Odată selectat, un verificator evaluează o afirmație în aproximativ patru pași ordonați — filtrele cele mai ieftine întâi, verificările de conținut costisitoare la urmă:
>
> 1. **Filtrarea prin politică.** Intră acest tip de afirmație în ceea ce verificatorul verifică public, în general? Dacă nu, cererea este respinsă din capul locului.
> 2. **Încrederea în autoritate.** Este autoritatea care a girat afirmația suficient de demnă de încredere sub propria politică declarată a verificatorului? O autoritate sub pragul de încredere al verificatorului este motiv de respingere indiferent de conținutul afirmației.
> 3. **Reputația emitentului.** Îndeplinește emitentul pragurile de reputație pe care verificatorul le-a declarat pentru acest tip de afirmație? Reputația scăzută poate fie ridica taxa, fie declanșa respingerea.
> 4. **Verificarea conținutului.** Doar când primele trei porți sunt trecute, verificatorul evaluează afirmația însăși — semnături, consecvență internă, corectitudine formală și cât de departe se abate de la politica verificatorului. Taxa percepută pentru acest ultim pas reflectă riscul real asumat.
>
> Verificatorul publică politica ce guvernează fiecare dintre aceste porți, așa că pașii nu sunt la discreția lui — sunt legați de ce a declarat deja. Abaterea de la politica publicată este ea însăși o afirmație publicabilă împotriva lui, și o plătește cu reputația lui.

Rezultatul: publicarea unei afirmații credibile și utile costă aproape nimic. Publicarea unei afirmații radicale costă mai mult. Publicarea unei minciuni devine prohibitiv de scumpă — trebuie să treci prin verificator după verificator, iar fiecare care te respinge adaugă costuri. Piața pune preț pe afirmația ta, iar prețul îți spune unde te afli în raport cu comunitățile în care te miști.

Nu e de ajuns să declari că respecți o regulă când în realitate n-o respecți. În acel caz, DID-ul tău riscă publicarea unei înregistrări negative care demască ipocrizia — ceea ce te transformă într-un risc pentru toți ceilalți. Rezultatul ar trebui să fie reguli mai puține, dar mai consecvent respectate, și o curățare a acelei jungle de legi și reglementări în care abia se descurcă până și profesioniștii dreptului.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consens vs răspundere
> Pentru ca rețeaua să servească drept sursă valoroasă de informație, un DID nu ar trebui să fie prea radical — altfel ceilalți îl vor respinge. Presiunea socială va căuta echilibrul, iar încercările de a-l destabiliza vor fi probabil pedepsite.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Numărul de voturi nu este totuna cu greutatea unei voci
> Juraj Karpiš spune că „banii sunt memoria faptelor bune”. Aș adăuga că reputația este memoria celor rele.
>
> De aici rezultă că, meritocratic, cine contribuie mai mult și nu are reputație proastă merită o greutate mai mare a vocii în comunitate. Privind prin lentila relațiilor bilaterale: când cântăresc ce presiuni de consens să acomodez, cea mai mare greutate o au relațiile din care obțin cel mai mare beneficiu economic. Zece oameni cu care nu am schimburi active mă vor influența mult mai puțin decât un partener de afaceri permanent. Această paradigmă nu se limitează la comerț — se extinde la relațiile sociale, politice și de altă natură.
