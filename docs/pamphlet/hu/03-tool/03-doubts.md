---
title: "Addressing Obvious Doubts"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: "v1 callouts extended in v4"
---

# Kézenfekvő kételyek eloszlatása

A leírt rendszer természetesen számos kérdést vet fel. Vegyük sorra a leggyakoribbakat.

## Technológiafüggőség

Valószínűleg már észrevetted, hogy a modern állammal ellentétben — amely mintegy 150 éve van velünk — az itt leírt reputációs hálózati megoldás erősen függ a globális/lokális internet technológiájától. Kimaradás esetén egy ilyen hálózat működése veszélybe kerül.

Ha a kimaradás átmeneti, nincs adatvesztés, sem a hálózatbeli állítások konzisztenciájának sérülése, és a közösségeken belül elért reputációs egyenlegeknek sem szabad megbomlaniuk. A hasonló fizetési hálózatokkal ellentétben ez a hálózat nagyon alacsony folyamat- és adatgyakoriságot feltételez. Ebben a tekintetben a decentralizált reputációs hálózat nem különbözik a mai államtól, amely szintén erősen függ a technológiától, és elfelejtett papíralapú kartotékrendszerrel dolgozni (bár válságtervekben nem lenne más választása).

Az állam evolúciós utódja reputációs hálózat formájában tartós kimaradás esetén (példátlan léptékű katasztrófa) visszaeshet egy primitívebb, centralizált rendszerre — az államra.

A technológia lehetővé teszi, hogy az emberiség magasabb civilizációs kormányzási formákat érjen el, és előnyöket hoz nekünk, de kockázatokat is.

## Kidobom-e az ablakon a pénzem, ha közzéteszek a hálózatban?

Egy állítás reputációs hálózatban való közzétételének költségei nagyrészt nem süllyednek el. Egy közzétevő hálózatba juttatott üzenetének hasznossága — valós sérelmekről szóló információ, ellenőrzött tapasztalatok, releváns figyelmeztetések — statisztikailag hosszabb távon megtérül a közösségből érkező mások állításainak ellenőrzéséért járó díjak formájában. A közösség profitál, a közzétevő reputációt épít, és az igaz információ közzétételének költsége így egy visszatéríthető letéthez közelít, amelyből csak a tényleges hálózatfenntartási költségek kisebb részét kell levonni. Ezzel szemben a valótlan vagy jelentéktelen bejegyzések nem térülnek meg — a költségük tiszta veszteség. A becsületesség tehát nemcsak erkölcsi választás, hanem gazdaságilag racionális stratégia is.

A hálózatfenntartási költségek levonása után ezt az elvet a gazdasági semlegesség elvének nevezhetnénk — nem veszítek, amikor a közösséggel vagyok, veszítek, amikor ellene.

A közösségnek szolidaritási csatornái is vannak arra, hogy megbecsülje tagjainak becsületes hozzáállását. De ne legyenek illúzióink: a szolidaritásra való hivatkozás többnyire a közösségi társadalmi nyomásból fakad, így ez nem feltétlenül szolidaritás a szó önkéntes értelmében.

## Mi van, ha valaki több identitást hoz létre?

Egy ember párhuzamosan több DID-identitást is működtethet. Ám az egyes identitások reputációjának építése önálló erőfeszítést igényel — időt, energiát, pénzt.

Nincs rövidebb út: minden identitásnak valós tevékenységen keresztül kell felhalmoznia a track recordját[^trackrecord]. A párhuzamos identitások fenntartása tehát szándékosan drága.

A szabad társadalmakban a költségek elveszik a visszaélés kedvét.

A diktatúrákban azonban a párhuzamos identitások túlélési eszközzé válnak: lehetővé teszik földalatti hálózatok szervezését, a feketepiacon való biztonságosabb eligazodást és a kompartmentalizált[^compartmentalization] ellenállást, amelyben az egyik identitás lelepleződése nem fedi fel a többit — a rezsim bukása után pedig zökkenőmentes visszatérést engednek a közéletbe és az ott felépített reputációhoz, sőt lehetővé teszik a korábban hivatalos és a titkos DID egyetlen, egyesített bejegyzéshalmazba való összefésülését is egy állítás révén.

