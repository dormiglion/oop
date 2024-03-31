def duons(ar: list):
    if sum(ar) % 2 != 0:
        return ["IMPOSSIBLE"]

    answ = []

    for x, y, z in moves:
        mins = min(ar[x], ar[y])
        if mins > 0:
            answ.append((z, mins))
            ar[x] -= mins
            ar[y] -= mins


    for x, y, i, j, k in perms:
        if ar[x] > 0 and ar[x] == ar[y]:
            answ.append((i, ar[x]))
            answ.append((j, ar[x]))
            answ.append((k, ar[x]))
            ar[x], ar[y] = 0, 0

    if sum(ar) > 0:
        return ["IMPOSSIBLE"]

    result = []
    for x, y in answ:
        for i in range(y):
            result.append(x)

    return result


ar = list(map(int, (input().split())))

moves = [(0, 1, 'AB-'), (0, 3, 'AD-'),
         (0, 4, 'AE-'), (1, 2, 'BC-'),
         (1, 5, 'BF-'), (2, 3, 'CD-'),
         (2, 6, 'CG-'), (3, 7, 'DH-'),
         (4, 5, 'EF-'), (4, 7, 'EH-'),
         (5, 6, 'FG-'), (6, 7, 'GH-')]

perms = [(0, 6, 'BC+', 'AB-', 'CG-'),
         (1, 7, 'CD+', 'BC-', 'DH-'),
         (2, 4, 'AB+', 'BC-', 'AE-'),
         (3, 5, 'BC+', 'CD-', 'BF-')]

print("\n".join(duons(ar)))

