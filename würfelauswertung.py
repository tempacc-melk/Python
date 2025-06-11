import random
import statistics

w = []
# a)
for i in range(1_000_000):
    w.append(random.randint(1,6)) 

# b)
print(f"Mittelwert: {statistics.mean(w)}")

# c)
check = 6*[0]
for i in w:
    for j in range(6):
        if j + 1 == i: 
            check[j] += 1
            break

print()
for o in range(6):
    print(f"Die Zahl {o + 1} erscheint in der Liste: {check[o]}x")
