import sys
sys.path.append('./')
from Lib import meinmodul as mm

do = open ("./Textdateien/zahlen-unsortiert.txt", "r")
liste = []
for zeile in do:
    liste.append (int(zeile))

mm.Bubblesort (liste)
do.close ()

do = open ("./Textdateien/zahlen-sortiert.txt", "w", encoding="utf-8")
for zeile in liste:
    do.write (f"{zeile}\n")

do.close ()
