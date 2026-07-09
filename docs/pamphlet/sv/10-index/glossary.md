---
title: "Glossary"
part: "Appendix"
lang: en
version: v6
---

# Ordlista

| Term | Svenska | Betydelse |
|------|-------|---------|
| **Authority** | Auktoritet | En betrodd entitet (person, organisation) som verifierar information och sätter sitt anseende på spel för den. Kan vara specialiserad (utredande, juridisk, teknisk). |
| **Claim** | Påstående | Generellt: varje verifierbart uttalande. Här: en post publicerad till anseendenätverket — en utsaga om en händelse, egenskap eller relation som är kryptografiskt signerad och verifierad. T.ex. ”Jag är bosatt i kommun X” eller ”denna person bröt ett avtal.” |
| **Compartmentalization** | Avskärmning | Generellt: att separera information i isolerade enheter så att exponeringen av en enhet inte äventyrar de andra. En princip känd från underrättelsetjänster. Här: parallella DID-identiteter i diktaturer — att kompromettera en avslöjar inte de andra. |
| **Consistent Hash Ring** | Konsistent hash-ring | En algoritmisk mekanism för att välja verifierare — en position på ringen bestäms av hashen av DID-dokumentet inom den sociala grafen. Säkerställer ett icke-deterministiskt men ändå verifierbart val. |
| **DID** | DID (Decentraliserad identitet) | En digital identitet som du själv skapar och kontrollerar, utan en central auktoritet. Kryptografiskt signerad med din privata nyckel — ingen kan återkalla den eller förfalska den. |
| **DID Document** | DID-dokument | En offentligt tillgänglig datafil som beskriver din DID-identitet — innehåller offentliga nycklar, nätverksadresser och metadata. Används för att verifiera din identitet i nätverket. |
| **Due Diligence** | Due diligence | Generellt: fördjupad kontroll av en motpart innan man inträder i en affärs- eller rättsrelation — granskning av deras historik, ekonomi, anseende och risker. Här: i anseendenätverket sker det snabbare och mer automatiskt tack vare tillgången till verifierade poster. |
| **Economic Neutrality Principle** | Principen om ekonomisk neutralitet | Ärligt beteende i nätverket är ekonomiskt nära noll — publiceringskostnader återkommer som verifieringsbelöningar. Ohederligt beteende är en ren förlust. |
| **Emergent** | Emergent | Spontant uppkommande ur interaktioner mellan enklare delar, utan att någon designar eller styr det. En fågelflock flyger i formation utan en plan — formationen framträder ur enkla regler som varje individ följer. |
| **Emergent Social Contract** | Emergent samhällskontrakt | Beteenderegler som uppstår inte uppifrån (lag) utan nerifrån — ur upprepade interaktioner och konsensus inom en gemenskap. |
| **ESR** | Electronic Spending Register | Ett föreslaget system för transparent spårning av offentliga utgifter — varje realiserad statlig utgift matchas mot en planerad betalning. Inspirerat av den tjeckiska EET, men vänt mot staten. |
| **Hash** | Hash (avtryck) | Generellt: en enkelriktad matematisk funktion som producerar ett unikt ”fingeravtryck” med fast längd från vilken indata som helst — som ett fingeravtryck av dokumentet. Samma indata ger alltid samma utdata, men indata kan inte härledas ur utdata. Här: används för att bestämma en position på hash-ringen och för att verifiera dokumentets integritet. |
| **Just-in-Time Funding** | Just-in-time-finansiering | Statlig finansiering villkorad av transparens — pengar flödar endast när staten accepterar ESR och matchar sina utgifter. En hävstång för att framtvinga samarbete. |
| **Meritocracy** | Meritokrati | Generellt: ett system där ställning avgörs av faktisk förtjänst och bevisad förmåga, inte formella titlar, kontakter eller ärvda privilegier. Här: anseendenätverket gynnar naturligt dem som bevisligen bidrar till gemenskapen — deras röst väger tyngre på grund av track record, inte på grund av ämbete. |
| **Onion Gateway** | Onion gateway | En DID-identitets nätverksadress på onion-nätverket. Skild från DID-dokumentet — den kan ändras utan att identiteten går förlorad (liknande att ändra IP-adressen bakom en domän). |
| **Onion Routing** | Onion routing (Tor) | Ett kommunikationsprotokoll som säkerställer nätverkets ocensurerbarhet. Meddelanden krypteras i lager — varje nod skalar av ett lager men känner inte till hela vägen. |
| **Oracle Problem** | Orakelproblem | Generellt: hur man säkerställer att data som förs in i ett digitalt system troget motsvarar det som faktiskt hände i den fysiska världen. Termen härstammar från blockkedjeområdet. Här: hanteras genom auktoriteter som sätter sitt anseende på spel som garanti för att en digital post motsvarar den fysiska verkligheten. |
| **Phenomenological** | Fenomenologisk | Generellt: ett förhållningssätt som studerar fenomen så som de manifesterar sig i den direkta erfarenheten, genom att iaktta vad som följer av dem, utan förhandsgivna teorier. Här: frihet, samhällskontraktet och beteendenormer är iakttagna fenomen — följder av tusentals mikrointeraktioner mellan människor, inte principer definierade uppifrån. |
| **Policy** | Policy | Generellt: en uppsättning regler eller principer som styr beteende i en given kontext. Här: varje deltagare i DID-nätverket deklarerar sin policy — hur de reagerar på andras specifika beteende, vilka regler de följer, och vilka straff de anser vara proportionerliga. Sammanslagningen av policyer bildar det emergenta samhällskontraktet. |
| **Proxy** | Proxy | Generellt: en ställföreträdare eller mellanhand — ett system eller en entitet som agerar å en annans vägnar. Används här i två kontexter: (1) ESR som en proxy som matchar offentliga utgifter mot planerade betalningar; (2) observatörer som en proxy mellan utgivare och verifierare i observatörstricket. |
| **Publisher** | Utgivare | En nätverksdeltagare som skapar och publicerar en post (ett påstående om en orättvisa, avhjälpande och så vidare). Bär kostnaden för publicering. |
| **Reputation-Based Social Network (RSN)** | Anseendebaserat socialt nätverk | Ett decentraliserat socialt nätverk där deltagare utbyter återkoppling om beteende i den verkliga världen. Poster är kostsamma att skapa, billiga att läsa. |
| **Reputation Signal** | Anseendesignal | En enskild post i nätverket — positiv (avhjälpande av skada, uppfyllande av en förpliktelse) eller negativ (orättvisa, avtalsbrott). Kumulativt bildar signalerna en anseendeprofil. |
| **Social Graph** | Social graf | Nätverket av dina kontakter och dina kontakters kontakter. Algoritmen söker efter verifierare på ett konfigurerbart djup (till exempel 3 nivåer). Ingen global blockkedja — nätverket bildar naturligt gemenskaper med överlapp. |
| **Tax Allocation** | Skatteallokering | En mekanism genom vilken skattebetalaren avgör vart en del av deras skatter går. Den allokerbara procentandelen växer år för år. |
| **Track Record** | Track record | Generellt: historiken av tidigare resultat, framgångar och misslyckanden hos en person eller organisation. Här: summan av alla tidigare interaktioner för en given DID-identitet i nätverket — verifierade påståenden, accepterade och avvisade poster — utifrån vilka dess anseende härleds. |
| **Verifier** | Verifierare | En deltagare som algoritmiskt väljs ut för att verifiera och publicera en post. Sätter sitt goda namn på spel för informationens sanningsenlighet. |
