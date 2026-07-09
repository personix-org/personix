---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Preveritelj

Kateri koli DID lahko deluje kot preveritelj, bodisi neposredno bodisi prek pravic preverjanja, delegiranih tretjemu DID. Da bi jaz — ali moj delegat — lahko preverjal, moram biti dosegljiv na omrežju (na spletu). Ne bo se vsak želel zavezati k temu, zato lahko zapis DID v vrstnem redu prednosti navede nadomestne osebe, ki bodo funkcijo opravljale v njegovem imenu, dokler je brez povezave.

Vsak DID, aktiven v omrežju, javno deklarira svojo lastno politiko. Skozi pravila, opredeljena v tej politiki, med postopkom preverjanja presoja reputacijo nasprotne strani ter vsebino in obliko trditve, ki jo je izdajatelj označil za objavo v reputacijsko omrežje. Del politike je izračunska formula, uporabljena za izračun plačil za storitve preverjanja. Ko je to vzpostavljeno, potem skozi statistično veliko število trditev, ki tečejo skozi omrežje, čakam, da me algoritem omrežja izžreba na strani izdajatelja in mi v dani iteraciji dodeli preverjanje informacije, ki se izdaja. Izdajatelj lahko vnaprej izračuna, kako bi se odzval pravilno delujoč preveritelj, a se ne more izogniti temu, da bi ga (ali njegove nadomestne osebe) dejansko kontaktiral; iteracijo z izbranim preveriteljem mora izdajatelj izvesti tudi takrat, ko vnaprej ve, da ne bo prestala.

Kako vemo, da izdajatelj poganja algoritem izbire preveritelja nad pravilnim naborom kandidatnih DID-ov preveriteljev? Skupaj s svojo javno deklarirano politiko vsak DID objavi tudi trenutni seznam identifikatorjev svojega družbenega omrežja znotraj reputacijskega omrežja. Če izdajatelj svoje družbeno omrežje opredeli kot družbeni mehurček, ki le odmeva in krepi njegove lastne poglede, bodo druge skupnosti informacije, objavljene skozenj, komaj širše sprejele. Dejstvo, da mi z visokimi stroški uspe potisniti radikalno trditev v omrežje, ne pomeni, da ji bom pri presojanju reputacije nasprotne strani pripisal kakršno koli težo. Nekatere trditve me skupnost sili upoštevati (kazni in omejitve, naložene storilcem); druge so povsem prepuščene meni — sam se odločim o ekonomski vrednosti vključitve ali izključitve dane informacije.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
