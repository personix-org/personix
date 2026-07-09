---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputācijas sociālais tīkls

Lai īstenotu pārmaiņas, mums vajadzīgs rūpīgi izstrādāts rīks. Vispirms to īsi ieskicēsim; vēlākajās nodaļās katru daļu aplūkosim sīkāk un pievienosim vairāk. Iedomājies necenzējamu, globālu, decentralizētu sociālo tīklu, kurā tu varētu droši izveidot un pārvaldīt savu starpniekidentitāti — tā saukto decentralizēto identitāti (DID). DID ir digitāla identitāte, ko tu izveido un kontrolē pats, bez atkarības no kādas centrālas autoritātes. Neviens to nevar atņemt vai viltot, jo tā ir kriptogrāfiski parakstīta ar tavu privāto atslēgu (vai atslēgām, izmantojot multisig).

> [!note] Piezīme
> Viena no sekām ir tā, ka šāda identitāte pakāpeniski varētu aizstāt valsts izsniegtos identifikācijas dokumentus — bet par to vairāk nodaļā par pāreju.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Šādā tīklā tu caur savu identitāti varētu ziņot, ka kāds tev ir nodarījis kaitējumu (un vēlāk, iespējams, ka viņš to ir novērsis vai bijis spiests to darīt). Lai šai atgriezeniskajai saitei — vērstai pret kaitējuma izraisītāju — būtu vērtība kā atbilstošam avotam, informācijas ievadīšanai tīklā jāmaksā laiks, enerģija un nauda — un turklāt citiem jāsagatavo pārbaudāms pierādījums, ka tā nav tukša pļāpāšana.

Informācijas lasīšana būtu viegla un salīdzinoši lēta, bet atsevišķa ieraksta izveide būtu dārga un prasīga. Rakstīšana notiktu pēc skaidra protokola, kurā aprēķini saskaņā ar izvēlēto algoritmu stingri nosaka, kuram DID lūgt iesniegtās informācijas verifikāciju un kā rīkoties tā, lai izvēlētais dalībnieks apstrādā informāciju tavā vārdā, publicē to un kļūst par tās verificētāju.

> [!note] Algoritms pret radikālismu
> Verificētāju algoritmiska atlase nodrošina, ka neradikāli informācijas publicētāji ilgākā laikā uzturēs gandrīz neitrālu līdzsvaru starp publicētās informācijas izmaksām un atlīdzību par verifikāciju.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Aplūkosim, kā algoritms izvēlas verificētāju.

