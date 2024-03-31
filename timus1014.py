N = int(input())
ar = [N]
Q = ""
flag = True

if N == 0:
    print("10")

else:
    while ar[0] > 9:
        for i in range(9, 1, -1):
            if ar[0] % i == 0:
                ar[0] //= i
                ar.append(i)
                break
        else:
            print("-1")
            flag = False
            break
    if flag:
        ar.sort()
        for i in ar:
            Q += str(i)
        print(Q)
