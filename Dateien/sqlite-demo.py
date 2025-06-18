import sqlite3 as s

db = s.connect ("./Datenbanken/db1.sqlite")     # Datenbank öffnen
cursor = db.cursor ()

# sql = "CREATE TABLE tblArtikel (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Anzahl REAL)"

# n = input ("Name: ")
# a = int (input ("Anzahl: "))
# sql = f"INSERT INTO tblArtikel (Name, Anzahl) VALUES ('{n}', {a})"

# sql = "DELETE FROM tblArtikel WHERE id > 1 AND id < 6"
sql = "SELECT * FROM tblArtikel"

cursor.execute (sql)        # Befehl ausführen
db.commit ()                # Bestätigt die Speicherung/Transaktion der Daten (INSERT, UPDATE, DELETE)

daten = cursor.fetchall ()  # Alle Daten werden kopiert
db.close ()                 # Datenbank schließen

print (f"| ID   | Name                      | Anzahl |")
print (f"|------|---------------------------|--------|")
for ds in daten:
    print (f"| {ds[0]:4} | {ds[1]:25} | {ds[2]:6} |")