![MI VAN, HA VALAKI TÖBB IDENTITÁST HOZ LÉTRE?](../../Info%20Graphics/v5/v5-04a-vice-identit.webp)

> [!note] Kifordított érzékelés
> Az állammal ellentétben a decentralizált identitásra épülő reputációs hálózat elve megfordítja az érzékelt prioritás paradigmáját:
>
> - Ami számít, az a reputáció — vagyis a múlt, amelyet az ellenféllel való interakció kockázatainak felmérésére használunk —, a személyes adatok pedig, mint a nevek, címek stb., udvariassági adatcsere tárgyai lehetnek
> - Míg az állam elsősorban személyes adatokat követel, reputációs adatokat halmoz fel, és csak azt engedi látni a közösségnek, ami neki megfelel

## Nem tud-e egy gazdag ember egyszerűen „megvenni" több identitást (vagy virtuális közösségeket létrehozni)?

A párhuzamos decentralizált identitások létrehozásának lehetősége első ránézésre tisztességtelen előnynek tűnik a nagyobb gazdasági eszközökkel bíró emberek javára a kevesebbel rendelkezőkkel szemben. Hangsúlyozni kell azonban, hogy a centralizált rendszerrel ellentétben, ahol elég a hatalmi piramis néhány pontját megvesztegetni ahhoz, hogy bizonyos gaztettek eltűnjenek, egy decentralizált rendszerben az egész közösséget meg kellene vesztegetni.

Helyettesítő decentralizált identitások szolgálhatnának erre a célra, de a reputációjukat időben, valós, tényleges közösségi tagokkal folytatott interakción keresztül kell felépíteni — nem lehet egyszerűen megvenni, mert a hálózat ellenőrizhetővé teszi, hogyan teljesít egy adott identitás.

Ráadásul létezhetnek (és valószínűleg léteznek is majd) olyan piaci szolgáltatások, amelyek autoritásként eljárva olyan nyomozásokat kínálnak, amelyek bizonyítékot állítanak elő arról, hogy több decentralizált identitás valójában ugyanaz a személy. A reputációs hálózatba bevitt egyetlen bejegyzés így a költség töredékéért semmissé teheti a párhuzamos identitások felépítésébe fektetett teljes idő-, energia- és pénzberuházást.

Gazdaságilag tehát megéri nem becsapni a közösséget — és ha kell, felülvizsgálni a tetteinket és orvoslásba fogni, hogy a reputáció visszatérjen egy elfogadható szintre, és a viselője ne szenvedjen gazdaságilag vagy másképp a közösség haragjától.

Egy gazdaságilag erős identitás, amely elvesztette a reputációját a saját közösségében, megpróbálhatja alattomos alkukkal, célzott identitásokon keresztül elkerülni a közösség haragját — de azok ekkor szintén a saját reputációjuk elvesztését kockáztatják.

Még mindig marad a menekülés egy másik közösségbe friss identitással — de ez azt jelenti, hogy minden eredményt hátrahagy, és valahol nulláról, nulla reputációval kezdi. Néha érthető út lehet, és az egyetlen kiút.

![EGY EGÉSZ KÖZÖSSÉGET NEM LEHET MEGVESZTEGETNI](../../Info%20Graphics/v5/v5-04b-centralizace-vs-decentralizace.webp)

> [!note] Megjegyzés
> Hasonlóképpen kezelnék a közösségek azt a támadást, amelyben valaki erőforrásokat fordít egy virtuális identitás létrehozására: annak az identitásnak kockázatos ellenőrzés nélkül interakcióba lépni egy másik közösséggel — vagyis kritikátlanul elfogadni a másik közösség identitásairól szóló információt. A reputációt mindig egy közösségen belül építik, nem globálisan.

## Mi a helyzet a potyautasokkal, akik csak olvasni akarnak, és semmit nem adnak a közösségnek?

Az információhoz való hozzáférés nem korlátlan egy decentralizált identitás létrehozásának első napjától. Az új résztvevők — akik még nem építettek reputációt tényleges tevékenységgel — fokozatos korlátozásokba ütköznek: kevesebb információ, hosszabb várakozási idők, magasabb lekérdezési költségek. A hálózat a részvételt jutalmazza, nem a passzív fogyasztást és az önkényes adatlehalászást.

