import json
 
dict={}
for i in range(100,125):
    dict[i]=i*2                 # Erzeugt Key-Values mit Key als Integer (in JSON nicht gestattet)
 
print(dict)
 
do = open("export2.json", "w")  # Textdatei zum Schreiben öffnen
json.dump(dict, do)             # Dictionary config in Datei schreiben mit Einzug 5
do.close()
