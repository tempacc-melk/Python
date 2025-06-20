def leistung (volt, ampere): return volt * ampere

a = int(input("Volt: "))
b = int(input("Ampere: "))

print (f"Bei {a} Volt und {b} Ampere wird eine Leistung von {leistung(a, b)} Watt erzeugt.")