Egy decentralizált identitás a reputációját is kockáztatja, amikor pénzért kölcsönadja a reputációját egy másik személynek (aki lehet, hogy nincs is a DID-reputációs hálózatban). Ugyanaz az elv érvényes itt: a közösség ilyen elárulása (a magánélet megsértése) rávetülhet az áruló reputációjára, és a tettet nem lehet alattomos alkuval eltörölni, ahogyan az egy centralizált rendszerben működik. Számolniuk kell a közösség haragjával, beleértve az eredmények elvesztését is — mert a közösség az ő szemükben például az ingó és ingatlan vagyon birtoklásának kiváltságát garantálja.

> [!note] Horgony a valós világhoz
> A kockázat felmérésekor a kockázatosabb alany természetesen az, aki nem élvezi az adott közösség által elismert tulajdon kiváltságát — kevesebbet veszíthet az ügyleteiben (a digitális eszközöket könnyebb mozgatni).
>
Apró részletnek tűnhet, de nagy következményei vannak. Ha azt akarjuk, hogy a közösségnek befolyása legyen a tagjai fölött, az kiváltságként vonja maga után a tulajdont — a legszabadabb társadalmakban szinte érinthetetlenként, mégsem jogként, sem alapelvként, hanem kiváltságként, amely szélsőséges esetben visszavonható (el tudom képzelni például a közösség fegyveres konfliktusban való védelme alóli kibújás megtagadását).
>
Ez sejtelmesen arra is választ ad, hogyan bánik majd a közösség a tagjaival, és mi motiválja a tagot arra, hogy harcoljon a közösségért — hogy megőrizze a kiváltságait. Egy ember elbukhat a közösséggel szembeni felelősségében, de erkölcsileg nem várhat elnézést, amikor a nehezen kivívott kiváltságok megőrzéséről van szó.

![A HÁLÓZAT A RÉSZVÉTELT JUTALMAZZA](../../Info%20Graphics/v5/v5-04c-prizivnici.webp)

## Pénzügyi semlegesség

Amikor olyan szavakat olvasunk, mint decentralizált, cenzúrázhatatlan, korrumpálhatatlan, óhatatlanul a legismertebb kriptovalutákra asszociálunk — Bitcoin, Monero és mondjuk Kaspa —, amelyek leírhatók ilyen kifejezésekkel. Az intuíció itt azonban megtévesztő: az autoritások szolgáltatásaiért, az ellenőrzésért, a közzétételért és így tovább járó díjak bármely valutában vagy pénzben rendezhetők. Ami a DID-hálózatbeli közösségi hálózat összekapcsolt résztvevői (vagyis a közösséged) és annak környezete számára számít, az egy reputációval fedezett megerősítés, hogy a fizetés megtörtént. Egy állítás közzétételének egyénileg észszerű, ellenőrizhető költséget kell viselnie, hogy egy szereplő ne tehessen közzé annyi és bármilyen állítást, amennyit csak akar, energia, pénz és idő ráfordítása nélkül — ez erősen nemkívánatos állapot lenne, amely a mai korrupcióval terhelt államrendszerekben az elit kiváltságának felel meg.

Ebben a tekintetben az említett kriptovalutáknak van egy kis előnyük: a hálózataik megbízható autoritásként működnek annak ellenőrzésében, hogy egy adott fizetés megtörtént, a magánélet kis elvesztése és néhány cím felfedésének árán.

[^trackrecord]: **Track record** — általánosan: egy személy vagy szervezet múltbeli eredményeinek, sikereinek és kudarcainak története. Itt: egy adott DID-identitás összes múltbeli interakciója a hálózatban — ellenőrzött állítások, elfogadott és elutasított bejegyzések —, amelyekből a reputációja levezethető.

[^compartmentalization]: **Kompartmentalizáció** (az ang. *compartment* szóból) az információ elszigetelt egységekre való szétválasztását jelenti, hogy az egyik egység lelepleződése ne veszélyeztesse a többit. A titkosszolgálatoktól ismert elv: egy ügynök csak a saját műveletrészét ismeri, így kényszer alatt sem tudja felfedni az egészet.
