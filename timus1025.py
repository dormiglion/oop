"""Этот код позволяет нам решить задачу Timus 1025 """


def bubble_sort(lst: list, n: int) -> list:
    """The function performs a so-called bubble sort
    :param: lst (list) - the source list for sorting
    :param: n (int) - the number of items in the list
    :return: lst (list) - sorted array
    """
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


k = int(input())
ar = list(map(int, input().split()))
count = 0

bubble_sort(ar, k)

for m in range(k // 2 + 1):
    count += ar[m] // 2 + 1

print(count)
