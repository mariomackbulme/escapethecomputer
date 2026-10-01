# Working with Jira – Stories anlegen

<details>
<summary>Changelog</summary>

| Ver. | Datum | Änderung | Autor |
| :----: | :----: | ------ | :----: |
| v0.1 | 30.09.26 | Erste Version | Team |
| v0.2 | 30.09.26 | Abschnitte Tasks/Subtasks und Zeiterfassung (Original Estimate) ergänzt | Team |

</details>

## Worum geht's

Kurzanleitung, wie im Jira-Projekt **ETC (Escape the Computer)** Stories und Tasks angelegt werden – Format, Sprache, Aufbau, Schätzung.

## Aufbau einer Story

Jede Story besteht aus drei Teilen:

1. **Titel** – kurz, beschreibt das Ergebnis aus Nutzersicht (nicht die Technik)
2. **Beschreibung** – im Format "As a [role], I want [goal], so that [benefit]."
3. **Akzeptanzkriterien** – kurze, prüfbare Stichpunkte, keine Fließtext-Beschreibung

**Sprache:** Story-Beschreibung, Akzeptanzkriterien und Subtasks werden **auf Englisch** geschrieben.

## Format der Beschreibung

Satzbau: **"As a [role], I want [goal], so that [benefit]."**

- **Role** – die Person aus deren Sicht geschrieben wird, bei uns meist "player" (nicht "the system" oder "the app")
- **Goal** – WAS die Person will/erlebt, nicht WIE es technisch umgesetzt wird (Technik gehört in die Tasks)
- **Benefit** – WARUM das wichtig ist. Fällt einem kein Nutzen ein, ist es vermutlich eher ein Task als eine eigene Story

## Akzeptanzkriterien

Kurze, geprüfbare Stichpunkte, z. B.:

```
- The mainboard background is fully loaded and displayed when the game starts
- The Nibble sprite appears at a defined starting position on the board
```

Optional strenger im "Given-When-Then"-Stil: *"Given the game starts, when the mainboard loads, then Nibble is visible at position X."*

## INVEST-Regel (Qualitätscheck für Stories)

- **I**ndependent – möglichst unabhängig von anderen Stories umsetzbar
- **N**egotiable – kein fixes Pflichtenheft, Details verhandelbar
- **V**aluable – bringt erkennbaren Wert für Spieler/Nutzer
- **E**stimable – Aufwand lässt sich grob schätzen
- **S**mall – passt in einen Sprint
- **T**estable – Akzeptanzkriterien lassen sich klar prüfen (erfüllt/nicht erfüllt)

## Zuordnung zum Epic

Stories werden als "Übergeordnet" (Parent) dem passenden Produkt-Epic zugeordnet (z. B. ETC-1 Core-Mechanik). Bei Stories, die mehrere Ressourcenbereiche betreffen (Programmierung + Grafik + Content), lieber pro Bereich eine eigene Story anlegen statt eine große – erleichtert Sprintplanung und individuelles Abhaken pro Teammitglied.

## Tasks / Subtasks

Eine Story wird bei Bedarf in **Subtasks** (Vorgangstyp "Subtask", "Übergeordnet" = die Story) aufgeteilt – jeweils eine klar abgegrenzte technische Arbeitsanweisung statt eines Nutzerziels.

**Aufbau eines Tasks:**

1. **Titel** – Tätigkeit, nicht Nutzerziel (z. B. "Load mainboard as surface & display it")
2. **Beschreibung** – technische Arbeitsanweisung, kein "Als...möchte ich..."
3. **Definition of Done** – kurze, prüfbare Kriterien (analog zu Akzeptanzkriterien bei der Story)
4. **Zugewiesene Person** und **Ursprüngliche Schätzung** (Stunden)

**Beispiel (real angelegt: ETC-16, Subtask unter ETC-15):**

**Titel:** Load mainboard as surface & display it

**Beschreibung:**
> Load the mainboard background image as a Pygame surface at game start and display it on screen. Define the coordinate system for the board so later stations/objects can be positioned relative to it.

**Definition of Done:**
- Image file is loaded correctly via pygame.image.load() (relative path, no absolute path)
- Surface is blitted correctly every frame in the game loop
- No crash on missing image (clean error handling instead of a crash)
- Coordinate system (origin, scale) is documented/commented in the code

**Link:** https://escapethecomputer.atlassian.net/browse/ETC-16

## Zeiterfassung (Original Estimate)

Zeiterfassung ist im Projekt aktiviert (Projekteinstellungen → Funktionen → Zeiterfassung). Damit hat jeder Vorgang ein Feld **"Ursprüngliche Schätzung"** (Original Estimate), das in Stunden gefüllt wird (z. B. `3h`, `1d 2h`) – passt zu unserer stundenbasierten Aufwandsplanung aus `epics.md`, nicht zu Story Points.

**Empfehlung:** Schätzung nur auf **Subtask-Ebene** eintragen, die Story selbst ohne eigene Schätzung lassen. Jira zeigt dann im Story-Vorgang automatisch ein "Zeiterfassung"-Widget mit der **Summe aller Subtask-Schätzungen** – das ist ein reines Anzeige-Rollup, kein Wert, der ins Story-Feld zurückgeschrieben wird. Trägt man zusätzlich noch eine eigene Schätzung auf der Story ein, addiert Jira Story-Schätzung + Subtask-Summe zusammen, was das Bild verfälscht.

## Beispiel-Story (real angelegt: ETC-15)

**Titel:** Position Nibble on the mainboard at game start

**Beschreibung:**
> As a player, I want to see my Nibble positioned visibly on the mainboard when the game starts, so that I immediately know where I am and can start playing.

**Akzeptanzkriterien:**
- The mainboard background is fully loaded and displayed when the game starts
- The Nibble sprite appears at a defined starting position on the board
- The camera/view shows enough of the board for the starting position to be recognizable

**Übergeordnetes Epic:** ETC-1 (Core-Mechanik)

**Link:** https://escapethecomputer.atlassian.net/browse/ETC-15
