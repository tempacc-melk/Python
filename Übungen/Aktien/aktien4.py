import sqlite3 as s

db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
cursor = db.cursor ()

kürzel = input ("Kürzel: ")
name = input ("Name: ")
kauf = float (input ("Kaufkurs "))
kurs = float (input ("Kurs: "))
anzahl = int (input ("Anzahl: "))
branche = input ("Branche: ")

try:
    cursor.execute ("INSERT INTO aktien VALUES (?, ?, ?, ?, ?, ?)", [kürzel, name, kauf, kurs, anzahl, branche])
    db.commit ()
except:
    print ("Cannot execute sql statement")

db.close ()
