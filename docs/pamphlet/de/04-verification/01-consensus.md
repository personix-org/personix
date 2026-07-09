---
title: "Konsens und der Verifizierungsprozess"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsens und der Verifizierungsprozess

Um Konsens darüber aufzubauen, welche Regeln eine Gesellschaft im Durchschnitt hochhalten und durchsetzen sollte, kann der folgende Mechanismus helfen. Als DID-Teilnehmer erkläre ich die Regeln, zu denen ich mich bekenne und nach denen ich leben werde, und ich veröffentliche sie. (Denke es dir als die Satzung und die Statuten, die aus meiner Sicht meine ideale Welt ausmachen — eine Welt, in der ich mich nicht eingeschränkt, sondern sicher fühle.)

Ich kann im Voraus abschätzen, wie meine DID-Kontakte reagieren würden — und einschätzen, wie stark und von wem ich in gewöhnlichen sozialen oder geschäftlichen Interaktionen sanktioniert würde, sollten sie hypothetisch stattfinden.

Die endgültige Bewertung geschieht, wenn du Informationen von einer anderen DID anforderst oder sie bittest, eine Behauptung zu verifizieren (oder eine Autorität um einen Dienst bittest usw.), die du ins Reputationsnetzwerk veröffentlichen willst. Sie sollte genauso ausfallen, wie wenn du die Bewertung selbst im Trockenlauf gegen die erklärte Richtlinie der Gegenseite durchführst — und wenn nicht, dann stimmt etwas auf der Seite der Gegenseite nicht: Sie versucht, ein unehrliches Spiel zu spielen.

Das Ergebnis ist entweder eine Annahme mit einem genannten Preis für die Verifizierung (im Fall von Diensten eines Verifizierers oder einer Autorität) oder eine Ablehnung. Sowohl Sanktionen als auch Boni für Abweichungen von der Richtlinie des Bewertenden sind in den genannten Preis eingefaltet. Der Anfragende entscheidet dann, ob er die Bedingungen annimmt oder zur nächsten Runde der Verifizierung im Zuteilungsalgorithmus übergeht — und wiederholt den Prozess, bis er zufrieden ist oder bis die Ökonomie das Weitermachen sinnlos macht.

> [!note] Der soziale Graph
> Das Reputationsnetzwerk ist in erster Linie ein soziales Netzwerk. Du fügst Kontakte hinzu — Menschen, die der Verbindung zustimmen. Sie haben Kontakte, und jene Kontakte haben Kontakte. Der Algorithmus sucht Verifizierer innerhalb einer konfigurierbaren Tiefe (z. B. drei Ebenen: deine direkten Kontakte, deren Kontakte und eine Ebene darüber hinaus). Keine globale Blockchain ist nötig — das Netzwerk bildet auf natürliche Weise Gemeinschaften mit Überlappungen in andere Gemeinschaften.
>
> Der Algorithmus ist nichtdeterministisch: Er hasht dein Behauptungsdokument, bildet den Hash auf eine Position auf einem Ring bekannter Identitäten innerhalb dieses Kreises ab und wählt die nächstgelegene als Kandidaten-Verifizierer. Du kannst weder vorhersagen noch beeinflussen, wer deine Behauptung verifiziert.

Jede Ablehnung eines Verifizierers vergrößert dein Dokument und erhöht seine Verarbeitungskosten — das ist der erste Kostenkanal (Wachstum des Dokuments). Jeder neue Verifizierer verlangt eine Gebühr auf Basis des Datenvolumens, deiner Reputation und wie weit der Inhalt deiner Behauptung von seiner erklärten Verifizierungsrichtlinie abweicht — das ist der zweite Kostenkanal (Risikoprämie). Und jede Iteration kostet Zeit und Energie — der dritte Kostenkanal.

