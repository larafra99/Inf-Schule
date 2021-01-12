from tkinter import *
from random import randint
from tkinter import messagebox
wettzahl=0
budget = 10
fehler = 0
gewinn = 0
#Programm
def resetButtonfarbe():
    label1.config(background='white')
    label2.config(background='white')
    label3.config(background='white')
    label4.config(background='white')
    label5.config(background='white')
    label6.config(background='white')

def Button_1_Click():
    global wettzahl
    resetButtonfarbe()
    wettzahl=1
    label1.config(background='grey')
    
def Button_2_Click():
    global wettzahl
    resetButtonfarbe()
    wettzahl=2
    label2.config(background='grey')

def Button_3_Click():
    global wettzahl
    resetButtonfarbe()
    wettzahl=3
    label3.config(background='grey')

def Button_4_Click():
    global wettzahl
    resetButtonfarbe()
    wettzahl=4
    label4.config(background='grey')

def Button_5_Click():
    global wettzahl
    resetButtonfarbe()
    wettzahl=5
    label5.config(background='grey')

def Button_6_Click():
    global wettzahl
    resetButtonfarbe()
    wettzahl=6
    label6.config(background='grey')

def WuerfelDaten(wuerfel1,wuerfel2,wuerfel3):
     # Anzeige der Daten Würfel 1
    if wuerfel1 == 1:
        labelWuerfel1.config(image=imageWuerfel1)
    elif wuerfel1 == 2:
        labelWuerfel1.config(image=imageWuerfel2)
    elif wuerfel1 == 3:
        labelWuerfel1.config(image=imageWuerfel3)
    elif wuerfel1 == 4:
        labelWuerfel1.config(image=imageWuerfel4)
    elif wuerfel1 == 5:
        labelWuerfel1.config(image=imageWuerfel5)
    elif wuerfel1 == 6:
        labelWuerfel1.config(image=imageWuerfel6)
    # Anzeige der Daten Würfel 2
    if wuerfel2 == 1:
        labelWuerfel2.config(image=imageWuerfel1)
    elif wuerfel2 == 2:
        labelWuerfel2.config(image=imageWuerfel2)
    elif wuerfel2 == 3:
        labelWuerfel2.config(image=imageWuerfel3)
    elif wuerfel2 == 4:
        labelWuerfel2.config(image=imageWuerfel4)
    elif wuerfel2 == 5:
        labelWuerfel2.config(image=imageWuerfel5)
    elif wuerfel2 == 6:
        labelWuerfel2.config(image=imageWuerfel6)
    # Anzeige der Daten Würfel 3
    if wuerfel3 == 1:
        labelWuerfel3.config(image=imageWuerfel1)
    elif wuerfel3 == 2:
        labelWuerfel3.config(image=imageWuerfel2)
    elif wuerfel3 == 3:
        labelWuerfel3.config(image=imageWuerfel3)
    elif wuerfel3 == 4:
        labelWuerfel3.config(image=imageWuerfel4)
    elif wuerfel3 == 5:
        labelWuerfel3.config(image=imageWuerfel5)
    elif wuerfel3 == 6:
        labelWuerfel3.config(image=imageWuerfel6)
        
def FarbenLabeluWuerfel(wettzahl,wuerfel1,wuerfel2,wuerfel3):
    if wettzahl==wuerfel1 or wettzahl==wuerfel2 or wettzahl==wuerfel3:
        if wettzahl == wuerfel1:
            labelWuerfel1.config(background='green')
            labelWuerfel2.config(background='white')
            labelWuerfel3.config(background='white')
        if wettzahl == wuerfel2:
            labelWuerfel1.config(background='white')
            labelWuerfel2.config(background='green')
            labelWuerfel3.config(background='white')
        if wettzahl == wuerfel3:
            labelWuerfel1.config(background='white')
            labelWuerfel2.config(background='white')
            labelWuerfel3.config(background='green')
        if wettzahl==1:
            label1.config(background='green')
        elif wettzahl==2:
            label2.config(background='green')
        elif wettzahl==3:
            label3.config(background='green')
        elif wettzahl==4:
            label4.config(background='green')
        elif wettzahl==5:
            label5.config(background='green')
        elif wettzahl==6:
            label6.config(background='green')
    else:
        labelWuerfel1.config(background='red')
        labelWuerfel2.config(background='red')
        labelWuerfel3.config(background='red')
        if wettzahl==1:
            label1.config(background='red')
        elif wettzahl==2:
            label2.config(background='red')
        elif wettzahl==3:
            label3.config(background='red')
        elif wettzahl==4:
            label4.config(background='red')
        elif wettzahl==5:
            label5.config(background='red')
        elif wettzahl==6:
            label6.config(background='red')
            
    wettzahl=0


