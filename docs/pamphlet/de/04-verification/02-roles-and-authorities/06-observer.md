---
title: "Beobachter"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Beobachter

Die Beobachterrolle nimmt dem Verifizierer den Anreiz, die Regeln zu beugen. In Situationen, in denen einem Verifizierer die Anfrage des Ausstellers oder der Autorität nicht gefällt, könnte er einfach schweigen — nicht antworten und die algorithmische Abfolge blockieren. Der Beobachter — oder eine Gruppe von Beobachtern — setzt seine Reputation darauf, zu dokumentieren, wie der Verifizierer abgefragt wurde. Schweigt der Verifizierer trotz einer erklärten Richtlinie, die etwas anderes besagt, kann er des Verstoßes gegen das Protokoll überführt werden.

![DER BEOBACHTER — HÄLT DAS VERHALTEN DES VERIFIZIERERS FEST](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Der Mechanismus: Zeitstempel und Challenge-Code

Bevor du eine Behauptung an den Verifizierer schickst, leitest du sie über Beobachter — Menschen, denen du vertraust, oder spezialisierte Beobachter-Dienstleister, die eine kleine Gebühr verlangen. Jeder Beobachter empfängt deine Einreichung, versieht sie mit einem Zeitstempel, signiert, dass er sie hat hinausgehen sehen, und erzeugt einen Challenge-Code — einen kryptografischen Hash seiner Signatur. Die Codes werden an deine Anfrage angehängt. Der Verifizierer sieht sie, hat aber keine Ahnung, wer die Beobachter sind oder ob die Codes überhaupt echt sind. Beobachter fungieren so als Mittler zwischen dem Aussteller und dem Verifizierer und halten einen unabhängigen Nachweis, dass die Behauptung eingereicht wurde und was sie enthielt. Es kann null bis N von ihnen geben.

Wenn sich der Verifizierer ehrlich verhält — annehmend oder ablehnend im Einklang mit seiner erklärten Richtlinie —, bleiben die Codes undurchsichtig. Niemand wird bloßgestellt.

Doch wenn der Verifizierer trotz einer entgegenkommenden Richtlinie schweigt oder in einer Weise antwortet, die dem widerspricht, was er veröffentlicht hat, hältst du die ursprünglichen Beobachter-Signaturen. Du kannst sie als stellvertretendes Zeugnis dafür veröffentlichen, dass die Behauptung eingereicht wurde und dass der Verifizierer dem Protokoll nicht gefolgt ist. Jeder kann überprüfen, dass die Signaturen zu den Challenge-Codes passen.

## Die Pointe: Du brauchst keine echten Beobachter

Und hier kommt der eleganteste Teil: **Du brauchst überhaupt keine echten Beobachter.** Du kannst Zufallszahlen erzeugen, die genau wie Challenge-Codes aussehen. Der Verifizierer kann den Unterschied nicht erkennen — er muss würfeln, ob er seine Reputation riskiert. Hinter jeder Anfrage, die er erhält, könnte ein angesehener Beobachter inkognito zusehen — oder es könnte reines Rauschen sein. Der Verifizierer weiß es nicht. Und diese Ungewissheit ist der Mechanismus.

Die Kosten, ehrlichen Druck aufrechtzuerhalten: nahezu null (Zufallszahlen sind gratis). Die potenziellen Kosten der Unehrlichkeit für den Verifizierer: katastrophal. Ehrliches Verhalten wird selbst dann incentiviert, wenn niemand tatsächlich zusieht.

Das System funktioniert, weil jeder ein wenig paranoid ist. Ungewissheit ist billiger als Überwachung.

![DER BLUFF, DER DEN VERIFIZIERER EHRLICH HÄLT](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Mehrere Verifizierer in einer einzigen Iteration
> Eine verstärkende Begleitregel für die Verfügbarkeit von Verifizierern kann eine algorithmische Erweiterung sein, die in einer einzigen Iteration eine Menge von Kandidaten-Verifizierern statt nur eines einzigen zurückgibt.
