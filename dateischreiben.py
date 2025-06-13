import meinmodul as mm

do = open ("testdatei1.txt", "w", encoding="utf-8")

liste = mm.primzahlen_bis(10)

text = ""
for i in liste:
    text += f"{i} "

do.write (
    "Das ist unsere erste Datei" + "\n"
    f"Primzahlen bis 10 (Liste): {liste}" + "\n"
    f"Primzahlen bis 10 (Einzeln): {text}" + "\n"
    "Umlaute ÄÖÜäöüß" + "\n"
    )

for i in range (0,5):
    do.write (f"{i}\n")

do.close ()
print ("Datei geschrieben!")
