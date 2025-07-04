dict1 = [
    {"Name":"Anna",
    "Geburtsjahr":1988,
    "Kontostand":130.56,
    "Bezahlt": True},
         
    {"Name":"Fritz",
    "Geburtsjahr":1980,
    "Kontostand":0,
    "Bezahlt":False}
    ]  # mutable
 
 
# for k,v in dict1.items():  # Durch alle Werte (key + value)
#     print(f"{k:12} {v:>10}")
 
# print(dict1)

einwohner = {
    "Berlin": 3669491,
    "Hamburg": 1847253,
    "München": 1484226,
    "Köln": 1087863,
    "Frankfurt aM": 763380,
    "Stuttgart": 635911,
    "Düsseldorf": 621877,
    "Leipzig": 593145,
    "Dortmund": 588250,
    "Essen": 582760,
    "Bremen": 567559,
    "Dresden": 556780,
    "Hannover": 536925,
    "Nürnberg": 518370
    }

# Ausgabe der Einwohner mit den genannten Keys
print (einwohner["Essen"])
print (einwohner.get("Testhausen"))

# Element in die Dictionary einfügen wenn nicht vorhanden andernfalls überschreiben
einwohner["Testhausen"] = 512
print (einwohner.get("Testhausen"))

# Element von Dictionary entfernen
del einwohner["Testhausen"]
print (einwohner.get("Testhausen"))

# Export nach json
import json

config = {
    "host": "localhost",
    "port": 3306,
    "user": "admin",
    "password": "geheim"
}

print(config["user"], config["password"])
 
do = open("export.json", "w")   # Textdatei zum Schreiben öffnen
json.dump(config, do, indent = 5)   # Dictionary config in Datei schreiben mit Einzug 5
do.close()
