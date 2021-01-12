from random import randint

class Kartenstapel(object):
    def __init__(self):

        self.kartenListe = [
            'X-A', 'X-K', 'X-D', 'X-B', 'X-10', 'X-9', 'X-8', 'X-7',
            'P-A', 'P-K', 'P-D', 'P-B', 'P-10', 'P-9', 'P-8', 'P-7',
            'H-A', 'H-K', 'H-D', 'H-B', 'H-10', 'H-9', 'H-8', 'H-7',
            'K-A', 'K-K', 'K-D', 'K-B', 'K-10', 'K-9', 'K-8', 'K-7'
            ]

    def mischen(self):

        neueListe = []
        aktuelleAnzahl = len(self.kartenListe)
        while aktuelleAnzahl > 0:
            i = randint(0, aktuelleAnzahl-1)
            neueListe = neueListe + [self.kartenListe[i]]
            del self.kartenListe[i]
            aktuelleAnzahl = len(self.kartenListe)
        self.kartenListe = neueListe

    def istLeer(self):

        if len(self.kartenListe) > 0:
            ergebnis = False
        else:
            ergebnis = True
        return ergebnis

    def karteZiehen(self):

        if len(self.kartenListe) > 0:
            gezogeneKarte = self.kartenListe[0]
            self.kartenListe = self.kartenListe[1:]
        else:
            gezogeneKarte = None
        return gezogeneKarte


    def hinzufuegen(self,zahlenwert,ass):
        karte = stapel.karteZiehen()
        print('Karte:',karte)
        if karte[2] == 'K':
            zahlenwert = zahlenwert + 10
        elif karte[2] == 'D':
            zahlenwert = zahlenwert + 10
        elif karte[2] == 'B':
            zahlenwert = zahlenwert + 10
        elif karte[2] == '1':
            zahlenwert = zahlenwert + 10
        elif karte[2] == '9':
            zahlenwert = zahlenwert + 9
        elif karte[2] =='8':
            zahlenwert = zahlenwert + 8
        elif karte[2] == '7':
            zahlenwert = zahlenwert + 7
        elif karte[2] == 'A':
            zahlenwert = zahlenwert +11
            ass= True 
        return zahlenwert,ass
ass = False
ass2 = False
zahlenwert = 0             
stapel= Kartenstapel()
stapel.mischen()
gezogenKarte,ass= stapel.hinzufuegen(zahlenwert,ass)
print('Handwert:',gezogenKarte)
gezogenKarte2,ass2 = stapel.hinzufuegen(gezogenKarte,ass2)
print('Handwert:',gezogenKarte2)
weiter = str(input(" Möchten sie noch eine weitere Karte ziehen, Ja/Nein"))
                   
if weiter == 'ja'or weiter =='JA' or weiter == 'Ja' :
    gezogenKarte3,ass =stapel.hinzufuegen(gezogenKarte2,ass)
    if gezogenKarte< 21:
        if ass == True or ass2 == True:
            gezogenKarte3 =gezogenKarte3-10
            print('Ihr Kartenwert ist:',gezogenKarte3)
        else:
            print('Sie haben verloren, Ihr Kartenwert ist:',gezogenKarte3)
    else :
          print(' Ihr Kartenwert ist:',gezogenKarte3)         
else:
    if ass == True or ass2 == True:
            gezogenKarte2 =gezogenKarte2-10
    print('Ihr Kartenwert ist:',gezogenKarte2)
    
    
        
