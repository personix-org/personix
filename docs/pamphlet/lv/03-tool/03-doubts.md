---
title: "Addressing Obvious Doubts"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: "v1 callouts extended in v4"
---

# Acīmredzamo šaubu kliedēšana

Aprakstītā sistēma dabiski rada virkni jautājumu. Aplūkosim visizplatītākos.

## Atkarība no tehnoloģijām

Tu droši vien jau esi ievērojis, ka atšķirībā no modernās valsts — kas mums ir apmēram 150 gadus — šeit aprakstītais reputācijas tīkla risinājums lielā mērā ir atkarīgs no globālā/lokālā interneta tehnoloģijas. Traucējuma gadījumā šāda tīkla funkcionēšana ir apdraudēta.

Ja traucējums ir īslaicīgs, nezūd ne dati, ne apgalvojumu konsekvence tīklā, un arī kopienās sasniegtajiem reputācijas atlikumiem nevajadzētu tikt izjauktiem. Atšķirībā no salīdzināmiem maksājumu tīkliem šis tīkls paredz ļoti zemu procesu un datu vienību biežumu. Šajā ziņā decentralizētais reputācijas tīkls neatšķiras no šodienas valsts, kura arī tagad ir smagi atkarīga no tehnoloģijām un ir aizmirsusi, kā strādāt ar papīra kartotēkām (lai gan krīzes plānos tai nebūtu izvēles).

Valsts evolucionārais pēctecis reputācijas tīkla veidā pastāvīga traucējuma gadījumā (nepieredzēta mēroga katastrofa) var atgriezties pie primitīvākas centralizētas sistēmas — valsts.

Tehnoloģija ļauj cilvēcei sasniegt augstākas civilizācijas pārvaldes formas un nes mums ieguvumus, bet arī riskus.

## Vai, publicējot tīklā, es nemetu naudu pa logu?

Apgalvojuma publicēšanas izmaksas reputācijas tīklā lielākoties nav neatgriezeniskas. Publicētāja tīklā ieliktā vēstījuma noderīgums — informācija par reālām sūdzībām, pārbaudītu pieredzi, atbilstoši brīdinājumi — statistiski atgriežas ilgākā laika horizontā maksu veidā par kāda cita kopienas apgalvojuma verifikāciju. Kopiena gūst labumu, publicētājs veido reputāciju, un tādējādi patiesas informācijas publicēšanas izmaksas tuvojas atmaksājamai drošības naudai, no kuras jāatvelk tikai mazāka daļa faktisko tīkla uzturēšanas izmaksu. Turpretī nepatiesi vai nenozīmīgi ieraksti neatgriežas — to izmaksas ir tīri zaudējumi. Godīgums tādējādi ir ne tikai morāla izvēle, bet arī ekonomiski racionāla stratēģija.

Pēc tīkla uzturēšanas izmaksu atvilkšanas šo principu varētu saukt par ekonomiskās neitralitātes principu — es nezaudēju, kad esmu ar kopienu, es zaudēju, kad esmu pret to.

Kopienai ir arī solidaritātes kanāli, ar ko novērtēt savu locekļu godīgo pieeju. Bet nekļūdīsimies: aicinājumi uz solidaritāti lielākoties rodas no kopienas sociālā spiediena, tāpēc tā var nebūt solidaritāte vārda brīvprātīgajā nozīmē.

## Kā būs, ja kāds izveidos vairākas identitātes?

Cilvēks var paralēli darbināt vairākas DID identitātes. Tomēr reputācijas veidošana katrai identitātei prasa neatkarīgu piepūli — laiku, enerģiju, naudu.

Nekādu īsceļu: katrai identitātei jāuzkrāj sava track record[^trackrecord] ar faktisku darbību. Paralēlu identitāšu uzturēšana tāpēc ir apzināti dārga.

Brīvās sabiedrībās izmaksas attur no ļaunprātīgas izmantošanas.

Diktatūrās savukārt paralēlas identitātes kļūst par izdzīvošanas rīku: tās ļauj organizēt pagrīdes tīklus, drošāk orientēties melnajā tirgū un veidot kompartmentalizētu[^compartmentalization] pretestību, kurā vienas identitātes kompromitēšana neatklāj pārējās — un pēc režīma krišanas tās ļauj nemanāmi atgriezties publiskajā dzīvē un tur uzkrātajā reputācijā, un pat apvienot iepriekš oficiālo un slepeno DID vienā kombinētā ierakstu kopā ar apgalvojumu.

