---
title: "Konsenzus a proces ověřování"
chapter: 3
part: "Jak funguje ověřování"
lang: cs
version: v6
source: v1
---

# Konsenzus a proces ověřování

Konsenzu o tom, která pravidla by se měla ve společnosti v průměru dodržovat a vynucovat, může pomoci následující mechanismus. Jako účastník DID deklaruji pravidla, ke kterým se hlásím a budu se jimi řídit, a zveřejním je. (Obdoba vyhlášek a zákonů, které podle mě tvoří můj vysněný svět — svět, ve kterém se neomezuji, ale cítím bezpečně.)

Můžu si u svých DID kontaktů dopředu odhadnout, jak by reagovali — a posoudit, jak silně a od koho by mě v běžných sociálních či obchodních interakcích sankce zasáhly, kdyby k nim hypoteticky došlo.

K definitivnímu vyhodnocení dojde, když od jiného DID požadujete informace nebo ho žádáte o ověření tvrzení (nebo žádáte službu od autority atp.), které chcete publikovat do reputační sítě. Mělo by to dopadnout stejně, jako když to vyhodnocujete u sebe nanečisto vůči deklarované politice (policy) protistrany — a když ne, něco není v pořádku u protistrany: snaží se hrát nečistou hru.

Výsledkem je buď přijetí s nabídnutou cenou za ověření (u služeb ověřovatele, autority), nebo odmítnutí. Sankce i bonusy za odchýlení se od politiky hodnotitele se promítají do nabídnuté ceny. Žadatel se rozhodne, zda podmínky přijme, nebo přejde do dalšího kola ověřování v alokačním algoritmu — a proces opakuje, dokud není spokojený, nebo to ekonomicky nevzdá.

> [!note] Sociální graf (The Social Graph)
> Reputační síť je především sociální sítí. Přidáváte kontakty — lidi, kteří spojení povolí. Ti mají kontakty a ty mají další kontakty. Algoritmus hledá ověřovatele v konfigurovatelné hloubce (např. tři úrovně: vaše přímé kontakty, jejich kontakty a jedna úroveň dál). Žádný globální blockchain není potřeba — síť přirozeně vytváří komunity s přesahy do dalších komunit.
>
> Algoritmus je nedeterministický: zahashuje váš dokument s tvrzením, namapuje hash na pozici na kruhu známých identit v tomto okruhu a jako kandidáta na ověřovatele vybere nejbližšího. Nemůžete předpovědět ani ovlivnit, kdo vaše tvrzení ověří.

Každé odmítnutí ověřovatele váš dokument zvětší a zdraží jeho zpracování — to je první nákladový kanál (narůstání dokumentu). Každý další ověřovatel účtuje poplatek podle objemu dat, vaší reputace a podle toho, jak daleko se obsah vašeho tvrzení odchyluje od jeho deklarované politiky ověřování — druhý nákladový kanál (riziková přirážka). A každá iterace stojí čas a energii — třetí nákladový kanál.

> [!note] Co ověřovatel kontroluje a v jakém pořadí
> Jakmile algoritmus vybere ověřovatele, prochází tvrzení zhruba čtyřmi kroky — od nejlevnějšího filtru po nejdražší obsahovou kontrolu:
>
> 1. **Policy gating.** Spadá tenhle typ tvrzení vůbec do toho, co ověřovatel veřejně dělá? Když ne, požadavek rovnou odmítne.
> 2. **Důvěra v autoritu.** Je autorita, která tvrzení podepsala, podle ověřovatelovy deklarované politiky dost důvěryhodná? Autorita pod jeho prahem důvěry je důvod k odmítnutí bez ohledu na obsah.
> 3. **Reputace vydavatele.** Splňuje vydavatel reputační prahy, které si ověřovatel pro tento typ tvrzení deklaroval? Nízká reputace může buď zvednout poplatek, nebo vést k odmítnutí.
> 4. **Obsahová kontrola.** Teprve když projdou první tři kroky, ověřovatel posuzuje samotné tvrzení — podpisy, vnitřní konzistenci, formální správnost a to, jak se odchyluje od jeho politiky. Poplatek za tento poslední krok odráží skutečně podstoupené riziko.
>
> Politiku, která řídí každou z těchto bran, ověřovatel veřejně publikuje — kroky tedy nejsou na jeho libovůli, je vázán tím, co sám deklaroval. Odchylka od publikované politiky je sama o sobě publikovatelným tvrzením proti němu a platí za ni svou reputací.

Výsledkem je, že zveřejnění věrohodného a užitečného tvrzení stojí skoro nic. Zveřejnit radikální tvrzení stojí víc. Zveřejnit lež se stane neúnosně drahým — musíte iterovat ověřovatele za ověřovatelem a každý, kdo vás odmítne, přidá náklady. Trh nacení vaše tvrzení a cena vám řekne, kde stojíte vůči komunitám, ve kterých se pohybujete.

Nestačí deklarovat, že pravidlo dodržuji, když ho v realitě nedodržuji. V takovém případě hrozí mému DID zveřejnění negativního záznamu, který odhalí pokrytectví — a ze mě udělá riziko pro ostatní. Výsledkem by mělo být méně pravidel, ale dodržovaných důsledněji, a pročištění té džungle zákonů a předpisů, ve které se sotva vyznají i právníci.

![POKRYTECTVÍ JE NEJDRAŽŠÍ CHOVÁNÍ](../../Info%20Graphics/v5-cz/v5-07c-pokrytectvi.webp)

> [!note] Konsenzus vs odpovědnost
> Aby síť sloužila jako hodnotný zdroj informací, DID by neměl být příliš radikální — jinak ho ostatní odmítnou. Sociální tlak bude hledat rovnováhu a pokusy o narušení stability si pravděpodobně vyberou svou daň.

![DEKLARUJ SVÁ PRAVIDLA, ZAPLAŤ CENU](../../Info%20Graphics/v5-cz/v5-07-deklarace-a-cena.webp)

> [!warning] Počet hlasů není to samé jako síla hlasu
> Juraj Karpiš říká, že „peníze jsou pamětí dobrých skutků". Dodávám, že reputace je pamětí těch špatných.
> 
> Z toho plyne, že meritokraticky by si větší váhu hlasu v komunitě zasloužil ten, kdo přispívá víc a nemá špatnou reputaci. Pokud se na to podíváme z pozice bilaterálních vztahů: když zvažuji, kterým tlakům na konsenzus víc vyjdu vstříc, zahrnu s největší vahou ty vztahy, ze kterých mám největší ekonomickou výhodu. Deset lidí, se kterými nemám čilý obchod, na mě zapůsobí mnohem méně než jeden trvalý obchodní partner. Toto paradigma se neomezuje jen na obchod — dá se rozšířit na sociální, politické a další vztahy.