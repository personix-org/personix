---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# A szerepek áttekintése

Néhány ezek közül a szerepek közül már röviden érintettük a hálózatról és annak alaptulajdonságairól szóló fejezetben. Most itt az ideje, hogy részletesebben újra megnézzük őket, és hozzátegyük a továbbiakat, amelyekre szükségünk van, hogy a hálózat robusztusabb legyen. Minden ellenőrzési tranzakcióban több szerep vesz részt — lássuk, hogyan viselkednek.

> [!note] Szerepek egy ellenőrzési tranzakcióban
> Minden ellenőrzésben legfeljebb hat különböző szerep vesz részt, amelyeket az alábbi táblázat foglal össze. Mindegyiknek lehet saját DID-je a decentralizált reputációs hálózatban.

| Szerep | Leírás |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kibocsátó** | Az a személy, aki információt tesz közzé a hálózatban — állítja, hogy valami történt (egy DID jött létre, módosult vagy szűnt meg, egy állítás, egy adott DID elvei stb.) |
| **Alany** | Az a személy, akiről az információ szól — az állítás címzettje |
| **Autoritás** | Megbízható entitás, amely a jó nevét teszi az állítás minőségére azzal, hogy kivizsgálja, és vagy áttekinti a bemutatott bizonyítékokat, vagy aktívan összegyűjti azokat |
| **Megfigyelő** | Független harmadik fél, aki nyilvántartást vezet arról, hogyan kezeli az ellenőrző az állítást — biztosítva, hogy az ellenőrző se ne hallgasson, se ne térjen el az általa deklarált elvektől |
| **Ellenőrző** | Algoritmikusan kiválasztott résztvevő, aki feldolgozza a tranzakciót |
| **Megbízott** | Egy másik résztvevő nevében eljáró személy |