> [!note] Algoritms
> Algoritmiskā atlase nedeterministiski izvēlas atšķirīgu verificētāju (vai iespējamo verificētāju kopu) dažādām informācijas vienībām. Pilnā DID dokumenta jaucējkods (hash — vienvirziena matemātiska funkcija, kas no jebkuras ievades rada unikālu “nospiedumu” — līdzīgi dokumenta pirkstu nospiedumam) nosaka pozīciju uz konsekventā jaucējgredzena (hash ring) un izvēlas verificētāju kandidātus.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Vienkāršā valodā: algoritms paņem visu tavu DID dokumentu, aprēķina no tā nospiedumu, un šis nospiedums nosaka tavu verificētāju.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Ar pirmo verificētāju, ko algoritms izvēlas, tev kā publicētājam var neizdoties — tava reputācija vai deklarētie iestatījumi var neatbilst viņa prasībām. Tu algoritmiski turpinātu meklēt nākamo, veicot vēl vienu rekursīvu iterāciju, kas tev piešķir tālāku verificētāju. Ar katru soli “attālums” līdz mērķa verificētājam pieaug, un līdz ar to arī pavadošie metadati, kas jāpublicē. Datiem pieaugot, izmaksas dabiski ceļas (ne tikai apgalvojuma sākotnējā apjoma dēļ, bet arī tāpēc, ka ar katru noraidījumu metadati uzkrājas). Ticama informācija iziet daudz vieglāk nekā bezjēdzīgas iegribas. Katra paša ziņā ir, cik augstu cenu viņš gatavs uzņemties un cik ieraksts viņam ir svarīgs — radikālisms garantēti kļūs dārgs.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Lai ko verificētājs izlemtu, atbildot uz tavu verifikācijas pieprasījumu, bumba atkal ir publicētāja pusē: viņš var pieņemt verificētāja piedāvājumu par verifikācijas pakalpojumiem, ievīt atbildi hronoloģijā un mēģināt vēlreiz (dārgāk) vai aiziet un norīt jau ieguldītās izmaksas.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Lai piešķirtu savai informācijai lielāku svaru un labākas izredzes tikt pieņemtai pie verificētājiem, tu — kā publicētājs, kurš ir ieinteresēts izsniedzamajā informācijā — varētu izmantot **uzticamas autoritātes** pakalpojumus. Autoritāte iesniegto informāciju vai nu noraida, vai pieņem un liek uz spēles savu labo vārdu (reputāciju). Autoritāte parasti pieprasa reālus pierādījumus, tos pārbauda un klasificē. Rezultāts ir protokols par tās vērtējumu attiecīgajā lietā attiecīgajā laikā. Iedomājies autoritāti kā noteikta veida pakalpojuma speciālistu gan reālajā, gan digitālajā pasaulē — piemēram, izmeklētāju, auditoru, apdrošinātāju, noteiktas preču klases piegādātāju (būtībā jebkuru ekonomisko dalībnieku tirgū).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Kad tu mēģināsi publicēt informāciju tīklā, tas visdrīzāk jau saturēs informāciju par saviem dalībniekiem — tie ir reputācijas signāli. Orientēšanās tajā, kā lasīt reputācijas signālus — ko tie tev nozīmē dažādās situācijās un kādus riskus tie nes — var nebūt triviāla. Katrs dalībnieks var uz reputācijas ierakstiem raudzīties caur savu DID atšķirīgi, atkarībā no situācijas, ko viņš risina attiecībā uz otru pusi. Vai otra puse ir uzticams maksātājs, vai man biznesa darījumā jāpieprasa nauda avansā? Vai piedāvātā prece nes atsauksmes par slēptu krāpšanu vai defektiem? Vai viņi mēģina izlocīties no līgumiskās atbildības, kad kaut kas noiet greizi? Reizēm noder sarežģītāks skatījums uz otras puses vispārējo konsekvenci — tas atkarīgs no tā, kurš pārskatu pieprasa. Tirgus varētu piedāvāt produktus un pakalpojumus, kas vienkāršo, apstrādā un noskaidro reputācijas lasīšanu attiecīgās situācijas kontekstā. Šim nolūkam var kalpot arī dažādas autoritātes un to piedāvātie pakalpojumi.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Piemēri
> Tipiska informācija, kas interesē publicētājus — un ir vērtīga citiem — attiecas uz notikumiem ārpus parastās starpcilvēku saziņas reālajā vai virtuālajā pasaulē.
>
> Negatīvi piemēri:
> - pierādījumi par noziedzīgiem nodarījumiem (piem., ko auditējusi uzticama izmeklēšanas iestāde)
> - netieši pierādījumi (paši par sevi vāji, bet statistiski kumulatīvi) — piem., atkārtota klātbūtne vairāku zādzību tuvumā īsā laikā → vai vēl sakritība?
> - līguma pārkāpums
>
> Pozitīvi piemēri:
> - novērsts kaitējums (brīvprātīgi vai kopienas spiediena rezultātā kā sods)
> - autoritātes X piedāvāta soda pieņemšana un izciešana
> - autoritāte X noteiktā mērā atsauca pārkāpēja īpašuma tiesību atzīšanu
>
> Katra paša ziņā ir savākt pieejamo informāciju par otru pusi un izvērtēt riskus pēc savām vēlmēm.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Vai informācija par tevi parādās tīklā, ir atkarīgs vienīgi no tavas paša uzvedības.
> Tev nekad nav jāpievienojas šādam tīklam, tomēr informācija par tevi tajā var parādīties. Tas ir atkarīgs vienīgi no tavas rīcības un tās ietekmes uz citiem.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Tas, ko tikko īsi ieskicēju, ir tas, kā varētu darboties sociālais tīkls, kura iedvesmas avots ir decentralizētā identitāte (DID). DID koncepciju galvenais mērķis ir stiprināt privātumu un brīvību caur principu, ka es apņemos noteikumus, kurus ievērošu un pēc kuriem dzīvošu — dodot lietotājiem iespēju izlemt, kādu informāciju dalīt un ar kādiem nosacījumiem.

Es piedāvāju DID tālāk savienot komunikācijas tīklā, kurā to turētāji apmainās ar atgriezenisko saiti pat ārpus situācijām, kad kādam kaut kas ir noticis un kopienai vai indivīdam jāreaģē. Šāds preventīvs to noteikumu salīdzinājums, kurus esam parakstījuši — ar iespēju aprēķināt ekonomiskās un citas sekas savstarpējām novirzēm gaidās par to, kā otrai pusei būtu jādarbojas — varētu tikt uzskatīts par motivāciju meklēt konsensu. Brīvības vietā šāda sistēma uzsvērtu brīvprātīgu lēmumu pieņemšanu apvienojumā ar atbildību par uzvedību reālajā pasaulē.

Indivīds vienatnē sistēmu salauzt nespēj — cilvēku grupai ir lielākas izredzes, un cilvēku grupai ar izcīnītu konsensu un motivāciju vilkt kopā daudzos jautājumos ir vēl lielākas izredzes pretoties autoritārām tendencēm. Organizācijas priekšnoteikums no pirmās nodaļas tiks izpildīts, tiklīdz būs izpildīti divi nosacījumi: DID reputācijas tīkls pietiekami reprezentatīvi aptvers kopienas, ka tā lietošana pārstās būt eksotiska. Un vienlaikus šis kopienas segments kļūs par ekonomiski nozīmīgu minoritāti, kas var pašpārliecināti risināt sarunas ar pārējo sabiedrību.

> [!note] Brīvprātība pret brīvību
> Brīvība — pozitīvā nozīmē — būtu sekundārs efekts divu faktoru līdzsvarošanai: brīvprātības un apkārtējās vides spiediena uz atbildību.

> [!note] MI laikmets un reputācijas vērtība
> Mākslīgā intelekta laikmetā viss, kas saistīts ar kognitīvo domāšanu, tiek automatizēts — un tas var iet vēl tālāk. Kas tad cilvēka darbībā paliek kā konkurences priekšrocība? Atbilde ir grūta, un kaut kas noteikti tiks atrasts, bet vienu varam pateikt droši: izšķirs reputācija. Pārbaudāma tavas uzvedības vēsture, tavas saistības un to izpilde — tas ir kaut kas, ko MI tev neuzbūvēs.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
