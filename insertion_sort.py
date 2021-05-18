"""
CLRS page18 INSERTION-SORT

Time complexity: O(n^2)
"""

from typing import List
import random


def insertion_sort(input_list: List) -> List:
    for i in range(1, len(input_list)):
        key = input_list[i]
        while (i > 0 and input_list[i-1] > key):
            input_list[i] = input_list[i-1]
            i -= 1
        input_list[i] = key
    return input_list


if __name__ == "__main__":
    test_list = [] 
    for i in range(100):
        test_list.append(random.randint(100))
    print(f"test_list before insertion sort: {test_list}\n")
    sorted_list = insertion_sort(test_list)
    print(f"sorted_list after insertion sort: {sorted_list}\n")
    assert sorted(test_list) == sorted(sorted_list)

