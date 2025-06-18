import sqlite3 as s

db = s.connect ("./Datenbanken/planeten.sqlite")
cursor = db.cursor ()

sql = "SELECT * FROM tblPlaneten"
cursor.execute (sql)
daten = cursor.fetchall ()
db.close ()

for i in daten:
    print (f"| {i[1]:10} | {i[2]:5} | {i[3]:6} | {i[4]:3} |")
