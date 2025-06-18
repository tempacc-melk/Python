import sqlite3 as s

db = s.connect ("./Datenbanken/telefon.sqlite")
cursor = db.cursor ()

while True:
    n = input ("Name: ")
    if not n: break
    t = input ("Telefonnummer: ")

    sql = f"INSERT INTO telefon (Name, Telefonnummer) VALUES ('{n}','{t}')"
    cursor.execute (sql)

db.commit ()
db.close ()