def Button_Start_Click():
    # Verarbeitung der Daten
    global wettzahl
    global budget
    global fehler
    global gewinn
    #Einsatz
    if wettzahl==0:
        fehler = fehler+1
        if fehler > 10:
            fehlertext='Setzen Sie einfach auf die 1'
        elif fehler > 7:
            fehlertext='Wenn Sie nicht setzen startet das Glückspiel nicht'
        elif fehler > 4:
            fehlertext='Drücken Sie bitte einen Button um auf eine Zahl zu setzen'
        else:
            fehlertext='Setzen sie bitte auf eine Zahl'
        messagebox.showinfo("Fehler",fehlertext)
        return

    try:
        Wetteinsatz= int(entryEinsatz.get())
        
    except:
        fehler = fehler+1
        if fehler > 10:
            fehlertext='Geben sie einfach eine 1 ins Feld'
        elif fehler > 7:
            fehlertext='Falls sie es nicht verstanden haben in den Wetteinsatz soll eine Zahl rein wie zB. die 1'
        elif fehler > 4:
            fehlertext='Sie sollen eine Zahl als Wetteinsatz eingeben'
        else:
            fehlertext='Bitte geben Sie als Wetteinsatz eine Zahl ein'
        messagebox.showinfo("Fehler",fehlertext)
        entryEinsatz.delete(0,END)
        return
    if Wetteinsatz > budget:
        fehler = fehler+1
        if fehler > 10:
            fehlertext='Geben sie einfach eine 1 ins Feld'
        elif fehler > 7:
            fehlertext='Sind sie schwer von Begriff ihr Einsatz muss unter 10€ sein'
        elif fehler > 4:
            fehlertext='Haben Sie es nicht verstanden, so viel Geld haben Sie nicht'
        else:
            fehlertext='So viel Geld haben Sie nicht'
        messagebox.showinfo("Fehler",fehlertext)
        entryEinsatz.delete(0,END)
        return
    #Würfel
    wuerfel1 = randint(1,6)
    wuerfel2 = randint(1,6)
    wuerfel3 = randint(1,6)
    #Grafische oberfläche für die Würfel
    WuerfelDaten(wuerfel1,wuerfel2,wuerfel3)
    #Wettzahlen
    FarbenLabeluWuerfel(wettzahl,wuerfel1,wuerfel2,wuerfel3)
    if wettzahl==wuerfel1 or wettzahl==wuerfel2 or wettzahl==wuerfel3:
        if wettzahl == wuerfel1:
            budget = budget+ Wetteinsatz
            gewinn = gewinn + Wetteinsatz
        if wettzahl == wuerfel2:
            budget = budget+ Wetteinsatz
            gewinn = gewinn + Wetteinsatz
        if wettzahl == wuerfel3:
            budget = budget+ Wetteinsatz
            gewinn = gewinn + Wetteinsatz
    else:
        budget = budget-Wetteinsatz
        gewinn = gewinn - Wetteinsatz
       
    labelBudgetAusgabe.config(text=budget)
    #Gewinn Ausgabe 
    if gewinn >=0:
      labelMomentangewinnAusgabe.config(text=gewinn,
                                        background='green')
    else:
      labelMomentangewinnAusgabe.config(text=gewinn,
                                        background='red')
    gewinn = 0
    if budget<=0:
        messagebox.showinfo("You lost", "Game over")
        Button_Reset_Click()

                        
