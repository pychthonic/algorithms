"""
CLRS page18 INSERTION-SORT

Time complexity: O(n^2)
"""
import copy
from typing import List
import random


def insertion_sort(input_list: List) -> List:
    for i in range(1, len(input_list)):
        key = input_list[i]
        while (i > 0 and input_list[i-1] > key):
            input_list[i] = input_list[i-1]
            i -= 1
        input_list[i] = key
    return None   # List is modified in place, so None is returned to avoid confusion.


def ins_sort(arr):
    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return None


if __name__ == "__main__":
    test_list1 = []
    test_list2 = []
    for i in range(100):
        test_list1.append(random.randint(0, 100))
    test_list2 = copy.deepcopy(test_list1)
    assert test_list1 == test_list2  # sanity check
    insertion_sort(test_list1)
    
    assert test_list1 != test_list2  # in the very rare case where the array came out sorted,
                                     # this test wouldn't tell us anything.
    assert test_list1 == sorted(test_list2)   # sorted(), unlike the two functions above, 
                                              # returns a sorted list with the elements of the
                                              # passed-in array, without sorting the passed-in
                                              # array itself.

    ins_sort(test_list2)

    assert test_list1 == test_list2

    print(f"test_list2 after insertion sort: {test_list2}\n")
    
    



