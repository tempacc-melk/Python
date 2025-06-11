def handshake (n): return n * (n - 1) / 2

print("| Personen | Händeschüttler |")
print("|----------+----------------|")
for i in range (1,21):
    print (f"| {i:8} | {int(handshake(i)):14} |")
