---
title: "Reputacijska društvena mreža"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputacijska društvena mreža

Da bismo ostvarili promjenu, treba nam pomno osmišljen alat. Najprije ćemo ga ukratko skicirati; u kasnijim poglavljima svaki ćemo dio razmotriti podrobnije i dodati još. Zamisli necenzurabilnu, globalnu, decentraliziranu društvenu mrežu na kojoj bi mogao sigurno stvoriti i upravljati svojim posredničkim identitetom — takozvanim Decentraliziranim identitetom (DID). DID je digitalni identitet koji sam stvaraš i sam njime upravljaš, bez ovisnosti o bilo kojem središnjem autoritetu. Nitko ti ga ne može oduzeti ni krivotvoriti, jer je kriptografski potpisan tvojim privatnim ključem (ili ključevima, putem multisiga).

> [!note] Napomena
> Jedna je implikacija to da bi takav identitet postupno mogao zamijeniti državne identifikacijske isprave — ali o tome više u poglavlju o prijelazu.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Na takvoj bi mreži kroz svoj identitet mogao prijaviti da ti je netko nanio štetu (i kasnije, eventualno, da ju je popravio ili bio prisiljen popraviti). Da bi ta povratna informacija — usmjerena na uzročnika štete — imala vrijednost kao relevantan izvor, unos informacije u mrežu mora stajati vremena, energije i novca — a povrh toga mora se za druge proizvesti provjerljiv dokaz da nije riječ o praznom naklapanju.

Čitanje informacija bilo bi lako i razmjerno jeftino, ali stvaranje pojedinačnog zapisa bilo bi skupo i zahtjevno. Pisanje bi slijedilo jasan protokol u kojem izračun prema odabranom algoritmu strogo određuje koji DID zatražiti za provjeru podnesene informacije i kako postupiti tako da odabrani sudionik obradi informaciju u tvoje ime, objavi je i postane njezin verifikator.

> [!note] Algoritam vs radikalizam
> Algoritamski odabir verifikatora osigurava da će neradikalni objavljivači informacija tijekom vremena održavati gotovo neutralnu ravnotežu između troškova objavljenih informacija i nagrada za provjeru.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Pogledajmo kako algoritam odabire verifikatora.

