---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsenz in postopek preverjanja

Pri gradnji konsenza o tem, katera pravila naj bi družba v povprečju upoštevala in uveljavljala, lahko pomaga naslednji mehanizem. Kot udeleženec DID deklariram pravila, ki se jim zavezujem in po katerih bom živel, ter jih objavim. (Predstavljaj si to kot pravilnik in statut, ki po mojem mnenju sestavljajo moj idealni svet — svet, kjer se ne počutim omejenega, temveč varnega.)

Vnaprej lahko ocenim, kako bi se odzvali moji stiki DID — in presodim, kako močno in s strani koga bi bil sankcioniran v običajnih družbenih ali poslovnih interakcijah, če bi do njih hipotetično prišlo.

Dokončna presoja se zgodi, ko od drugega DID zahtevaš informacijo ali ga prosiš, naj preveri trditev (ali prosiš avtoriteto za storitev in tako naprej), ki jo želiš objaviti v reputacijsko omrežje. Izid mora biti enak kot takrat, ko presojo izvedeš sam, na suho, glede na deklarirano politiko nasprotne strani — in če ni, je nekaj narobe na strani nasprotne strani: poskuša igrati nepošteno igro.

Izid je bodisi sprejem s ponujeno ceno za preverjanje (v primeru storitev preveritelja ali avtoritete) bodisi zavrnitev. Tako sankcije kot bonusi za odstopanje od politike presojevalca so vključeni v ponujeno ceno. Prosilec se nato odloči, ali bo sprejel pogoje ali se premaknil v naslednji krog preverjanja v algoritmu dodeljevanja — pri čemer postopek ponavlja, dokler ni zadovoljen ali dokler ekonomika ne naredi nadaljevanja nesmiselnega.

> [!note] Družbeni graf
> Reputacijsko omrežje je predvsem družbeno omrežje. Dodajaš stike — ljudi, ki privolijo v povezavo. Ti imajo stike, in ti stiki imajo stike. Algoritem išče preveritelje znotraj nastavljive globine (npr. tri ravni: tvoji neposredni stiki, njihovi stiki in ena raven dlje). Nobena globalna veriga blokov ni potrebna — omrežje naravno oblikuje skupnosti s prekrivanji v druge skupnosti.
>
> Algoritem je nedeterministilen: zgošči tvoj dokument s trditvijo, zgoščeno vrednost preslika v položaj na obroču znanih identitet znotraj tega kroga in izbere najbližjo kot kandidata za preveritelja. Ne moreš predvideti ali vplivati na to, kdo bo preveril tvojo trditev.

Vsaka zavrnitev preveritelja poveča tvoj dokument in poveča strošek njegove obdelave — to je prvi cenovni kanal (rast dokumenta). Vsak nov preveritelj zaračuna plačilo glede na obseg podatkov, tvojo reputacijo in to, kako daleč vsebina tvoje trditve odstopa od njegove deklarirane politike preverjanja — to je drugi cenovni kanal (premija za tveganje). In vsaka iteracija stane čas in energijo — tretji cenovni kanal.

> [!note] Kaj preveritelj preverja in v kakšnem vrstnem redu
> Ko je izbran, preveritelj presoja trditev v grobem v štirih zaporednih korakih — najcenejši filtri najprej, dragi vsebinski pregledi nazadnje:
>
> 1. **Filtriranje po politiki.** Ali ta vrsta trditve sploh sodi v tisto, kar preveritelj javno preverja? Če ne, je zahteva takoj zavrnjena.
> 2. **Zaupanje v avtoriteto.** Ali je avtoriteta, ki je podprla trditev, po preveriteljevi lastni deklarirani politiki dovolj zaupanja vredna? Avtoriteta pod preveriteljevim pragom zaupanja je razlog za zavrnitev ne glede na vsebino trditve.
> 3. **Reputacija izdajatelja.** Ali izdajatelj izpolnjuje pragove reputacije, ki jih je preveritelj deklariral za to vrsto trditve? Nizka reputacija lahko bodisi zviša plačilo bodisi sproži zavrnitev.
> 4. **Preverjanje vsebine.** Šele ko prvi trije filtri prestanejo, preveritelj presoja trditev samo — podpise, notranjo doslednost, formalno pravilnost in to, kako daleč odstopa od preveriteljeve politike. Plačilo, zaračunano za ta zadnji korak, odraža dejansko prevzeto tveganje.
>
> Preveritelj objavi politiko, ki ureja vsakega od teh filtrov, tako da koraki niso stvar njegove presoje — vezan je na to, kar je že deklariral. Odstopanje od objavljene politike je samo po sebi objavljiva trditev proti njemu in zanjo plača s svojo reputacijo.

Rezultat: objava verodostojne in koristne trditve stane skoraj nič. Objava radikalne trditve stane več. Objava laži postane pretirano draga — iterirati moraš skozi preveritelja za preveriteljem, in vsak, ki te zavrne, doda stroške. Trg ovrednoti tvojo trditev, cena pa ti pove, kje stojiš v odnosu do skupnosti, po katerih se giblješ.

Ni dovolj deklarirati, da se držiš nekega pravila, ko se v resnici ne. V tem primeru tvoj DID tvega objavo negativnega zapisa, ki razkrije hinavščino — kar te spremeni v tveganje za vse druge. Izid naj bi bilo manj, a bolj dosledno upoštevanih pravil, in počiščenje tiste džungle zakonov in predpisov, po kateri se komaj znajdejo celo pravni strokovnjaki.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsenz proti odgovornosti
> Da bi omrežje služilo kot dragocen vir informacij, DID ne sme biti preveč radikalen — sicer ga bodo drugi zavrnili. Družbeni pritisk bo iskal ravnovesje, poskusi njegove destabilizacije pa bodo najverjetneje kaznovani.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Število glasov ni isto kot teža glasu
> Juraj Karpiš pravi, da je „denar spomin na dobra dejanja". Dodal bi, da je reputacija spomin na slaba.
>
> Iz tega sledi, da si meritokratsko tisti, ki prispeva več in nima slabe reputacije, zasluži večjo težo glasu v skupnosti. Gledano skozi prizmo dvostranskih odnosov: ko tehtam, katerim pritiskom za konsenz ustreči, gre največja teža odnosom, iz katerih črpam največjo ekonomsko korist. Deset ljudi, s katerimi nimam aktivne trgovine, bo name vplivalo veliko manj kot en stalni poslovni partner. Ta paradigma ni omejena na trgovino — razteza se na družbene, politične in druge odnose.
