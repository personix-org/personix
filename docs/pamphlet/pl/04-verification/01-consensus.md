---
title: "Konsensus i proces weryfikacji"
chapter: 3
part: "Jak działa weryfikacja"
lang: pl
version: v6
source: v1
---

# Konsensus i proces weryfikacji

Aby zbudować konsensus co do tego, jakie reguły społeczeństwo powinno średnio podtrzymywać i egzekwować, może pomóc następujący mechanizm. Jako uczestnik DID deklaruję reguły, do których się zapisuję i według których będę żyć, i publikuję je. (Wyobraź je sobie jako regulamin i statut, które w moim odczuciu składają się na mój idealny świat — świat, w którym nie czuję się ograniczony, lecz bezpieczny.)

Mogę z góry oszacować, jak zareagowaliby moi kontaktowi DID — i ocenić, jak mocno i przez kogo zostałbym ukarany w zwykłych interakcjach społecznych czy biznesowych, gdyby hipotetycznie do nich doszło.

Ostateczna ocena następuje, gdy żądasz informacji od innego DID albo prosisz go o weryfikację tezy (albo prosisz autorytet o usługę itd.), którą chcesz opublikować do sieci reputacji. Powinno to wypaść tak samo, jak wtedy, gdy sam przeprowadzasz ocenę na sucho względem deklarowanej polityki drugiej strony — a jeśli tak nie jest, coś jest nie tak po stronie drugiej strony: próbuje grać w nieuczciwą grę.

Wynikiem jest albo przyjęcie, z podaną ceną za weryfikację (w przypadku usług weryfikatora lub autorytetu), albo odrzucenie. Zarówno sankcje, jak i premie za odchylenie od polityki oceniającego są wliczone w podaną cenę. Wnioskujący następnie decyduje, czy przyjąć warunki, czy przejść do kolejnej rundy weryfikacji w algorytmie przydziału — powtarzając proces, aż będzie zadowolony albo aż ekonomia sprawi, że dalsze kontynuowanie stanie się bezcelowe.

> [!note] Graf społeczny
> Sieć reputacji jest przede wszystkim siecią społecznościową. Dodajesz kontakty — ludzi, którzy zgadzają się na połączenie. Oni mają kontakty, a tamte kontakty mają kontakty. Algorytm szuka weryfikatorów w konfigurowalnej głębokości (np. trzy poziomy: twoje bezpośrednie kontakty, ich kontakty i jeden poziom dalej). Nie jest potrzebny żaden globalny blockchain — sieć naturalnie tworzy wspólnoty z zazębieniami w inne wspólnoty.
>
> Algorytm jest niedeterministyczny: hashuje twój dokument tezy, mapuje hash na pozycję na pierścieniu znanych tożsamości w obrębie tego kręgu i wybiera najbliższą jako kandydata na weryfikatora. Nie możesz przewidzieć ani wpłynąć na to, kto zweryfikuje twoją tezę.

Każde odrzucenie przez weryfikatora powiększa twój dokument i zwiększa koszt jego przetworzenia — to pierwszy kanał kosztowy (wzrost dokumentu). Każdy nowy weryfikator pobiera opłatę zależną od wolumenu danych, twojej reputacji i tego, jak daleko treść twojej tezy odchyla się od jego deklarowanej polityki weryfikacyjnej — to drugi kanał kosztowy (premia za ryzyko). A każda iteracja kosztuje czas i energię — to trzeci kanał kosztowy.

> [!note] Co sprawdza weryfikator i w jakiej kolejności
> Po wybraniu weryfikator ocenia tezę w mniej więcej czterech uporządkowanych krokach — najpierw najtańsze filtry, na końcu drogie sprawdzanie treści:
>
> 1. **Bramka polityki.** Czy ten rodzaj tezy w ogóle mieści się w tym, co weryfikator publicznie weryfikuje? Jeśli nie, żądanie zostaje od razu odrzucone.
> 2. **Zaufanie do autorytetu.** Czy autorytet, który poręczył tezę, jest wystarczająco zaufany według własnej deklarowanej polityki weryfikatora? Autorytet poniżej progu zaufania weryfikatora jest podstawą do odrzucenia niezależnie od treści tezy.
> 3. **Reputacja wystawcy.** Czy wystawca spełnia progi reputacji, które weryfikator zadeklarował dla tego typu tezy? Niska reputacja może albo podnieść opłatę, albo wywołać odrzucenie.
> 4. **Sprawdzenie treści.** Dopiero gdy przejdą pierwsze trzy bramki, weryfikator ocenia samą tezę — podpisy, wewnętrzną spójność, poprawność formalną i to, jak daleko odchyla się od polityki weryfikatora. Opłata pobierana za ten ostatni krok odzwierciedla faktycznie podjęte ryzyko.
>
> Weryfikator publikuje politykę, która rządzi każdą z tych bramek, więc kroki nie są kwestią jego uznania — jest związany tym, co już zadeklarował. Odchylenie od opublikowanej polityki samo w sobie jest tezą, którą można opublikować przeciw niemu, a płaci za nie swoją reputacją.

Rezultat: opublikowanie wiarygodnej i użytecznej tezy kosztuje niemal nic. Opublikowanie tezy radykalnej kosztuje więcej. Opublikowanie kłamstwa staje się zaporowo drogie — musisz iterować przez weryfikatora za weryfikatorem, a każdy, kto cię odrzuca, dokłada kosztów. Rynek wycenia twoją tezę, a cena mówi ci, gdzie stoisz względem wspólnot, w których się poruszasz.

Nie wystarczy zadeklarować, że przestrzegasz reguły, gdy w rzeczywistości tego nie robisz. W takim przypadku twój DID ryzykuje publikację negatywnego zapisu odsłaniającego obłudę — co czyni cię ryzykiem dla wszystkich innych. Rezultatem powinno być mniej reguł, ale konsekwentniej przestrzeganych, oraz oczyszczenie tej dżungli praw i przepisów, po której nawet prawnicy z trudem się poruszają.

![OBŁUDA TO NAJDROŻSZE ZACHOWANIE](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus kontra rozliczalność
> Aby sieć służyła jako wartościowe źródło informacji, DID nie powinien być zbyt radykalny — inaczej pozostali go odrzucą. Presja społeczna będzie szukać równowagi, a próby jej destabilizacji będą prawdopodobnie karane.

![ZADEKLARUJ SWOJE REGUŁY, ZAPŁAĆ CENĘ](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Liczba głosów to nie to samo co waga głosu
> Juraj Karpiš mówi, że „pieniądze są pamięcią dobrych uczynków”. Dodałbym, że reputacja jest pamięcią tych złych.
>
> Wynika z tego, że merytokratycznie ten, kto wnosi więcej i nie ma złej reputacji, zasługuje na większą wagę głosu we wspólnocie. Patrząc przez pryzmat relacji dwustronnych: gdy ważę, którym naciskom konsensusu ustąpić, największą wagę mają relacje, z których czerpię największą korzyść ekonomiczną. Dziesięciu ludzi, z którymi nie prowadzę żadnego aktywnego handlu, wpłynie na mnie znacznie mniej niż jeden stały partner biznesowy. Ten paradygmat nie ogranicza się do handlu — rozciąga się na relacje społeczne, polityczne i inne.
