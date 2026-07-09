---
title: "Glossary"
part: "Appendix"
lang: en
version: v6
---

# Ordliste

| Begrep | Norsk | Betydning |
|------|-------|---------|
| **Authority** | Autoritet | En betrodd enhet (person, organisasjon) som verifiserer informasjon og setter sitt omdømme på spill for den. Kan være spesialisert (etterforskende, juridisk, teknisk). |
| **Claim** | Påstand | Generelt: enhver etterprøvbar utsagn. Her: en oppføring publisert til omdømmenettverket — en påstand om en hendelse, egenskap eller relasjon som er kryptografisk signert og verifisert. F.eks. «Jeg er innbygger i kommune X» eller «denne personen brøt en kontrakt». |
| **Compartmentalization** | Oppdeling (avskjerming) | Generelt: å skille informasjon i isolerte enheter slik at eksponering av én enhet ikke kompromitterer de andre. Et prinsipp kjent fra etterretningstjenester. Her: parallelle DID-identiteter i diktaturer — kompromittering av én avslører ikke de andre. |
| **Consistent Hash Ring** | Hash-ring | En algoritmisk mekanisme for å velge verifikatorer — en posisjon på ringen bestemmes av hashen av DID-dokumentet innenfor den sosiale grafen. Sikrer et ikke-deterministisk, men likevel etterprøvbart valg. |
| **DID** | DID (desentralisert identitet) | En digital identitet som du selv skaper og kontrollerer, uten en sentral autoritet. Kryptografisk signert med din private nøkkel — ingen kan tilbakekalle den eller forfalske den. |
| **DID Document** | DID-dokument | En offentlig tilgjengelig datafil som beskriver din DID-identitet — inneholder offentlige nøkler, nettverksadresser og metadata. Brukes til å verifisere din identitet i nettverket. |
| **Due Diligence** | Due diligence | Generelt: inngående verifisering av en motpart før man inngår et forretningsmessig eller juridisk forhold — kontroll av historikk, økonomi, omdømme og risiko. Her: i omdømmenettverket skjer det raskere og mer automatisk takket være tilgjengeligheten av verifiserte oppføringer. |
| **Economic Neutrality Principle** | Prinsippet om økonomisk nøytralitet | Ærlig atferd i nettverket er økonomisk nær null — publiseringskostnader kommer tilbake som verifiseringsbelønninger. Uærlig atferd er et rent tap. |
| **Emergent** | Emergent | Oppstår spontant fra interaksjoner mellom enklere deler, uten at noen utformer eller styrer det. En fugleflokk flyr i formasjon uten en plan — formasjonen vokser frem av enkle regler fulgt av hvert individ. |
| **Emergent Social Contract** | Emergent samfunnskontrakt | Atferdsregler som ikke oppstår ovenfra (lov), men nedenfra — fra gjentatte interaksjoner og konsensus innad i et fellesskap. |
| **ESR** | Elektronisk utgiftsregister | Et foreslått system for gjennomsiktig sporing av offentlige utgifter — hver realiserte statlige utgift matches mot en planlagt betaling. Inspirert av den tsjekkiske EET, men snudd mot staten. |
| **Hash** | Hash (avtrykk) | Generelt: en enveis matematisk funksjon som lager et unikt «fingeravtrykk» med fast lengde av en hvilken som helst inndata — som et fingeravtrykk av dokumentet. Samme inndata gir alltid samme utdata, men inndata kan ikke utledes fra utdata. Her: brukt til å bestemme en posisjon på hash-ringen og til å verifisere dokumentets integritet. |
| **Just-in-Time Funding** | Just-in-time-finansiering | Statlig finansiering betinget av gjennomsiktighet — penger flyter bare når staten godtar ESR og matcher utgiftene sine. En brekkstang for å fremtvinge samarbeid. |
| **Meritocracy** | Meritokrati | Generelt: et system der posisjon avgjøres av faktisk fortjeneste og påvist evne, ikke formelle titler, forbindelser eller arvet privilegium. Her: omdømmenettverket favoriserer naturlig dem som påviselig bidrar til fellesskapet — stemmen deres bærer mer vekt på grunn av merittliste, ikke på grunn av embete. |
| **Onion Gateway** | Onion gateway | En DID-identitets nettverksadresse på onion-nettverket. Atskilt fra DID-dokumentet — den kan endres uten å miste identiteten (som å endre IP-adressen bak et domene). |
| **Onion Routing** | Løkruting (Tor) | En kommunikasjonsprotokoll som sikrer nettverkets sensurfrihet. Meldinger krypteres i lag — hver node fjerner ett lag, men kjenner ikke hele ruten. |
| **Oracle Problem** | Orakelproblemet | Generelt: hvordan sikre at data som går inn i et digitalt system, tro mot gjengir det som faktisk hendte i den fysiske verden. Uttrykket stammer fra blokkjededomenet. Her: løst gjennom autoriteter som setter omdømmet sitt på spill som en garanti for at en digital oppføring svarer til fysisk virkelighet. |
| **Phenomenological** | Fenomenologisk | Generelt: en tilnærming som studerer fenomener slik de manifesterer seg i direkte erfaring, ved å observere hva som følger av dem, uten forhåndsgitte teorier. Her: frihet, samfunnskontrakten og atferdsnormer er observerte fenomener — følger av tusenvis av mikrointeraksjoner mellom mennesker, ikke prinsipper definert ovenfra. |
| **Policy** | Policy (politikk) | Generelt: et sett av regler eller prinsipper som styrer atferd i en gitt sammenheng. Her: hver deltaker i DID-nettverket erklærer sin policy — hvordan de reagerer på bestemt atferd fra andre, hvilke regler de følger, og hvilke straffer de anser som forholdsmessige. Summen av policyer danner den emergente samfunnskontrakten. |
| **Proxy** | Proxy | Generelt: en stedfortreder eller mellommann — et system eller en enhet som handler på vegne av en annen. Brukt her i to sammenhenger: (1) ESR som en proxy som matcher offentlige utgifter med planlagte betalinger; (2) observatører som en proxy mellom utgiver og verifikator i observatørtrikset. |
| **Publisher** | Utgiver | En nettverksdeltaker som skaper og publiserer en oppføring (en påstand om en urett, en utbedring og så videre). Bærer kostnaden ved publiseringen. |
| **Reputation-Based Social Network (RSN)** | Omdømmenettverk | Et desentralisert sosialt nettverk der deltakere utveksler tilbakemeldinger om atferd i den virkelige verden. Oppføringer er kostbare å skape, billige å lese. |
| **Reputation Signal** | Omdømmesignal | En enkelt oppføring i nettverket — positiv (utbedring av skade, oppfyllelse av en forpliktelse) eller negativ (urett, kontraktsbrudd). Kumulativt danner signalene en omdømmeprofil. |
| **Social Graph** | Sosial graf | Nettverket av dine kontakter og dine kontakters kontakter. Algoritmen leter etter verifikatorer på en konfigurerbar dybde (for eksempel 3 nivåer). Ingen global blokkjede — nettverket danner naturlig fellesskap med overlapp. |
| **Tax Allocation** | Skatteallokering | En mekanisme der skattebetaleren bestemmer hvor en del av skattene deres går. Den allokerbare prosentandelen vokser år for år. |
| **Track Record** | Track record | Generelt: historikken over tidligere resultater, suksesser og feil hos en person eller organisasjon. Her: summen av alle tidligere interaksjoner til en gitt DID-identitet i nettverket — verifiserte påstander, godtatte og avviste oppføringer — som omdømmet dens utledes fra. |
| **Verifier** | Verifikator | En deltaker algoritmisk valgt til å verifisere og publisere en oppføring. Setter sitt gode navn på spill for at informasjonen er sannferdig. |
