"""Этот код помогает нам решить задачу Timus1551"""

from math import log2, floor


def shell_sort(lst: list, n: int) -> list:
    """The function performs a Shell's sort
    :param: lst (list) - the source list for sorting
    :param: n (int) - the number of items in the list
    :return: lst (list) - sorted array
    """
    step = n // 2
    while step > 0:
        for i in range(step, n):
            key = lst[i]
            temp = i - step
            while temp >= 0 and lst[temp] > key:
                lst[temp + step] = lst[temp]
                temp -= step
            lst[temp + step] = key
        step //= 2
    return lst


n = int(input())
pref_base = []

for j in range(2 ** n):
    name, prefecture = input().split()
    pref_base.append(prefecture)

pref_base_c = shell_sort(pref_base.copy(), 2 ** n)

mx = 1
c = 1

for m in range(2 ** n - 1):
    if pref_base_c[m] == pref_base_c[m + 1]:
        c += 1
        if c > mx:
            mx = c
    else:
        c = 1

answ = n - log2(mx)
print(floor(answ))
