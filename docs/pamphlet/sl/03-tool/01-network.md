---
title: "Reputacijsko družbeno omrežje"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputacijsko družbeno omrežje

Za uvedbo spremembe potrebujemo skrbno zasnovano orodje. Najprej ga bomo na kratko orisali; v poznejših poglavjih bomo vsak del preučili podrobneje in dodali še kaj. Predstavljaj si necenzurljivo, globalno, decentralizirano družbeno omrežje, kjer bi lahko varno ustvaril in upravljal svojo posredniško identiteto — tako imenovano decentralizirano identiteto (DID). DID je digitalna identiteta, ki jo ustvariš in nadzoruješ sam, brez odvisnosti od katere koli centralne avtoritete. Nihče je ne more odvzeti ali ponarediti, ker je kriptografsko podpisana s tvojim zasebnim ključem (ali ključi, prek multisiga).

> [!note] Opomba
> Ena od posledic je, da bi takšna identiteta lahko postopno nadomestila državno izdane identifikacijske dokumente — a o tem več v poglavju o prehodu.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

V takšnem omrežju bi lahko prek svoje identitete prijavil, da ti je nekdo povzročil škodo (in pozneje morda, da jo je odpravil ali bil k temu prisiljen). Da bi imela ta povratna informacija — usmerjena na povzročitelja škode — vrednost kot relevanten vir, mora vnašanje informacij v omrežje stati čas, energijo in denar — poleg tega pa je treba za druge izdelati preverljiv dokaz, da ne gre za prazno govorjenje.

Branje informacij bi bilo enostavno in razmeroma poceni, ustvarjanje posameznega zapisa pa drago in zahtevno. Pisanje bi sledilo jasnemu protokolu, v katerem izračun po izbranem algoritmu strogo določi, kateri DID zaprositi za preverjanje predložene informacije in kako naprej, da izbrani udeleženec obdela informacijo v tvojem imenu, jo objavi in postane njen preveritelj.

> [!note] Algoritem proti radikalizmu
> Algoritemska izbira preveriteljev zagotavlja, da bodo neradikalni objavljavci informacij sčasoma ohranjali skoraj nevtralno ravnovesje med stroški objavljenih informacij in nagradami za preverjanje.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Poglejmo, kako algoritem izbere preveritelja.

