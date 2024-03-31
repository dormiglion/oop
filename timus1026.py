"""Этот код позволяет нам решить задачу Timus 1026 """
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


n = int(input())
data_base = []
for j in range(n):
    data_base.append(int(input()))

input()

k = int(input())
request_base = []
for l in range(k):
    request_base.append(int(input()))

data_base_c = quick_sort(data_base.copy())

for m in request_base:
    print(data_base_c[m - 1])
