---
title: "Konsenzus a proces overovania"
chapter: 3
part: "Ako funguje overovanie"
lang: en
version: v6
source: v1
---

# Konsenzus a proces overovania

Pri budovaní konsenzu o tom, ktoré pravidlá by mala spoločnosť v priemere dodržiavať a vymáhať, môže pomôcť nasledujúci mechanizmus. Ako účastník DID deklarujem pravidlá, ku ktorým sa hlásim a podľa ktorých budem žiť, a zverejním ich. (Predstav si to ako stanovy a poriadky, ktoré podľa mňa tvoria môj ideálny svet — svet, kde sa necítim obmedzený, ale bezpečne.)

Vopred si viem odhadnúť, ako by moje DID kontakty zareagovali — a posúdiť, ako silno a kým by som bol sankcionovaný v bežných spoločenských či obchodných interakciách, keby k nim hypoteticky došlo.

Definitívne vyhodnotenie prebehne, keď si vyžiadaš informáciu od iného DID alebo ho požiadaš o overenie tvrdenia (prípadne požiadaš autoritu o službu a podobne), ktoré chceš zverejniť do reputačnej siete. Malo by to dopadnúť rovnako, ako keď si vyhodnotenie spustíš sám nanečisto oproti deklarovanej politike protistrany — a ak nie, niečo je na strane protistrany zle: pokúša sa hrať nečestnú hru.

Výsledkom je buď prijatie s vyčíslenou cenou za overenie (v prípade služieb overovateľa alebo autority), alebo zamietnutie. Sankcie aj bonusy za odchýlku od politiky vyhodnocovateľa sú zapracované do vyčíslenej ceny. Žiadateľ potom rozhodne, či prijme podmienky, alebo prejde na ďalšie kolo overovania v alokačnom algoritme — a proces opakuje, kým nie je spokojný, alebo kým ekonomika nespraví ďalšie pokračovanie nezmyselným.

> [!note] Sociálny graf
> Reputačná sieť je v prvom rade sociálna sieť. Pridávaš si kontakty — ľudí, ktorí so spojením súhlasia. Oni majú kontakty a tie kontakty majú kontakty. Algoritmus hľadá overovateľov do konfigurovateľnej hĺbky (napr. tri úrovne: tvoje priame kontakty, ich kontakty a jednu úroveň za nimi). Nie je potrebný žiadny globálny blockchain — sieť prirodzene tvorí komunity s presahmi do iných komunít.
>
> Algoritmus je nedeterministický: zhashuje tvoj dokument s tvrdením, namapuje hash na pozíciu na ringu známych identít v tomto okruhu a vyberie najbližšiu ako kandidáta na overovateľa. Nemôžeš predpovedať ani ovplyvniť, kto tvoje tvrdenie overí.

Každé zamietnutie overovateľa zväčšuje tvoj dokument a zvyšuje náklady na jeho spracovanie — to je prvý nákladový kanál (rast dokumentu). Každý nový overovateľ účtuje poplatok podľa objemu dát, tvojej reputácie a toho, ako ďaleko sa obsah tvojho tvrdenia odchyľuje od jeho deklarovanej overovacej politiky — to je druhý nákladový kanál (riziková prirážka). A každá iterácia stojí čas a energiu — tretí nákladový kanál.

> [!note] Čo overovateľ kontroluje, v poradí
> Po výbere vyhodnocuje overovateľ tvrdenie v zhruba štyroch usporiadaných krokoch — najlacnejšie filtre najprv, drahé kontroly obsahu naposledy:
>
> 1. **Filtrovanie politikou.** Spadá tento druh tvrdenia vôbec do toho, čo overovateľ verejne overuje? Ak nie, žiadosť je rovno zamietnutá.
> 2. **Dôvera k autorite.** Je autorita, ktorá tvrdenie zaštítila, dostatočne dôveryhodná podľa vlastnej deklarovanej politiky overovateľa? Autorita pod prahom dôvery overovateľa je dôvodom na zamietnutie bez ohľadu na obsah tvrdenia.
> 3. **Reputácia vydavateľa.** Spĺňa vydavateľ reputačné prahy, ktoré overovateľ deklaroval pre tento typ tvrdenia? Nízka reputácia môže buď zvýšiť poplatok, alebo spustiť zamietnutie.
> 4. **Kontrola obsahu.** Až keď prejdú prvé tri brány, overovateľ vyhodnotí samotné tvrdenie — podpisy, vnútornú konzistentnosť, formálnu správnosť a to, ako ďaleko sa odchyľuje od politiky overovateľa. Poplatok účtovaný za tento posledný krok odzrkadľuje skutočne podstúpené riziko.
>
> Overovateľ zverejňuje politiku, ktorá riadi každú z týchto brán, takže kroky nie sú na jeho ľubovôli — je viazaný tým, čo už deklaroval. Odchýlka od zverejnenej politiky je sama zverejniteľným tvrdením proti nemu a platí za ňu svojou reputáciou.

Výsledok: zverejnenie dôveryhodného a užitočného tvrdenia nestojí takmer nič. Zverejnenie radikálneho tvrdenia stojí viac. Zverejnenie lži sa stáva neúnosne drahým — musíš iterovať cez overovateľa za overovateľom a každý, kto ťa zamietne, pridáva náklady. Trh ocení tvoje tvrdenie a cena ti povie, kde stojíš vo vzťahu ku komunitám, v ktorých sa pohybuješ.

Nestačí deklarovať, že dodržiavaš pravidlo, keď ho v skutočnosti nedodržiavaš. V takom prípade tvoj DID riskuje zverejnenie negatívneho záznamu odhaľujúceho pokrytectvo — ktorý ťa robí rizikom pre všetkých ostatných. Výsledkom by malo byť menej, ale dôslednejšie dodržiavaných pravidiel a vyčistenie tej džungle zákonov a predpisov, v ktorej sa sotva vyznajú aj právni profesionáli.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsenzus vs zodpovednosť
> Aby sieť slúžila ako cenný zdroj informácií, nemal by byť DID príliš radikálny — inak ho ostatní zamietnu. Sociálny tlak bude hľadať rovnováhu a pokusy o jej rozkolísanie budú pravdepodobne potrestané.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Počet hlasov nie je to isté ako váha hlasu
> Juraj Karpiš hovorí, že „peniaze sú pamäťou dobrých skutkov.“ Ja by som dodal, že reputácia je pamäťou tých zlých.
>
> Z toho vyplýva, že meritokraticky si ten, kto prispieva viac a nemá zlú reputáciu, zaslúži väčšiu váhu hlasu v komunite. Cez optiku obojstranných vzťahov: keď zvažujem, ktorým konsenzuálnym tlakom vyhovieť, najväčšia váha patrí vzťahom, z ktorých mám najväčší ekonomický prospech. Desať ľudí, s ktorými nemám žiadny aktívny obchod, ma ovplyvní oveľa menej ako jeden stály obchodný partner. Táto paradigma sa neobmedzuje na obchod — rozširuje sa na sociálne, politické a iné vzťahy.
