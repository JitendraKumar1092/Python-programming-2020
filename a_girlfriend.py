n = int(input("ENTER THE TOTAL STEPS to reach GF's home"))
total = 0
for i in range (5, 0, -1):
    a = n // i
    n -= (n // i) * i
    total += a
print(total)
