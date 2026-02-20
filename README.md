# DHBW-Mannheim-WI2024SEA-EDA-CQRS

1. Fork anlegen
2. Eigenen Ordner anlegen
3. Aufgabe 3+4 bearbeiten (10 Punkte)

# README – Steuerung der TP-Link Tapo L530E über Python

Dieses Projekt ermöglicht das Steuern einer TP‑Link Tapo L530E Smart‑Glühbirne über Python mithilfe eines Producer-Consumer-Systems.

---

## Voraussetzungen

- TP-Link Tapo L530E Smart-Glühbirne
- Smartphone mit Tapo App (Android oder iOS)
- Laptop/PC mit Python 3.9 oder höher
- Alle Geräte (Laptop, Glühbirne, Smartphone) müssen im selben WLAN sein
- Installation aller Pakete aus requirements.txt

---

## Installation der Python-Abhängigkeiten

Vor dem Start müssen alle benötigten Pakete installiert werden:

```bash
pip install -r requirements.txt
``



1. Tapo App vorbereiten

Lade die Tapo App auf dein Smartphone.
Erstelle ein Konto oder melde dich an.

2. Glühbirne koppeln

Schließe die Tapo L530E Glühbirne an eine Steckdose oder Lampenfassung an.
Schalte den physischen Ein-/Ausschalter fünfmal hintereinander an und aus.
Die Glühbirne beginnt schnell zu blinken → Pairing-Modus aktiv.

3. Glühbirne in der App hinzufügen

Öffne die Tapo App.
Wähle „Gerät hinzufügen“ → „Glühbirne“ → „Tapo L530E“.
Folge dem Einrichtungsprozess, bis das Gerät verbunden ist.

4. IP-Adresse der Glühbirne ermitteln

Öffne das Gerät in der Tapo App.
Gehe zu den Geräteeinstellungen.
Notiere die dort angezeigte IP-Adresse der Glühbirne.

5. In Consumer.py die Anmeldedaten und Ip Adresse eintragen.

...