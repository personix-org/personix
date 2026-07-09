---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konszenzus és az ellenőrzési folyamat

Ahhoz, hogy konszenzus épüljön arról, mely szabályokat kellene egy társadalomnak átlagosan betartania és érvényesítenie, a következő mechanizmus segíthet. DID-résztvevőként bejelentem azokat a szabályokat, amelyekre aláiratkozom és amelyek szerint élni fogok, és közzéteszem őket. (Gondolj rá úgy, mint az alapszabályra és a statútumokra, amelyek az én nézetem szerint az ideális világomat alkotják — egy világot, amelyben nem korlátozottnak, hanem biztonságban érzem magam.)

Előre megbecsülhetem, hogyan reagálnának a DID-kapcsolataim — és felmérhetem, milyen erősen és ki által lennék szankcionálva a szokásos társadalmi vagy üzleti interakciókban, ha azok hipotetikusan bekövetkeznének.

A végleges kiértékelés akkor történik, amikor információt kérsz egy másik DID-től, vagy megkéred egy állítás ellenőrzésére (vagy egy autoritástól szolgáltatást kérsz, és így tovább), amelyet közzé akarsz tenni a reputációs hálózatban. Ugyanúgy kellene végződnie, mint amikor magad futtatod le a kiértékelést, próbafutásban, az ellenfél deklarált elveivel szemben — és ha nem így van, akkor valami baj van az ellenfél oldalán: tisztességtelen játékot próbál játszani.

A kimenet vagy elfogadás, az ellenőrzésre adott árajánlattal (ellenőrző- vagy autoritásszolgáltatások esetén), vagy elutasítás. Az értékelő elveitől való eltérés szankciói és bónuszai egyaránt beépülnek az árajánlatba. A kérelmező ezután eldönti, elfogadja-e a feltételeket, vagy továbblép az elosztási algoritmus következő ellenőrzési fordulójára — addig ismételve a folyamatot, amíg elégedett nem lesz, vagy amíg a gazdasági logika értelmetlenné nem teszi a folytatást.

> [!note] A közösségi gráf
> A reputációs hálózat mindenekelőtt közösségi hálózat. Kapcsolatokat adsz hozzá — embereket, akik beleegyeznek a kapcsolatba. Nekik is vannak kapcsolataik, azoknak a kapcsolatoknak pedig további kapcsolataik. Az algoritmus egy konfigurálható mélységen belül keres ellenőrzőket (pl. három szint: a közvetlen kapcsolataid, azok kapcsolatai és egy szinttel tovább). Nincs szükség globális blockchainre — a hálózat természetesen közösségeket formál, más közösségekbe való átfedésekkel.
>
> Az algoritmus nemdeterminisztikus: hasheli az állításdokumentumodat, a hasht egy pozícióhoz rendeli az ismert identitások gyűrűjén ezen a körön belül, és a legközelebbit választja ellenőrzőjelöltnek. Nem tudod megjósolni vagy befolyásolni, ki fogja ellenőrizni az állításodat.

Minden ellenőrző elutasítása megnöveli a dokumentumodat és növeli a feldolgozási költségét — ez az első költségcsatorna (a dokumentum növekedése). Minden új ellenőrző díjat számít fel az adatmennyiség, a reputációd, valamint annak alapján, hogy az állításod tartalma mennyire tér el a deklarált ellenőrzési elveitől — ez a második költségcsatorna (kockázati felár). És minden iteráció időbe és energiába kerül — ez a harmadik költségcsatorna.

> [!note] Mit ellenőriz az ellenőrző, sorrendben
> A kiválasztás után az ellenőrző nagyjából négy sorrendbe rendezett lépésben értékel egy állítást — először a legolcsóbb szűrők, végül a drága tartalmi ellenőrzések:
>
> 1. **Elvi kapuzás.** Ez a fajta állítás egyáltalán beleesik-e abba, amit az ellenőrző nyilvánosan ellenőriz? Ha nem, a kérést azonnal elutasítja.
> 2. **Autoritásbizalom.** Az állítást jóváhagyó autoritás elég megbízható-e az ellenőrző saját deklarált elvei szerint? Az ellenőrző bizalmi küszöbe alatti autoritás az állítás tartalmától függetlenül elutasítási ok.
> 3. **Kibocsátói reputáció.** A kibocsátó megfelel-e azoknak a reputációs küszöböknek, amelyeket az ellenőrző az ilyen típusú állításra deklarált? Az alacsony reputáció vagy megemelheti a díjat, vagy elutasítást válthat ki.
> 4. **Tartalmi ellenőrzés.** Csak amikor az első három kapu átmegy, értékeli az ellenőrző magát az állítást — aláírásokat, belső konzisztenciát, formai helyességet, valamint azt, mennyire tér el az ellenőrző elveitől. Az ezért az utolsó lépésért felszámított díj a ténylegesen vállalt kockázatot tükrözi.
>
> Az ellenőrző közzéteszi az egyes kapukat szabályozó elveket, így a lépések nem az ő diszkréciójától függnek — azt kötik őt, amit már deklarált. A közzétett elvektől való eltérés maga is közzétehető állítás ellene, és a reputációjával fizet érte.

Az eredmény: egy hiteles és hasznos állítás közzététele szinte semmibe sem kerül. Egy radikális állítás közzététele többe. Egy hazugság közzététele elrettentően drágává válik — ellenőrzőről ellenőrzőre kell iterálnod, és mindenki, aki elutasít, hozzáad a költséghez. A piac beárazza az állításodat, és az ár megmondja, hol állsz azokhoz a közösségekhez képest, amelyekben mozogsz.

Nem elég bejelenteni, hogy betartasz egy szabályt, amikor valójában nem. Ebben az esetben a DID-ed egy olyan negatív bejegyzés közzétételét kockáztatja, amely leleplezi a képmutatást — ami kockázattá tesz téged mindenki más számára. Az eredmény kevesebb, de következetesebben betartott szabály legyen, valamint a törvények és rendeletek azon dzsungelének kitisztítása, amelyben még a jogi szakemberek is alig igazodnak el.

![A KÉPMUTATÁS A LEGDRÁGÁBB VISELKEDÉS](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konszenzus kontra elszámoltathatóság
> Ahhoz, hogy a hálózat értékes információforrásként szolgáljon, egy DID ne legyen túl radikális — különben a többiek elutasítják. A társadalmi nyomás egyensúlyt keres, és a destabilizálására tett kísérleteket valószínűleg megbüntetik.

![DEKLARÁLD A SZABÁLYAIDAT, FIZESD MEG AZ ÁRAT](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] A szavazatok száma nem ugyanaz, mint egy hang súlya
> Juraj Karpiš azt mondja, hogy „a pénz a jó cselekedetek emlékezete". Én hozzátenném, hogy a reputáció a rosszaké.
>
> Ebből következik, hogy meritokratikusan az, aki többel járul hozzá és nincs rossz reputációja, nagyobb hangsúlyt érdemel a közösségben. A kétoldalú kapcsolatok szemüvegén át nézve: amikor mérlegelem, mely konszenzusnyomásoknak engedjek, a legnagyobb súly azoknak a kapcsolatoknak jut, amelyekből a legnagyobb gazdasági hasznot húzom. Tíz ember, akikkel nincs aktív kereskedelmem, sokkal kevésbé befolyásol, mint egyetlen állandó üzleti partner. Ez a paradigma nem korlátozódik a kereskedelemre — kiterjed a társadalmi, politikai és egyéb kapcsolatokra is.