> [!note] Was der Verifizierer prüft, der Reihe nach
> Einmal ausgewählt, bewertet ein Verifizierer eine Behauptung in etwa vier geordneten Schritten — die günstigsten Filter zuerst, die teuren Inhaltsprüfungen zuletzt:
>
> 1. **Richtlinien-Gate.** Fällt diese Art von Behauptung überhaupt in das, was der Verifizierer öffentlich verifiziert? Wenn nicht, wird die Anfrage rundweg abgelehnt.
> 2. **Vertrauen in die Autorität.** Ist die Autorität, die die Behauptung befürwortet hat, unter der eigenen erklärten Richtlinie des Verifizierers vertrauenswürdig genug? Eine Autorität unterhalb der Vertrauensschwelle des Verifizierers ist ein Ablehnungsgrund, unabhängig vom Inhalt der Behauptung.
> 3. **Reputation des Ausstellers.** Erfüllt der Aussteller die Reputationsschwellen, die der Verifizierer für diese Art von Behauptung erklärt hat? Niedrige Reputation kann entweder die Gebühr erhöhen oder eine Ablehnung auslösen.
> 4. **Inhaltsprüfung.** Erst wenn die ersten drei Gates passiert sind, bewertet der Verifizierer die Behauptung selbst — Signaturen, innere Konsistenz, formale Korrektheit und wie weit sie von der Richtlinie des Verifizierers abweicht. Die für diesen letzten Schritt berechnete Gebühr spiegelt das tatsächlich eingegangene Risiko wider.
>
> Der Verifizierer veröffentlicht die Richtlinie, die jedes dieser Gates regelt, sodass die Schritte nicht in seinem Ermessen stehen — er ist an das gebunden, was er bereits erklärt hat. Eine Abweichung von der veröffentlichten Richtlinie ist selbst eine veröffentlichbare Behauptung gegen ihn, und er bezahlt sie mit seiner Reputation.

Das Ergebnis: Die Veröffentlichung einer glaubwürdigen und nützlichen Behauptung kostet fast nichts. Die Veröffentlichung einer radikalen Behauptung kostet mehr. Die Veröffentlichung einer Lüge wird prohibitiv teuer — du musst Verifizierer um Verifizierer durchlaufen, und jeder, der dich ablehnt, fügt Kosten hinzu. Der Markt bepreist deine Behauptung, und der Preis sagt dir, wo du im Verhältnis zu den Gemeinschaften stehst, in denen du dich bewegst.

Es genügt nicht, zu erklären, dass du dich an eine Regel hältst, wenn du es in Wahrheit nicht tust. In diesem Fall riskiert deine DID die Veröffentlichung eines negativen Eintrags, der die Heuchelei offenlegt — was dich zu einem Risiko für alle anderen macht. Das Ergebnis sollten weniger, aber konsequenter befolgte Regeln sein und eine Lichtung jenes Dschungels aus Gesetzen und Vorschriften, in dem sich selbst Rechtsprofis kaum zurechtfinden.

![HEUCHELEI IST DAS TEUERSTE VERHALTEN](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsens vs. Rechenschaft
> Damit das Netzwerk als wertvolle Informationsquelle dienen kann, sollte eine DID nicht zu radikal sein — sonst weisen die anderen sie ab. Der soziale Druck wird ein Gleichgewicht suchen, und Versuche, es zu destabilisieren, werden wahrscheinlich bestraft.

![ERKLÄRE DEINE REGELN, ZAHLE DEN PREIS](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Die Anzahl der Stimmen ist nicht dasselbe wie das Gewicht einer Stimme
> Juraj Karpiš sagt, „Geld ist das Gedächtnis der guten Taten". Ich würde hinzufügen, dass Reputation das Gedächtnis der schlechten ist.
>
> Daraus folgt, dass meritokratisch derjenige, der mehr beiträgt und keine schlechte Reputation hat, ein größeres Stimmgewicht in der Gemeinschaft verdient. Durch die Linse bilateraler Beziehungen betrachtet: Wenn ich abwäge, welchen Konsensdrücken ich entgegenkomme, geht das größte Gewicht an die Beziehungen, aus denen ich den größten wirtschaftlichen Nutzen ziehe. Zehn Menschen, mit denen ich keinen aktiven Handel habe, werden mich weit weniger beeinflussen als ein dauerhafter Geschäftspartner. Dieses Paradigma ist nicht auf den Handel beschränkt — es erstreckt sich auf soziale, politische und andere Beziehungen.
