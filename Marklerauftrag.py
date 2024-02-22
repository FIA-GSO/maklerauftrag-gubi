weiterer_raum = True
gesamtflaeche = 0
anzahl_raeume = 0

while weiterer_raum:
    anzahl_raeume += 1

    # Eingabe der Raumbezeichnung
    bezeichnung = input("Bitte geben sie die Bezeichnung des Raumes an: ")

    # Eingabe ob Teilraeume vorhanden sind
    anzahl_teilraeume = int(input("aus wie vielen Teilräumen besteht der Raum: "
                                  "(Bei keinen Teilräumen [1] eingeben) "))

    gesamtflaeche_raum = 0
    for anzahl_raum in range(anzahl_teilraeume):
        # Eingabe der Raumlänge
        laenge_teilraum = float(input("Bitte geben sie die Länge des " + str(anzahl_raum + 1) +
                                      ". Raumes/Teilraumes an (in Meter): "))
        # Eingabe der Raumbreite
        breite_teilraum = float(input("Bitte geben sie die Breite des " + str(anzahl_raum + 1) +
                                      ". Raumes/Teilraumes an (in Meter): "))

        # Flächenberechnung
        gesamtflaeche_raum += (laenge_teilraum * breite_teilraum)

    # Addieren der "neuen" Fläche auf die Gesamtfläche
    gesamtflaeche += gesamtflaeche_raum
    # Berechnung des Durchschnitts
    durchschnitt = gesamtflaeche / anzahl_raeume

    # Ausgabe der Fläche des Raumes bzw. des Teilraumes
    print("Die Fläche des Raumes " + "(" + bezeichnung + ")" +
          " beträgt " + str(gesamtflaeche_raum) + " Quadratmeter")
    # Ausgabe der Gesamtfläche
    print("Die Gesamtfläche der/des Wohnung/Hauses beträgt " +
          str(gesamtflaeche) + " Quadratmeter")
    # Ausgabe des Quadratmeter Durchschnitts
    print("Der Durchschnitt der Raüme beträgt " +
          str(durchschnitt) + " Quadratmeter")

    # Abfrage ob weiterer Raum
    weiterer_raum_input = (input("möchten sie einen weiteren Raum hinzu addieren?(ja/nein): ")
                           .lower())

    weiterer_raum = weiterer_raum_input == "ja"

print("Schönen Tag!")
        
