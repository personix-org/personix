---
title: "Pojmovnik"
part: "Appendix"
lang: en
version: v6
---

# Pojmovnik

| Term | Hrvatski | Značenje |
|------|-------|---------|
| **Authority** | Autoritet | Pouzdan entitet (osoba, organizacija) koji provjerava informacije i ulaže u njih svoju reputaciju. Može biti specijaliziran (istražni, pravni, tehnički). |
| **Claim** | Tvrdnja | Općenito: bilo koja provjerljiva izjava. Ovdje: zapis objavljen u reputacijsku mrežu — tvrdnja o događaju, svojstvu ili odnosu koja je kriptografski potpisana i provjerena. Npr. „stanovnik sam općine X" ili „ova je osoba prekršila ugovor". |
| **Compartmentalization** | Kompartmentalizacija | Općenito: razdvajanje informacija u izolirane jedinice tako da izlaganje jedne jedinice ne ugrožava ostale. Načelo poznato iz obavještajnih službi. Ovdje: paralelni DID identiteti u diktaturama — kompromitiranje jednog ne otkriva druge. |
| **Consistent Hash Ring** | Konzistentni hash prsten | Algoritamski mehanizam za odabir verifikatora — pozicija na prstenu određena je hashom DID dokumenta unutar društvenog grafa. Osigurava nedeterministički, a ipak provjerljiv odabir. |
| **DID** | DID (Decentralizirani identitet) | Digitalni identitet koji sam stvaraš i sam njime upravljaš, bez središnjeg autoriteta. Kriptografski potpisan tvojim privatnim ključem — nitko ga ne može opozvati ni krivotvoriti. |
| **DID Document** | DID dokument | Javno dostupna podatkovna datoteka koja opisuje tvoj DID identitet — sadrži javne ključeve, mrežne adrese i metapodatke. Služi za provjeru tvojeg identiteta u mreži. |
| **Due Diligence** | Due diligence | Općenito: temeljita provjera druge strane prije stupanja u poslovni ili pravni odnos — provjera njezine povijesti, financija, reputacije i rizika. Ovdje: u reputacijskoj se mreži odvija brže i automatiziranije zahvaljujući dostupnosti provjerenih zapisa. |
| **Economic Neutrality Principle** | Načelo ekonomske neutralnosti | Pošteno je ponašanje u mreži ekonomski blizu nule — troškovi objavljivanja vraćaju se kao nagrade za provjeru. Nepošteno je ponašanje neto gubitak. |
| **Emergent** | Emergentno | Spontano nastajanje iz interakcija jednostavnijih dijelova, bez ičijeg dizajniranja ili usmjeravanja. Jato ptica leti u formaciji bez plana — formacija emergira iz jednostavnih pravila kojih se drži svaka jedinka. |
| **Emergent Social Contract** | Emergentni društveni ugovor | Pravila ponašanja koja ne nastaju odozgo (zakon), nego odozdo — iz opetovanih interakcija i konsenzusa unutar zajednice. |
| **ESR** | Elektronički registar rashoda | Predloženi sustav za transparentno praćenje javnih rashoda — svaki ostvareni državni rashod uparuje se s planiranim plaćanjem. Nadahnut češkim EET-om, ali okrenut protiv države. |
| **Hash** | Hash (otisak) | Općenito: jednosmjerna matematička funkcija koja iz bilo kojeg ulaza proizvodi jedinstveni „otisak" fiksne duljine — poput otiska prsta nekog dokumenta. Isti ulaz uvijek daje isti izlaz, ali se ulaz ne može izvesti iz izlaza. Ovdje: koristi se za određivanje pozicije na hash prstenu i za provjeru cjelovitosti dokumenta. |
| **Just-in-Time Funding** | Just-in-time financiranje | Financiranje države uvjetovano transparentnošću — novac teče tek kad država prihvati ESR i upari svoje rashode. Poluga za iznuđivanje suradnje. |
| **Meritocracy** | Meritokracija | Općenito: sustav u kojem položaj određuje stvarna zasluga i dokazana sposobnost, a ne formalne titule, veze ili naslijeđena povlastica. Ovdje: reputacijska mreža prirodno favorizira one koji dokazivo pridonose zajednici — njihov glas nosi veću težinu zbog track recorda, a ne zbog funkcije. |
| **Onion Gateway** | Onion gateway | Mrežna adresa DID identiteta na onion mreži. Odvojena od DID dokumenta — može se promijeniti bez gubitka identiteta (slično promjeni IP adrese iza domene). |
| **Onion Routing** | Onion routing (Tor) | Komunikacijski protokol koji osigurava necenzurabilnost mreže. Poruke su enkriptirane u slojevima — svaki čvor skida jedan sloj, ali ne poznaje cijeli put. |
| **Oracle Problem** | Problem proročišta | Općenito: kako osigurati da podaci koji ulaze u digitalni sustav vjerno odgovaraju onome što se stvarno dogodilo u fizičkom svijetu. Pojam potječe iz područja blockchaina. Ovdje: rješava se kroz autoritete koji stavljaju svoju reputaciju na kocku kao jamstvo da digitalni zapis odgovara fizičkoj stvarnosti. |
| **Phenomenological** | Fenomenološki | Općenito: pristup koji proučava pojave onako kako se očituju u izravnom iskustvu, promatrajući što iz njih slijedi, bez unaprijed zadanih teorija. Ovdje: sloboda, društveni ugovor i norme ponašanja promatrane su pojave — posljedice tisuća mikrointerakcija među ljudima, a ne načela definirana odozgo. |
| **Policy** | Policy (politika) | Općenito: skup pravila ili načela koja upravljaju ponašanjem u danom kontekstu. Ovdje: svaki sudionik u DID mreži deklarira svoju politiku — kako reagira na konkretno ponašanje drugih, kojih se pravila pridržava i koje kazne smatra razmjernima. Zbroj politika tvori emergentni društveni ugovor. |
| **Proxy** | Proxy | Općenito: zamjena ili posrednik — sustav ili entitet koji djeluje u ime drugoga. Ovdje se koristi u dva konteksta: (1) ESR kao proxy koji uparuje javne rashode s planiranim plaćanjima; (2) promatrači kao proxy između objavljivača i verifikatora u triku s promatračem. |
| **Publisher** | Objavljivač | Sudionik mreže koji stvara i objavljuje zapis (tvrdnju o nepravdi, popravljanju i tako dalje). Snosi trošak objavljivanja. |
| **Reputation-Based Social Network (RSN)** | Reputacijska mreža | Decentralizirana društvena mreža na kojoj sudionici razmjenjuju povratne informacije o ponašanju u stvarnom svijetu. Zapise je skupo stvarati, jeftino čitati. |
| **Reputation Signal** | Reputacijski signal | Pojedinačan zapis u mreži — pozitivan (popravljanje štete, ispunjenje obveze) ili negativan (nepravda, kršenje ugovora). Kumulativno, signali tvore reputacijski profil. |
| **Social Graph** | Društveni graf | Mreža tvojih kontakata i kontakata tvojih kontakata. Algoritam traži verifikatore na konfigurabilnoj dubini (primjerice 3 razine). Bez globalnog blockchaina — mreža prirodno tvori zajednice s preklapanjima. |
| **Tax Allocation** | Alokacija poreza | Mehanizam kojim porezni obveznik odlučuje kamo ide dio njegovih poreza. Postotak koji se može alocirati raste iz godine u godinu. |
| **Track Record** | Track record | Općenito: povijest prošlih rezultata, uspjeha i neuspjeha osobe ili organizacije. Ovdje: zbroj svih prošlih interakcija danog DID identiteta u mreži — provjerene tvrdnje, prihvaćeni i odbijeni zapisi — iz kojih se izvodi njegova reputacija. |
| **Verifier** | Verifikator | Sudionik algoritamski odabran da provjeri i objavi zapis. Ulaže svoje dobro ime u istinitost informacije. |
