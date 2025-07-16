import sys
sys.path.append ('./')
import sqlite3 as s

class Person:
    def __init__ (self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
 
    def __repr__ (self):
        return f"Person(ID={self.id}, Name='{self.name}', Alter={self.age})"
 
db = s.connect ("./Datenbanken/personen.sqlite3")
cursor = db.cursor ()
 
cursor.execute ("""
               CREATE TABLE IF NOT EXISTS persons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
                """)
 
cursor.executemany ("INSERT INTO persons (name, age) VALUES (?, ?)",
                   [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Onkel Otto", 83)] )
 
db.commit ()
 
cursor.execute ("SELECT * FROM persons")
daten = cursor.fetchall ()
db.close ()
 
persons = []
for row in daten:
    id = row[0]
    name = row[1]
    age = row[2]
    persons.append (Person(id, name, age))
 
for person in persons:
    print (person)
