# Epics – Übersicht

<details>
<summary>Changelog</summary>

| Ver. | Datum | Änderung | Autor |
| :----: | :----: | ------ | :----: |
| v0.1 | 29.09.26 | Erste Version | Team |
| v0.2 | 29.09.26 | Aufwand je Epic ergänzt, verschmolzen mit offizieller Projektaufwandstabelle (285h) | Team |

</details>

## Worum geht's

Übersicht aller Epics für "Escape the Computer" – nicht nur Programmierung, sondern das ganze Projekt (Programmierung, Grafik, Gameplay/Content, Setup, Projektsteuerung). Produkt-Epics bekommen Stories aus mehreren Ressourcenbereichen gleichzeitig (z. B. hat "Station: CPU" sowohl eine Programmier- als auch eine Grafik- und eine Content-Story); Projekt-Epics sind eher bereichsspezifisch.

## Produkt-Epics

1. **Core-Mechanik** – Nibble-Bewegung, Kollision, Lebenspunkte/Batterie (Programmierung + zugehörige Sprites/Grafik)
2. **Bit-Gefahr-System** – CPU-Spawn, Leiterbahn-Bewegung, Wurf-/Zerstörungsmechanik (Programmierung + Grafik der Bits/Projektile)
3. **Station: Kopfhörer** – Trigger, Minispiel/Frage, Sound-Aktivierung, Grafik
4. **Station: CPU** – Trigger, Minispiel/Frage, Grafik, Kopplung an Bit-Spawning
5. **Station: RAM 1** – Trigger, Minispiel/Frage, Grafik, Tempo-Erhöhung
6. **Station: Grafikkarte** – Trigger, Minispiel/Frage, visuelles Upgrade des gesamten Boards
7. **Station: RAM 2** – Trigger, Minispiel/Frage, Grafik, zweite Tempo-Erhöhung
8. **Station: USB & Spielende** – Sieg-Erkennung, PDF-Zertifikat, Grafik/Text dafür
9. **Highscore-System** – Tracking, Berechnung, Anzeige/UI
10. **Backlog / Post-MVP** – Transistor, LED, weitere Stationen, Highscore-Polish

## Projekt-Epics

11. **Projekt-Setup & Tooling** – Repo, venv, Ordnerstruktur, Pygame-Grundgerüst, CI/Deploy (Web-Landingpage)
12. **Projektplanung & Steuerung** – Sprintplan, Jira-Boards, Meilensteine, Risikomanagement, Aufwandstracking
13. **Testing & Qualitätssicherung** – Bugfixing, Playtests, Code-Reviews, Definition of Done
14. **Kommunikation & Reporting** – Team-Meetings, Confluence-Pflege, Lehrperson-Abstimmung

## Aufwand je Epic

Verschmolzen aus der offiziellen Projektaufwandstabelle (Projekt einrichten, Projektplanung, Projektsteuerung, Grafiken designen, Game Design und Fachinhalte erstellen, Datenbank entwickeln, Spiel programmieren, Tests erstellen, Tests durchführen, Bugs beheben, Dokumentation schreiben, Puffer – Summe 285h): "Spiel programmieren" und "Grafiken designen" wurden proportional nach Komplexität auf die Produkt-Epics verteilt (Grafikkarte und USB & Spielende bekommen mehr, wegen visuellem Upgrade bzw. Sieg-Screen/Zertifikat), "Projektplanung", "Projektsteuerung", "Tests" und "Bugs beheben" sind 1:1 den passenden Projekt-Epics zugeordnet, "Dokumentation schreiben" der Kommunikation & Reporting. Der Puffer bleibt bewusst epic-übergreifend.

| Epic | Programmierung | Grafik | Fachinhalte | Sonstiges | Summe |
| ------ | :----: | :----: | :----: | :----: | :----: |
| 1. Core-Mechanik | 16h | 19h | – | – | 35h |
| 2. Bit-Gefahr-System | 18h | 10h | 2h | – | 30h |
| 3. Station: Kopfhörer | 4,5h | 5h | 2h | – | 11,5h |
| 4. Station: CPU | 4,5h | 5h | 3h | – | 12,5h |
| 5. Station: RAM 1 | 3,5h | 5h | 2h | – | 10,5h |
| 6. Station: Grafikkarte | 3,5h | 15h | 2h | – | 20,5h |
| 7. Station: RAM 2 | 3,5h | 5h | 2h | – | 10,5h |
| 8. Station: USB & Spielende | 7h | 12h | 2h | – | 21h |
| 9. Highscore-System | 4,5h | 4h | – | Datenbank 5h | 13,5h |
| 10. Backlog / Post-MVP | – | – | – | – | 0h (nur bei Zeitüberschuss) |
| 11. Projekt-Setup & Tooling | – | – | – | 5h | 5h |
| 12. Projektplanung & Steuerung | – | – | – | 40h | 40h |
| 13. Testing & Qualitätssicherung | – | – | – | 30h | 30h |
| 14. Kommunikation & Reporting | – | – | – | 20h | 20h |
| Puffer (projektweit, nicht epic-gebunden) | – | – | – | 25h | 25h |

**Summe: 285h**
