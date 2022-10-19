"""

Recurrence:

In the worst case, the element at n - 1 is the lowest element, and it
will therefore take O(n) time to check all elements preceding it and
then insert it into the first position.

T = O(1) if n <= 1
T = T(n-1) + O(n) if n > 1

"""

import copy, random


def recursive_insertion_sort(arr, n=None):
    if n == None:
        n = len(arr)
    if n <= 1:
        return None

    recursive_insertion_sort(arr, n - 1)
    j = n - 2
    last_element = arr[n-1]
    while j >= 0 and arr[j] > last_element:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last_element

    return None


if __name__ == "__main__":
    test_list1 = []
    test_list2 = []
    for i in range(100):
        test_list1.append(random.randint(0, 100))
    test_list2 = copy.deepcopy(test_list1)
    assert test_list1 == test_list2

    recursive_insertion_sort(test_list1, len(test_list1))

    assert test_list1 != test_list2
    assert test_list1 == sorted(test_list2)
