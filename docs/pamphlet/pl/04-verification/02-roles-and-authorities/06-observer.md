---
title: "Obserwator"
chapter: 3
part: "Jak działa weryfikacja"
lang: pl
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Obserwator

Rola obserwatora odbiera weryfikatorowi bodziec do naginania reguł. W sytuacjach, gdy weryfikatorowi nie podoba się żądanie wystawcy lub autorytetu, mógłby po prostu milczeć — nie odpowiadać i zablokować algorytmiczną sekwencję. Obserwator — lub zbiór obserwatorów — stawia swoją reputację na udokumentowaniu tego, jak weryfikator został zapytany. Jeśli weryfikator milczy mimo zadeklarowanej polityki mówiącej co innego, można go skazać za naruszenie protokołu.

![OBSERWATOR — PROWADZI ZAPIS O WERYFIKATORZE](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mechanizm: znacznik czasu i kod wyzwania

Zanim wyślesz tezę do weryfikatora, przepuszczasz ją przez obserwatorów — ludzi, którym ufasz, albo wyspecjalizowanych dostawców usług obserwatorskich pobierających niewielką opłatę. Każdy obserwator otrzymuje twoje zgłoszenie, opatruje je znacznikiem czasu, podpisuje, że widział jego wysłanie, i generuje kod wyzwania — kryptograficzny hash swojego podpisu. Kody są dołączane do twojego żądania. Weryfikator je widzi, ale nie ma pojęcia, kim są obserwatorzy ani czy kody są w ogóle prawdziwe. Obserwatorzy działają więc jako pośrednicy między wystawcą a weryfikatorem, trzymając niezależny zapis, że teza została złożona i co zawierała. Może ich być od zera do N.

Gdy weryfikator zachowuje się uczciwie — przyjmując lub odrzucając zgodnie z zadeklarowaną polityką — kody pozostają nieprzejrzyste. Nikt nie zostaje odsłonięty.

Ale jeśli weryfikator milczy mimo przychylnej polityki albo odpowiada w sposób sprzeczny z tym, co opublikował, ty trzymasz oryginalne podpisy obserwatorów. Możesz je opublikować jako pośrednie świadectwo, że teza została złożona i że weryfikator nie zastosował się do protokołu. Każdy może sprawdzić, że podpisy pasują do kodów wyzwania.

## Puenta: nie potrzebujesz prawdziwych obserwatorów

I tu najbardziej elegancka część: **wcale nie potrzebujesz prawdziwych obserwatorów.** Możesz wygenerować liczby losowe, które wyglądają dokładnie jak kody wyzwania. Weryfikator nie odróżni jednego od drugiego — musi rzucić kością, czy zaryzykować swoją reputację. Za każdym otrzymanym żądaniem mógłby czuwać incognito szanowany obserwator — albo mógłby to być czysty szum. Weryfikator nie wie. I ta niepewność jest właśnie mechanizmem.

Koszt utrzymywania uczciwej presji: niemal zero (liczby losowe są darmowe). Potencjalny koszt nieuczciwości dla weryfikatora: katastrofalny. Uczciwe zachowanie jest premiowane nawet wtedy, gdy tak naprawdę nikt nie patrzy.

System działa, bo każdy jest odrobinę paranoiczny. Niepewność jest tańsza niż inwigilacja.

![BLEF, KTÓRY TRZYMA WERYFIKATORA W RYZACH](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Wielu weryfikatorów w jednej iteracji
> Wzmacniającą regułą towarzyszącą dla dostępności weryfikatorów może być rozszerzenie algorytmu zwracające w jednej iteracji zbiór kandydatów na weryfikatorów, a nie tylko jednego.
