from math import ceil
ar = input()
n, k = ar.split()
n = int(n)
k = int(k)

print(max(2, ceil((n * 2) / k)))
