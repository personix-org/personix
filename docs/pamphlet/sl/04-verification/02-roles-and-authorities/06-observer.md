---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Opazovalec

Vloga opazovalca odvzame preveritelju spodbudo, da bi kršil pravila. V situacijah, kjer preveritelju ni po volji zahteva izdajatelja ali avtoritete, bi lahko preprosto molčal — se ne odzval in blokiral algoritemsko zaporedje. Opazovalec — ali nabor opazovalcev — stavi svojo reputacijo na dokumentiranje tega, kako je bil preveritelj zaprošen. Če preveritelj molči kljub deklarirani politiki, ki pravi drugače, ga je mogoče obsoditi kršitve protokola.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mehanizem: časovni žig in izzivna koda

Preden pošlješ trditev preveritelju, jo usmeriš skozi opazovalce — ljudi, ki jim zaupaš, ali specializirane ponudnike opazovalskih storitev, ki zaračunajo majhno plačilo. Vsak opazovalec prejme tvojo predložitev, jo časovno žigosa, podpiše, da je videl, kako je odšla ven, in ustvari izzivno kodo — kriptografsko zgoščeno vrednost svojega podpisa. Kode se pripnejo tvoji zahtevi. Preveritelj jih vidi, a nima pojma, kdo so opazovalci ali ali so kode sploh resnične. Opazovalci tako delujejo kot posredniki med izdajateljem in preveriteljem in imajo neodvisen zapis, da je bila trditev predložena in kaj je vsebovala. Lahko jih je od nič do N.

Ko se preveritelj vede pošteno — sprejme ali zavrne v skladu s svojo deklarirano politiko — kode ostanejo neprozorne. Nihče ni razkrit.

Če pa preveritelj molči kljub prizanesljivi politiki ali se odzove na način, ki nasprotuje temu, kar je objavil, imaš izvirne podpise opazovalcev. Objaviš jih lahko kot posredniško pričanje, da je bila trditev predložena in da preveritelj ni sledil protokolu. Vsakdo lahko preveri, da se podpisi ujemajo z izzivnimi kodami.

## Poanta: pravih opazovalcev sploh ne potrebuješ

In tu je najbolj eleganten del: **pravih opazovalcev sploh ne potrebuješ.** Lahko generiraš naključna števila, ki so videti natanko kot izzivne kode. Preveritelj ne more razločiti razlike — mora metati kocke, ali tvegati svojo reputacijo. Za vsako zahtevo, ki jo prejme, bi lahko bil ugleden opazovalec, ki inkognito opazuje — ali pa je čist šum. Preveritelj ne ve. In prav ta negotovost je mehanizem.

Strošek vzdrževanja poštenega pritiska: skoraj nič (naključna števila so zastonj). Potencialni strošek nepoštenosti za preveritelja: katastrofalen. Pošteno vedenje je spodbujeno tudi takrat, ko dejansko nihče ne opazuje.

Sistem deluje, ker je vsak malo paranoičen. Negotovost je cenejša od nadzora.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Več preveriteljev v eni iteraciji
> Krepilno spremljevalno pravilo za razpoložljivost preveriteljev je lahko algoritemska razširitev, ki v eni iteraciji vrne nabor kandidatnih preveriteljev namesto le enega.
