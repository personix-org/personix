---
title: "Reputationsbasiertes soziales Netzwerk"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputationsbasiertes soziales Netzwerk

Um einen Wandel herbeizuführen, brauchen wir ein sorgfältig entworfenes Werkzeug. Zuerst skizzieren wir es kurz. In späteren Kapiteln betrachten wir jeden Baustein genauer und fügen mehr hinzu. Stell dir ein unzensierbares, globales, dezentrales soziales Netzwerk vor, in dem du sicher deine stellvertretende Identität erstellen und verwalten könntest — eine sogenannte dezentrale Identität (DID). Eine DID ist eine digitale Identität, die du selbst erstellst und kontrollierst, ohne Abhängigkeit von einer zentralen Autorität. Niemand kann sie dir wegnehmen oder fälschen, denn sie ist kryptografisch mit deinem privaten Schlüssel (oder mehreren Schlüsseln, per Multisig) signiert.

> [!note] Anmerkung
> Eine Konsequenz ist, dass eine solche Identität nach und nach staatlich ausgestellte Ausweisdokumente ersetzen könnte — dazu aber mehr im Kapitel über den Übergang.

![DEINE IDENTITÄT, DEINE SCHLÜSSEL, DEINE REGELN](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

In einem solchen Netzwerk könntest du über deine Identität melden, dass dir jemand einen Schaden zugefügt hat (und später womöglich, dass er ihn behoben hat oder dazu gezwungen wurde). Damit dieses Feedback — gerichtet an den Verursacher des Schadens — als relevante Quelle Wert hat, muss das Einspeisen von Informationen ins Netzwerk Zeit, Energie und Geld kosten — und darüber hinaus muss für andere ein überprüfbarer Beweis erbracht werden, dass es sich nicht um leeres Gerede handelt.

Das Lesen von Informationen wäre einfach und relativ günstig, doch das Anlegen eines einzelnen Eintrags wäre kostspielig und anspruchsvoll. Das Schreiben würde einem klaren Protokoll folgen, in dem eine Berechnung nach dem gewählten Algorithmus streng festlegt, welche DID zur Verifizierung der eingereichten Information zu befragen ist und wie vorzugehen ist, damit der ausgewählte Teilnehmer die Information in deinem Namen verarbeitet, sie veröffentlicht und ihr Verifizierer wird.

> [!note] Algorithmus vs. Radikalismus
> Die algorithmische Auswahl der Verifizierer stellt sicher, dass nicht-radikale Informationsveröffentlicher mit der Zeit eine nahezu neutrale Bilanz zwischen den Kosten veröffentlichter Informationen und den Belohnungen für die Verifizierung halten.

![VERÖFFENTLICHEN KOSTET ZEIT, ENERGIE UND GELD](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Schauen wir uns an, wie der Algorithmus einen Verifizierer auswählt.

> [!note] Algorithmus
> Die algorithmische Auswahl wählt für verschiedene Informationen nicht-deterministisch einen anderen Verifizierer (oder eine Menge möglicher Verifizierer). Ein Hash (eine mathematische Einwegfunktion, die aus einer beliebigen Eingabe einen eindeutigen „Fingerabdruck" erzeugt — wie ein Fingerabdruck eines Dokuments) des vollständigen DID-Dokuments bestimmt die Position auf einem konsistenten Hash-Ring und wählt die Kandidaten für die Verifizierung aus.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Einfach gesagt: Der Algorithmus nimmt dein gesamtes DID-Dokument, berechnet daraus einen Fingerabdruck, und dieser Fingerabdruck bestimmt deinen Verifizierer.

![WIE DER ALGORITHMUS DEINEN VERIFIZIERER AUSWÄHLT](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Beim ersten Verifizierer, den der Algorithmus auswählt, hast du als Veröffentlicher womöglich keinen Erfolg — deine Reputation oder deine erklärten Einstellungen erfüllen vielleicht seine Anforderungen nicht. Du würdest die Suche nach dem nächsten algorithmisch fortsetzen, indem du eine weitere rekursive Iteration durchführst, die dir einen weiteren Verifizierer zuweist. Mit jedem Schritt wächst die „Distanz" zum Zielverifizierer, und ebenso wachsen die begleitenden Metadaten, die veröffentlicht werden müssen. Mit den Daten steigen naturgemäß auch die Kosten (nicht nur wegen der anfänglichen Größe der Behauptung, sondern auch wegen der mit jeder Ablehnung anwachsenden Metadaten). Glaubwürdige Informationen kommen weit leichter durch als unsinnige Launen. Es liegt an jedem selbst, wie hohen Preis er zu tragen bereit ist und wie viel ihm der Eintrag bedeutet — Radikalismus wird garantiert teuer.

![WIE DER VERIFIZIERER ANTWORTET](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Was auch immer der Verifizierer als Antwort auf deine Verifizierungsanfrage entscheidet, der Ball liegt wieder beim Veröffentlicher: Er kann das Angebot des Verifizierers für Verifizierungsdienste annehmen, die Antwort in die Chronologie einfügen und es (teurer) erneut versuchen oder aufgeben und die versunkenen Kosten schlucken.

![DIE ENTSCHEIDUNG DES AUSSTELLERS](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Um deiner Information mehr Gewicht und eine bessere Chance auf Annahme bei den Verifizierern zu geben, könntest du — als Veröffentlicher mit einem Interesse an der Herausgabe der Information — die Dienste einer **vertrauenswürdigen Autorität** in Anspruch nehmen. Die Autorität lehnt die eingereichte Information entweder ab oder nimmt sie an und setzt ihren guten Namen (ihre Reputation) darauf. Die Autorität verlangt in der Regel reale Nachweise, überprüft sie und ordnet sie ein. Das Ergebnis ist ein Protokoll ihrer Bewertung des jeweiligen Falls zum jeweiligen Zeitpunkt. Denke dir eine Autorität als Spezialisten für eine bestimmte Art von Dienstleistung sowohl in der realen als auch in der digitalen Welt — zum Beispiel einen Ermittler, einen Auditor, einen Versicherer, einen Lieferanten einer bestimmten Warenklasse (im Grunde jeden Wirtschaftsakteur auf dem Markt).

![WIE EIN EINTRAG IM NETZWERK ENTSTEHT](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Wenn du versuchst, Informationen ins Netzwerk zu stellen, enthält es wahrscheinlich schon Informationen über seine Akteure — das sind Reputationssignale. Sich zurechtzufinden, wie man Reputationssignale liest — was sie für dich in verschiedenen Situationen bedeuten und welche Risiken sie bergen —, ist vielleicht nicht trivial. Jeder Teilnehmer kann Reputationseinträge über seine DID unterschiedlich betrachten, je nach der Situation, mit der er es gegenüber der Gegenseite zu tun hat. Ist die Gegenseite ein zuverlässiger Zahler, oder muss ich für ein Geschäft Geld im Voraus verlangen? Trägt das angebotene Produkt Bewertungen über verborgenen Betrug oder Mängel? Versucht sie, sich aus der vertraglichen Verantwortung zu winden, wenn etwas schiefgeht? Manchmal kommt ein komplexerer Blick auf die Gesamtkonsistenz der Gegenseite gelegen — es hängt von den Präferenzen dessen ab, der die Übersicht anfordert. Der Markt könnte Produkte und Dienstleistungen anbieten, die das Lesen der Reputation im Kontext der jeweiligen Situation vereinfachen, aufbereiten und verdeutlichen. Auch verschiedene Autoritäten und ihre angebotenen Dienste können diesem Zweck dienen.

![WIE MAN REPUTATION LIEST](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Beispiele
> Typische Informationen, die für Veröffentlicher von Interesse — und für andere wertvoll — sind, betreffen Ereignisse jenseits der gewöhnlichen zwischenmenschlichen Kommunikation in der realen oder virtuellen Welt.
>
> Negative Beispiele:
> - Belege für strafbare Handlungen (z. B. von einer vertrauenswürdigen Ermittlungsstelle geprüft)
> - Indizienbeweise (für sich allein schwach, aber statistisch kumulativ) — z. B. wiederholte Anwesenheit in der Nähe mehrerer Diebstähle in kurzer Zeit → noch Zufall?
> - Vertragsbruch
>
> Positive Beispiele:
> - behobener Schaden (freiwillig oder unter Druck der Gemeinschaft als Strafe)
> - Annahme und Verbüßung einer von Autorität X vorgeschlagenen Strafe
> - Autorität X hat die Anerkennung der Eigentumsrechte des Täters in gewissem Umfang entzogen
>
> Es liegt an jedem selbst, verfügbare Informationen über die Gegenseite zu sammeln und die Risiken nach seinen Präferenzen zu bewerten.

![WAS KANNST DU IM NETZWERK FESTHALTEN?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Ob Informationen über dich im Netzwerk erscheinen, hängt ausschließlich von deinem eigenen Verhalten ab.
> Du musst einem solchen Netzwerk nie beitreten, und dennoch können Informationen über dich darin erscheinen. Es hängt ausschließlich von deinen Handlungen und deren Auswirkungen auf andere ab.

![DIE GEMEINSCHAFT KANN EINE FÜR DICH ERÖFFNEN](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Was ich soeben kurz skizziert habe, ist, wie ein von der dezentralen Identität (DID) inspiriertes soziales Netzwerk funktionieren könnte. Der Hauptzweck der DID-Konzepte ist es, Privatsphäre und Freiheit durch das Prinzip zu stärken, sich zu den Regeln zu bekennen, denen ich folgen und nach denen ich leben werde — indem den Nutzern die Möglichkeit gegeben wird, zu entscheiden, welche Informationen sie unter welchen Bedingungen teilen.

Ich schlage vor, DIDs weiter zu einem Kommunikationsnetzwerk zu verbinden, in dem ihre Inhaber Feedback austauschen, auch über Situationen hinaus, in denen jemandem etwas zugestoßen ist und die Gemeinschaft oder ein Einzelner reagieren muss. Ein solcher präventiver Abgleich der Regeln, zu denen wir uns bekannt haben — mit der Möglichkeit, die wirtschaftlichen und sonstigen Folgen gegenseitiger Abweichungen in den Erwartungen darüber, wie die andere Seite agieren sollte, zu berechnen —, ließe sich als Motivation zum Finden von Konsens betrachten. Statt Freiheit würde ein solches System freiwillige Entscheidung in Verbindung mit Verantwortung für das Verhalten in der realen Welt betonen.

Ein Individuum kann das System nicht allein brechen — eine Gruppe von Menschen hat eine größere Chance, und eine Gruppe von Menschen mit ausgehandeltem Konsens und Motivationen, in vielen Fragen an einem Strang zu ziehen, hat eine noch größere Chance, autoritären Tendenzen zu widerstehen. Die Voraussetzung der Organisation aus dem ersten Kapitel wird erfüllt sein, sobald zwei Bedingungen gegeben sind: Das DID-Reputationsnetzwerk deckt Gemeinschaften repräsentativ genug ab, dass seine Nutzung nicht mehr exotisch ist. Und zugleich wird dieses Gemeinschaftssegment zu einer wirtschaftlich bedeutsamen Minderheit, die selbstbewusst mit dem Rest der Gesellschaft verhandeln kann.

> [!note] Freiwilligkeit vs. Freiheit
> Freiheit — im positiven Sinne — wäre ein sekundärer Effekt des Ausbalancierens zweier Faktoren: der Freiwilligkeit und des Drucks der Umgebung hin zur Verantwortung.

> [!note] Das KI-Zeitalter und der Wert der Reputation
> Im Zeitalter der künstlichen Intelligenz wird alles, was mit kognitivem Denken zusammenhängt, automatisiert — und es könnte noch weiter gehen. Was bleibt dann in der menschlichen Tätigkeit als Wettbewerbsvorteil? Die Antwort ist schwierig, und etwas wird sich sicher finden, aber eines können wir mit Gewissheit sagen: Die Reputation wird entscheiden. Eine überprüfbare Geschichte deines Verhaltens, deiner Verpflichtungen und ihrer Erfüllung — das ist etwas, das die KI nicht für dich aufbauen wird.

![DIE KI KANN DEINE REPUTATION NICHT AUFBAUEN — NUR DU KANNST ES](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![DIE ÖKONOMIE DER WAHRHEIT](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
