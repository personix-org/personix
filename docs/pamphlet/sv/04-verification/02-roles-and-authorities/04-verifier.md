---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifieraren

Vilken DID som helst kan agera verifierare, antingen direkt eller genom verifieringsrättigheter som delegerats till en tredje DID. För att jag — eller min delegat — ska kunna verifiera bör jag vara nåbar på nätverket (online). Alla kommer inte att vilja binda sig till det, och därför kan en DID-post lista, i prioritetsordning, de ersättare som ska utföra funktionen å dess vägnar medan den är offline.

Varje DID som är aktiv i nätverket deklarerar offentligt sin egen policy. Genom de regler som definieras i den policyn bedömer den, under verifieringsprocessen, motpartens anseende och innehållet och formen på det påstående som utfärdaren har flaggat för publicering till anseendenätverket. En del av policyn är den beräkningsformel som används för att räkna ut avgifter för verifieringstjänster. När det väl är på plats väntar jag, över ett statistiskt stort antal påståenden som flödar genom nätverket, på att nätverkets algoritm ska dra mig på utfärdarens sida och tilldela mig, i en given iteration, att verifiera den information som utfärdas. Utfärdaren kan i förväg beräkna hur en korrekt beteende verifierare skulle reagera, men kan inte undvika att faktiskt kontakta dem (eller deras ersättare); iterationen med den utvalda verifieraren måste utföras av utfärdaren även när de i förväg vet att den inte kommer att passera.

Hur vet vi att utfärdaren kör verifierarvals-algoritmen över den korrekta uppsättningen av kandidat-verifierar-DID:er? Tillsammans med sin offentligt deklarerade policy publicerar varje DID också den aktuella listan över identifierare för sitt sociala nätverk inom anseendenätverket. Om en utfärdare definierar sitt sociala nätverk som en social bubbla som blott ekar och förstärker dess egna åsikter, kommer information publicerad genom det knappast att tas emot bredare av andra gemenskaper. Att jag lyckas, till hög kostnad, tränga in ett radikalt påstående i nätverket innebär inte att jag, när jag bedömer motpartens anseende, kommer att ge det någon vikt. Vissa påståenden pressas jag av min gemenskap att ta i beaktande (domar och restriktioner ålagda gärningsmän); andra är helt upp till mig — jag avgör själv det ekonomiska värdet av att inkludera eller exkludera en given informationsdel.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
