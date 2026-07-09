---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificētājs

Jebkurš DID var darboties kā verificētājs, vai nu tieši, vai caur verifikācijas tiesībām, kas deleģētas trešajam DID. Lai es — vai mans deleģāts — spētu verificēt, man vajadzētu būt sasniedzamam tīklā (tiešsaistē). Ne visi gribēs tam apņemties, tāpēc DID ierakstā prioritātes secībā var uzskaitīt aizvietotājus, kas pildīs funkciju tā vietā, kamēr tas ir bezsaistē.

Katrs tīklā aktīvs DID publiski deklarē savu politiku. Ar šajā politikā definētajiem noteikumiem tas verifikācijas procesā vērtē otras puses reputāciju un tā apgalvojuma saturu un formu, ko izdevējs ir atzīmējis publicēšanai reputācijas tīklā. Daļa no politikas ir aprēķina formula, ko izmanto maksu par verifikācijas pakalpojumiem aprēķināšanai. Kad tas ir vietā, tad statistiski lielā skaitā apgalvojumu, kas plūst caur tīklu, es gaidu, kamēr tīkla algoritms izvelk mani izdevēja pusē un piešķir man attiecīgajā iterācijā verificēt izsniedzamo informāciju. Izdevējs var iepriekš aprēķināt, kā reaģētu pareizi uzvedošs verificētājs, bet nevar izvairīties no faktiskas sazināšanās ar viņu (vai viņa aizvietotājiem); iterācija ar izvēlēto verificētāju izdevējam jāizpilda pat tad, kad viņš iepriekš zina, ka tā neizies cauri.

Kā mēs zinām, ka izdevējs palaiž verificētāja atlases algoritmu pār pareizo kandidātverificētāju DID kopu? Līdz ar savu publiski deklarēto politiku katrs DID publicē arī aktuālo sava sociālā tīkla identifikatoru sarakstu reputācijas tīklā. Ja izdevējs definē savu sociālo tīklu kā sociālu burbuli, kas tikai atkārto un pastiprina viņa paša uzskatus, caur to publicētā informācija diez vai tiks plašāk uztverta citās kopienās. Tas, ka man par augstu cenu izdodas iespiest tīklā radikālu apgalvojumu, nenozīmē, ka, vērtējot otras puses reputāciju, es tam piešķiršu jebkādu svaru. Dažus apgalvojumus mani spiež ņemt vērā mana kopiena (pārkāpējiem piespriestie sodi un ierobežojumi); citi ir pilnībā manā ziņā — es pats izlemju attiecīgās informācijas iekļaušanas vai izslēgšanas ekonomisko vērtību.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
