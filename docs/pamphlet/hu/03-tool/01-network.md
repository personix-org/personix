---
title: "Reputációs közösségi hálózat"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputáció alapú közösségi hálózat

A változás előidézéséhez gondosan megtervezett eszközre van szükségünk. Először röviden felvázoljuk, a későbbi fejezetekben pedig részletesebben megvizsgáljuk az egyes darabokat, és továbbiakat is hozzáteszünk. Képzelj el egy cenzúrázhatatlan, globális, decentralizált közösségi hálózatot, ahol biztonságosan létrehozhatnád és kezelhetnéd a helyettesítő identitásodat — az úgynevezett decentralizált identitást (DID). A DID egy olyan digitális identitás, amelyet magad hozol létre és irányítasz, bármely központi hatóságtól való függés nélkül. Senki nem tudja elvenni vagy meghamisítani, mert kriptográfiailag a privát kulcsoddal (vagy kulcsaiddal, multisig révén) van aláírva.

> [!note] Megjegyzés
> Ennek egyik következménye, hogy egy ilyen identitás fokozatosan felválthatná az állam által kiadott azonosító okmányokat — de erről többet az átmenetről szóló fejezetben.

![A TE IDENTITÁSOD, A TE KULCSAID, A TE SZABÁLYAID](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Egy ilyen hálózatban az identitásodon keresztül bejelenthetnéd, hogy valaki kárt okozott neked (és később esetleg azt is, hogy orvosolta, vagy rákényszerült az orvoslásra). Ahhoz, hogy ez a visszajelzés — amely a károkozó felé irányul — releváns forrásként értéket képviseljen, az információ hálózatba juttatásának időbe, energiába és pénzbe kell kerülnie — ráadásul ellenőrizhető bizonyítékot kell előállítani mások számára, hogy ez nem üres fecsegés.

Az információ olvasása könnyű és viszonylag olcsó lenne, de egy egyéni bejegyzés létrehozása költséges és igényes. Az írás világos protokollt követne, amelyben a választott algoritmus szerinti számítás szigorúan meghatározza, melyik DID-et kell megkérni a benyújtott információ ellenőrzésére, és hogyan kell eljárni ahhoz, hogy a kiválasztott résztvevő a nevedben feldolgozza az információt, közzétegye, és annak ellenőrzőjévé váljon.

> [!note] Algoritmus kontra radikalizmus
> Az ellenőrzők algoritmikus kiválasztása biztosítja, hogy a nem radikális információközzétevők idővel közel semleges egyensúlyt tartanak fenn a közzétett információ költségei és az ellenőrzésért járó jutalmak között.

![A KÖZZÉTÉTEL IDŐBE, ENERGIÁBA ÉS PÉNZBE KERÜL](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Nézzük meg, hogyan választ ki az algoritmus egy ellenőrzőt.

> [!note] Algoritmus
> Az algoritmikus kiválasztás nemdeterminisztikusan más-más ellenőrzőt (vagy lehetséges ellenőrzők egy halmazát) választ ki különböző információdarabokhoz. A teljes DID-dokumentum hashe (egyirányú matematikai függvény, amely bármely bemenetből egyedi „ujjlenyomatot" állít elő — mint egy dokumentum ujjlenyomata) határozza meg a pozíciót egy konzisztens hash-gyűrűn, és jelöli ki az ellenőrzőjelölteket.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Egyszerűen szólva: az algoritmus fogja a teljes DID-dokumentumodat, ujjlenyomatot számol belőle, és ez az ujjlenyomat határozza meg az ellenőrződet.

![HOGYAN VÁLASZTJA KI AZ ALGORITMUS AZ ELLENŐRZŐDET](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Az első ellenőrzővel, amelyet az algoritmus kiválaszt, közzétevőként nem biztos, hogy sikerrel jársz — a reputációd vagy a deklarált beállításaid nem feltétlenül felelnek meg a követelményeiknek. Algoritmikusan folytatnád a keresést a következő után egy újabb rekurzív iterációval, amely további ellenőrzőt rendel hozzád. Minden lépéssel nő a „távolság" a célként kijelölt ellenőrzőig, és nő a hozzá tartozó, közzéteendő metaadat is. Ahogy az adat nő, a költségek természetes módon emelkednek (nemcsak az állítás kezdeti mérete miatt, hanem az egyes elutasításokkal felhalmozódó metaadat miatt is). A hiteles információ jóval könnyebben átmegy, mint az értelmetlen szeszélyek. Mindenkin múlik, mekkora árat hajlandó megfizetni, és mennyire fontos neki a bejegyzés — a radikalizmus garantáltan drágává válik.

![HOGYAN VÁLASZOL AZ ELLENŐRZŐ](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Bármit dönt is az ellenőrző az ellenőrzési kérésedre válaszul, a labda visszakerül a közzétevő térfelére: elfogadhatja az ellenőrző ajánlatát az ellenőrzési szolgáltatásra, beledolgozhatja a választ a kronológiába és újra próbálkozhat (drágábban), vagy elsétálhat és lenyelheti az elsüllyedt költséget.

![A KIBOCSÁTÓ DÖNTÉSE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Hogy nagyobb súlyt és jobb esélyt adj az információdnak az ellenőrzőknél való elfogadásra, közzétevőként — akinek érdeke fűződik a kibocsátott információhoz — igénybe vehetnéd egy **megbízható autoritás** szolgáltatásait. Az autoritás vagy elutasítja a benyújtott információt, vagy elfogadja, és a jó nevét (reputációját) teszi rá. Az autoritás jellemzően valós bizonyítékokat kér, ellenőrzi és osztályozza azokat. A kimenet egy jegyzőkönyv az adott ügy adott időpontban való megítéléséről. Úgy gondolj egy autoritásra, mint egy bizonyos szolgáltatástípus szakértőjére a valós és a digitális világban egyaránt — például nyomozó, könyvvizsgáló, biztosító, egy adott áruosztály beszállítója (lényegében a piac bármely gazdasági szereplője).

![HOGYAN KELETKEZIK BEJEGYZÉS A HÁLÓZATBAN](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Mire megpróbálsz információt közzétenni a hálózatban, az valószínűleg már tartalmaz információt a szereplőiről — ezek a reputációs jelek. Nem feltétlenül triviális eligazodni abban, hogyan olvassuk a reputációs jeleket — mit jelentenek számodra a különböző helyzetekben, és milyen kockázatokat hordoznak. Minden résztvevő másképp nézheti a reputációs bejegyzéseket a saját DID-jén keresztül, attól függően, milyen helyzetet kezel az ellenféllel kapcsolatban. Megbízható fizető-e az ellenfél, vagy elő kell kérnem a pénzt egy üzleti tranzakcióhoz? A kínált termékhez tartoznak-e értékelések rejtett csalásról vagy hibákról? Próbál-e kibújni a szerződéses felelősség alól, amikor valami balul üt ki? Néha jól jön az ellenfél általános konzisztenciájának összetettebb nézete — attól függ, mit preferál az, aki az áttekintést kéri. A piac kínálhatna termékeket és szolgáltatásokat, amelyek egyszerűsítik, feldolgozzák és tisztázzák a reputáció olvasását az adott helyzet kontextusában. Erre a célra a különféle autoritások és az általuk kínált szolgáltatások is szolgálhatnak.

![HOGYAN OLVASSUK A REPUTÁCIÓT](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Példák
> A közzétevők számára jellemzően érdekes — és mások számára értékes — információk a hétköznapi, valós vagy virtuális világbeli, személyközi kommunikáción túli eseményekre vonatkoznak.
>
> Negatív példák:
> - bűncselekmények bizonyítékai (pl. megbízható nyomozó testület által auditálva)
> - közvetett bizonyítékok (önmagukban gyengék, de statisztikailag halmozódók) — pl. ismételt jelenlét több lopás közelében rövid idő alatt → még mindig véletlen?
> - szerződésszegés
>
> Pozitív példák:
> - orvosolt kár (önként vagy a közösség nyomására, büntetésként)
> - egy X autoritás által javasolt büntetés elfogadása és letöltése
> - X autoritás bizonyos mértékig visszavonta az elkövető tulajdonjogainak elismerését
>
> Mindenkin múlik, hogy összegyűjti-e az ellenfélről elérhető információt, és a preferenciái szerint felméri-e a kockázatokat.

![MIT RÖGZÍTHETSZ A HÁLÓZATBAN?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Hogy megjelenik-e rólad információ a hálózatban, az kizárólag a saját viselkedéseden múlik.
> Sosem kell csatlakoznod egy ilyen hálózathoz, mégis megjelenhet rólad benne információ. Ez kizárólag a tetteiden és azok másokra gyakorolt hatásán múlik.

![A KÖZÖSSÉG NYITHAT EGYET NEKED](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Amit az imént röviden felvázoltam, az az, hogyan működhet egy decentralizált identitás (DID) ihlette közösségi hálózat. A DID-koncepciók elsődleges célja a magánélet és a szabadság erősítése az „aláiratkozás" elve mentén, vagyis azon szabályokra, amelyeket követni fogok és amelyek szerint élni fogok — megadva a felhasználóknak azt a képességet, hogy eldöntsék, milyen információt osztanak meg és milyen feltételekkel.

Azt javaslom, hogy a DID-eket kössük tovább egy kommunikációs hálózatba, amelyben a tulajdonosaik akkor is visszajelzést cserélnek, amikor éppen nem történt valakivel valami, amire a közösségnek vagy egy egyénnek reagálnia kellene. Azoknak a szabályoknak az ilyen megelőző összevetése, amelyekre aláiratkoztunk — azzal a lehetőséggel, hogy kiszámítsuk a kölcsönös eltérések gazdasági és egyéb következményeit abban, amit a másik féltől elvárunk annak működéséről — a konszenzuskeresés motivációjának tekinthető. A szabadság helyett egy ilyen rendszer az önkéntes döntéshozatalt hangsúlyozná, párosítva a valós viselkedésért való felelősséggel.

Egy egyén egyedül nem tudja megtörni a rendszert — egy embercsoportnak nagyobb esélye van, egy olyan embercsoportnak pedig, amely kialkudott konszenzussal és sok kérdésben az egy irányba húzás motivációjával bír, még nagyobb esélye van ellenállni a tekintélyelvű tendenciáknak. Az első fejezetből ismert szerveződési előfeltétel akkor teljesül, ha két feltétel megvalósul: a DID-reputációs hálózat elég reprezentatívan lefedi a közösségeket ahhoz, hogy a használata megszűnjön egzotikusnak lenni. És ezzel egy időben ez a közösségi szegmens olyan gazdaságilag jelentős kisebbséggé válik, amely magabiztosan képes tárgyalni a társadalom többi részével.

> [!note] Önkéntesség kontra szabadság
> A szabadság — pozitív értelemben — két tényező kiegyensúlyozásának másodlagos hatása lenne: az önkéntességé és a környezet felelősség felé irányuló nyomásáé.

> [!note] Az MI-korszak és a reputáció értéke
> A mesterséges intelligencia korában minden, ami a kognitív gondolkodáshoz kapcsolódik, automatizálódik — és lehet, hogy még tovább is megy. Mi marad ekkor az emberi tevékenységben versenyelőnyként? A válasz nehéz, és biztosan találunk valamit, de egyet bizonyosan mondhatunk: a reputáció fog dönteni. A viselkedésed ellenőrizhető története, a vállalásaid és azok teljesítése — ezt az MI nem építi fel helyetted.

![AZ MI NEM ÉPÍTI FEL A REPUTÁCIÓDAT — CSAK TE MAGAD](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![AZ IGAZSÁG GAZDASÁGTANA](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