> [!note] Algoritem
> Algoritemska izbira nedeterministično izbere drugega preveritelja (ali nabor mogočih preveriteljev) za različne koščke informacij. Zgoščena vrednost (hash — enosmerna matematična funkcija, ki iz katerega koli vhoda izdela edinstven „prstni odtis", kot prstni odtis dokumenta) celotnega DID dokumenta določi položaj na konsistentnem zgoščevalnem obroču in izbere kandidate za preveritelja.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Preprosto povedano: algoritem vzame tvoj celoten DID dokument, iz njega izračuna prstni odtis, in ta prstni odtis določi tvojega preveritelja.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Pri prvem preveritelju, ki ga algoritem izbere, ti kot objavljavcu morda ne bo uspelo — tvoja reputacija ali deklarirane nastavitve morda ne izpolnjujejo njegovih zahtev. Algoritemsko bi nadaljeval iskanje naslednjega z izvedbo nove rekurzivne iteracije, ki ti dodeli nadaljnjega preveritelja. Z vsakim korakom „razdalja" do ciljnega preveritelja narašča, prav tako spremljajoči metapodatki, ki jih je treba objaviti. Ko podatki rastejo, stroški naravno naraščajo (ne le zaradi začetne velikosti trditve, temveč tudi zaradi metapodatkov, ki se nabirajo z vsako zavrnitvijo). Verodostojna informacija se prebije veliko lažje kot nesmiselne muhe. Od vsakega je odvisno, kako visoko ceno je pripravljen prenesti in koliko mu je zapis pomemben — radikalizem se zagotovljeno podraži.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Karkoli se preveritelj odloči kot odgovor na tvojo zahtevo za preverjanje, je žoga spet na strani objavljavca: ta lahko sprejme preveriteljevo ponudbo za storitve preverjanja, odgovor vključi v kronologijo in poskusi znova (dražje) ali odide in požre potopljeni strošek.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Da bi svoji informaciji dal večjo težo in boljše možnosti za sprejem pri preveriteljih, bi lahko kot objavljavec, ki ima interes pri izdaji informacije, uporabil storitve **zaupanja vredne avtoritete**. Avtoriteta bodisi zavrne predloženo informacijo bodisi jo sprejme in nanjo stavi svoje dobro ime (reputacijo). Avtoriteta običajno zahteva dokaze iz resničnega sveta, jih preveri in razvrsti. Rezultat je protokol njene presoje danega primera v danem času. Avtoriteto si predstavljaj kot specialista za določeno vrsto storitev tako v resničnem kot v digitalnem svetu — na primer preiskovalca, revizorja, zavarovalnico, dobavitelja določenega razreda blaga (v bistvu katerega koli gospodarskega akterja na trgu).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Do trenutka, ko poskusiš objaviti informacijo v omrežje, bo to najbrž že vsebovalo informacije o svojih akterjih — to so reputacijski signali. Krmarjenje po tem, kako brati reputacijske signale — kaj ti pomenijo v različnih situacijah in kakšna tveganja nosijo — morda ni trivialno. Vsak udeleženec lahko na reputacijske zapise gleda drugače skozi svoj DID, odvisno od situacije, ki jo obravnava glede na nasprotno stran. Je nasprotna stran zanesljiv plačnik ali moram za poslovni posel zahtevati denar vnaprej? Ali ponujeni izdelek nosi ocene o prikriti prevari ali napakah? Ali se poskuša izmuzniti pogodbeni odgovornosti, ko gre kaj narobe? Včasih pride prav bolj kompleksen pogled na celotno doslednost nasprotne strani — odvisno je od preferenc tistega, ki zahteva pregled. Trg bi lahko ponujal izdelke in storitve, ki poenostavijo, obdelajo in razjasnijo branje reputacije v kontekstu dane situacije. Temu lahko služijo tudi različne avtoritete in njihove ponujene storitve.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Primeri
> Tipične informacije, ki zanimajo objavljavce — in so dragocene za druge — zadevajo dogodke onkraj običajne medosebne komunikacije v resničnem ali virtualnem svetu.
>
> Negativni primeri:
> - dokazi o kaznivih dejanjih (npr. revidirani s strani zaupanja vrednega preiskovalnega organa)
> - posredni dokazi (sami po sebi šibki, a statistično kumulativni) — npr. ponavljajoča se prisotnost blizu več kraj v kratkem času → še vedno naključje?
> - kršitev pogodbe
>
> Pozitivni primeri:
> - odpravljena škoda (prostovoljno ali pod pritiskom skupnosti kot kazen)
> - sprejem in prestajanje kazni, ki jo je predlagala avtoriteta X
> - avtoriteta X je storilcu v določenem obsegu preklicala priznanje lastninskih pravic
>
> Od vsakega je odvisno, da zbere razpoložljive informacije o nasprotni strani in oceni tveganja glede na svoje preference.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Ali se informacije o tebi pojavijo v omrežju, je odvisno izključno od tvojega lastnega vedenja.
> Takšnemu omrežju se nikoli ni treba pridružiti, pa se informacije o tebi vseeno lahko pojavijo v njem. Odvisno je izključno od tvojih dejanj in vpliva, ki ga imajo na druge.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

To, kar sem pravkar na kratko orisal, je, kako bi lahko delovalo družbeno omrežje, navdihnjeno z decentralizirano identiteto (DID). Primarni namen konceptov DID je krepiti zasebnost in svobodo prek načela zavezanosti pravilom, ki jih bom upošteval in po katerih bom živel — uporabnikom dati možnost odločati, katere informacije deliti in pod kakšnimi pogoji.

Predlagam, da DID-e še naprej povežemo v komunikacijsko omrežje, kjer si njihovi imetniki izmenjujejo povratne informacije tudi onkraj situacij, ko se je komu kaj zgodilo in se mora skupnost ali posameznik odzvati. Takšna preventivna primerjava pravil, na katera smo se prijavili — z možnostjo izračuna ekonomskih in drugih posledic vzajemnih odstopanj v pričakovanjih o tem, kako naj druga stran deluje — bi lahko veljala za motivacijo za iskanje konsenza. Namesto svobode bi takšen sistem poudarjal prostovoljno odločanje v kombinaciji z odgovornostjo za vedenje v resničnem svetu.

Posameznik sistema ne more razbiti sam — skupina ljudi ima večje možnosti, skupina ljudi z izpogajanim konsenzom in motivacijami, da vlečejo skupaj pri številnih vprašanjih, pa ima še večje možnosti, da se upre avtoritarnim težnjam. Predpogoj organiziranosti iz prvega poglavja bo izpolnjen, ko bosta izpolnjena dva pogoja: reputacijsko omrežje DID dovolj reprezentativno pokriva skupnosti, da njegova uporaba preneha biti eksotična. In hkrati ta segment skupnosti postane ekonomsko pomembna manjšina, ki se lahko odločno pogaja s preostankom družbe.

> [!note] Prostovoljnost proti svobodi
> Svoboda — v pozitivnem smislu — bi bila sekundarni učinek uravnoteženja dveh dejavnikov: prostovoljnosti in pritiska okolice v smeri odgovornosti.

> [!note] Doba UI in vrednost reputacije
> V dobi umetne inteligence se vse, kar je povezano s kognitivnim mišljenjem, avtomatizira — in gre lahko še dlje. Kaj potem ostane v človeški dejavnosti kot konkurenčna prednost? Odgovor je težak in nekaj se bo zagotovo našlo, a eno lahko rečemo z gotovostjo: reputacija bo odločila. Preverljiva zgodovina tvojega vedenja, tvojih zavez in njihovega izpolnjevanja — to je nekaj, česar UI ne bo zgradil zate.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
