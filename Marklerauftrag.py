weitererRaum = True;
gesamtflaeche = 0;
anzahlRaeume = 0;

while(weitererRaum):
    anzahlRaeume += 1
    
    laenge = int(input("Bitte geben sie die Länge des Raumes an(in Meter): "))
    breite = int(input("Bitte geben sie die Breite des Raumes an(in Meter): "))

    flaeche = laenge * breite
    gesamtflaeche += flaeche
    durchschnitt = gesamtflaeche / anzahlRaeume
    
    print("Die Fläche des Raumes (oder des Teilaumes) beträgt " + str(flaeche) + " Quadratmeter")
    print("Die Gesamtfläche der/des Wohnung/Hauses beträgt " + str(gesamtflaeche) + " Quadratmeter")
    print("Der Durchschnitt der/des Wohnung/Hauses beträgt " + str(durchschnitt) + " Quadratmeter")
    
    weitererRaumInput = input("möchten sie einen weiteren Raum hinzu addieren?(ja/nein): ").lower()

    weitererRaum = weitererRaumInput == "ja"

print("Schönen Tag!")

        
