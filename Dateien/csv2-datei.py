import csv

liste = [ [ "VW",1000 ], [ "BMW",2000 ], [ "Opel",500 ] ]

fo = open ("./Tabellen/autos.csv", "w", encoding="UTF-8")
wo = csv.writer (fo, delimiter=";", lineterminator="\n", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
wo.writerow([ "Autohersteller", "Stückzahl" ])
wo.writerows (liste)

fo.close ()
