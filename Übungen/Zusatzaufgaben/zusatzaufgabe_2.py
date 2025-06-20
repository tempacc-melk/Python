import sqlite3 as s
import os

def db_anlegen ():
    db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
    cursor = db.cursor ()

    cursor.execute ("""CREATE TABLE aktien (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Kürzel TEXT,
                    Name TEXT,
                    Kaufkurs REAL,
                    Kurs REAL,
                    Anzahl INTEGER,
                    Branche TEXT
                    )""")

    db.close ()

def ds_anlegen ():
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

def db_ausgabe():
    db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
    cursor = db.cursor ()

    liste = cursor.execute ("SELECT *, anzahl*(kurs-kaufkurs) AS Gewinn FROM aktien").fetchall ()
    db.close ()

    for ds in liste:
        print(f"{ds[0]:8} {ds[1]:20} {ds[2]:8.2f} {ds[3]:8.2f} {ds[4]:3} {ds[5]:12} G/V: {ds[6]:8.2f}")


def ds_einfügen ():
    db = s.connect ("././Datenbanken/aktienportfolio.sqlite")
    cursor = db.cursor ()

    kürzel = input ("Kürzel: ")
    name = input ("Name: ")
    kauf = float (input ("Kaufkurs "))
    kurs = float (input ("Kurs: "))
    anzahl = int (input ("Anzahl: "))
    branche = input ("Branche: ")

    try:
        cursor.execute ("INSERT INTO aktien VALUES (?, ?, ?, ?, ?, ?)", [ kürzel, name, kauf, kurs, anzahl, branche ])
        db.commit ()
    except:
        print ("Cannot execute sql statement")

    db.close ()

while True:
    print ("*** Aktienverwaltung ***")
    print ("1 -> Datenbank anlegen")
    print ("2 -> Datensatz anlegen")
    print ("3 -> Datenbank ausgabe")
    print ("4 -> Datensatz einfügen")
    print ("9 -> Programm beenden")
    e = input ("Input: ")
    try:
        e = int (e)
    except:
        e = 0
    
    if e == 9: break
    elif e == 1: db_anlegen ()
    elif e == 2: ds_anlegen ()
    elif e == 3: db_ausgabe ()
    elif e == 4: ds_einfügen ()
    else: print ("Unbekannter Befehl")
