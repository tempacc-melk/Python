import sqlite3 as s

# 1)
db = s.connect (":memory:")
cursor = db.cursor ()

cursor.execute (
    """CREATE TABLE benutzer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    passwort TEXT)
    """)

cursor.execute("INSERT INTO benutzer (name, passwort) VALUES (?, ?)", ["alice", "geheim123"]), 
cursor.execute("INSERT INTO benutzer (name, passwort) VALUES (?, ?)", ["bob", "pass1234"])
db.commit ()

# 2)
eingabe = "' OR '1'='1"
sql = "SELECT * FROM benutzer WHERE name = '" + eingabe + "'"
print ("DEBUG SQL:", sql)
cursor.execute (sql)

for row in cursor.fetchall ():
    print (row)

# 3)
eingabe = "' OR '1'='1"
sql = "SELECT * FROM benutzer WHERE name = ?"
cursor.execute (sql, [eingabe])

for row in cursor.fetchall (): 
    print (row)

# Bonus 1)
eingabe = "x'; DROP TABLE benutzer; --"
sql = "SELECT * FROM benutzer WHERE name = '" + eingabe + "'"
print ("DEBUG SQL:", sql)
cursor.execute (sql)

for row in cursor.fetchall ():
    print (row)

# Bonus 2)
eingabe = "x'; DROP TABLE benutzer; --"
sql = "SELECT * FROM benutzer WHERE name = ?"
cursor.execute (sql, [eingabe])

for row in cursor.fetchall (): 
    print (row)

db.close ()
