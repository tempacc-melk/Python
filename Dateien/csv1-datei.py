import csv

do = open ("./Tabellen/Verkaufsstatistik.csv", "r", encoding="ANSI")
r = csv.reader (do, delimiter=";")
h = next(r)

daten = []
for ds in r:
    ds[2] = int (ds[2])
    ds[3] = float (ds[3])
    ds[4] = float (ds[4])
    daten.append (ds)

do.close ()

do2 = open ("./Tabellen/Verkaufsstatistik.csv", "w", encoding="UTF-8")
wo = csv.writer (do2, delimiter=";", lineterminator="\n", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
wo.writerow (h)
wo.writerows (daten)

do2.close ()
