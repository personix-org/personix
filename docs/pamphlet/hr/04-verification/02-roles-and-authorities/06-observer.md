---
title: "Promatrač"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Promatrač

Uloga promatrača uklanja verifikatorov poticaj da savija pravila. U situacijama u kojima se verifikatoru ne sviđa izdavateljev ili autoritetov zahtjev, mogao bi jednostavno šutjeti — ne odgovoriti i blokirati algoritamski slijed. Promatrač — ili skup promatrača — ulaže svoju reputaciju u dokumentiranje toga kako je verifikator upitan. Ako verifikator šuti unatoč deklariranoj politici koja govori drukčije, može biti osuđen za kršenje protokola.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mehanizam: vremenska oznaka i izazovni kôd

Prije nego što tvrdnju pošalješ verifikatoru, usmjeravaš je kroz promatrače — ljude kojima vjeruješ, ili specijalizirane pružatelje promatračke usluge koji naplaćuju malu naknadu. Svaki promatrač prima tvoj podnesak, vremenski ga označava, potpisuje da je vidio kako izlazi i generira izazovni kôd — kriptografski hash svojeg potpisa. Kôdovi se dodaju tvojem zahtjevu. Verifikator ih vidi, ali nema pojma tko su promatrači ni jesu li kôdovi uopće stvarni. Promatrači tako djeluju kao posrednici između izdavatelja i verifikatora, čuvajući neovisan zapis da je tvrdnja podnesena i što je sadržavala. Može ih biti od nula do N.

Kad se verifikator ponaša pošteno — prihvaćajući ili odbijajući u skladu sa svojom deklariranom politikom — kôdovi ostaju neprozirni. Nitko nije izložen.

Ali ako verifikator šuti unatoč popustljivoj politici, ili odgovori na način koji proturječi onome što je objavio, ti držiš izvorne potpise promatrača. Možeš ih objaviti kao posredničko svjedočanstvo da je tvrdnja podnesena i da verifikator nije slijedio protokol. Svatko može provjeriti da se potpisi podudaraju s izazovnim kôdovima.

## Poanta: ne trebaš stvarne promatrače

I evo najelegantnijeg dijela: **stvarni ti promatrači uopće ne trebaju.** Možeš generirati nasumične brojeve koji izgledaju posve kao izazovni kôdovi. Verifikator ne može razaznati razliku — mora bacati kocku hoće li riskirati svoju reputaciju. Iza svakog zahtjeva koji primi mogao bi biti ugledan promatrač koji gleda inkognito — ili bi to mogao biti čisti šum. Verifikator ne zna. I ta je neizvjesnost mehanizam.

Trošak održavanja poštenog pritiska: gotovo nula (nasumični su brojevi besplatni). Potencijalni trošak nepoštenja za verifikatora: katastrofalan. Pošteno ponašanje potiče se čak i kad nitko zapravo ne gleda.

Sustav funkcionira zato što je svatko pomalo paranoičan. Neizvjesnost je jeftinija od nadzora.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Više verifikatora u jednoj iteraciji
> Pojačavajuće prateće pravilo za dostupnost verifikatora može biti algoritamsko proširenje koje u jednoj iteraciji vraća skup kandidata za verifikatora umjesto samo jednog.
