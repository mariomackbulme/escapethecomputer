# Pygame Referenz – Lernfortschritt

> Nachschlage-Übersicht aller Pygame-Befehle und -Konzepte, die im Lernprozess (siehe `learning-pygame.md`) bereits mit "Go" abgeschlossen wurden. Wird laufend ergänzt, sobald weitere Konzepte gelernt werden.

## Epic 1: Projekt-Setup & Grundgerüst

### Grundgerüst

| Befehl / Methode | Modul | Beschreibung |
| --- | --- | --- |
| `pygame.init()` | `pygame` | Initialisiert alle Pygame-Module |
| `pygame.display.set_mode((w, h))` | `pygame.display` | Erstellt das Spielfenster in gegebener Auflösung |
| `pygame.display.set_caption(text)` | `pygame.display` | Setzt den Fenstertitel |
| `pygame.time.Clock()` | `pygame.time` | Erzeugt ein Clock-Objekt zur Steuerung der Framerate |
| `clock.tick(fps)` | Clock-Objekt | Begrenzt die Framerate und gibt die vergangene Zeit seit dem letzten Aufruf zurück (in Millisekunden) |
| `pygame.event.get()` | `pygame.event` | Liefert die Liste aller aktuell anstehenden Events |
| `event.type == pygame.QUIT` | – | Prüft, ob das Fenster geschlossen werden soll |
| `screen.fill(farbe)` | Surface | Füllt die gesamte Surface mit einer Farbe (Name als String, z.B. `'white'`, reicht) |
| `screen.blit(surface, position)` | Surface | Zeichnet eine Surface auf eine andere (z.B. Bild aufs Fenster) |
| `pygame.display.flip()` | `pygame.display` | Zeigt das fertig gezeichnete Bild an |
| `pygame.quit()` | `pygame` | Beendet Pygame sauber |
| `pygame.image.load(pfad).convert()` | `pygame.image` | Lädt ein Bild, optimiert fürs Zeichnen (ohne Transparenz, z.B. JPG) |
| `pygame.image.load(pfad).convert_alpha()` | `pygame.image` | Wie `.convert()`, aber mit Transparenzkanal (für PNGs) |

**Koordinatensystem:** `(0, 0)` ist oben links, `x` wächst nach rechts, `y` wächst nach unten. Zum Zentrieren: `fenstergröße // 2 - objektgröße // 2`. Bei Pixel-Rechnungen `//` (Ganzzahl-Division) statt `/` verwenden.

### Rect & colliderect

| Befehl / Methode | Modul | Beschreibung |
| --- | --- | --- |
| `pygame.Rect(x, y, w, h)` | – | Erstellt ein Rechteck-Objekt für Position/Kollision |
| `rect.colliderect(anderes_rect)` | Rect-Objekt | Prüft, ob sich zwei Rechtecke überschneiden (`True`/`False`) |
| `rect.center`, `rect.topleft`, `rect.x`, `rect.y` | Rect-Objekt | Zugriff/Änderung einzelner Positionswerte |

### Sprite-Klasse & Group

| Befehl / Methode | Modul | Beschreibung |
| --- | --- | --- |
| `class X(pygame.sprite.Sprite)` | `pygame.sprite` | Basisklasse für eigene Spielobjekte; braucht `self.image` (Surface) und `self.rect` (Rect), `super().__init__()` aufrufen |
| `pygame.sprite.Group()` | `pygame.sprite` | Container für mehrere Sprites |
| `pygame.sprite.GroupSingle()` | `pygame.sprite` | Container für genau ein Sprite |
| `group.add(sprite, ...)` | Group-Objekt | Fügt Sprite(s) der Gruppe hinzu |
| `group.draw(screen)` | Group-Objekt | Zeichnet alle Sprites der Gruppe |
| `group.update()` | Group-Objekt | Ruft `update()` auf jedem Sprite der Gruppe auf |
| `pygame.sprite.spritecollide(sprite, group, dokill)` | `pygame.sprite` | Prüft Kollision eines Sprites mit allen Mitgliedern einer Gruppe; `dokill=True` entfernt kollidierte Sprites automatisch |
| `sprite.kill()` | Sprite-Objekt | Entfernt ein Sprite aus allen Gruppen |

> **Wichtig:** Eine `Group` leitet Attribut-Zuweisungen (z.B. `group.speed = x`) nicht an ihre Mitglieder weiter – dafür muss man selbst über die Sprites iterieren (`for s in group: s.speed = x`).

## Epic 2: Core-Mechanik (bisher)

### Tastatur-Input

| Befehl / Methode | Modul | Beschreibung |
| --- | --- | --- |
| `pygame.KEYDOWN` | Event-Typ | Feuert **einmalig**, wenn eine Taste gedrückt wird |
| `pygame.KEYUP` | Event-Typ | Feuert **einmalig**, wenn eine Taste losgelassen wird |
| `event.key == pygame.K_x` | – | Prüft, welche Taste genau das Event ausgelöst hat (z.B. `pygame.K_SPACE`) |
| `pygame.key.get_pressed()` | `pygame.key` | Gibt den aktuellen Zustand **aller** Tasten zurück – Dauerabfrage, jeden Frame neu geprüft |

> **Merksatz:** `KEYDOWN`/`KEYUP` = einmaliger Trigger (wie der Klick eines Lichtschalters) → für einmalige Aktionen (Menü, Umschalten). `get_pressed()` = Dauerzustand (wie "steht der Schalter gerade auf An?") → für kontinuierliche Bewegung.

### Delta-Time-Bewegung

| Befehl / Methode | Modul | Beschreibung |
| --- | --- | --- |
| `dt = clock.tick(fps)` | Clock-Objekt | Liefert die vergangene Zeit seit dem letzten Frame in **Millisekunden** |
| Formel | – | `bewegung_pro_frame = pixel_pro_sekunde * (dt / 1000)` |

> **Merksatz:** Ohne Delta-Time hängt die Geschwindigkeit von der Framerate ab (mehr FPS = schneller). Mit Delta-Time bewegt sich ein Objekt pro Sekunde immer gleich weit, egal ob 30, 60 oder 120 FPS – nur die "Ruckeligkeit" ändert sich mit der Framerate, nicht die tatsächliche Geschwindigkeit.

---

*Wird ergänzt, sobald weitere Konzepte mit "Go" abgeschlossen sind (als Nächstes: Font-Rendering).*
