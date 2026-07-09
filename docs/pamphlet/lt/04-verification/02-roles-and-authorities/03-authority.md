---
title: "Authority"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Autoritetas

Autoritetas atlieka dvejopą vaidmenį: jis gali būti **auditorius** (patikrinantis įrodymų kokybę prieš paskelbiant teiginį) arba **garantas** (statantis savo reputaciją ant teiginio teisingumo). Bet kuriuo atveju jis sustiprina išdavėjo teiginį. Šios dvi paslaugos yra atskiriamos — autoritetas gali siūlyti vieną, kitą arba abi iš karto. Darbinė prielaida yra ta, kad daugumą autoritetų teikiamų paslaugų galima pristatyti laisvosios rinkos pagrindu. Tai galioja net srityse, kurias sunku įsivaizduoti privatizuotas, tokiose kaip teisingumas, kur specializuotas paslaugas — tyrimą, įrodymų vertinimą, iki pat paslaugų, kurias šiandien teikia centralizuotos armijos (strateginis planavimas, standartizuotas mokymas, viešieji pirkimai ir atsargų valdymas ir t. t.) — gali efektyviai pristatyti rinkos veikėjai. Vargu ar yra kas nors, ko, pertvarkius, negalima būtų padaryti efektyvesnio laisvosios rinkos paskatomis.

> [!warning] Autoritetas, išdavėjas ir stebėtojas niekada negali būti savo paties atvejo tikrintoju.
> Algoritminė tikrintojo atranka garantuoja nepriklausomumą. Niekas negali patikrinti savo paties teiginio ar teiginio, kuriuo turi tiesioginį interesą. Tai viena iš pagrindinių taisyklių, kurios laikytis suinteresuota visa DID bendruomenė.

Toliau esantys grafikai rodo papildančius autoritetų aprėpiamos veiklos platumo vaizdus (terminą „autoritetas“ galima skaityti kaip lygiavertį „paslaugų teikėjui“).

![AUTORITETAS — KAS STATO SAVO VARDĄ](../../../Info%20Graphics/v5/v5-08d-role-authority.webp)

![DU AUTORITETO VEIDAI](../../../Info%20Graphics/v5/v5-08a-autorita-auditor-garant.webp)

> [!note] Autoritetas kaip inkognito stebėtojas
> Reputaciją turintis autoritetas — įsivaizduok notarą, kurio verslas priklauso vien nuo jo pasiekimų istorijos — gali, greta pagrindinių funkcijų (auditorius / garantas), pasiūlyti trečiąją: inkognito stebėtojo vaidmenį patikros metu. Jis saugo laiko žyma pažymėtą pateikto teiginio įrašą, kad tikrintojas negalėtų jo tyliai numesti. Stebėtojo vaidmens mechanizmas aprašytas toliau skiltyje apie Stebėtojo vaidmenį.
