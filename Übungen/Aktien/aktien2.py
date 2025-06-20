import sqlite3 as s

db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
cursor = db.cursor ()

liste = [
    ("META", "Meta Platforms Inc.", 289.90, 469.59, 35, "Internet"),
    ("TSLA", "Teslna Inc.", 195.50, 170.90, 10, "Automobil"),
    ("MSFT", "Microsoft Corp.", 340.90, 413.20, 20, "Technologie"),
    ("VOW.DE", "Volkswagen AG", 160.10, 132.89, 45, "Automobil")
        ]
try:
    cursor.executemany ("INSERT INTO aktien VALUES (?, ?, ?, ?, ?, ?)", liste)
    db.commit ()
except:
    print ("Cannot execute sql statement")

db.close ()
