---
title: "Glossary"
part: "Appendix"
lang: en
version: v6
---

# Ordliste

| Udtryk | Tjekkisk | Betydning |
|------|-------|---------|
| **Authority** | Autorita | En betroet enhed (person, organisation), der verificerer information og sætter sit omdømme på spil for den. Kan være specialiseret (efterforskende, juridisk, teknisk). |
| **Claim** | Tvrzení | Generelt: enhver verificerbar udtalelse. Her: en registrering offentliggjort til omdømmenetværket — en påstand om en hændelse, egenskab eller relation, der er kryptografisk signeret og verificeret. F.eks. “Jeg er bosat i kommune X” eller “denne person brød en kontrakt.” |
| **Compartmentalization** | Compartmentalizace | Generelt: at adskille information i isolerede enheder, så eksponering af én enhed ikke kompromitterer de andre. Et princip kendt fra efterretningstjenester. Her: parallelle DID-identiteter i diktaturer — kompromittering af én afslører ikke de andre. |
| **Consistent Hash Ring** | Hash ring | En algoritmisk mekanisme til udvælgelse af verifikatorer — en position på ringen bestemmes af DID-dokumentets hash inden for den sociale graf. Sikrer en ikke-deterministisk, men verificerbar udvælgelse. |
| **DID** | DID (Decentralizovaná identita) | En digital identitet, som du selv skaber og kontrollerer, uden en central autoritet. Kryptografisk signeret med din private nøgle — ingen kan tilbagekalde den eller forfalske den. |
| **DID Document** | DID dokument | En offentligt tilgængelig datafil, der beskriver din DID-identitet — indeholder offentlige nøgler, netværksadresser og metadata. Bruges til at verificere din identitet i netværket. |
| **Due Diligence** | Due diligence | Generelt: dybdegående verifikation af en modpart, før man indgår et forretnings- eller retsforhold — tjek af deres historik, økonomi, omdømme og risici. Her: i omdømmenetværket sker det hurtigere og mere automatisk takket være tilgængeligheden af verificerede registreringer. |
| **Economic Neutrality Principle** | Princip ekonomické neutrality | Ærlig adfærd i netværket er økonomisk tæt på nul — publikationsomkostninger returneres som verifikationsbelønninger. Uærlig adfærd er et nettotab. |
| **Emergent** | Emergentní | Spontant opstået af interaktioner mellem simplere dele, uden at nogen designer eller styrer det. En fugleflok flyver i formation uden en plan — formationen emergerer af simple regler fulgt af hvert individ. |
| **Emergent Social Contract** | Emergentní společenská smlouva | Adfærdsregler, der ikke opstår oppefra (lov), men nedefra — af gentagne interaktioner og konsensus inden for et fællesskab. |
| **ESR** | Electronic Spending Register | Et foreslået system til gennemsigtig sporing af offentlige udgifter — hver realiseret statslig udgift matches med en planlagt betaling. Inspireret af den tjekkiske EET, men vendt mod staten. |
| **Hash** | Hash (otisk) | Generelt: en envejs matematisk funktion, der frembringer et unikt “fingeraftryk” med fast længde fra ethvert input — som et fingeraftryk af dokumentet. Det samme input frembringer altid det samme output, men inputtet kan ikke udledes af outputtet. Her: bruges til at bestemme en position på hash-ringen og til at verificere dokumentintegritet. |
| **Just-in-Time Funding** | Just-in-time financování | Statsfinansiering betinget af gennemsigtighed — penge flyder kun, når staten accepterer ESR og matcher sine udgifter. En løftestang til at fremtvinge samarbejde. |
| **Meritocracy** | Meritokracie | Generelt: et system, hvor status bestemmes af faktisk fortjeneste og bevist evne, ikke formelle titler, forbindelser eller nedarvet privilegium. Her: omdømmenetværket favoriserer naturligt dem, der påviseligt bidrager til fællesskabet — deres stemme bærer mere vægt på grund af track record, ikke på grund af embede. |
| **Onion Gateway** | Onion gateway | En DID-identitets netværksadresse på onion-netværket. Adskilt fra DID-dokumentet — den kan ændres uden at miste identiteten (svarende til at ændre IP-adressen bag et domæne). |
| **Onion Routing** | Onion routing (Tor) | En kommunikationsprotokol, der sikrer netværkets ucensurerbarhed. Beskeder krypteres i lag — hver node fjerner ét lag, men kender ikke hele stien. |
| **Oracle Problem** | Oracle problém | Generelt: hvordan man sikrer, at data, der indføres i et digitalt system, trofast svarer til det, der faktisk skete i den fysiske verden. Udtrykket stammer fra blockchain-domænet. Her: håndteret gennem autoriteter, der sætter deres omdømme på spil som garanti for, at en digital registrering svarer til den fysiske virkelighed. |
| **Phenomenological** | Fenomenologický | Generelt: en tilgang, der studerer fænomener, som de manifesterer sig i den direkte erfaring, ved at observere, hvad der følger af dem, uden forudgivne teorier. Her: frihed, samfundskontrakten og adfærdsnormer er observerede fænomener — konsekvenser af tusindvis af mikro-interaktioner mellem mennesker, ikke principper defineret oppefra. |
| **Policy** | Policy (politika) | Generelt: et sæt regler eller principper, der styrer adfærd i en given kontekst. Her: hver deltager i DID-netværket erklærer sin politik — hvordan de reagerer på andres specifikke adfærd, hvilke regler de følger, og hvilke straffe de anser for forholdsmæssige. Aggregatet af politikker danner den emergente samfundskontrakt. |
| **Proxy** | Proxy | Generelt: en stedfortræder eller mellemmand — et system eller en enhed, der handler på vegne af en anden. Brugt her i to kontekster: (1) ESR som en proxy, der matcher offentlige udgifter med planlagte betalinger; (2) observatører som en proxy mellem udgiver og verifikator i observatør-tricket. |
| **Publisher** | Vydavatel | En netværksdeltager, der skaber og offentliggør en registrering (en påstand om en uretfærdighed, udbedring og så videre). Bærer omkostningen ved offentliggørelsen. |
| **Reputation-Based Social Network (RSN)** | Reputační síť | Et decentraliseret socialt netværk, hvor deltagere udveksler feedback om adfærd i den virkelige verden. Registreringer er kostbare at skabe, billige at læse. |
| **Reputation Signal** | Reputační signál | En enkelt registrering i netværket — positiv (udbedring af skade, opfyldelse af en forpligtelse) eller negativ (uretfærdighed, kontraktbrud). Kumulativt danner signaler en omdømmeprofil. |
| **Social Graph** | Sociální graf | Netværket af dine kontakter og dine kontakters kontakter. Algoritmen søger efter verifikatorer i en konfigurerbar dybde (for eksempel 3 niveauer). Ingen global blockchain — netværket danner naturligt fællesskaber med overlap. |
| **Tax Allocation** | Alokace daní | En mekanisme, hvorved skatteyderen beslutter, hvor en del af deres skatter går hen. Den allokerbare procentdel vokser år for år. |
| **Track Record** | Track record | Generelt: historikken over tidligere resultater, succeser og fejl hos en person eller organisation. Her: summen af alle tidligere interaktioner for en given DID-identitet i netværket — verificerede påstande, accepterede og afviste registreringer — hvorfra dens omdømme udledes. |
| **Verifier** | Ověřovatel | En deltager, der algoritmisk udvælges til at verificere og offentliggøre en registrering. Sætter sit gode navn på spil for informationens sandfærdighed. |
