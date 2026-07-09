---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsenss un verifikācijas process

Lai veidotu konsensu par to, kurus noteikumus sabiedrībai vidēji vajadzētu uzturēt un ieviest, var palīdzēt šāds mehānisms. Kā DID dalībnieks es deklarēju noteikumus, kuriem parakstos un pēc kuriem dzīvošu, un tos publicēju. (Iedomājies to kā tos iekšējos statūtus un noteikumus, kas, manuprāt, veido manu ideālo pasauli — pasauli, kurā es nejūtos ierobežots, bet drošs.)

Es varu iepriekš aptuveni novērtēt, kā manas DID kontaktpersonas reaģētu — un izvērtēt, cik stipri un kas mani sodītu parastā sociālā vai biznesa mijiedarbībā, ja tā hipotētiski notiktu.

Galīgais vērtējums notiek, kad tu pieprasi informāciju no cita DID vai lūdz to verificēt apgalvojumu (vai lūdz autoritātei pakalpojumu utt.), ko vēlies publicēt reputācijas tīklā. Tam vajadzētu iznākt tāpat, kā iznāk, ja vērtējumu palaid pats, izmēģinājuma režīmā, pret otras puses deklarēto politiku — un, ja tā neiznāk, kaut kas otras puses pusē nav kārtībā: viņi mēģina spēlēt negodīgu spēli.

Iznākums ir vai nu pieņemšana ar norādītu cenu par verifikāciju (verificētāja vai autoritātes pakalpojumu gadījumā), vai noraidījums. Gan sankcijas, gan bonusi par novirzi no vērtētāja politikas tiek ievīti norādītajā cenā. Pieprasītājs tad izlemj, vai pieņemt nosacījumus, vai pāriet uz nākamo verifikācijas kārtu atlases algoritmā — atkārtojot procesu, līdz apmierināts vai līdz ekonomika padara turpināšanu bezjēdzīgu.

> [!note] Sociālais grafs
> Reputācijas tīkls pirmām kārtām ir sociāls tīkls. Tu pievieno kontaktpersonas — cilvēkus, kas piekrīt savienojumam. Viņiem ir kontaktpersonas, un tām kontaktpersonām ir kontaktpersonas. Algoritms meklē verificētājus konfigurējamā dziļumā (piem., trīs līmeņi: tavas tiešās kontaktpersonas, viņu kontaktpersonas un vēl viens līmenis tālāk). Nav vajadzīga globāla blokķēde — tīkls dabiski veido kopienas ar pārklāšanos citās kopienās.
>
> Algoritms ir nedeterministisks: tas jauc tavu apgalvojuma dokumentu, kartē jaucējkodu uz pozīciju zināmo identitāšu gredzenā šajā lokā un izvēlas tuvāko kā kandidātverificētāju. Tu nevari paredzēt vai ietekmēt, kas verificēs tavu apgalvojumu.

Katrs verificētāja noraidījums palielina tavu dokumentu un ceļ tā apstrādes izmaksas — tas ir pirmais izmaksu kanāls (dokumenta augšana). Katrs jaunais verificētājs iekasē maksu, balstoties uz datu apjomu, tavu reputāciju un to, cik tālu tava apgalvojuma saturs novirzās no viņa deklarētās verifikācijas politikas — tas ir otrais izmaksu kanāls (riska prēmija). Un katra iterācija maksā laiku un enerģiju — tas ir trešais izmaksu kanāls.

> [!note] Ko verificētājs pārbauda, un kādā secībā
> Reiz izvēlēts, verificētājs izvērtē apgalvojumu aptuveni četros sakārtotos soļos — vislētākie filtri vispirms, dārgās satura pārbaudes pēdējās:
>
> 1. **Politikas vārti.** Vai šāda veida apgalvojums vispār ietilpst tajā, ko verificētājs publiski verificē? Ja nē, pieprasījums tiek tūlīt noraidīts.
> 2. **Uzticēšanās autoritātei.** Vai autoritāte, kas apstiprināja apgalvojumu, saskaņā ar verificētāja paša deklarēto politiku ir pietiekami uzticama? Autoritāte zem verificētāja uzticēšanās sliekšņa ir pamats noraidījumam neatkarīgi no apgalvojuma satura.
> 3. **Izdevēja reputācija.** Vai izdevējs atbilst reputācijas sliekšņiem, ko verificētājs deklarējis šāda veida apgalvojumam? Zema reputācija var vai nu celt maksu, vai izraisīt noraidījumu.
> 4. **Satura pārbaude.** Tikai tad, kad pirmie trīs vārti ir izieti, verificētājs izvērtē pašu apgalvojumu — parakstus, iekšējo konsekvenci, formālo pareizību un to, cik tālu tas novirzās no verificētāja politikas. Maksa par šo pēdējo soli atspoguļo faktiski uzņemto risku.
>
> Verificētājs publicē politiku, kas pārvalda katrus no šiem vārtiem, tāpēc soļi nav viņa ziņā — viņu saista tas, ko viņš jau deklarējis. Novirze no publicētās politikas pati par sevi ir publicējams apgalvojums pret viņu, un viņš par to maksā ar savu reputāciju.

Rezultāts: ticama un noderīga apgalvojuma publicēšana maksā gandrīz neko. Radikāla apgalvojuma publicēšana maksā vairāk. Meli kļūst pārmērīgi dārgi — tev jāiterē cauri verificētājam pēc verificētāja, un katrs, kas tevi noraida, pievieno izmaksas. Tirgus nosaka cenu tavam apgalvojumam, un cena tev pasaka, kur tu stāvi attiecībā pret kopienām, kurās pārvietojies.

Nepietiek deklarēt, ka tu ievēro noteikumu, kad patiesībā to nedari. Tādā gadījumā tavs DID riskē ar negatīva ieraksta publicēšanu, kas atmasko liekulību — kas tevi padara par risku visiem citiem. Iznākumam vajadzētu būt mazāk, bet konsekventāk ievērotiem noteikumiem un tā likumu un regulējumu džungļa iztīrīšanai, kurā tikko spēj orientēties pat juristi.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsenss pret atbildību
> Lai tīkls kalpotu kā vērtīgs informācijas avots, DID nedrīkstētu būt pārāk radikāls — citādi citi to noraidīs. Sociālais spiediens meklēs līdzsvaru, un mēģinājumi to destabilizēt visdrīzāk tiks sodīti.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Balsu skaits nav tas pats, kas balss svars
> Juraj Karpiš saka, ka “nauda ir labo darbu atmiņa”. Es piebilstu, ka reputācija ir slikto darbu atmiņa.
>
> No tā izriet, ka meritokrātiski tas, kurš dod vairāk un kam nav sliktas reputācijas, pelna lielāku balss svaru kopienā. Skatoties caur divpusēju attiecību prizmu: kad es sveru, kuriem konsensa spiedieniem piekāpties, vislielākais svars ir tām attiecībām, no kurām gūstu vislielāko ekonomisko labumu. Desmit cilvēki, ar kuriem man nav aktīvas tirdzniecības, ietekmēs mani daudz mazāk nekā viens pastāvīgs biznesa partneris. Šī paradigma neaprobežojas ar tirdzniecību — tā attiecas arī uz sociālajām, politiskajām un citām attiecībām.
