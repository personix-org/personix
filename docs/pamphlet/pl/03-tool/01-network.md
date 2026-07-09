---
title: "Reputacyjna sieć społecznościowa"
chapter: 2
part: "Narzędzie"
lang: pl
version: v6
source: v1
---

# Reputacyjna sieć społecznościowa

Aby doprowadzić do zmiany, potrzebujemy starannie zaprojektowanego narzędzia. Najpierw naszkicujemy je pokrótce; w kolejnych rozdziałach przyjrzymy się każdemu elementowi dokładniej i dodamy więcej. Wyobraź sobie niecenzurowalną, globalną, zdecentralizowaną sieć społecznościową, w której mógłbyś bezpiecznie utworzyć swoją zastępczą tożsamość i nią zarządzać — tak zwaną tożsamość zdecentralizowaną (DID). DID to cyfrowa tożsamość, którą tworzysz i kontrolujesz sam, bez zależności od jakiejkolwiek centralnej władzy. Nikt nie może jej odebrać ani podrobić, ponieważ jest kryptograficznie podpisana twoim kluczem prywatnym (lub kluczami, poprzez multisig).

> [!note] Uwaga
> Jedną z implikacji jest to, że taka tożsamość mogłaby stopniowo zastąpić wydawane przez państwo dokumenty tożsamości — ale o tym więcej w rozdziale o przejściu.

