weitererRaum = True;
gesamtflaeche = 0;
anzahlRaeume = 0;

while(weitererRaum):
    anzahlRaeume += 1
    
    laenge = int(input("Bitte geben sie die Länge des Raumes an(in Meter): "))  #Eingabe der Raumlänge
    breite = int(input("Bitte geben sie die Breite des Raumes an(in Meter): ")) #Eingabe der Raumbreite

    bezeichnung = input("Bitte geben sie die Bezeichnung des Raumes an: ") #Eingabe der Raumbezeichnung

    flaeche = laenge * breite #Flächen-Berechnung
    gesamtflaeche += flaeche  #Addieren der "neuen" Fläche auf die Gesamtfläche
    durchschnitt = gesamtflaeche / anzahlRaeume #Berechnung des Durchschnitts
    
    print("Die Fläche des Raumes " + "(" + bezeichnung + ")" + " (oder des Teilaumes) beträgt " + str(flaeche) + " Quadratmeter")#Ausgabe der Fläche des Raumes bzw. des Teilraumes
    print("Die Gesamtfläche der/des Wohnung/Hauses beträgt " + str(gesamtflaeche) + " Quadratmeter")#Ausgabe der Gesamtfläche
    print("Der Durchschnitt der/des Wohnung/Hauses beträgt " + str(durchschnitt) + " Quadratmeter") #Ausgabe des Quadratmeter Durchschnitts
    
    weitererRaumInput = input("möchten sie einen weiteren Raum hinzu addieren?(ja/nein): ").lower() #Abfrage ob weiterer Raum

    weitererRaum = weitererRaumInput == "ja" 

print("Schönen Tag!")

        
