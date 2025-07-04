import sys
sys.path.append ('./')
# Aufgabe 1
bevölkerung = {}

# Aufgabe 2
bevölkerung["Indien"] = 1392

# Aufgabe 3
bevölkerung["USA"] = 329
bevölkerung["Indonesien"] = 26

# Aufgabe 4
from pprint import pprint
# Opt1
bevölkerung["Pakistan"] = 217
bevölkerung["Brasilien"] = 209
bevölkerung["Nigeria"] = 201
bevölkerung["Deutschland"] = 83

# Opt2 
# bevölkerung["Pakistan"], bevölkerung["Brasilien"], bevölkerung["Nigeria"], bevölkerung["Deutschland"] = 217, 209, 201, 83

print ("Print:",bevölkerung)

print ("Pprint:")
pprint (bevölkerung)

# Aufgabe 5
for k,v in bevölkerung.items():
    print (f"{k:12} {v:4}")

# Aufgabe 6
bevölkerung["Pakistan"] = 268
del bevölkerung["Nigeria"]

# Aufgabe 7
print ("Aufgabe 7")
summe = 0
for k,v in bevölkerung.items():
    bevölkerung[k] = v * 1_000_000
    summe += bevölkerung[k]

pprint (bevölkerung)
pprint (summe)

# Zusatzaufgabe
import json

do = open ("./Exports/export-bevölkerung.json", "w")  # Textdatei zum Schreiben öffnen
json.dump (bevölkerung, do, indent= 5)             # Dictionary config in Datei schreiben mit Einzug 5
do.close ()