![TWOJA TOŻSAMOŚĆ, TWOJE KLUCZE, TWOJE ZASADY](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

W takiej sieci mógłbyś zgłosić poprzez swoją tożsamość, że ktoś wyrządził ci krzywdę (a później, potencjalnie, że ją naprawił lub został do tego zmuszony). Aby ta informacja zwrotna — skierowana do sprawcy krzywdy — miała wartość jako istotne źródło, wprowadzenie informacji do sieci musi kosztować czas, energię i pieniądze — a na dodatek trzeba wytworzyć dla innych weryfikowalny dowód, że nie jest to czcza gadanina.

Czytanie informacji byłoby łatwe i stosunkowo tanie, ale utworzenie pojedynczego zapisu byłoby kosztowne i wymagające. Zapis podlegałby jasnemu protokołowi, w którym obliczenie według wybranego algorytmu ściśle wyznacza, którego DID poprosić o weryfikację przesłanej informacji i jak postępować, by wybrany uczestnik przetworzył informację w twoim imieniu, opublikował ją i stał się jej weryfikatorem.

> [!note] Algorytm kontra radykalizm
> Algorytmiczny wybór weryfikatorów zapewnia, że nieradykalni wydawcy informacji z czasem utrzymają niemal neutralny bilans między kosztami publikowanych informacji a nagrodami za weryfikację.

![PUBLIKACJA KOSZTUJE CZAS, ENERGIĘ I PIENIĄDZE](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Przyjrzyjmy się, jak algorytm wybiera weryfikatora.

> [!note] Algorytm
> Wybór algorytmiczny niedeterministycznie dobiera innego weryfikatora (lub zbiór możliwych weryfikatorów) dla różnych informacji. Hash (jednokierunkowa funkcja matematyczna, która z dowolnego wejścia wytwarza unikalny „odcisk” — jak odcisk palca dokumentu) kompletnego dokumentu DID wyznacza pozycję na spójnym pierścieniu haszującym i wybiera kandydatów na weryfikatorów.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Mówiąc prosto: algorytm bierze cały twój dokument DID, oblicza z niego odcisk, a ten odcisk wyznacza twojego weryfikatora.

![JAK ALGORYTM WYBIERA TWOJEGO WERYFIKATORA](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

U pierwszego weryfikatora, którego wybierze algorytm, ty jako wydawca możesz nie odnieść sukcesu — twoja reputacja albo deklarowane ustawienia mogą nie spełniać jego wymagań. Algorytmicznie kontynuowałbyś poszukiwania kolejnego, wykonując następną rekurencyjną iterację, która przydziela ci dalszego weryfikatora. Z każdym krokiem rośnie „odległość” do docelowego weryfikatora, a wraz z nią towarzyszące metadane, które trzeba opublikować. W miarę jak dane rosną, naturalnie rosną koszty (nie tylko z powodu początkowego rozmiaru tezy, ale i metadanych narastających z każdym odrzuceniem). Wiarygodna informacja przechodzi znacznie łatwiej niż bezsensowne kaprysy. Od każdego zależy, jak wysoką cenę jest gotów ponieść i jak bardzo zależy mu na zapisie — radykalizm z gwarancją zrobi się drogi.

![JAK ODPOWIADA WERYFIKATOR](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Cokolwiek weryfikator postanowi w odpowiedzi na twoje żądanie weryfikacji, piłka wraca na połowę wydawcy: może przyjąć ofertę weryfikatora na usługi weryfikacji, dołączyć odpowiedź do chronologii i spróbować ponownie (drożej) albo odejść i przełknąć poniesiony koszt.

![DECYZJA WYSTAWCY](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Aby nadać swojej informacji większą wagę i lepszą szansę na przyjęcie przez weryfikatorów, ty — jako wydawca zainteresowany wystawieniem informacji — mógłbyś skorzystać z usług **zaufanego autorytetu**. Autorytet albo odrzuca przesłaną informację, albo ją przyjmuje i stawia na nią swoje dobre imię (reputację). Autorytet zazwyczaj żąda dowodów ze świata rzeczywistego, weryfikuje je i klasyfikuje. Wynikiem jest protokół jego oceny danej sprawy w danym czasie. Wyobraź sobie autorytet jako specjalistę od pewnego rodzaju usług zarówno w świecie rzeczywistym, jak i cyfrowym — na przykład śledczego, audytora, ubezpieczyciela, dostawcę pewnej klasy towarów (w istocie dowolnego podmiotu gospodarczego na rynku).

![JAK POWSTAJE ZAPIS W SIECI](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Zanim spróbujesz opublikować informację w sieci, będzie ona już prawdopodobnie zawierać informacje o swoich uczestnikach — to sygnały reputacyjne. Poruszanie się po tym, jak czytać sygnały reputacyjne — co znaczą dla ciebie w różnych sytuacjach i jakie niosą ryzyka — może nie być trywialne. Każdy uczestnik może patrzeć na zapisy reputacyjne inaczej poprzez swój DID, zależnie od sytuacji, którą rozgrywa wobec drugiej strony. Czy druga strona jest rzetelnym płatnikiem, czy muszę zażądać pieniędzy z góry za transakcję handlową? Czy oferowany produkt nosi recenzje o ukrytym oszustwie lub wadach? Czy próbują wywinąć się od odpowiedzialności kontraktowej, gdy coś idzie nie tak? Czasem przydaje się bardziej złożony obraz ogólnej spójności drugiej strony — zależy to od preferencji tego, kto zamawia przegląd. Rynek mógłby oferować produkty i usługi, które upraszczają, przetwarzają i wyjaśniają odczyt reputacji w kontekście danej sytuacji. Do tego celu mogą służyć również różne autorytety i oferowane przez nie usługi.

![JAK CZYTA SIĘ REPUTACJĘ](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Przykłady
> Typowe informacje interesujące wydawców — i cenne dla innych — dotyczą zdarzeń wykraczających poza zwykłą komunikację międzyludzką w świecie rzeczywistym lub wirtualnym.
>
> Przykłady negatywne:
> - dowody czynów przestępczych (np. zaudytowane przez zaufany organ śledczy)
> - dowody poszlakowe (słabe same w sobie, ale statystycznie kumulatywne) — np. wielokrotna obecność w pobliżu kilku kradzieży w krótkim czasie → wciąż przypadek?
> - naruszenie umowy
>
> Przykłady pozytywne:
> - naprawiona krzywda (dobrowolnie lub pod presją wspólnoty jako kara)
> - przyjęcie i odbycie kary zaproponowanej przez autorytet X
> - autorytet X cofnął w pewnym zakresie uznanie praw własności sprawcy
>
> Od każdego zależy, by zebrać dostępne informacje o drugiej stronie i ocenić ryzyko według własnych preferencji.

![CO MOŻESZ ZAPISAĆ W SIECI?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] To, czy informacja o tobie pojawi się w sieci, zależy wyłącznie od twojego własnego zachowania.
> Nigdy nie musisz dołączać do takiej sieci, a mimo to informacja o tobie może się w niej pojawić. Zależy to wyłącznie od twoich czynów i wpływu, jaki mają na innych.

![WSPÓLNOTA MOŻE ZAŁOŻYĆ GO ZA CIEBIE](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

To, co przed chwilą pokrótce naszkicowałem, to sposób, w jaki mogłaby działać sieć społecznościowa zainspirowana tożsamością zdecentralizowaną (DID). Podstawowym celem koncepcji DID jest wzmocnienie prywatności i wolności poprzez zasadę subskrybowania reguł, których będę przestrzegać i według których będę żyć — dającej użytkownikom możliwość decydowania, jakie informacje udostępniać i na jakich warunkach.

Proponuję dalej połączyć DID w sieć komunikacyjną, w której ich posiadacze wymieniają informację zwrotną nawet poza sytuacjami, gdy coś się komuś stało i wspólnota lub jednostka musi zareagować. Takie prewencyjne porównywanie reguł, do których się zapisaliśmy — z możliwością obliczenia ekonomicznych i innych konsekwencji wzajemnych odchyleń w oczekiwaniach co do tego, jak druga strona powinna działać — można by uznać za motywację do znajdowania konsensusu. Zamiast wolności taki system kładłby nacisk na dobrowolne podejmowanie decyzji połączone z odpowiedzialnością za zachowanie w świecie rzeczywistym.

Jednostka nie jest w stanie złamać systemu sama — grupa ludzi ma większą szansę, a grupa ludzi z wynegocjowanym konsensusem i motywacjami, by w wielu kwestiach ciągnąć wspólnie, ma jeszcze większą szansę na oparcie się tendencjom autorytarnym. Warunek organizacji z pierwszego rozdziału zostanie spełniony, gdy zajdą dwa warunki: sieć reputacji DID obejmie wspólnoty na tyle reprezentatywnie, że jej używanie przestanie być egzotyczne. A jednocześnie ten segment wspólnoty stanie się ekonomicznie znaczącą mniejszością, która potrafi asertywnie negocjować z resztą społeczeństwa.

> [!note] Dobrowolność kontra wolność
> Wolność — w sensie pozytywnym — byłaby wtórnym efektem równoważenia dwóch czynników: dobrowolności i presji otoczenia ku odpowiedzialności.

> [!note] Era AI i wartość reputacji
> W erze sztucznej inteligencji automatyzowane jest wszystko, co związane z myśleniem poznawczym — i może to pójść jeszcze dalej. Co wtedy pozostaje w ludzkiej aktywności jako przewaga konkurencyjna? Odpowiedź jest trudna i coś na pewno się znajdzie, ale jedno możemy powiedzieć z pewnością: zadecyduje reputacja. Weryfikowalna historia twojego zachowania, twoich zobowiązań i ich wypełnienia — tego AI za ciebie nie zbuduje.

![AI NIE ZBUDUJE TWOJEJ REPUTACJI — TYLKO TY](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![EKONOMIA PRAWDY](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
