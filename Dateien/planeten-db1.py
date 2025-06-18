import sqlite3 as s

merkur = ['Merkur', 0.39, 2440, 0] 
venus = ['Venus', 0.72, 6052, 0] 
erde = ['Erde', 1.0, 6378, 1] 
mars = ['Mars', 1.52, 3397, 2] 
jupiter = ['Jupiter', 5.2, 71493, 79] 
saturn = ['Saturn', 9.54, 60267, 82] 
uranus = ['Uranus', 19.19, 25559, 27] 
neptun = ['Neptun', 30.07, 24764, 14] 

planetentabelle = []
planetentabelle.append(merkur)
planetentabelle.append(venus)
planetentabelle.append(erde)
planetentabelle.append(mars)
planetentabelle.append(jupiter)
planetentabelle.append(saturn)
planetentabelle.append(uranus)
planetentabelle.append(neptun)

db = s.connect ("./Datenbanken/planeten.sqlite")
cursor = db.cursor ()

sql = """CREATE TABLE IF NOT EXISTS tblPlaneten (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Abstand REAL,
        Radius INTEGER,
        Monde INTEGER
        )"""

cursor.execute (sql)

for ds in planetentabelle:
    sql = f"""INSERT INTO tblPlaneten (Name, Abstand, Radius, Monde)
            VALUES
            ('{ds[0]}',{ds[1]},{ds[2]},{ds[3]})
            """
    cursor.execute (sql)

db.commit ()
db.close ()
