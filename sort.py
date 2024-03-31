def insertion_sort(lst: list, n: int) -> list:
    """The function performs a so-called insertion sort
    :param: lst (list) - the source list for sorting
    :param: n (int) - the number of items in the list
    :return: lst (list) - sorted array
    """
    for i in range(1, n):
        key = lst[i]
        temp = i - 1
        while temp >= 0 and lst[temp] > key:
            lst[temp + 1] = lst[temp]
            temp -= 1
        lst[temp + 1] = key
    return lst