import sys
sys.path.append('./')
from Lib import meinmodul as mm

zahlenvon = int (input ("Startwert der Zufallszahlen: "))
zahlenbis = int (input ("Endwert der Zufallszahlen: "))
zahlenanzahl = int (input ("Wie viele Zahlen sollen generiert werden?: "))

liste = mm.randomliste (zahlenvon, zahlenbis, zahlenanzahl)

do = open ("././Textdateien/zufallszahlen.txt", "w", encoding="utf-8")

for zeile in liste:
    do.write (f"{zeile}\n")

do.close ()
