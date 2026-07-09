---
title: "Rrjet social i bazuar në reputacion"
chapter: 2
part: "Mjeti"
lang: en
version: v6
source: v1
---

# Rrjet social i bazuar në reputacion

Për të sjellë ndryshim, na duhet një mjet i konceptuar me kujdes. Fillimisht do ta skicojmë shkurt; në kapitujt e mëvonshëm do ta shqyrtojmë çdo pjesë në më shumë hollësi dhe do të shtojmë të tjera. Përfytyro një rrjet social të pacensurueshëm, global, të decentralizuar ku mund të krijoje dhe të menaxhoje me siguri identitetin tënd përfaqësues — një të ashtuquajtur Identitet të Decentralizuar (DID). Një DID është një identitet dixhital që e krijon dhe e kontrollon vetë, pa varësi nga ndonjë autoritet qendror. Askush nuk mund të ta marrë apo ta falsifikojë, sepse është nënshkruar kriptografikisht me çelësin tënd privat (ose çelësat, përmes multisig).

> [!note] Note
> Një pasojë është se një identitet i tillë mund të zëvendësonte gradualisht dokumentet e identifikimit të lëshuara nga shteti — por për këtë më shumë në kapitullin mbi tranzicionin.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Në një rrjet të tillë, mund të raportoje përmes identitetit tënd se dikush të ka shkaktuar dëm (dhe më vonë, potencialisht, se e ka riparuar atë ose është detyruar ta bëjë). Që ky reagim — drejtuar shkaktarit të dëmit — të ketë vlerë si burim i rëndësishëm, futja e informacionit në rrjet duhet të kushtojë kohë, energji dhe para — dhe përveç kësaj, duhet të prodhohet provë e verifikueshme për të tjerët se nuk bëhet fjalë për muhabet të kotë.

Leximi i informacionit do të ishte i lehtë dhe relativisht i lirë, por krijimi i një regjistrimi të veçantë do të ishte i kushtueshëm dhe kërkues. Shkrimi do të ndiqte një protokoll të qartë, në të cilin llogaritja sipas algoritmit të zgjedhur përcakton rreptësisht cilit DID t’i kërkosh verifikimin e informacionit të parashtruar dhe si të veprosh që pjesëmarrësi i përzgjedhur ta përpunojë informacionin në emrin tënd, ta publikojë dhe të bëhet verifikuesi i tij.

> [!note] Algorithm vs radicalism
> Përzgjedhja algoritmike e verifikuesve siguron që botuesit joradikalë të informacionit, me kalimin e kohës, do të ruajnë një ekuilibër thuajse neutral midis kostove të informacionit të publikuar dhe shpërblimeve për verifikimin.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Le të shohim si e përzgjedh algoritmi një verifikues.

