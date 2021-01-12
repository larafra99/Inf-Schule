#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      frengann
#
# Created:     07.02.2019
# Copyright:   (c) frengann 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint

class Wuerfel(object):
    def __init__(self):
        self.augenzahl = 1

    def wuerfeln(self):
            zahl = randint(1,6)
            return zahl

w1 = Wuerfel()
w2 = Wuerfel()
wurf1 = w1.wuerfeln()
wurf2 = w2.wuerfeln()

if wurf1 > wurf2:
    #print(wurf1)
    #print(wurf2)
    ergebnis = wurf1 * 10 + wurf2
    if ergebnis == 21:
        print(ergebnis, 'Maexchen')
    else:
        print(ergebnis)

elif wurf2 > wurf1:
    #print(wurf2)
    #print(wurf1)
    ergebnis = wurf2 * 10 + wurf1
    if ergebnis == 21:
        print(ergebnis, 'Maexchen')
    else:
        print(ergebnis)

elif wurf2 == wurf1:
    ergebnis = wurf2 * 10 + wurf1
    print(ergebnis, 'Pasch')

