weiterer_raum = True
gesamtflaeche = 0
anzahl_raeume = 0

while weiterer_raum:
    weiterer_raum += 1

    # Eingabe der Raumbezeichnung
    bezeichnung = input("Bitte geben sie die Bezeichnung des Raumes an: ")

    # Eingabe der Raumlänge
    laenge = int(input("Bitte geben sie die Länge des Raumes an(in Meter): "))
    # Eingabe der Raumbreite
    breite = int(input("Bitte geben sie die Breite des Raumes an(in Meter): "))

    # Flächenberechnung
    flaeche = laenge * breite
    # Addieren der "neuen" Fläche auf die Gesamtfläche
    gesamtflaeche += flaeche
    # Berechnung des Durchschnitts
    durchschnitt = gesamtflaeche / weiterer_raum

    # Ausgabe der Fläche des Raumes bzw. des Teilraumes
    print("Die Fläche des Raumes " + "(" + bezeichnung + ")" +
          " (oder des Teilaumes) beträgt " + str(flaeche) + " Quadratmeter")
    # Ausgabe der Gesamtfläche
    print("Die Gesamtfläche der/des Wohnung/Hauses beträgt " +
          str(gesamtflaeche) + " Quadratmeter")
    # Ausgabe des Quadratmeter Durchschnitts
    print("Der Durchschnitt der/des Wohnung/Hauses beträgt " +
          str(durchschnitt) + " Quadratmeter")

    # Abfrage ob weiterer Raum
    weiterer_raum_input = (input("möchten sie einen weiteren Raum hinzu addieren?(ja/nein): ")
                           .lower())

    weiterer_raum = weiterer_raum_input == "ja"

print("Schönen Tag!")

        
