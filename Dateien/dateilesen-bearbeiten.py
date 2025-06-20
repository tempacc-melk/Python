import sys
sys.path.append('./')
from Lib import sortierungsmodul as sm

do = open ("./Textdateien/zahlen-unsortiert.txt", "r")
liste = []
for zeile in do:
    liste.append (int(zeile))

sm.bubblesort (liste)
do.close ()

do = open ("./Textdateien/zahlen-sortiert.txt", "w", encoding="utf-8")
for zeile in liste:
    do.write (f"{zeile}\n")

do.close ()
