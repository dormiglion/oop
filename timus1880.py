"""Этот код помогает нам решить задачу Timus1880"""

from random import choice


def quick_sort(lst: list) -> list:
    """The function performs a so-called quick sort
    :param: lst (list) - the source list for sorting
    :return: (list) - sorted array
    """
    if len(lst) <= 1:
        return lst
    else:
        i = choice(lst)
        left_array = []
        middle_array = []
        right_array = []
        for ind in lst:
            if ind < i:
                left_array.append(ind)
            elif ind > i:
                right_array.append(ind)
            else:
                middle_array.append(ind)
        return (quick_sort(left_array) + middle_array
                + quick_sort(right_array))


lst = []
for j in range(3):
    input()
    lst.extend(set(map(int, input().split())))

n = len(lst)
lst_c = quick_sort(lst.copy())

count = 0
for k in range(1, n - 1):
    if lst_c[k - 1] == lst_c[k] == lst_c[k + 1]:
        count += 1

print(count)
