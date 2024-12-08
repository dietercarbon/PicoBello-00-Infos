zeit_in_millisekunden = 123456789  # Beispiel: 37.800.456 Millisekunden

# Umrechnung in Stunden, Minuten, Sekunden und Millisekunden
stunden = zeit_in_millisekunden // 3600000  # Ganze Stunden
rest_millisekunden = zeit_in_millisekunden % 3600000  # Verbleibende Millisekunden
minuten = rest_millisekunden // 60000  # Ganze Minuten
rest_millisekunden %= 60000  # Verbleibende Millisekunden
sekunden = rest_millisekunden // 1000  # Ganze Sekunden
millisekunden = rest_millisekunden % 1000  # Verbleibende Millisekunden

# Ausgabe im Format HH:MM:SS.mmm
print()
print("HH:MM:SS.mmm")
print(f"{stunden:02d}:{minuten:02d}:{sekunden:02d}.{millisekunden:03d}")

"""
Erklärung:

    Berechnung der Stunden:
        zeit_in_millisekunden // 3600000 teilt die Gesamtzeit durch 3.600.000 (1 Stunde in Millisekunden) und liefert die Anzahl der vollen Stunden.

    Rest der Millisekunden nach den Stunden:
        zeit_in_millisekunden % 3600000 gibt die verbleibenden Millisekunden, die nicht zu einer vollen Stunde gehören.

    Berechnung der Minuten:
        rest_millisekunden // 60000 berechnet die Anzahl der vollen Minuten aus dem Rest.

    Rest der Millisekunden nach den Minuten:
        rest_millisekunden %= 60000 reduziert die verbleibenden Millisekunden auf die, die nicht in eine volle Minute passen.

    Berechnung der Sekunden:
        rest_millisekunden // 1000 liefert die Anzahl der vollen Sekunden.

    Berechnung der verbleibenden Millisekunden:
        rest_millisekunden % 1000 gibt die verbleibenden Millisekunden.

    Formatierung:
        {stunden:02d}: Zweistellige Stundenanzeige.
        {minuten:02d}: Zweistellige Minutenanzeige.
        {sekunden:02d}: Zweistellige Sekundenanzeige.
        {millisekunden:03d}: Dreistellige Millisekundenanzeige.
"""
