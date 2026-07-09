---
title: "Verificatorul"
chapter: 3
part: "Cum funcționează verificarea"
lang: en
version: v6
---

# Verificatorul

Orice DID poate acționa ca verificator, fie direct, fie prin drepturi de verificare delegate unui al treilea DID. Pentru ca eu — sau delegatul meu — să pot verifica, ar trebui să fiu accesibil în rețea (online). Nu toată lumea va vrea să se angajeze la asta, motiv pentru care o înregistrare DID poate lista, în ordinea priorității, înlocuitorii care vor îndeplini funcția în numele ei cât timp este offline.

Fiecare DID activ în rețea își declară public propria politică. Prin regulile definite în acea politică el judecă, pe durata procesului de verificare, reputația părții adverse și conținutul și forma afirmației pe care emitentul a marcat-o pentru publicare în rețeaua de reputație. Parte din politică este formula de calcul folosită pentru a calcula taxele pentru serviciile de verificare. Odată ce e stabilită, atunci pe un număr statistic mare de afirmații care curg prin rețea aștept ca algoritmul rețelei să mă tragă de partea emitentului și să mă atribuie, într-o iterație dată, verificării informației emise. Emitentul poate calcula dinainte cum ar reacționa un verificator care se comportă corect, dar nu poate evita să-l contacteze efectiv (pe el sau pe înlocuitorii lui); iterația cu verificatorul selectat trebuie parcursă de emitent chiar și atunci când știe dinainte că nu va trece.

De unde știm că emitentul rulează algoritmul de selecție a verificatorului pe setul corect de DID-uri candidate de verificatori? Împreună cu politica sa declarată public, fiecare DID publică și lista curentă de identificatori ai rețelei sale sociale din interiorul rețelei de reputație. Dacă un emitent își definește rețeaua socială ca pe o bulă socială care doar îi ecouă și îi întărește propriile păreri, informația publicată prin ea cu greu va fi primită mai larg de alte comunități. Faptul că reușesc, cu mari costuri, să împing o afirmație radicală în rețea nu implică faptul că, judecând reputația părții adverse, îi voi acorda vreo greutate. Unele afirmații sunt împins de comunitatea mea să le iau în seamă (sentințe și restricții impuse făptașilor); altele îmi rămân în întregime la latitudine — decid singur valoarea economică a includerii sau excluderii unei anumite informații.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