![WHAT IF SOMEONE CREATES MULTIPLE IDENTITIES?](../../Info%20Graphics/v5/v5-04a-vice-identit.webp)

> [!note] Uztvere apgriezta otrādi
> Atšķirībā no valsts, reputācijas tīkla princips, kas balstīts uz decentralizēto identitāti, apgriež uztvertās prioritātes paradigmu:
>
> - Svarīga ir reputācija — t. i., pagātne, ko izmanto, lai novērtētu mijiedarbības ar otru pusi riskus — un personas dati, piemēram, vārdi, adreses utt., var būt pieklājības datu apmaiņas jautājums
> - Turpretī valsts galvenokārt pieprasa personas datus, uzkrāj reputācijas datus un ļauj kopienai redzēt tikai to, kas tai izdevīgi

## Vai turīgs cilvēks nevar vienkārši “nopirkt” vairāk identitāšu (vai izveidot virtuālas kopienas)?

Iespēja izveidot paralēlas decentralizētas identitātes no pirmā skatiena izskatās pēc negodīgas priekšrocības cilvēkiem ar lielākiem ekonomiskajiem līdzekļiem pār tiem, kam to ir mazāk. Tomēr jāuzsver, ka atšķirībā no centralizētas sistēmas, kur pietiek uzpirkt dažus punktus varas piramīdā, lai noteikti pārkāpumi pazustu, decentralizētā sistēmā būtu jāuzpērk visa kopiena.

Aizvietojošas decentralizētas identitātes šim nolūkam varētu kalpot, taču to reputācija laika gaitā jāveido ar reālu mijiedarbību ar faktiskiem citiem kopienas locekļiem — to nevar vienkārši nopirkt, jo tīkls padara pārbaudāmu, kā konkrētajai identitātei klājas.

Turklāt tirgū var pastāvēt (un visdrīzāk pastāvēs) pakalpojumi, kas, darbojoties kā autoritāte, piedāvā izmeklēšanu, kas rada pierādījumus, ka vairākas decentralizētas identitātes patiesībā ir viens un tas pats cilvēks. Viens reputācijas tīklā ievadīts ieraksts tādējādi var par izmaksu daļiņu anulēt visu laika, enerģijas un naudas ieguldījumu, kas iztērēts paralēlu identitāšu veidošanai.

Ekonomiski tāpēc atmaksājas kopienu nekrāpt — un, ja vajadzīgs, izvērtēt savu rīcību un tiekties uz novēršanu, lai reputācija atgriežas pieņemamā līmenī un tās nesējs ekonomiski vai citādi neciestu no kopienas dusmām.

Ekonomiski spēcīga identitāte, kas savā kopienā zaudējusi reputāciju, var mēģināt izbēgt no kopienas dusmām caur necaurspīdīgiem darījumiem ar mērķtiecīgi izvēlētām identitātēm — bet tad arī tās riskē zaudēt savu reputāciju.

Vēl paliek bēgšana uz citu kopienu ar svaigu identitāti — bet tas nozīmē atstāt visus sasniegumus un sākt kaut kur no nulles ar nulles reputāciju. Reizēm tas var būt saprotams ceļš un vienīgā izeja.

