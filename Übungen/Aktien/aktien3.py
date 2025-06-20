import sqlite3 as s

db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
cursor = db.cursor ()

liste = cursor.execute ("SELECT *, anzahl*(kurs-kaufkurs) AS Gewinn FROM aktien").fetchall ()
db.close ()

for ds in liste:
    print(f"{ds[0]:8} {ds[1]:20} {ds[2]:8.2f} {ds[3]:8.2f} {ds[4]:3} {ds[5]:12} G/V: {ds[6]:8.2f}")
