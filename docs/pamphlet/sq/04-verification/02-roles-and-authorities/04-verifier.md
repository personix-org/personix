---
title: "Verifikuesi"
chapter: 3
part: "Si funksionon verifikimi"
lang: en
version: v6
---

# Verifikuesi

Çdo DID mund të veprojë si verifikues, qoftë drejtpërdrejt qoftë përmes të drejtave të verifikimit të deleguara te një DID i tretë. Që unë — ose i deleguari im — të mund të verifikoj, duhet të jem i arritshëm në rrjet (online). Jo të gjithë do të duan të angazhohen për këtë, prandaj një regjistrim DID mund të listojë, në rend prioriteti, zëvendësuesit që do ta kryejnë funksionin në emrin e tij ndërkohë që ai është offline.

Çdo DID aktiv në rrjet shpall publikisht politikën e vet. Përmes rregullave të përcaktuara në atë politikë ai gjykon, gjatë procesit të verifikimit, reputacionin e palës tjetër dhe përmbajtjen e formën e pohimit që lëshuesi ka shenjuar për publikim në rrjetin e reputacionit. Pjesë e politikës është formula e llogaritjes që përdoret për të llogaritur tarifat për shërbimet e verifikimit. Sapo kjo të jetë vendosur, atëherë përgjatë një numri statistikisht të madh pohimesh që rrjedhin nëpër rrjet unë pres që algoritmi i rrjetit të më zgjedhë nga ana e lëshuesit dhe të më caktojë, në një iteracion të dhënë, të verifikoj informacionin që po lëshohet. Lëshuesi mund të llogarisë paraprakisht si do të reagonte një verifikues që sillet saktë, por nuk mund ta shmangë kontaktimin real me të (ose me zëvendësuesit e tij); iteracioni me verifikuesin e përzgjedhur duhet të kryhet nga lëshuesi edhe kur e di paraprakisht se s’do të kalojë.

Si e dimë që lëshuesi e ekzekuton algoritmin e përzgjedhjes së verifikuesit mbi grupin e saktë të DID-eve kandidate verifikuese? Së bashku me politikën e vet të shpallur publikisht, çdo DID publikon edhe listën aktuale të identifikuesve të rrjetit të vet social brenda rrjetit të reputacionit. Nëse një lëshues e përcakton rrjetin e vet social si një flluskë sociale që thjesht i bën jehonë dhe i përforcon pikëpamjet e veta, informacioni i publikuar përmes tij vështirë se do të pritet më gjerësisht nga komunitetet e tjera. Fakti që unë arrij, me kosto të lartë, të fus një pohim radikal në rrjet nuk nënkupton se, kur gjykoj reputacionin e palës tjetër, do t’i jap ndonjë peshë. Disa pohime më shtyn komuniteti t’i marr parasysh (dënime dhe kufizime të vendosura ndaj shkelësve); të tjera janë krejtësisht në dorën time — unë vendos vetë vlerën ekonomike të përfshirjes ose përjashtimit të një copë të dhënë informacioni.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
