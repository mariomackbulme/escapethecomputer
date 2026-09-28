# Game Vision

<details>
<summary>Changelog</summary>

| Ver. | Datum | Änderung | Autor |
| :----: | :----: | ------ | :----: |
| v0.1 | 21.09.26 | Erste Version | Team |

</details>

## Worum geht's

Escape the Computer ist ein 2D-Lernspiel im comicartigen Look, das Kindern und Computer-Neulingen die grundlegenden Hardwarekomponenten eines PCs beibringt - nicht als Text zum Nachlesen, sondern eingebaut in die Spielmechanik selbst.

## Die Spielwelt

Das Spielfeld ist ein Motherboard, von oben betrachtet, im vollen comicartigen Stil - bunt und einladend von der ersten Sekunde an, damit das Spiel gerade für Kinder sofort ansprechend wirkt. Zu Spielbeginn wirkt die Welt aber spürbar gedämpft und unbelebt: leicht entsättigte Farben, ruhige, flache Darstellung, kein Ton. Mit jeder erfolgreich aktivierten Station verändert sich das Board sichtbar und/oder hörbar: Der Kopfhörer-Anschluss bringt Sound ins Spiel, die Grafikkarte hebt die Darstellung auf die volle Stufe (siehe unten). Der Spieler sieht seinen Fortschritt also direkt an der Spielwelt selbst.

## Die Hauptfigur: Nibble

Der Spieler steuert die Figur **Nibble**. Der Name ist bewusst gewählt: Ein Nibble ist in der Informatik die Bezeichnung für 4 Bit (ein halbes Byte) - und genau daraus besteht die Figur: Sie hat vier Bits, die gleichzeitig ihre vier Lebenspunkte sind. Das Spiel vermittelt den Fachbegriff also nicht als Definition, sondern dadurch, dass man ihn im Kern der Spielfigur direkt erlebt.

Der aktuelle Lebensstand wird zusätzlich als Batterieanzeige am Motherboard dargestellt. Verliert Nibble alle vier Bits, ist die Batterie leer - Nibble "hüpft" aus dem Spielfeld, und das Spiel ist vorbei.

## Bewegung & Stationen

Nibble bewegt sich frei über das Motherboard, in alle Richtungen - anders als die Bits (siehe unten) ist er an keine festen Bahnen gebunden. Die Hardware-Stationen sind an festen Positionen auf dem Board platziert, ähnlich wie bei einem echten Motherboard angeordnet. Jede Station stellt eine eigene Aufgabe. Das MVP umfasst sechs Stationen:

1. **Kopfhörer-Anschluss** - nach erfolgreicher Aufgabe wird Sound aktiviert. Ruhiger Einstieg ohne Gefahr, hier lernt der Spieler Bewegung und Fragenbeantwortung in Ruhe kennen.
2. **CPU** - nach erfolgreicher Aufgabe beginnt die eigentliche Gefahr (siehe unten): Die CPU erzeugt ab jetzt fortlaufend Bits, die über das Board wandern und den Spieler bis zum Spielende begleiten.
3. **RAM-Slot 1** - nach erfolgreicher Aufgabe werden die umherfliegenden Bits schneller.
4. **PCI-Express-Slot / Grafikkarte** - nach erfolgreicher Aufgabe wird die Darstellung aufgewertet: Farbsättigung und Kontrast steigen spürbar, dazu kommen ein sanfter Leuchteffekt an den Bauteilen und kleine Partikel-Effekte im Hintergrund. Das Board wirkt danach deutlich lebendiger - nicht, weil vorher Farbe fehlte, sondern weil die Grafikkarte die Darstellung sichtbar verbessert.
5. **RAM-Slot 2** - wie RAM-Slot 1, das Tempo steigt ein weiteres Mal, das Spiel wird spürbar schwerer.
6. **USB-Anschluss** - die letzte Station, siehe "Spielende" unten.

An jeder Station wartet ein Minispiel und eine Wissensfrage zur jeweiligen Hardwarekomponente. Erst nach erfolgreichem Lösen wird die Station aktiv.

Das Motherboard hat einen Rand: Bewegt sich Nibble zu weit hinaus, fällt er vom Board herunter - das Spiel ist dann sofort vorbei, unabhängig vom aktuellen Lebensstand (siehe "Spielende" unten).

## Die Fragen wechseln bei jedem Durchlauf

Zu jeder Station gibt es mehrere hinterlegte Fragen bzw. Minispiel-Varianten. Bei jedem Neustart des Spiels wird zufällig ausgewählt, welche davon jeweils gestellt wird - wer das Spiel mehrmals spielt, bekommt also nicht immer dieselben Fragen und lernt so nach und nach mehr zu jedem Thema.

## Die Gefahr: Bits

Sobald die CPU-Station aktiviert wurde, erzeugt sie laufend 0en und 1en. Anders als Nibble bewegen sich diese Bits nur entlang der Leiterbahnen des Motherboards - fest vorgegebene Bahnen, denen sie folgen. Berührt eine davon Nibble, verliert er ein Bit (Lebenspunkt). Nibble kann sich wehren: Zwei Tasten sind ihm zugeordnet, eine zum Werfen einer 1, eine zum Werfen einer 0 - damit lässt sich eine anfliegende Bit-Einheit zerstören, bevor sie trifft.

## Spielende: Sieg oder Niederlage

**Niederlage:** Das Spiel endet, wenn entweder Nibble alle vier Bits verliert (Batterie leer) oder er vom Rand des Motherboards fällt (zu weit bewegt) - in beiden Fällen, ohne dass er entkommen konnte.

**Sieg:** Hat der Spieler alle sechs Stationen erfolgreich gemeistert, erreicht Nibble den USB-Anschluss und entkommt darüber - das Spiel hat nur diesen einen Ausgang. Dabei wird automatisch eine PDF erzeugt: Nibble als Symbol oben, darunter der Schriftzug "I escaped the computer! Juhu!", die verbliebene Batterieanzeige sowie die im Spiel beantworteten Fragen zum Nachlesen. Ist am Rechner ein Drucker angeschlossen, wird diese PDF zusätzlich automatisch ausgedruckt; ist keiner angeschlossen, bleibt sie als digitale Datei bestehen.

## Highscore

Während des Spiels werden zwei Werte laufend oben am Bildschirm angezeigt: die Anzahl der zerstörten Bits und die verstrichene Zeit. Der eigentliche Highscore ergibt sich aber aus einer Kombination beider Werte - je mehr Bits zerstört und je schneller das Spiel durchgespielt wurde, desto besser das Ranking. Damit lohnt es sich sowohl, offensiv zu verteidigen (viele Bits zerstören), als auch, zügig zu spielen - beides fließt gemeinsam in die Bestenliste ein. Die genaue Berechnungsformel wird im Zuge der Umsetzung festgelegt und getestet.