> [!note] Algorithm
> Përzgjedhja algoritmike jodeterministikisht zgjedh një verifikues të ndryshëm (ose një grup verifikuesish të mundshëm) për copa të ndryshme informacioni. Një hash (një funksion matematik njëkahësh që prodhon një “gjurmë gishti” unike nga çdo hyrje — si gjurma e gishtit të një dokumenti) i dokumentit të plotë DID përcakton pozicionin në një consistent hash ring dhe përzgjedh kandidatët verifikues.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Thënë thjesht: algoritmi merr krejt dokumentin tënd DID, llogarit një gjurmë gishti prej tij, dhe ajo gjurmë përcakton verifikuesin tënd.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Me verifikuesin e parë që përzgjedh algoritmi, ti si botues mund të mos ia dalësh — reputacioni yt ose parametrat e shpallur mund të mos përmbushin kërkesat e tyre. Do të vazhdoje algoritmikisht kërkimin për tjetrin duke kryer një iteracion tjetër rekursiv, që të cakton një verifikues të mëtejshëm. Me çdo hap “distanca” deri te verifikuesi i synuar rritet, e po ashtu rriten edhe metatë dhënat shoqëruese që duhen publikuar. Ndërsa të dhënat rriten, kostot natyrshëm ngjiten (jo vetëm për shkak të madhësisë fillestare të pohimit, por edhe për shkak të metatë dhënave që grumbullohen me çdo refuzim). Informacioni i besueshëm kalon shumë më lehtë sesa tekat pa kuptim. Është në dorën e secilit sa çmim është i gatshëm të përballojë dhe sa i rëndësishëm është regjistrimi për të — radikalizmi është i garantuar që të bëhet i shtrenjtë.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Çfarëdo që të vendosë verifikuesi si përgjigje ndaj kërkesës sate për verifikim, topi kthehet në fushën e botuesit: ai mund ta pranojë ofertën e verifikuesit për shërbimet e verifikimit, ta fusë përgjigjen në kronologji dhe të provojë sërish (më shtrenjtë), ose të largohet dhe të gëlltisë koston e humbur.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Për t’i dhënë informacionit tënd peshë më të madhe dhe një shans më të mirë pranimi te verifikuesit, ti — si botues me interes që informacioni të lëshohet — mund të përdorësh shërbimet e një **autoriteti të besuar**. Autoriteti ose e refuzon informacionin e parashtruar, ose e pranon dhe vë emrin e tij të mirë (reputacionin) mbi të. Autoriteti zakonisht kërkon prova nga bota reale, i verifikon dhe i klasifikon. Rezultati është një protokoll i vlerësimit të tij për rastin e dhënë në kohën e dhënë. Mendo për një autoritet si specialist në një lloj të caktuar shërbimi si në botën reale ashtu edhe në atë dixhitale — për shembull një hetues, një auditor, një siguraues, një furnizues i një klase të caktuar mallrash (në thelb, çdo aktor ekonomik në treg).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Në kohën kur ti provon të publikosh informacion në rrjet, ai ka gjasa të përmbajë tashmë informacion për aktorët e tij — këto janë sinjale reputacioni. Të lundrosh se si të lexosh sinjalet e reputacionit — çfarë kuptimi kanë për ty në situata të ndryshme dhe çfarë rreziqesh mbartin — mund të mos jetë e thjeshtë. Secili pjesëmarrës mund t’i shohë ndryshe regjistrimet e reputacionit përmes DID-it të vet, në varësi të situatës që po trajton lidhur me palën tjetër. A është pala tjetër paguese e besueshme, apo më duhet të kërkoj para paraprakisht për një transaksion biznesi? A mbart produkti i ofruar vlerësime për mashtrim apo defekte të fshehta? A po përpiqet t’i shmanget përgjegjësisë kontraktuale kur diçka shkon keq? Ndonjëherë vjen ndër duar një pamje më e ndërlikuar e konsistencës së përgjithshme të palës tjetër — varet nga preferencat e atij që kërkon pasqyrën. Tregu mund të ofrojë produkte dhe shërbime që thjeshtojnë, përpunojnë dhe qartësojnë leximin e reputacionit në kontekstin e situatës në fjalë. Autoritete të ndryshme dhe shërbimet e tyre të ofruara mund t’i shërbejnë po ashtu këtij qëllimi.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Examples
> Informacioni tipik me interes për botuesit — dhe i vlefshëm për të tjerët — ka të bëjë me ngjarje përtej komunikimit të zakonshëm ndërnjerëzor në botën reale ose virtuale.
>
> Shembuj negativë:
> - prova për vepra kriminale (p.sh. të audituara nga një trup hetimor i besuar)
> - prova indirekte (të dobëta më vete, por statistikisht kumulative) — p.sh. prania e përsëritur pranë disa vjedhjeve brenda një kohe të shkurtër → ende rastësi?
> - shkelje kontrate
>
> Shembuj pozitivë:
> - dëm i riparuar (vullnetarisht ose nën presionin e komunitetit si ndëshkim)
> - pranimi dhe vuajtja e një dënimi të propozuar nga autoriteti X
> - autoriteti X i hoqi njohjen shkelësit ndaj të drejtave të pronësisë deri në një masë të caktuar
>
> Është në dorën e secilit të mbledhë informacionin e disponueshëm për palën tjetër dhe të vlerësojë rreziqet sipas preferencave të veta.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Nëse informacioni për ty shfaqet në rrjet varet ekskluzivisht nga sjellja jote.
> Nuk je i detyruar kurrë të bashkohesh me një rrjet të tillë, e megjithatë informacioni për ty mund të shfaqet aty. Kjo varet ekskluzivisht nga veprimet e tua dhe nga ndikimi që kanë te të tjerët.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Ajo që sapo e skicova shkurt është se si mund të funksiononte një rrjet social i frymëzuar nga Identiteti i Decentralizuar (DID). Qëllimi kryesor i koncepteve DID është forcimi i privatësisë dhe i lirisë përmes parimit të pajtimit me rregullat që do t’i ndjek dhe do të jetoj sipas tyre — duke u dhënë përdoruesve mundësinë të vendosin çfarë informacioni të ndajnë dhe në çfarë kushtesh.

Propozoj që DID-et të lidhen më tej në një rrjet komunikimi ku mbajtësit e tyre shkëmbejnë reagime edhe përtej situatave ku dikujt i ka ndodhur diçka dhe komuniteti ose një individ ka nevojë të reagojë. Një krahasim i tillë parandalues i rregullave që kemi pranuar — me mundësinë për të llogaritur pasojat ekonomike dhe të tjera të devijimeve të ndërsjella në pritshmëritë se si duhet të veprojë pala tjetër — mund të konsiderohej motivim për gjetjen e konsensusit. Në vend të lirisë, një sistem i tillë do të theksonte vendimmarrjen vullnetare të kombinuar me përgjegjësinë për sjelljen në botën reale.

Një individ nuk mund ta thyejë sistemin i vetëm — një grup njerëzish ka shans më të madh, dhe një grup njerëzish me konsensus të negociuar dhe motivime për të tërhequr bashkë në shumë çështje ka shans edhe më të madh t’u rezistojë prirjeve autoritare. Parakushti i organizimit nga kapitulli i parë do të plotësohet sapo të përmbushen dy kushte: rrjeti i reputacionit DID të mbulojë komunitetet mjaftueshëm përfaqësueshëm sa përdorimi i tij të pushojë së qeni ekzotik. Dhe njëkohësisht, ky segment komuniteti të bëhet një pakicë ekonomikisht domethënëse që mund të negociojë me kembëngulje me pjesën tjetër të shoqërisë.

> [!note] Voluntariness vs freedom
> Liria — në kuptimin pozitiv — do të ishte një efekt dytësor i balancimit të dy faktorëve: vullnetarizmit dhe presionit të rrethanave drejt përgjegjësisë.

> [!note] The AI Era and the Value of Reputation
> Në epokën e inteligjencës artificiale, gjithçka e lidhur me të menduarin njohës po automatizohet — dhe mund të shkojë edhe më tej. Çfarë mbetet atëherë në veprimtarinë njerëzore si avantazh konkurrues? Përgjigjja është e vështirë, dhe diçka sigurisht do të gjendet, por një gjë mund ta themi me siguri: reputacioni do të vendosë. Një histori e verifikueshme e sjelljes sate, e zotimeve të tua dhe e përmbushjes së tyre — kjo është diçka që AI nuk do ta ndërtojë për ty.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
