import sqlite3 as s
import os

if (os.path.isfile ("./Datenbanken/telefon.sqlite")):
    os.remove ("./Datenbanken/telefon.sqlite")

db = s.connect ("./Datenbanken/telefon.sqlite")
cursor = db.cursor ()

sql = "CREATE TABLE IF NOT EXISTS telefon (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Telefonnummer TEXT)"

cursor.execute (sql)

db.close ()
