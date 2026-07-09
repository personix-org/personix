---
title: "Überblick über die Rollen"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Überblick über die Rollen

Einige dieser Rollen haben wir im Kapitel über das Netzwerk und seine grundlegenden Eigenschaften bereits kurz gestreift. Nun ist es an der Zeit, sie erneut genauer zu betrachten und die weiteren hinzuzufügen, die wir brauchen, um das Netzwerk robuster zu machen. An jeder Verifizierungstransaktion sind mehrere Rollen beteiligt — sehen wir uns an, wie sie sich verhalten.

> [!note] Rollen in einer Verifizierungstransaktion
> An jeder Verifizierung sind bis zu sechs verschiedene Rollen beteiligt, zusammengefasst in der Tabelle unten. Sie alle können ihre eigene DID im dezentralen Reputationsnetzwerk haben.

| Rolle | Beschreibung |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Aussteller** | Die Person, die Informationen im Netzwerk veröffentlicht — behauptet, dass etwas geschehen ist (eine DID wurde erstellt, bearbeitet oder aufgelöst, eine Behauptung, die Richtlinie einer gegebenen DID usw.) |
| **Subjekt** | Die Person, über die die Information handelt — der Adressat der Behauptung |
| **Autorität** | Eine vertrauenswürdige Entität, die ihren Namen für die Qualität der Behauptung einsetzt, indem sie sie untersucht und entweder die vorgelegten Beweise prüft oder sie aktiv sammelt |
| **Beobachter** | Ein unabhängiger Dritter, der festhält, wie der Verifizierer mit der Behauptung umgeht — und sicherstellt, dass der Verifizierer weder schweigt noch von der von ihm erklärten Richtlinie abweicht |
| **Verifizierer** | Ein algorithmisch ausgewählter Teilnehmer, der die Transaktion verarbeitet |
| **Delegierter** | Eine Person, die im Namen eines anderen Teilnehmers handelt |
