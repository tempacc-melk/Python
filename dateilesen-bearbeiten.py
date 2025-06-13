import meinmodul as mm

do = open ("Dateien/zahlen-unsortiert.txt", "r")
liste = []
for zeile in do:
    liste.append (int(zeile))

mm.Bubblesort (liste)
do.close ()

do = open ("Dateien/zahlen-sortiert.txt", "w", encoding="utf-8")
for zeile in liste:
    do.write (f"{zeile}\n")

do.close ()
