---
title: "Verifizierer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifizierer

Jede DID kann als Verifizierer auftreten, entweder direkt oder über Verifizierungsrechte, die an eine dritte DID delegiert sind. Damit ich — oder mein Stellvertreter — verifizieren kann, sollte ich im Netzwerk erreichbar sein (online). Nicht jeder wird sich dazu verpflichten wollen, weshalb ein DID-Eintrag in Prioritätsreihenfolge die Stellvertreter auflisten kann, die die Funktion in seinem Namen ausüben, während die DID offline ist.

Jede im Netzwerk aktive DID erklärt öffentlich ihre eigene Richtlinie. Durch die in dieser Richtlinie definierten Regeln beurteilt sie während des Verifizierungsprozesses die Reputation der Gegenseite sowie Inhalt und Form der Aussage, die der Aussteller zur Veröffentlichung ins Reputationsnetzwerk vorgesehen hat. Teil der Richtlinie ist die Berechnungsformel, mit der die Gebühren für Verifizierungsdienste berechnet werden. Sobald das steht, warte ich über eine statistisch große Zahl von Aussagen, die durchs Netzwerk fließen, darauf, dass mich der Algorithmus des Netzwerks auf die Seite des Ausstellers zieht und mir in einer gegebenen Iteration zuweist, die ausgestellte Information zu verifizieren. Der Aussteller kann im Voraus berechnen, wie ein sich korrekt verhaltender Verifizierer reagieren würde, kann es aber nicht vermeiden, ihn (oder seine Stellvertreter) tatsächlich zu kontaktieren; die Iteration mit dem ausgewählten Verifizierer muss der Aussteller selbst dann durchführen, wenn er im Voraus weiß, dass sie nicht durchgehen wird.

Woher wissen wir, dass der Aussteller den Algorithmus zur Verifiziererauswahl über die richtige Menge von Kandidaten-Verifizierer-DIDs laufen lässt? Zusammen mit ihrer öffentlich erklärten Richtlinie veröffentlicht jede DID auch die aktuelle Liste der Kennungen ihres sozialen Netzwerks innerhalb des Reputationsnetzwerks. Definiert ein Aussteller sein soziales Netzwerk als eine soziale Blase, die seine eigenen Ansichten lediglich widerspiegelt und verstärkt, so werden über sie veröffentlichte Informationen von anderen Gemeinschaften kaum breiter aufgenommen. Dass es mir gelingt, unter hohen Kosten eine radikale Aussage im Netzwerk durchzusetzen, bedeutet nicht, dass ich ihr bei der Beurteilung der Reputation der Gegenseite irgendein Gewicht beimessen werde. Bei manchen Aussagen drängt mich meine Gemeinschaft, sie zu berücksichtigen (über Täter verhängte Strafen und Beschränkungen); andere stehen ganz mir frei — ich entscheide selbst über den wirtschaftlichen Wert, eine gegebene Information einzubeziehen oder auszuschließen.

![DER VERIFIZIERER — VOM ALGORITHMUS GEWÄHLT](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