def Button_Reset_Click():
    global wettzahl
    global budget
    global fehler
    global gewinn
    #Wettzahl
    wettzahl=0
    #Budget
    budget = 10
    #Fehler
    fehler =0
    #Gewinn
    gewinn = 0
    #Wetteinsatz
    entryEinsatz.delete(0,END)
    #Farbe Spielfeld
    label1.config(background='white')
    label2.config(background='white')
    label3.config(background='white')
    label4.config(background='white')
    label5.config(background='white')
    label6.config(background='white')
    #Würfel
    labelWuerfel3.config(image='',background='white')
    labelWuerfel2.config(image='',background='white')
    labelWuerfel1.config(image='',background='white')                    
    #Ausgaben
    labelMomentangewinnAusgabe.config(text=gewinn)
    labelBudgetAusgabe.config(text=budget)
    #farbe ausgabefeld
    labelMomentangewinnAusgabe.config(background='white')
    


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Chuck-a-luck')
tkFenster.geometry('590x590')

# Rahmen für die Überschrift
frameUeberschrift = Frame(master=tkFenster,
                          background='#0040FF')
frameUeberschrift.place(x=5, y=5, width=550, height=40)
# Label für die Überschrift
labelUeberschrift = Label(master=frameUeberschrift,
                          background='white',
                          text='Lara die Glücksfee?')
labelUeberschrift.place(x=180, y=12, width=190, height=20)


# Rahmen für die Wetten(Geld)
frameWette = Frame(master=tkFenster,
                      background='#088A68')
frameWette.place(x=5, y=50, width=550, height=72)
# Label mit Aufschrift Einsatz
labelEinsatz = Label(master=frameWette,
                                    background='white',
                                    text='Wetteinsatz in €')
labelEinsatz.place(x=145, y=26, width=175, height=20)

# Entry für den Einsatz
entryEinsatz= Entry(master=frameWette)
entryEinsatz.place(x=345, y=26, width=60, height=20)


# Rahmen für das Setzen + Starten
frameSetzen = Frame(master=tkFenster,
                          background='#04B4AE')
frameSetzen.place(x=5, y=127, width=550, height=140)
# Label mit Aufschrift Setzen
labelSetzen = Label(master=frameSetzen,
                                    background='white',
                                    text='Auf welche Zahl setzen Sie?')
labelSetzen.place(x=48, y=10, width=175, height=20)
# Label mit Aufschrift Starten
labelStarten = Label(master=frameSetzen,
                                    background='white',
                                    text='Hier würfeln Sie und starten')
labelStarten.place(x=365, y=10, width=175, height=20)
# Label mit Aufschrift Reseten
labelReset = Label(master=frameSetzen,
                                    background='white',
                                    text='Hier setzen Sie das Spiel zurück')
labelReset.place(x=365, y=80, width=175, height=20)
#Button für 1
button1 = Button(master=frameSetzen,
                         text='1',
                         command=Button_1_Click)
button1.place(x=12, y=50, width=120, height=20)
# Button für 2
button2= Button(master=frameSetzen,
                     text='2',
                     command = Button_2_Click)
button2.place(x= 12, y= 80, width = 120, height= 20)
# Button für 3
button3= Button(master=frameSetzen,
                     text='3',
                     command = Button_3_Click)
button3.place(x= 12, y= 110, width = 120, height= 20)
#Button für 4
button4= Button(master=frameSetzen,
                     text='4',
                     command = Button_4_Click)
button4.place(x=150, y=50, width = 120, height= 20)
#Button für 5
button5 = Button(master=frameSetzen,
                         text='5',
                         command=Button_5_Click)
button5.place(x=150, y=80, width=120, height=20)
# Button für 6
button6= Button(master=frameSetzen,
                     text='6',
                     command = Button_6_Click)
button6.place(x= 150, y= 110, width = 120, height= 20)
# Button Reset
buttonReset= Button(master=frameSetzen,
                     text='Reset',
                     command = Button_Reset_Click)
buttonReset.place(x= 400, y= 110, width = 120, height= 20)
#Button Start
buttonStart= Button(master=frameSetzen,
                     text='Würfeln + Starten',
                     command = Button_Start_Click)
buttonStart.place(x=400, y=40, width = 120, height= 20)


# Rahmen für das Spielfeld
frameSpielfeld = Frame(master=tkFenster,
                      background='#00FFFF')
