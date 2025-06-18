import sqlite3 as s

db = s.connect ("./Datenbanken/telefon.sqlite")
cursor = db.cursor ()

sql = "SELECT * FROM telefon"

cursor.execute (sql)
daten = cursor.fetchall ()
db.close ()

print ("| ID | Name       | Telefonnummer     |")
print ("|----+------------+-------------------|")
for ds in daten:
    print (f"| {ds[0]:2} | {ds[1]:10} | {ds[2]:17} |")
