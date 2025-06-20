import sqlite3 as s
import os

def db_löschen (dbname):
    if not dbname: return
    if (os.path.isfile (f"./Datenbanken/{dbname}")):
        os.remove (f"./Datenbanken/{dbname}")

def db_anlegen (dbname, tabelle):
    if not dbname or not tabelle: return
    db = s.connect (f"./Datenbanken/{dbname}")
    cursor = db.cursor ()

    sql = f"CREATE TABLE IF NOT EXISTS {tabelle} (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Telefonnummer TEXT)"

    cursor.execute (sql)

    db.close ()

def db_anzeigen (dbname, tabelle):
    db = s.connect (f"./Datenbanken/{dbname}")
    cursor = db.cursor ()

    sql = f"SELECT * FROM {tabelle}"

    cursor.execute (sql)
    daten = cursor.fetchall ()
    db.close ()

    print ("| ID | Name       | Telefonnummer     |")
    print ("|----+------------+-------------------|")
    for ds in daten:
        print (f"| {ds[0]:2} | {ds[1]:10} | {ds[2]:17} |")

def ds_einfügen (dbname, tabelle):
    if not dbname or not tabelle: return
    db = s.connect (f"./Datenbanken/{dbname}")
    cursor = db.cursor ()

    while True:
        n = input ("Name: ")
        if not n: break
        t = input ("Telefonnummer: ")

        # sql = f"INSERT INTO {tabelle} (Name, Telefonnummer) VALUES ('{n}','{t}')"
        # cursor.execute (sql)
        sql = f"INSERT INTO {tabelle} (Name, Telefonnummer) VALUES (?,?)"
        cursor.execute (sql, [n,t])

    db.commit ()
    db.close ()

def ds_löschen (dbname, tabelle):
    if not dbname or not tabelle: return
    db = s.connect (f"./Datenbanken/{dbname}")
    cursor = db.cursor ()

    id = int (input ("Welche ID soll gelöscht werden? "))

    sql = f"DELETE FROM telefon WHERE ID = {id}"
    cursor.execute (sql)
    db.commit ()
    print (f"Benutzer von der {tabelle} Telefon gelöscht.")

    db.close ()

while True:
    print ("*** TELEFONVERWALTUNG ***")
    print ("1 -> Datenbank löschen")
    print ("2 -> Datenbank anlegen")
    print ("3 -> Datenbank anzeigen")
    print ("4 -> Datensatz einfügen")
    print ("5 -> Datensatz löschen")
    print ("9 -> Programm beenden")
    e = input ("Input: ")
    try:
        e = int (e)
    except:
        e = 0
    
    if e == 9: break
    elif e == 1: 
        db = input ("Datenbank: ")
        db_löschen (db)
    elif e == 2: 
        db = input ("Datenbank: ")
        tbl = input ("Tabelle: ")
        db_anlegen (db, tbl)
    elif e == 3:
        db = input ("Datenbank: ")
        tbl = input ("Tabelle: ")
        db_anzeigen (db, tbl)
    elif e == 4:
        db = input ("Datenbank: ")
        tbl = input ("Tabelle: ")
        ds_einfügen (db, tbl)
    elif e == 5:
        db = input ("Datenbank: ")
        tbl = input ("Tabelle: ")
        ds_löschen (db, tbl)
    else: print ("Unbekannter Befehl")
