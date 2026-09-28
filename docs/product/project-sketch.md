# Project Sketch

<details>
<summary>Changelog</summary>

| Ver. | Datum | Änderung | Autor |
| :----: | :----: | ------ | :----: |
| v0.1 | 21.09.26 | Erste Version | Team |
| v0.2 | 24.09.26 | Erste Aufwandsschätzungen, Ressourcenaufteilung in Tabellenformat übertragen | Team |

</details>

## Idee

2D-Lernspiel – Nibble bewegt sich über ein Motherboard, löst an jeder Hardware-Komponente ein Minispiel und eine Frage und aktiviert sie dadurch. Muss sich gegen umherfliegende Bits (0/1) verteidigen. Ziel: alle Stationen schaffen, am Ende über USB/Drucker "ausdrucken" und entkommen.

**Stichwörter:** Lernspiel · Hardware-Wissen · Pygame · 2D Top-Down · Motherboard-Welt · Nibble (4-Bit) · Minispiele · Verteidigungsmechanik

## Ressourcenaufteilung

| ID | Bezeichnung | Remarks | Aufwand | Lead | Support | 
| :---: | --- | --- | :---: | :---: | :---: |
| 1  | Programmierung & Spiellogik | *Charakters - Gegner - Leiterbahnen - Minispiele* | 65h | Mario | Oliver |
| 2  | Grafik & Visualisierung | *Motherboard-Layout - Animationen*  | - | Melanie | Oliver |
| 3  | Game-Design & Fachinhalte | *Minispiele - Quizfragen - Fachliche Korrektheit - Schwierigkeitskurve*  | - | Oliver | Melanie |
| 4  | Sound/Audio | *Soundeffekte - Musik - Kopfhörer-Aktivierung* | - | Melanie | Mario |
| 5  | Testing | *Bugfixing - Durchspielen - Usability* | - | Oliver | Mario |
| 6  | Toling & Repo-Pflege | *Git-Workflow - Branching - venv/requirements.txt - Ordnerstruktur - VS-Code-Setup* | - | Mario | Melanie |
| 7  | Anforderungsmanagement | *Scope-Abgrenzung - MVP vs. Backlog - Lasten-/Pflichtenheft - Priorisierung* | - | Team | - |
| 8  | Anforderungsmanagement | *Sprintplan - Jira-Boards - Fortschritts-Tracking - Zeitpuffer* | - | Team | - |
| 9  | Risikomanagement | *Risikoliste · Gegenmaßnahmen - regelmäßige Überprüfung - Frühwarnung* | - | Team | - |
| 10 | Qualitätssicherung | *Definition of Done - Code-Reviews - Coding-Standards - Review-Prozess* | - | Team | - |
| 11 | Kommunikation & Reporting | *Team-Meetings - Confluence-Pflege - Status-Updates - Lehrperson-Abstimmung* | - | Team | - |

## Warum wir fertig werden

Magisches Dreieck (Leistung, Aufwand, Termin):
- Termin & Aufwand sind fix, kein Spielraum (Abgabetermin extern vorgegeben, Zeit durch Stundenplan begrenzt)
- Puffer liegt bewusst in der Leistung (Qualität + Quantität)
- Zeitdruck → zuerst Qualität reduzieren (z. B. einfachere Grafik), Kernfunktionen bleiben bestehen
- Quantität bleibt über das Backlog steuerbar (Extras nur bei Zeitüberschuss, nicht fix eingeplant)

Technologische Sicht:
- Scope fix (MVP) klein gehalten: 6 Stationen, weitere Features kommen in den Backlog – bewusst schlank, da uns die Erfahrung mit Python/Pygame noch fehlt und der tatsächliche Aufwand pro Feature schwer einzuschätzen ist
- Wiederverwendbare Kernarchitektur
- Bewährter, einsteigerfreundlicher Tech-Stack (Python/Pygame)

Projektmanagement Sicht:
- Klare Verantwortlichkeiten: jeder Bereich hat Lead + Zuarbeiter (wird bis Mittwoch im Team nach Kompetenz aufgeteilt)
- Risiken werden vorab identifiziert und benannt sowie Abhilfemaßnahmen bereits vorher überlegt
- Meilensteine werden festgelegt und getrackt, um einen Überblick zu haben, wo wir stehen
- Aufwände (Stunden) werden abgeschätzt und ebenfalls getrackt (Clockify)
- Projektplan wird in zweiwöchige Sprints unterteilt: Start 28.09.2026, Fertigstellung inkl. Testing spätestens 18.01.2027 (16 Wochen → 8 Sprints) – Aufgaben werden je Sprint klar niedergeschrieben
