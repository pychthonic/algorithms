import copy
import random

def insertion_sort_decreasing(arr):
    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        j = i - 1
        while arr[j] < key and j >= 0:
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
    
    insertion_sort_decreasing(test_list1)
    
    assert test_list1 != test_list2  # in the very rare case where the
                                     # array came out sorted in
                                     # decreasing order, this test
                                     # wouldn't tell us anything.
    assert test_list1 == sorted(test_list2, reverse=True)   # sorted(), unlike the two functions above, 
                                              # returns a sorted list with the elements of the
                                              # passed-in array, without sorting the passed-in
                                              # array itself.
