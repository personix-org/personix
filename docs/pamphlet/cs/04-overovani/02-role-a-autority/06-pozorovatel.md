---
title: "Pozorovatel"
chapter: 3
part: "Jak funguje ověřování"
lang: cs
version: v6
source: "merge 02-pozorovatel + 04-trik-s-pozorovateli, esenci přesunuto do role"
---

# Pozorovatel

Role pozorovatele eliminuje u ověřovatele motivaci ohýbat pravidla. Ověřovatel by mohl v situacích, kdy mu žádost vydavatele nebo autority nesedí, prostě mlčet — neodpovědět, zablokovat algoritmickou posloupnost. Pozorovatel — nebo množina pozorovatelů — svou reputací ručí za to, že dokladuje průběh dotazování ověřovatele. Pokud ověřovatel mlčí navzdory deklarované politice, lze ho z porušení protokolu usvědčit.

![POZOROVATEL — VEDE ZÁZNAM O OVĚŘOVATELI](../../../Info%20Graphics/v5-cz/v5-08g-role-observer.webp)

## Mechanismus: časové razítko a kód výzvy

Než pošlete tvrzení ověřovateli, projdete s ním přes pozorovatele — lidi, kterým důvěřujete, nebo specializované poskytovatele pozorovatelských služeb za drobný poplatek. Každý pozorovatel vaše podání přijme, časově razítkuje, podepíše, že ho viděl odcházet, a vytvoří kód výzvy (challenge code) — kryptografický hash svého podpisu. Kódy se připojí k vašemu požadavku. Ověřovatel je vidí, ale netuší, kdo pozorovatelé jsou ani zda jsou kódy vůbec skutečné. Pozorovatelé tak fungují jako proxy mezi vydavatelem a ověřovatelem a drží nezávislý záznam, že tvrzení bylo odesláno a co obsahovalo. Může jich být nula až N.

Když se ověřovatel chová poctivě — přijme nebo odmítne v souladu se svou deklarovanou politikou — kódy zůstanou neprůhledné. Nikdo není odhalen.

Když ale ověřovatel mlčí navzdory vstřícné politice, nebo odpoví v rozporu s tím, co publikoval, máte v ruce originální podpisy pozorovatelů. Můžete je zveřejnit jako proxy svědectví, že tvrzení bylo odesláno a že se ověřovatel nezachoval podle protokolu. Kdokoli může ověřit, že podpisy odpovídají kódům výzvy.

## Pointa: skutečné pozorovatele nepotřebujete

A tady přichází ta nejelegantnější část: **reálné pozorovatele vůbec nepotřebujete.** Můžete vygenerovat náhodná čísla, která vypadají přesně jako kódy výzvy. Ověřovatel nepozná rozdíl — musí si hodit kostkou, jestli riskne svou reputaci. Za každým požadavkem, který dostane, může stát respektovaný pozorovatel sledující inkognito — nebo to může být jen šum. Ověřovatel to neví. A ta nejistota je ten mechanismus.

Náklady na udržení poctivého tlaku: skoro nulové (náhodná čísla jsou zadarmo). Potenciální náklady nepoctivosti pro ověřovatele: katastrofální. Poctivé chování je motivováno, i když ve skutečnosti nikdo nesleduje.

Systém funguje, protože jsou všichni trochu paranoidní. Nejistota vyjde levněji než dohled.

![BLUF, KTERÝ UDRŽUJE OVĚŘOVATELE POCTIVÝM](../../../Info%20Graphics/v5-cz/v5-09-trik-s-pozorovateli.webp)

> [!note] Násobnost ověřovatelů v jedné iteraci
> Posilujícím doprovodným pravidlem dostupnosti ověřovatelů, může být algoritmické rozšíření, aby v jedné iteraci vracel množinu potenciálních ověřovatelů a nikoliv jen jednoho. 