---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Novērotājs

Novērotāja loma novērš verificētāja stimulu locīt noteikumus. Situācijās, kad verificētājam nepatīk izdevēja vai autoritātes pieprasījums, viņš varētu vienkārši klusēt — neatbildēt un bloķēt algoritmisko secību. Novērotājs — vai novērotāju kopa — liek uz spēles savu reputāciju par to, ka dokumentē, kā verificētājam tika vaicāts. Ja verificētājs klusē, neraugoties uz deklarētu politiku, kas saka pretējo, viņu var notiesāt par protokola pārkāpšanu.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mehānisms: laika zīmogs un izaicinājuma kods

Pirms tu nosūti apgalvojumu verificētājam, tu virzi to caur novērotājiem — cilvēkiem, kuriem uzticies, vai specializētiem novērotāja pakalpojumu sniedzējiem, kas iekasē nelielu maksu. Katrs novērotājs saņem tavu iesniegumu, apzīmogo to ar laika zīmogu, paraksta, ka redzēja to izejam, un ģenerē izaicinājuma kodu — sava paraksta kriptogrāfisku jaucējkodu. Kodi tiek pievienoti tavam pieprasījumam. Verificētājs tos redz, bet viņam nav ne jausmas, kas ir novērotāji un vai kodi vispār ir īsti. Novērotāji tādējādi darbojas kā starpnieki (proxy) starp izdevēju un verificētāju, turot neatkarīgu ierakstu, ka apgalvojums tika iesniegts un ko tas saturēja. Tos var būt no nulles līdz N.

Kad verificētājs uzvedas godīgi — pieņemot vai noraidot saskaņā ar savu deklarēto politiku — kodi paliek necaurredzami. Neviens netiek atklāts.

Bet, ja verificētājs klusē, neraugoties uz pieņemošu politiku, vai atbild veidā, kas ir pretrunā ar publicēto, tu turi oriģinālos novērotāju parakstus. Tu vari tos publicēt kā starpnieka liecību, ka apgalvojums tika iesniegts un ka verificētājs neievēroja protokolu. Ikviens var pārbaudīt, ka paraksti sakrīt ar izaicinājuma kodiem.

## Puante: tev nav vajadzīgi īsti novērotāji

Un šeit ir viselegantākā daļa: **tev vispār nav vajadzīgi īsti novērotāji.** Tu vari ģenerēt gadījuma skaitļus, kas izskatās tieši kā izaicinājuma kodi. Verificētājs nevar pamanīt atšķirību — viņam jāmet kauliņš par to, vai riskēt ar savu reputāciju. Aiz katra pieprasījuma, ko viņš saņem, varētu būt cienījams novērotājs, kas skatās inkognito — vai arī tas var būt tīrs troksnis. Verificētājs to nezina. Un šī nenoteiktība ir mehānisms.

Godīga spiediena uzturēšanas izmaksas: gandrīz nulle (gadījuma skaitļi ir bez maksas). Negodīguma iespējamās izmaksas verificētājam: katastrofālas. Godīga uzvedība tiek stimulēta pat tad, kad neviens patiešām neskatās.

Sistēma darbojas tāpēc, ka ikviens ir mazliet paranoisks. Nenoteiktība ir lētāka par uzraudzību.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Vairāki verificētāji vienā iterācijā
> Pastiprinošs pavadonoteikums verificētāja pieejamībai var būt algoritmisks paplašinājums, kas vienā iterācijā atgriež kandidātverificētāju kopu, nevis tikai vienu.
