---
title: "Konsensusi dhe procesi i verifikimit"
chapter: 3
part: "Si funksionon verifikimi"
lang: en
version: v6
source: v1
---

# Konsensusi dhe procesi i verifikimit

Për të ndërtuar konsensus se cilat rregulla një shoqëri duhet, mesatarisht, të mbajë dhe të zbatojë, mund të ndihmojë mekanizmi i mëposhtëm. Si pjesëmarrës DID, unë shpall rregullat që i pranoj dhe do të jetoj sipas tyre, dhe i publikoj. (Mendo për të si statutet dhe rregulloret që, sipas meje, përbëjnë botën time ideale — një botë ku nuk ndihem i kufizuar, por i sigurt.)

Mund të vlerësoj paraprakisht si do të reagonin kontaktet e mia DID — dhe të gjykoj sa fort, dhe nga kush, do të sanksionohesha në ndërveprime të zakonshme shoqërore ose biznesi, nëse ato do të ndodhnin hipotetikisht.

Vlerësimi përfundimtar ndodh kur i kërkon informacion një DID-i tjetër, ose i kërkon të verifikojë një pohim (ose i kërkon një autoriteti një shërbim, e kështu me radhë) që dëshiron ta publikosh në rrjetin e reputacionit. Duhet të dalë njësoj si kur e kryen vetë vlerësimin, në dry run, kundrejt politikës së shpallur të palës tjetër — dhe nëse jo, diçka nuk shkon nga ana e palës tjetër: ata po përpiqen të luajnë një lojë të pandershme.

Rezultati është ose pranimi, me një çmim të kuotuar për verifikimin (në rastin e shërbimeve të verifikuesit ose autoritetit), ose refuzimi. Si sanksionet, ashtu edhe bonuset për devijim nga politika e vlerësuesit futen te çmimi i kuotuar. Kërkuesi pastaj vendos nëse i pranon kushtet, ose kalon te raundi tjetër i verifikimit në algoritmin e shpërndarjes — duke përsëritur procesin derisa të jetë i kënaqur, ose derisa ekonomia e bën të kotë vazhdimin.

> [!note] The Social Graph
> Rrjeti i reputacionit është, para së gjithash, një rrjet social. Ti shton kontakte — njerëz që pajtohen me lidhjen. Ata kanë kontakte, dhe ato kontakte kanë kontakte. Algoritmi kërkon verifikues brenda një thellësie të konfigurueshme (p.sh. tri nivele: kontaktet e tua të drejtpërdrejta, kontaktet e tyre dhe një nivel më tej). Nuk nevojitet asnjë blockchain global — rrjeti natyrshëm formon komunitete me mbivendosje në komunitete të tjera.
>
> Algoritmi është jodeterministik: bën hash-in e dokumentit të pohimit tënd, e hedh hash-in në një pozicion në një unazë identitetesh të njohura brenda këtij rrethi, dhe zgjedh më të afërtin si verifikuesin kandidat. Nuk mund të parashikosh apo të ndikosh se kush do të verifikojë pohimin tënd.

Çdo refuzim i një verifikuesi e zmadhon dokumentin tënd dhe rrit koston e përpunimit të tij — ky është kanali i parë i kostos (rritja e dokumentit). Çdo verifikues i ri ngarkon një tarifë të bazuar në vëllimin e të dhënave, në reputacionin tënd dhe në sa larg përmbajtja e pohimit tënd devijon nga politika e tij e shpallur e verifikimit — ky është kanali i dytë i kostos (prima e rrezikut). Dhe çdo iteracion kushton kohë dhe energji — kanali i tretë i kostos.

> [!note] What the Verifier Checks, in Order
> Sapo përzgjidhet, një verifikues e vlerëson një pohim në rreth katër hapa të renditur — filtrat më të lirë të parët, kontrollet e shtrenjta të përmbajtjes të fundit:
>
> 1. **Filtrimi i politikës.** A bie ky lloj pohimi brenda asaj që verifikuesi verifikon publikisht fare? Nëse jo, kërkesa refuzohet drejtpërdrejt.
> 2. **Besimi te autoriteti.** A është autoriteti që e mbështeti pohimin mjaftueshëm i besuar sipas politikës vetjake të shpallur të verifikuesit? Një autoritet nën pragun e besimit të verifikuesit është bazë për refuzim pavarësisht përmbajtjes së pohimit.
> 3. **Reputacioni i lëshuesit.** A i përmbush lëshuesi pragjet e reputacionit që verifikuesi ka shpallur për këtë lloj pohimi? Reputacioni i ulët mund ose ta ngrejë tarifën ose të nxisë refuzim.
> 4. **Kontrolli i përmbajtjes.** Vetëm kur kalojnë tri filtrat e parë verifikuesi e vlerëson vetë pohimin — nënshkrimet, konsistencën e brendshme, korrektësinë formale dhe sa larg devijon nga politika e verifikuesit. Tarifa e ngarkuar për këtë hap të fundit reflekton rrezikun real të marrë.
>
> Verifikuesi publikon politikën që qeveris secilin nga këta filtra, kështu që hapat nuk janë sipas gjykimit të tij të lirë — ai është i lidhur nga ajo që ka shpallur tashmë. Devijimi nga politika e publikuar është vetë një pohim i publikueshëm kundër tij, dhe ai e paguan me reputacionin e vet.

Rezultati: publikimi i një pohimi të besueshëm dhe të dobishëm kushton thuajse asgjë. Publikimi i një pohimi radikal kushton më shumë. Publikimi i një gënjeshtre bëhet ndaluesisht i shtrenjtë — duhet të iterosh nëpër verifikues pas verifikuesi, dhe secili që të refuzon shton kosto. Tregu e çmon pohimin tënd, dhe çmimi të tregon ku qëndron në raport me komunitetet nëpër të cilat lëviz.

Nuk mjafton të shpallësh se u përmbahesh një rregulli kur në realitet nuk i përmbahesh. Në atë rast, DID-i yt rrezikon publikimin e një regjistrimi negativ që ekspozon hipokrizinë — çka të kthen në rrezik për të gjithë të tjerët. Rezultati duhet të jetë më pak rregulla, por të ndjekura më me konsistencë, dhe një pastrim i asaj xhungle ligjesh e rregulloresh nëpër të cilën mezi lundrojnë as vetë profesionistët e ligjit.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consensus vs Accountability
> Që rrjeti të shërbejë si burim i vlefshëm informacioni, një DID nuk duhet të jetë tepër radikal — përndryshe të tjerët do ta refuzojnë. Presioni social do të kërkojë ekuilibër, dhe përpjekjet për ta destabilizuar atë me gjasë do të ndëshkohen.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] The Number of Votes Is Not the Same as the Weight of a Voice
> Juraj Karpiš thotë se “paraja është kujtesa e veprave të mira.” Do të shtoja se reputacioni është kujtesa e atyre të këqijave.
>
> Prej kësaj rrjedh se, meritokratikisht, ai që kontribuon më shumë dhe s’ka reputacion të keq meriton një peshë më të madhe zëri në komunitet. Parë përmes prizmit të marrëdhënieve dypalëshe: kur peshoj cilat presione konsensusi t’i pranoj, pesha më e madhe u shkon marrëdhënieve prej të cilave nxjerr përfitimin më të madh ekonomik. Dhjetë vetë me të cilët s’kam tregti aktive do të më ndikojnë shumë më pak sesa një partner i përhershëm biznesi. Kjo paradigmë nuk kufizohet te tregtia — shtrihet te marrëdhëniet shoqërore, politike e të tjera.
