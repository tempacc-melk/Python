import sys 
sys.path.append ('./.')
from Lib import meinmodul as mm
from Lib import sortierungsmodul as sm
import time as t

liste = mm.randomliste (0, 100_000, 20_000)
liste2 = liste.copy()
liste3 = liste.copy()

start = t.time ()
sm.mergesort (liste)
stop = t.time ()
print (f"Dauer (Mergesort): {stop-start}")

start = t.time ()
sm.insertsort (liste2)
stop = t.time ()
print (f"Dauer (Insertsort): {stop-start}")

start = t.time ()
sm.bubblesort (liste3)
stop = t.time ()
print (f"Dauer (Bubblesort): {stop-start}")

do = open ("././Textdateien/zufallszahlen2-sortiert.txt", "w", encoding="utf-8")
for zeile in liste:
    do.write (f"{zeile}\n")
do.close ()