> [!note] Algoritam
> Algoritamski odabir nedeterministički bira drugog verifikatora (ili skup mogućih verifikatora) za različite dijelove informacija. Hash (jednosmjerna matematička funkcija koja iz bilo kojeg ulaza proizvodi jedinstveni „otisak" — poput otiska prsta nekog dokumenta) potpunog DID dokumenta određuje poziciju na konzistentnom hash prstenu i odabire kandidate za verifikatora.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Jednostavnim rječnikom: algoritam uzima tvoj cijeli DID dokument, izračuna iz njega otisak, a taj otisak određuje tvojeg verifikatora.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

S prvim verifikatorom kojeg algoritam odabere ti kao objavljivač možda nećeš uspjeti — tvoja reputacija ili deklarirane postavke možda ne zadovoljavaju njegove zahtjeve. Algoritamski bi nastavio pretragu za sljedećim izvodeći još jednu rekurzivnu iteraciju koja ti dodjeljuje daljnjeg verifikatora. Sa svakim korakom raste „udaljenost" do ciljanog verifikatora, a s njom i prateći metapodaci koji se moraju objaviti. Kako podaci rastu, prirodno rastu i troškovi (ne samo zbog početne veličine tvrdnje, nego i zbog metapodataka koji se nagomilavaju sa svakim odbijanjem). Vjerodostojna informacija prolazi mnogo lakše od besmislenih hirova. Na svakome je koliko je visoku cijenu spreman podnijeti i koliko mu je zapis važan — radikalizam se zajamčeno pretvara u trošak.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Kako god verifikator odlučio kao odgovor na tvoj zahtjev za provjerom, lopta se vraća objavljivaču: može prihvatiti verifikatorovu ponudu za usluge provjere, uklopiti odgovor u kronologiju i pokušati ponovno (skuplje), ili odustati i progutati potopljeni trošak.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Da bi svojoj informaciji dao veću težinu i bolju priliku da je verifikatori prihvate, ti — kao objavljivač s udjelom u informaciji koja se izdaje — mogao bi se poslužiti uslugama **pouzdanog autoriteta**. Autoritet ili odbija podnesenu informaciju ili je prihvaća i ulaže u nju svoje dobro ime (reputaciju). Autoritet obično traži dokaze iz stvarnog svijeta, provjerava ih i razvrstava. Rezultat je protokol njegove procjene danog slučaja u danom trenutku. Zamisli autoritet kao specijalista za određenu vrstu usluge, kako u stvarnom tako i u digitalnom svijetu — primjerice istražitelja, revizora, osiguravatelja, dobavljača određene klase robe (u biti bilo kojeg ekonomskog aktera na tržištu).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Dok pokušaš objaviti informaciju u mreži, ona će vjerojatno već sadržavati informacije o svojim akterima — to su reputacijski signali. Snalaženje u tome kako čitati reputacijske signale — što ti znače u različitim situacijama i kakve rizike nose — možda neće biti trivijalno. Svaki sudionik kroz svoj DID može reputacijske zapise sagledavati drukčije, ovisno o situaciji s kojom se nosi u odnosu na drugu stranu. Je li druga strana pouzdan platitelj, ili moram za poslovnu transakciju tražiti novac unaprijed? Nose li ponuđeni proizvodi recenzije o skrivenoj prijevari ili nedostacima? Pokušavaju li se izvući iz ugovorne odgovornosti kad nešto pođe po zlu? Ponekad dobro dođe složeniji pogled na cjelokupnu dosljednost druge strane — ovisi o sklonostima onoga tko pregled zatraži. Tržište bi moglo ponuditi proizvode i usluge koje pojednostavnjuju, obrađuju i razjašnjavaju čitanje reputacije u kontekstu dane situacije. Toj svrsi mogu poslužiti i razni autoriteti i njihove ponuđene usluge.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Primjeri
> Tipične informacije koje zanimaju objavljivače — i vrijedne su drugima — tiču se događaja izvan uobičajene međuljudske komunikacije u stvarnom ili virtualnom svijetu.
>
> Negativni primjeri:
> - dokazi kaznenih djela (npr. auditirani od strane pouzdanog istražnog tijela)
> - posredni dokazi (sami po sebi slabi, ali statistički kumulativni) — npr. opetovana prisutnost blizu više krađa u kratkom razdoblju → i dalje slučajnost?
> - kršenje ugovora
>
> Pozitivni primjeri:
> - popravljena šteta (dobrovoljno ili pod pritiskom zajednice kao kazna)
> - prihvaćanje i odsluživanje kazne koju je predložio autoritet X
> - autoritet X u određenoj je mjeri opozvao priznavanje počiniteljevih vlasničkih prava
>
> Na svakome je da prikupi dostupne informacije o drugoj strani i procijeni rizike prema svojim sklonostima.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Hoće li se informacija o tebi pojaviti u mreži, ovisi isključivo o tvojem vlastitom ponašanju.
> Nikad se ne moraš pridružiti takvoj mreži, a informacije o tebi mogu se u njoj ipak pojaviti. Ovisi isključivo o tvojim postupcima i o učinku koji imaju na druge.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Ono što sam upravo ukratko skicirao jest kako bi mogla funkcionirati društvena mreža nadahnuta Decentraliziranim identitetom (DID). Primarna je svrha DID koncepata ojačati privatnost i slobodu kroz načelo pretplaćivanja na pravila kojih ću se pridržavati i po kojima ću živjeti — dajući korisnicima mogućnost da odluče koje informacije dijeliti i pod kojim uvjetima.

Predlažem da se DID-ovi dodatno povežu u komunikacijsku mrežu u kojoj njihovi nositelji razmjenjuju povratne informacije čak i izvan situacija u kojima se nekome nešto dogodilo i zajednica ili pojedinac treba reagirati. Takva preventivna usporedba pravila na koja smo se pretplatili — uz mogućnost izračuna ekonomskih i drugih posljedica uzajamnih odstupanja u očekivanjima o tome kako bi druga strana trebala djelovati — mogla bi se smatrati motivacijom za pronalaženje konsenzusa. Umjesto slobode, takav bi sustav naglašavao dobrovoljno odlučivanje u kombinaciji s odgovornošću za ponašanje u stvarnom svijetu.

Pojedinac sam ne može slomiti sustav — skupina ljudi ima veće izglede, a skupina ljudi s ispregovaranim konsenzusom i motivacijama da zajedno povuku u mnogim pitanjima ima još veće izglede oduprijeti se autoritarnim tendencijama. Preduvjet organizacije iz prvog poglavlja bit će ispunjen kad se ispune dva uvjeta: DID reputacijska mreža dovoljno reprezentativno pokriva zajednice da njezina uporaba prestane biti egzotična. I istodobno taj segment zajednice postaje ekonomski značajna manjina koja može asertivno pregovarati s ostatkom društva.

> [!note] Dobrovoljnost vs sloboda
> Sloboda — u pozitivnom smislu — bila bi sekundarni učinak uravnoteženja dvaju čimbenika: dobrovoljnosti i pritiska okoline prema odgovornosti.

> [!note] Doba UI-ja i vrijednost reputacije
> U doba umjetne inteligencije automatizira se sve što je povezano s kognitivnim mišljenjem — a moglo bi ići i dalje. Što tada u ljudskoj djelatnosti ostaje kao konkurentska prednost? Odgovor je težak, i nešto će se sigurno naći, ali jedno možemo reći sa sigurnošću: reputacija će odlučivati. Provjerljiva povijest tvojeg ponašanja, tvojih obveza i njihovog ispunjenja — to je nešto što UI neće izgraditi umjesto tebe.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
