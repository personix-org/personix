---
title: "Weryfikator"
chapter: 3
part: "Jak działa weryfikacja"
lang: pl
version: v6
---

# Weryfikator

Każdy DID może działać jako weryfikator, bezpośrednio albo poprzez prawa weryfikacji delegowane na trzeci DID. Abym ja — lub mój delegat — mógł weryfikować, powinienem być osiągalny w sieci (online). Nie każdy będzie chciał się do tego zobowiązać, dlatego zapis DID może wymienić, w kolejności priorytetu, zastępców, którzy będą pełnić tę funkcję w jego imieniu, gdy jest offline.

Każdy DID aktywny w sieci publicznie deklaruje własną politykę. Poprzez reguły określone w tej polityce ocenia podczas procesu weryfikacji reputację drugiej strony oraz treść i formę tezy, którą wystawca oznaczył do publikacji w sieci reputacji. Częścią polityki jest wzór obliczeniowy używany do wyliczania opłat za usługi weryfikacji. Gdy to jest gotowe, wtedy w statystycznie dużej liczbie tez przepływających przez sieć czekam, aż algorytm sieci wylosuje mnie po stronie wystawcy i przydzieli mi, w danej iteracji, weryfikację wystawianej informacji. Wystawca może z góry obliczyć, jak zareagowałby poprawnie zachowujący się weryfikator, ale nie może uniknąć faktycznego skontaktowania się z nim (lub jego zastępcami); iterację z wybranym weryfikatorem wystawca musi przeprowadzić nawet wtedy, gdy z góry wie, że nie przejdzie.

Skąd wiemy, że wystawca uruchamia algorytm wyboru weryfikatora na właściwym zbiorze kandydackich DID weryfikatorów? Wraz z publicznie zadeklarowaną polityką każdy DID publikuje też aktualną listę identyfikatorów swojej sieci społecznościowej w obrębie sieci reputacji. Jeśli wystawca definiuje swoją sieć społecznościową jako bańkę społeczną, która jedynie powiela i wzmacnia jego własne poglądy, opublikowana przez nią informacja z trudem zostanie szerzej przyjęta przez inne wspólnoty. To, że udaje mi się wysokim kosztem przepchnąć radykalną tezę do sieci, nie oznacza, że oceniając reputację drugiej strony, nadam jej jakąkolwiek wagę. Niektóre tezy jestem popychany przez moją wspólnotę, by je uwzględnić (wyroki i ograniczenia nałożone na sprawców); inne zależą wyłącznie ode mnie — sam decyduję o ekonomicznej wartości włączenia lub wyłączenia danej informacji.

![WERYFIKATOR — WYBRANY PRZEZ ALGORYTM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