frameSpielfeld.place(x=5, y=272, width=550, height=140)
# Label Überschrift Spielfeld
labelspielfeld = Label(master=frameSpielfeld,
                          background='white',
                          text='Spielfeld',
                          foreground='black')
labelspielfeld.place(x=186, y=10, width=175, height=20)
# Label für 1
label1 = Label(master=frameSpielfeld,
                          background='white',
                          text='1',
                          foreground='black')
label1.place(x=75, y=40, width=175, height=20)
# Label für 2
label2 = Label(master=frameSpielfeld,
                              background='white',
                              text='2',
                              foreground='black')
label2.place(x=275, y=40, width=175, height=20)
# Label für 3
label3 = Label(master=frameSpielfeld,
                      background='white',
                      text='3',
                      foreground='black')
label3.place(x=75, y=70, width=175, height=20)
# Label für 4
label4 = Label(master=frameSpielfeld,
                          background='white',
                          text='4',
                          foreground='black')
label4.place(x=275, y=70, width=175, height=20)
# Label für 5
label5 = Label(master=frameSpielfeld,
                        background='white',
                        text='5',
                        foreground='black')
label5.place(x=75, y=100, width=175, height=20)
# Label für 6
label6 = Label(master=frameSpielfeld,
                            background='white',
                            text='6',
                            foreground='black')
label6.place(x=275, y=100, width=175, height=20)

#Rahmen für die Ausgabe(würfel)
frameAusgabe = Frame(master =tkFenster,
                    background='#81DAF5')
frameAusgabe.place(x=5,y=417, width = 550, height=70)
# Label für Würfel 1
labelWuerfel1 = Label(master=frameAusgabe,
                          background='white',
                          text='',
                          foreground='black')
labelWuerfel1.place(x=125, y=10, width=50, height=50)
# Label für Würfel 2
labelWuerfel2 = Label(master=frameAusgabe,
                        background='white',
                        text='',
                        foreground='black')
labelWuerfel2.place(x=250, y=10, width=50, height=50)
# Label für Würfel 3
labelWuerfel3 = Label(master=frameAusgabe,
                            background='white',
                            text='',
                            foreground='black')
labelWuerfel3.place(x=375, y=10, width=50, height=50)
# Bilder
imageWuerfel1 = PhotoImage(file='.\\Test 39 chuck-a-luck\\w1.gif')
imageWuerfel2 = PhotoImage(file='.\\Test 39 chuck-a-luck\\w2.gif')
imageWuerfel3 = PhotoImage(file='.\\Test 39 chuck-a-luck\\w3.gif')
imageWuerfel4 = PhotoImage(file='.\\Test 39 chuck-a-luck\\w4.gif')
imageWuerfel5 = PhotoImage(file='.\\Test 39 chuck-a-luck\\w5.gif')
imageWuerfel6 = PhotoImage(file='.\\Test 39 chuck-a-luck\\w6.gif')

#Rahmen für die Ausgabe(gewinn/verlust)
frameGewinn = Frame(master =tkFenster,
                    background='#2ECCFA')
frameGewinn.place(x=5,y=492, width = 550, height=70)
# Label für Budget
labelBudget = Label(master=frameGewinn,
                        background='white',
                        text='Budget in €',
                        foreground='black')
labelBudget.place(x=145, y=40, width=175, height=20)
# Label für Budget Ausgabe
labelBudgetAusgabe = Label(master=frameGewinn,
                        background='white',
                        text=budget,
                        foreground='black')
labelBudgetAusgabe.place(x=345, y=40, width=60, height=20)
# Label für Momentangewinn
labelMomentangewinn = Label(master=frameGewinn,
                            background='white',
                            text='Gewinn in jeder Runde in €',
                            foreground='black')
labelMomentangewinn.place(x=145, y=10, width=175, height=20)
# Label für Momentangewinn Augabe
labelMomentangewinnAusgabe = Label(master=frameGewinn,
                            background='white',
                            text=gewinn,
                            foreground='black')
labelMomentangewinnAusgabe.place(x=345, y=10, width=60, height=20)


#Aktivierung des Fensters
tkFenster.mainloop()
