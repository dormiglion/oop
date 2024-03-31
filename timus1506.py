import math

n, k = input().split()
ar = input().split()
n = int(n)
k = int(k)

count_rows = math.ceil(n/k)

for i in range(count_rows):
    for j in range(i, n, count_rows):
        if j >= n:
            print(end="    ")
        else:
            print(f"{ar[j]: >4}", end="")
    print()
