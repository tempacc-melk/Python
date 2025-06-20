import sqlite3 as s

db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
cursor = db.cursor ()

cursor.execute ("""CREATE TABLE IF NOT EXISTS aktien (
                Kürzel TEXT PRIMARY KEY,
                Name TEXT,
                Kaufkurs REAL,
                Kurs REAL,
                Anzahl INTEGER,
                Branche TEXT
                )""")

db.close ()
