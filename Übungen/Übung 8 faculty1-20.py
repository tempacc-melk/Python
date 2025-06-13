print("for-schleife (Fakultät berechnen)")

for i in range(1,20 + 1):
    fakult = 1
    for j in range(1,i + 1):
        fakult = fakult * j

    print("Die Fakultät von:",i,"ist:",fakult)

import math
print()
for x in range(1,21):
    print (f"{x} {math.factorial(x)}")