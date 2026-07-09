---
title: "Vëzhguesi"
chapter: 3
part: "Si funksionon verifikimi"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Vëzhguesi

Roli i vëzhguesit e heq nxitjen e verifikuesit për të shtrembëruar rregullat. Në situatat ku një verifikuesi nuk i pëlqen kërkesa e lëshuesit ose e autoritetit, ai thjesht mund të heshtë — të mos përgjigjet, dhe të bllokojë sekuencën algoritmike. Vëzhguesi — ose një grup vëzhguesish — vë reputacionin e vet mbi dokumentimin se si u pyet verifikuesi. Nëse verifikuesi hesht pavarësisht një politike të shpallur që thotë të kundërtën, ai mund të dënohet për shkelje të protokollit.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanizmi: vula kohore dhe kodi i sfidës

Para se t’ia dërgosh një pohim verifikuesit, e rrugëton përmes vëzhguesve — njerëz që i beson, ose ofrues të specializuar shërbimesh vëzhgimi që ngarkojnë një tarifë të vogël. Çdo vëzhgues merr parashtresën tënde, i vë vulën kohore, nënshkruan se e pa duke dalë, dhe gjeneron një kod sfide — një hash kriptografik të nënshkrimit të vet. Kodet i bashkëngjiten kërkesës sate. Verifikuesi i sheh por s’ka ide se kush janë vëzhguesit, apo nëse kodet janë vërtet reale. Vëzhguesit veprojnë kështu si përfaqësues midis lëshuesit dhe verifikuesit, duke mbajtur një regjistrim të pavarur se pohimi u parashtrua dhe çfarë përmbante. Ata mund të jenë nga zero deri në N.

Kur verifikuesi sillet ndershëm — duke pranuar ose refuzuar në përputhje me politikën e vet të shpallur — kodet mbeten të errëta. Askush nuk ekspozohet.

Por nëse verifikuesi hesht pavarësisht një politike akomoduese, ose përgjigjet në një mënyrë që bie ndesh me atë që publikoi, ti mban nënshkrimet origjinale të vëzhguesve. Mund t’i publikosh si dëshmi përfaqësuese se pohimi u parashtrua dhe se verifikuesi nuk e ndoqi protokollin. Kushdo mund të verifikojë që nënshkrimet përputhen me kodet e sfidës.

## Poenta: nuk të duhen vëzhgues realë

Dhe këtu është pjesa më elegante: **nuk të duhen fare vëzhgues realë.** Mund të gjenerosh numra të rastësishëm që duken saktësisht si kode sfide. Verifikuesi nuk e dallon dot ndryshimin — duhet të hedhë zaret nëse ta rrezikojë reputacionin e vet. Pas çdo kërkese që marrin mund të ketë një vëzhgues të respektuar që shikon inkognito — ose mund të jetë zhurmë e pastër. Verifikuesi nuk e di. Dhe ai pasiguri është mekanizmi.

Kostoja e mbajtjes së presionit të ndershëm: thuajse zero (numrat e rastësishëm janë falas). Kostoja e mundshme e pandershmërisë për verifikuesin: katastrofike. Sjellja e ndershme nxitet edhe kur askush nuk po shikon vërtet.

Sistemi funksionon sepse të gjithë janë pak paranojakë. Pasiguria është më e lirë se mbikëqyrja.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Multiple verifiers in a single iteration
> Një rregull përforcues shoqërues për disponueshmërinë e verifikuesve mund të jetë një zgjerim algoritmik që kthen, në një iteracion të vetëm, një grup verifikuesish kandidatë në vend të vetëm njërit.
