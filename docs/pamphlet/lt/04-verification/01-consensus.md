---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsensusas ir patikros procesas

Kad būtų kuriamas konsensusas dėl to, kokias taisykles visuomenė vidutiniškai turėtų laikytis ir įgyvendinti, gali padėti toliau aprašytas mechanizmas. Kaip DID dalyvis deklaruoju taisykles, prie kurių prisirašau ir pagal kurias gyvensiu, ir jas paskelbiu. (Įsivaizduok tai kaip įstatus ir nuostatus, kurie, mano manymu, sudaro mano idealų pasaulį — pasaulį, kuriame jaučiuosi ne suvaržytas, o saugus.)

Galiu iš anksto įvertinti, kaip reaguotų mano DID kontaktai — ir įsivertinti, kaip stipriai ir kieno būčiau sankcionuojamas įprastose socialinėse ar verslo sąveikose, jei jos hipotetiškai įvyktų.

Galutinis įvertinimas įvyksta, kai prašai informacijos iš kitos DID arba paprašai jos patikrinti teiginį (arba paprašai autoriteto paslaugos ir taip toliau), kurį nori paskelbti reputacijos tinkle. Turėtų išeiti taip pat, kaip išeina, kai įvertinimą atlieki pats, sausąja eiga, pagal kitos šalies deklaruotą politiką — o jei ne, kažkas negerai kitos šalies pusėje: ji mėgina žaisti nesąžiningą žaidimą.

Rezultatas yra arba priėmimas su nurodyta patikros kaina (tikrintojo ar autoriteto paslaugų atveju), arba atmetimas. Tiek sankcijos, tiek premijos už nuokrypį nuo vertintojo politikos įtraukiamos į nurodytą kainą. Prašytojas tuomet sprendžia, ar priimti sąlygas, ar pereiti prie kito patikros rato paskirstymo algoritme — kartodamas procesą, kol bus patenkintas arba kol ekonomika padarys beprasmiška tęsti.

> [!note] Socialinis grafas
> Reputacijos tinklas yra pirmiausia socialinis tinklas. Prisideda kontaktų — žmonių, sutinkančių su ryšiu. Jie turi kontaktų, o tie kontaktai turi kontaktų. Algoritmas ieško tikrintojų konfigūruojamu gyliu (pvz., trys lygiai: tavo tiesioginiai kontaktai, jų kontaktai ir vienas lygis toliau). Jokios globalios blokų grandinės nereikia — tinklas natūraliai formuoja bendruomenes su persidengimais į kitas bendruomenes.
>
> Algoritmas yra nedeterministinis: jis apskaičiuoja tavo teiginio dokumento hash'ą, atvaizduoja hash'ą į poziciją žinomų tapatybių žiede šiame rate ir parenka artimiausią kaip kandidatą tikrintoją. Negali nuspėti ar paveikti, kas patikrins tavo teiginį.

Kiekvieno tikrintojo atmetimas padidina tavo dokumentą ir jo apdorojimo kaštą — tai pirmasis kaštų kanalas (dokumento augimas). Kiekvienas naujas tikrintojas ima mokestį, priklausantį nuo duomenų apimties, tavo reputacijos ir to, kaip toli tavo teiginio turinys nukrypsta nuo jo deklaruotos patikros politikos — tai antrasis kaštų kanalas (rizikos priedas). Ir kiekviena iteracija kainuoja laiką bei energiją — trečiasis kaštų kanalas.

> [!note] Ką tikrintojas tikrina ir kokia tvarka
> Parinktas tikrintojas teiginį įvertina maždaug keturiais nuosekliais žingsniais — pirma pigiausi filtrai, gale brangūs turinio patikrinimai:
>
> 1. **Politikos vartai.** Ar toks teiginys apskritai patenka į tai, ką tikrintojas viešai tikrina? Jei ne, užklausa iškart atmetama.
> 2. **Pasitikėjimas autoritetu.** Ar autoritetas, patvirtinęs teiginį, pakankamai patikimas pagal paties tikrintojo deklaruotą politiką? Autoritetas žemiau tikrintojo pasitikėjimo slenksčio yra pagrindas atmesti, nepaisant teiginio turinio.
> 3. **Išdavėjo reputacija.** Ar išdavėjas atitinka reputacijos slenksčius, kuriuos tikrintojas deklaravo šio tipo teiginiui? Žema reputacija gali arba padidinti mokestį, arba sukelti atmetimą.
> 4. **Turinio patikra.** Tik kai pirmieji trys vartai praeinami, tikrintojas įvertina patį teiginį — parašus, vidinį nuoseklumą, formalų teisingumą ir tai, kaip toli jis nukrypsta nuo tikrintojo politikos. Už šį paskutinį žingsnį imamas mokestis atspindi faktiškai prisiimtą riziką.
>
> Tikrintojas paskelbia politiką, valdančią kiekvienus iš šių vartų, tad žingsniai nėra jo nuožiūrai palikti — jį saisto tai, ką jis jau deklaravo. Nuokrypis nuo paskelbtos politikos pats yra skelbtinas teiginys prieš jį, ir jis už tai moka savo reputacija.

Rezultatas: patikimo ir naudingo teiginio paskelbimas kainuoja beveik nieko. Radikalaus teiginio paskelbimas kainuoja daugiau. Melo paskelbimas tampa neįkandamai brangus — turi iteruoti per tikrintoją po tikrintojo, ir kiekvienas, kuris tave atmeta, prideda kaštų. Rinka įkainoja tavo teiginį, o kaina pasako, kur stovi santykyje su bendruomenėmis, kuriose sukiesi.

Neužtenka deklaruoti, kad laikaisi taisyklės, kai iš tikrųjų nesilaikai. Tokiu atveju tavo DID rizikuoja neigiamo įrašo, atskleidžiančio veidmainystę, paskelbimu — o tai paverčia tave rizika visiems kitiems. Rezultatas turėtų būti mažiau, bet nuosekliau laikomasi taisyklių, ir tų įstatymų bei taisyklių džiunglių, kuriose vos susigaudo net teisės profesionalai, iškirtimas.

![VEIDMAINYSTĖ YRA BRANGIAUSIAS ELGESYS](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensusas prieš atskaitomybę
> Kad tinklas tarnautų kaip vertingas informacijos šaltinis, DID neturėtų būti pernelyg radikali — kitaip kiti ją atmes. Socialinis spaudimas ieškos pusiausvyros, o mėginimai ją destabilizuoti greičiausiai bus baudžiami.

![DEKLARUOK SAVO TAISYKLES, MOKĖK KAINĄ](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Balsų skaičius nėra tas pat kas balso svoris
> Juraj Karpiš sako, kad „pinigai yra gerų darbų atmintis“. Aš pridurčiau, kad reputacija yra blogųjų atmintis.
>
> Iš to seka, kad, meritokratiškai, kas prisideda daugiau ir neturi blogos reputacijos, nusipelno didesnio balso svorio bendruomenėje. Žiūrint per dvišalių santykių prizmę: kai sveriu, kuriuos konsensuso spaudimus pritaikyti, didžiausias svoris tenka santykiams, iš kurių gaunu didžiausią ekonominę naudą. Dešimt žmonių, su kuriais neturiu aktyvios prekybos, mane paveiks kur kas mažiau nei vienas nuolatinis verslo partneris. Ši paradigma neapsiriboja komercija — ji tęsiasi į socialinius, politinius ir kitus santykius.
