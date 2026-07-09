---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsensus och verifieringsprocessen

För att bygga konsensus om vilka regler ett samhälle i genomsnitt bör upprätthålla och verkställa kan följande mekanism hjälpa. Som DID-deltagare deklarerar jag de regler jag ansluter mig till och ska leva efter, och jag publicerar dem. (Tänk på det som de stadgar och regler som, enligt min syn, utgör min ideala värld — en värld där jag inte känner mig inskränkt, utan trygg.)

Jag kan i förväg uppskatta hur mina DID-kontakter skulle reagera — och bedöma hur starkt, och av vem, jag skulle sanktioneras i vanliga sociala eller affärsmässiga interaktioner, om de hypotetiskt skulle inträffa.

Den definitiva utvärderingen sker när du begär information från en annan DID, eller ber dem verifiera ett påstående (eller ber en auktoritet om en tjänst, och så vidare) som du vill publicera till anseendenätverket. Det bör utfalla på samma sätt som när du kör utvärderingen själv, i torrkörning, mot motpartens deklarerade policy — och om det inte gör det är något fel på motpartens sida: de försöker spela ett ohederligt spel.

Utfallet är antingen accepterande, med ett offererat pris för verifiering (i fallet med verifierar- eller auktoritetstjänster), eller avslag. Både sanktioner och bonusar för avvikelse från utvärderarens policy vävs in i det offererade priset. Beställaren avgör sedan om de ska acceptera villkoren, eller gå vidare till nästa verifieringsrunda i fördelningsalgoritmen — och upprepar processen tills de är nöjda, eller tills ekonomin gör det meningslöst att fortsätta.

> [!note] Den sociala grafen
> Anseendenätverket är, först och främst, ett socialt nätverk. Du lägger till kontakter — människor som samtycker till kopplingen. De har kontakter, och de kontakterna har kontakter. Algoritmen söker efter verifierare inom ett konfigurerbart djup (t.ex. tre nivåer: dina direkta kontakter, deras kontakter, och en nivå bortom). Ingen global blockkedja behövs — nätverket bildar naturligt gemenskaper med överlapp in i andra gemenskaper.
>
> Algoritmen är icke-deterministisk: den hashar ditt påståendedokument, mappar hashen till en position på en ring av kända identiteter inom denna krets, och väljer den närmaste som kandidatverifierare. Du kan inte förutse eller påverka vem som kommer att verifiera ditt påstående.

Varje verifierares avslag förstorar ditt dokument och ökar dess bearbetningskostnad — det är den första kostnadskanalen (dokumenttillväxt). Varje ny verifierare tar ut en avgift baserad på datavolym, ditt anseende, och hur långt innehållet i ditt påstående avviker från deras deklarerade verifieringspolicy — det är den andra kostnadskanalen (riskpremie). Och varje iteration kostar tid och energi — den tredje kostnadskanalen.

> [!note] Vad verifieraren kontrollerar, i ordning
> När den väl valts utvärderar en verifierare ett påstående i ungefär fyra ordnade steg — billigaste filtren först, dyra innehållskontroller sist:
>
> 1. **Policygrindning.** Faller den här sortens påstående över huvud taget inom det verifieraren offentligt verifierar? Om inte avvisas begäran direkt.
> 2. **Auktoritetstillit.** Är den auktoritet som ställde sig bakom påståendet tillräckligt betrodd enligt verifierarens egen deklarerade policy? En auktoritet under verifierarens tillitströskel är grund för avslag oavsett påståendets innehåll.
> 3. **Utgivarens anseende.** Uppfyller utgivaren de anseendetrösklar som verifieraren har deklarerat för denna typ av påstående? Lågt anseende kan antingen höja avgiften eller utlösa avslag.
> 4. **Innehållskontroll.** Först när de tre första grindarna passeras utvärderar verifieraren själva påståendet — signaturer, intern konsekvens, formell korrekthet, och hur långt det avviker från verifierarens policy. Avgiften som tas ut för detta sista steg återspeglar den faktiska risk som tas.
>
> Verifieraren publicerar den policy som styr var och en av dessa grindar, så stegen ligger inte i deras godtycke — de är bundna av det de redan har deklarerat. Avvikelse från den publicerade policyn är i sig ett publicerbart påstående mot dem, och de betalar för det med sitt anseende.

Resultatet: att publicera ett trovärdigt och användbart påstående kostar nästan ingenting. Att publicera ett radikalt påstående kostar mer. Att publicera en lögn blir prohibitivt dyrt — du måste iterera genom verifierare efter verifierare, och var och en som avvisar dig lägger till kostnader. Marknaden prissätter ditt påstående, och priset talar om för dig var du står i förhållande till de gemenskaper du rör dig i.

Det räcker inte att deklarera att du håller dig till en regel när du i verkligheten inte gör det. I det fallet riskerar din DID publiceringen av en negativ post som blottar hyckleriet — vilket gör dig till en risk för alla andra. Utfallet bör bli färre men mer konsekvent följda regler, och en uppröjning av den djungel av lagar och förordningar som till och med juridiskt yrkesfolk knappt kan navigera.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus kontra ansvarsutkrävande
> För att nätverket ska tjäna som en värdefull informationskälla bör en DID inte vara alltför radikal — annars kommer de andra att avvisa den. Socialt tryck kommer att söka jämvikt, och försök att destabilisera den kommer sannolikt att bestraffas.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Antalet röster är inte detsamma som en rösts vikt
> Juraj Karpiš säger att ”pengar är minnet av goda gärningar.” Jag skulle tillägga att anseende är minnet av de dåliga.
>
> Härav följer att, meritokratiskt, den som bidrar mer och inte har något dåligt anseende förtjänar en större röstvikt i gemenskapen. Sett genom de bilaterala relationernas lins: när jag väger vilka konsensustryck jag ska tillmötesgå går den största vikten till de relationer ur vilka jag härleder den största ekonomiska nyttan. Tio personer med vilka jag inte har någon aktiv handel kommer att påverka mig långt mindre än en permanent affärspartner. Detta paradigm är inte begränsat till handel — det sträcker sig till sociala, politiska och andra relationer.
