---
title: "Konsenzus i proces provjere"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsenzus i proces provjere

Za izgradnju konsenzusa o tome koja bi pravila društvo trebalo u prosjeku održavati i provoditi može pomoći sljedeći mehanizam. Kao DID sudionik deklariram pravila na koja se pretplaćujem i po kojima ću živjeti te ih objavljujem. (Zamisli to kao unutarnji pravilnik i statute koji, po mojem mišljenju, čine moj idealni svijet — svijet u kojem se ne osjećam ograničeno, nego sigurno.)

Mogu unaprijed procijeniti kako bi moji DID kontakti reagirali — i procijeniti koliko snažno, i tko bi me sankcionirao u uobičajenim društvenim ili poslovnim interakcijama, kad bi se one hipotetski dogodile.

Konačna se procjena događa kad zatražiš informaciju od drugog DID-a, ili ga zamoliš da provjeri tvrdnju (ili zamoliš autoritet za uslugu i tako dalje) koju želiš objaviti u reputacijsku mrežu. Trebala bi ispasti jednako kao i kad procjenu pokreneš sam, u probnom pokušaju, u odnosu na deklariranu politiku druge strane — a ako ne ispadne, nešto nije u redu na strani druge strane: pokušava igrati nepoštenu igru.

Ishod je ili prihvaćanje, uz iskazanu cijenu za provjeru (u slučaju usluga verifikatora ili autoriteta), ili odbijanje. I sankcije i bonusi za odstupanje od politike procjenitelja uklopljeni su u iskazanu cijenu. Podnositelj potom odlučuje hoće li prihvatiti uvjete ili prijeći na sljedeći krug provjere u algoritmu raspodjele — ponavljajući proces dok ne bude zadovoljan, ili dok ekonomija ne učini besmislenim nastaviti.

> [!note] Društveni graf
> Reputacijska mreža je prije svega društvena mreža. Dodaješ kontakte — ljude koji pristaju na povezivanje. Oni imaju kontakte, a ti kontakti imaju kontakte. Algoritam traži verifikatore unutar konfigurabilne dubine (npr. tri razine: tvoji izravni kontakti, njihovi kontakti i jedna razina dalje). Nije potreban globalni blockchain — mreža prirodno tvori zajednice s preklapanjima u druge zajednice.
>
> Algoritam je nedeterministički: hashira tvoj dokument tvrdnje, preslikava hash u poziciju na prstenu poznatih identiteta unutar tog kruga i odabire najbliži kao kandidata za verifikatora. Ne možeš predvidjeti ni utjecati na to tko će tvoju tvrdnju provjeriti.

Svako odbijanje verifikatora povećava tvoj dokument i podiže trošak njegove obrade — to je prvi kanal troška (rast dokumenta). Svaki novi verifikator naplaćuje naknadu na temelju opsega podataka, tvoje reputacije i toga koliko sadržaj tvoje tvrdnje odstupa od njegove deklarirane politike provjere — to je drugi kanal troška (premija za rizik). A svaka iteracija stoji vremena i energije — treći kanal troška.

> [!note] Što verifikator provjerava, redom
> Nakon što je odabran, verifikator procjenjuje tvrdnju kroz otprilike četiri uređena koraka — najprije najjeftiniji filtri, skupe provjere sadržaja na kraju:
>
> 1. **Filtriranje politikom.** Spada li ova vrsta tvrdnje uopće u ono što verifikator javno provjerava? Ako ne, zahtjev se odmah odbija.
> 2. **Povjerenje u autoritet.** Je li autoritet koji je podržao tvrdnju dovoljno pouzdan prema verifikatorovoj vlastitoj deklariranoj politici? Autoritet ispod verifikatorova praga povjerenja razlog je za odbijanje neovisno o sadržaju tvrdnje.
> 3. **Reputacija izdavatelja.** Zadovoljava li izdavatelj pragove reputacije koje je verifikator deklarirao za ovu vrstu tvrdnje? Niska reputacija može ili podići naknadu ili izazvati odbijanje.
> 4. **Provjera sadržaja.** Tek kad prva tri filtra prođu, verifikator procjenjuje samu tvrdnju — potpise, unutarnju dosljednost, formalnu ispravnost i koliko odstupa od verifikatorove politike. Naknada naplaćena za taj posljednji korak odražava stvarno preuzeti rizik.
>
> Verifikator objavljuje politiku koja upravlja svakim od tih filtara, pa koraci nisu prepušteni njegovoj slobodnoj procjeni — vezani su onim što je već deklarirao. Odstupanje od objavljene politike samo je po sebi tvrdnja koja se protiv njega može objaviti, i on to plaća svojom reputacijom.

Rezultat: objavljivanje vjerodostojne i korisne tvrdnje ne stoji gotovo ništa. Objavljivanje radikalne tvrdnje stoji više. Objavljivanje laži postaje pretjerano skupo — moraš iterirati kroz verifikatora za verifikatorom, a svatko tko te odbije dodaje troškove. Tržište određuje cijenu tvoje tvrdnje, a cijena ti govori gdje stojiš u odnosu na zajednice u kojima se krećeš.

Nije dovoljno deklarirati da se pridržavaš pravila kad ga se u stvarnosti ne pridržavaš. U tom slučaju tvoj DID riskira objavu negativnog zapisa koji razotkriva licemjerje — što te pretvara u rizik za sve druge. Ishod bi trebao biti manje pravila, ali ih se dosljednije pridržava, i raščišćavanje one džungle zakona i propisa u kojoj se jedva snalaze i pravni stručnjaci.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsenzus vs odgovornost
> Da bi mreža služila kao vrijedan izvor informacija, DID ne bi trebao biti previše radikalan — inače će ga drugi odbiti. Društveni će pritisak tražiti ravnotežu, a pokušaji njezine destabilizacije vjerojatno će biti kažnjeni.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Broj glasova nije isto što i težina glasa
> Juraj Karpiš kaže da je „novac pamćenje dobrih djela". Dodao bih da je reputacija pamćenje loših.
>
> Iz toga slijedi da, meritokratski, tko više pridonosi i nema lošu reputaciju zaslužuje veću težinu glasa u zajednici. Gledano kroz prizmu bilateralnih odnosa: kad vagam kojim pritiscima konsenzusa udovoljiti, najveću težinu dobivaju odnosi iz kojih izvlačim najveću ekonomsku korist. Deset ljudi s kojima nemam aktivne trgovine utjecat će na mene daleko manje od jednog stalnog poslovnog partnera. Ta se paradigma ne ograničava na trgovinu — proteže se na društvene, političke i druge odnose.
