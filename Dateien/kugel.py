import math

pi = math.pi
r = float(input("Radius in Meter: "))
v = 4/3 * pi * r**3
print ("Kugel Volumen:",round(v,2))

o = 4 * pi * r**2
print ("Kugel Oberfläche:",round(o,2))
