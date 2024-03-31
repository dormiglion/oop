k = int(input())
ar = []

for i in range(k):
    ar.append(int(input()))

primes = []
maximum = max(ar)
count = 0
num = 2

while count < maximum:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        primes.append(num)
        count += 1
    num += 1

for i in range(k):
    print(primes[ar[i]-1])