![YOU CAN'T CORRUPT AN ENTIRE COMMUNITY](../../Info%20Graphics/v5/v5-04b-centralizace-vs-decentralizace.webp)

> [!note] Piezīme
> Līdzīgi kopienas rīkotos ar uzbrukumu, kurā kāds velta resursus virtuālas identitātes izveidei: šai identitātei ir riskanti iesaistīties mijiedarbībā ar citu kopienu bez verifikācijas — proti, nekritiski pieņemt informāciju par otras kopienas identitātēm. Reputācija vienmēr tiek veidota kopienas iekšienē, nevis globāli.

## Kā ar “braukšanu par velti” — tiem, kas grib tikai lasīt un neko nedot kopienai?

Piekļuve informācijai nav neierobežota jau no decentralizētās identitātes izveides pirmās dienas. Jauni dalībnieki — tie, kas vēl nav izveidojuši reputāciju ar faktisku darbību — saskaras ar pakāpeniskiem ierobežojumiem: mazāk informācijas, garāks gaidīšanas laiks, augstākas pieprasījumu izmaksas. Tīkls atalgo dalību, nevis pasīvu patēriņu un patvaļīgu datu novākšanu.

Decentralizēta identitāte riskē ar savu reputāciju arī tad, kad tā par samaksu aizdod savu reputāciju citam cilvēkam (kurš pat var nebūt DID reputācijas tīklā). Šeit spēkā ir tas pats princips: šāda nodevība pret kopienu (privātuma pārkāpums) var atspoguļoties nodevēja reputācijā, un darbību nevar izdzēst caur necaurspīdīgu darījumu, kā tas notiek centralizētā sistēmā. Viņam jārēķinās ar kopienas dusmām, tostarp sasniegumu zaudēšanu — jo kopiena viņa acīs ir garants, piemēram, kustamā un nekustamā īpašuma piederības privilēģijai.

> [!note] Enkurs pie reālās pasaules
> Novērtējot risku, riskantāks subjekts dabiski ir tas, kurš nebauda attiecīgās kopienas atzītu īpašuma privilēģiju — viņam savos darījumos ir mazāk ko zaudēt (digitālos aktīvus ir vieglāk pārvietot).
>
Tas var izskatīties pēc nelielas detaļas, bet tam ir lielas sekas. Vēlme, lai kopienai būtu sviras pār saviem locekļiem, paredz īpašumu kā privilēģiju — visbrīvākajās sabiedrībās gandrīz neaizskaramu, tomēr ne tiesības, ne pamatprincipu, bet privilēģiju, ko galējos gadījumos var atsaukt (varu iedomāties, piemēram, atteikšanos aizstāvēt kopienu bruņotā konfliktā).
>
Tas arī zemapziņā atbild uz to, kā kopiena izturēsies pret saviem locekļiem un kāda motivācija loceklim ir cīnīties par kopienu — lai saglabātu savas privilēģijas. Cilvēks var neizpildīt savu atbildību pret kopienu, bet morāli nevar gaidīt iecietību, kad runa ir par grūti nopelnītu privilēģiju saglabāšanu.

![THE NETWORK REWARDS PARTICIPATION](../../Info%20Graphics/v5/v5-04c-prizivnici.webp)

## Finansiālā neitralitāte

Lasot tādus vārdus kā decentralizēts, necenzējams, neuzpērkams, nevar nesaistīt tos ar pazīstamākajām kriptovalūtām — Bitcoin, Monero un, teiksim, Kaspa — kuras var raksturot ar šādiem vārdiem. Intuīcija te tomēr maldina: maksas par autoritāšu pakalpojumiem, par verifikāciju un publicēšanu utt. var kārtot jebkurā valūtā vai naudā. Kas svarīgi sociālā tīkla pievienotajiem dalībniekiem DID tīklā (proti, tavai kopienai) un tā apkārtnei, ir reputācijas atbalstīts apstiprinājums, ka maksājums ir veikts. Apgalvojuma publicēšanai atsevišķi jānes saprātīgas, pārbaudāmas izmaksas, lai dalībnieks nevarētu publicēt, cik un kādus vien apgalvojumus grib, netērējot enerģiju, naudu un laiku — stipri nevēlams stāvoklis, kas atbilst elites privilēģijai šodienas korupcijas pārņemtajās valsts sistēmās.

Šajā ziņā minētajām kriptovalūtām ir neliela priekšrocība tajā, ka to tīkli darbojas kā uzticamas autoritātes, kas apliecina, ka attiecīgais maksājums ir noticis, par nelielu privātuma zaudējumu un dažu savu adrešu atklāšanu.

[^trackrecord]: **Track record** — vispārīgi: cilvēka vai organizācijas pagātnes rezultātu, panākumu un neveiksmju vēsture. Šeit: visu attiecīgās DID identitātes pagātnes mijiedarbību tīklā summa — pārbaudīti apgalvojumi, pieņemti un noraidīti ieraksti — no kuras tiek atvasināta tās reputācija.

[^compartmentalization]: **Kompartmentalizācija** (no angļu *compartment*) nozīmē informācijas nodalīšanu izolētās vienībās tā, lai vienas vienības atklāšana neapdraud pārējās. Princips, kas pazīstams no izlūkdienestiem: aģents zina tikai savu operācijas daļu, tāpēc pat spiediena apstākļos nevar atklāt visu kopumu.
