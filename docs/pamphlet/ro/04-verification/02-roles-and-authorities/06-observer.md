---
title: "Observatorul"
chapter: 3
part: "Cum funcționează verificarea"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observatorul

Rolul de observator îndepărtează stimulentul verificatorului de a încălca regulile. În situațiile în care unui verificator nu-i place cererea emitentului sau a autorității, el ar putea pur și simplu să tacă — să nu răspundă și să blocheze secvența algoritmică. Observatorul — sau un set de observatori — își pune reputația în joc pentru a documenta cum a fost interogat verificatorul. Dacă verificatorul tace în ciuda unei politici declarate care spune altceva, poate fi condamnat pentru încălcarea protocolului.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mecanismul: marca de timp și codul de provocare

Înainte să trimiți o afirmație verificatorului, o direcționezi prin observatori — oameni în care ai încredere sau furnizori specializați de servicii de observare care percep o mică taxă. Fiecare observator îți primește transmisia, îi pune o marcă de timp, semnează că a văzut-o plecând și generează un cod de provocare — un hash criptografic al semnăturii lui. Codurile sunt adăugate la cererea ta. Verificatorul le vede, dar nu are nicio idee cine sunt observatorii sau dacă codurile sunt măcar reale. Observatorii acționează astfel ca proxy între emitent și verificator, ținând o evidență independentă că afirmația a fost transmisă și ce conținea. Pot fi de la zero la N.

Când verificatorul se comportă cinstit — acceptând sau respingând în acord cu politica lui declarată — codurile rămân opace. Nimeni nu este expus.

Dar dacă verificatorul tace în ciuda unei politici primitoare sau răspunde într-un fel care contrazice ce a publicat, tu deții semnăturile originale ale observatorilor. Le poți publica drept mărturie prin proxy că afirmația a fost transmisă și că verificatorul nu a respectat protocolul. Oricine poate verifica faptul că semnăturile corespund codurilor de provocare.

## Poanta: nu ai nevoie de observatori reali

Și aici e partea cea mai elegantă: **nu ai nevoie deloc de observatori reali.** Poți genera numere aleatorii care arată exact ca niște coduri de provocare. Verificatorul nu poate face diferența — trebuie să arunce zarurile decizând dacă își riscă reputația. În spatele fiecărei cereri pe care o primește ar putea fi un observator respectat care privește incognito — sau ar putea fi pur zgomot. Verificatorul nu știe. Iar acea incertitudine este mecanismul.

Costul menținerii presiunii oneste: aproape zero (numerele aleatorii sunt gratis). Costul potențial al necinstei pentru verificator: catastrofal. Comportamentul cinstit este stimulat chiar și când nimeni nu privește de fapt.

Sistemul funcționează pentru că fiecare este un pic paranoic. Incertitudinea este mai ieftină decât supravegherea.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Mai mulți verificatori într-o singură iterație
> O regulă însoțitoare de întărire pentru disponibilitatea verificatorilor poate fi o extensie algoritmică ce returnează, într-o singură iterație, un set de verificatori candidați, nu doar unul.
