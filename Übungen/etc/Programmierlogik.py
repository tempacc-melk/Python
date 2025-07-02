# Aufgabe 1
# Opt1
def is_evenBis (n):
    isEven = False
    for i in range (n + 1):
        isEven = not isEven
        print (i, isEven)

# Opt2
def is_even (n):
    z = n / 2
    if z > int (z): 
        return False
    else: 
        return True

zahl = int (input ("Zahl: "))
is_evenBis (zahl)

# Aufgabe 2
def collatz (n):
    loops = 0
    while n > 1:
        if n % 2 == 0: 
            n = n // 2
        elif n % 2 != 0: 
            n = n * 3 + 1

        loops += 1

    return loops

zahl = int (input ("Zahl: "))
print (f"Zahl: {zahl} -> {collatz(zahl)} - Wiederholungen")

# Aufgabe 3
def spezialzahlensuche ():
    liste = []
    for i in range (100, 1000):
        intToStr = str (i)
        z1 = intToStr [0:1]
        z2 = intToStr [1:2]
        z3 = intToStr [2:]

        if z1 != z2 and z1 != z3:
            if int (z1) + int (z3) == int (z2):
                strToInt = z1 + z2 + z3
                strToInt = int (strToInt)
                liste.append (strToInt)

    return liste

print (f"Liste von 100 bis 999: {spezialzahlensuche()}")

# Aufgabe 4
import math as m
def zahlenfolge (n):
    loops = 0
    while n > 1:
        wurzel = m.isqrt(n)
        if n ** 0.5 == wurzel:
            n += 1
        else: 
            n -= 2

        print (n, end= " ")

        
zahl = int (input ("Zahl: "))
zahlenfolge (zahl) # -> Nicht möglich, bei +1 und -1 kann die Zahl niemals 1 erreichen

# Aufgabe 5
import sys
sys.path.append ('./')
from Lib import meinmodul as mm

print (f"\nSumme: {sum (mm.primzahlen_vonbis (1_000_000, None, 1000))}")
