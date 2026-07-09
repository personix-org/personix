---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Stebėtojas

Stebėtojo vaidmuo pašalina tikrintojo paskatą lankstyti taisykles. Situacijose, kai tikrintojui nepatinka išdavėjo ar autoriteto užklausa, jis galėtų tiesiog nutylėti — neatsakyti ir užblokuoti algoritminę seką. Stebėtojas — arba stebėtojų aibė — stato savo reputaciją ant to, kad dokumentuoja, kaip tikrintojas buvo užklaustas. Jei tikrintojas nutyli, nepaisydamas deklaruotos politikos, sakančios kitaip, jį galima nuteisti už protokolo pažeidimą.

![STEBĖTOJAS — FIKSUOJA TIKRINTOJĄ](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mechanizmas: laiko žyma ir iššūkio kodas

Prieš siųsdamas teiginį tikrintojui, nukreipi jį per stebėtojus — žmones, kuriais pasitiki, arba specializuotus stebėjimo paslaugų teikėjus, imančius nedidelį mokestį. Kiekvienas stebėtojas gauna tavo pateiktį, pažymi ją laiko žyma, pasirašo, kad matė ją išsiunčiant, ir sugeneruoja iššūkio kodą — kriptografinį savo parašo hash'ą. Kodai pridedami prie tavo užklausos. Tikrintojas juos mato, bet neįsivaizduoja, kas yra stebėtojai ir ar kodai apskritai tikri. Stebėtojai tokiu būdu veikia kaip tarpininkai tarp išdavėjo ir tikrintojo, laikantys nepriklausomą įrašą, kad teiginys buvo pateiktas ir ką jis apėmė. Jų gali būti nuo nulio iki N.

Kai tikrintojas elgiasi sąžiningai — priimdamas ar atmesdamas pagal savo deklaruotą politiką — kodai lieka neperprantami. Niekas neatskleidžiamas.

Bet jei tikrintojas nutyli, nepaisydamas pritariančios politikos, arba atsako būdu, prieštaraujančiu tam, ką paskelbė, tu turi originalius stebėtojų parašus. Gali juos paskelbti kaip tarpininkų liudijimą, kad teiginys buvo pateiktas ir kad tikrintojas nesilaikė protokolo. Bet kas gali patikrinti, kad parašai atitinka iššūkio kodus.

## Kulminacija: tikrų stebėtojų tau nereikia

Ir štai elegantiškiausia dalis: **tikrų stebėtojų tau visai nereikia.** Gali sugeneruoti atsitiktinius skaičius, atrodančius lygiai kaip iššūkio kodai. Tikrintojas negali atskirti skirtumo — jam tenka mesti kauliuką, ar rizikuoti savo reputacija. Už kiekvienos gautos užklausos galėtų slypėti gerbiamas stebėtojas, stebintis inkognito — arba tai gali būti grynas triukšmas. Tikrintojas nežino. Ir tas neapibrėžtumas yra mechanizmas.

Sąžiningo spaudimo palaikymo kaštai: beveik nuliniai (atsitiktiniai skaičiai nemokami). Galimi nesąžiningumo kaštai tikrintojui: katastrofiški. Sąžiningas elgesys yra skatinamas net tada, kai iš tikrųjų niekas nestebi.

Sistema veikia todėl, kad kiekvienas šiek tiek paranojiškas. Neapibrėžtumas pigesnis nei sekimas.

![BLEFAS, IŠLAIKANTIS TIKRINTOJĄ SĄŽININGĄ](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Keli tikrintojai vienoje iteracijoje
> Sustiprinanti tikrintojų prieinamumo lydinčioji taisyklė gali būti algoritminis išplėtimas, grąžinantis vienoje iteracijoje kandidatų tikrintojų aibę, o ne tik vieną.
