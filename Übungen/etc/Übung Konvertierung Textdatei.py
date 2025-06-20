import sys
sys.path.append('./.')
from Lib import meinmodul as mm

do = open ("././Textdateien/Programmierer-Gedicht.txt", "r", encoding="utf-8")
gedicht = []
for zeile in do:
    gedicht.append(zeile[:-1])
do.close ()

neuesgedicht = []

for zeile in gedicht:
    zeile = mm.ersetzeumlaute (zeile)
    neuesgedicht.append (zeile)

do = open ("././Textdateien/Programmierer-Gedicht2.txt", "w", encoding="utf-8")
for zeile in neuesgedicht:
    do.write (f"{zeile}\n")
do.close ()