import math as m

def ellipsenumfang (a, b): return m.pi * (3 * (a+b) / 2 - m.sqrt(a * b))

print (f"{ellipsenumfang (87,78):.2f}")
