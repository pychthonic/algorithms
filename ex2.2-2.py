"""
This is not a fast algorithm. It is O(n^2), because there is a for
loop inside the outer for loop.

The loop invariant is that at the beginning of each (outer) iteration,
all elements to the left of i contain the sorted minimum elements of
the entire list.

The outer for loop doesn't have to iterate over the last element
because it will already have been swapped with the second-to-last
element when the for loop iterates over the second-to-last element
and checks for the minimum element after it.

Even in the best case where the array comes in sorted, the algorithm
will still need to check for the minimum element greater than each
element, so it will still take O(n^2) time. Worst case is the same
as best case.


"""
import copy
import random

def my_selection_sort(A):
    A_len = len(A)
    for i in range(A_len - 1):
        smallest_index = i
        for j in range(i+1, A_len):
            if A[j] < A[smallest_index]:
                smallest_index = j
        A[i], A[smallest_index] = A[smallest_index], A[i]
    return None



if __name__ == "__main__":
    test_list1 = []
    test_list2 = []
    for i in range(100):
        test_list1.append(random.randint(0, 100))
    
    test_list2 = copy.deepcopy(test_list1)
    assert test_list1 == test_list2  # sanity check
    
    my_selection_sort(test_list1)
    
    assert test_list1 != test_list2  # in the very rare case where the
                                     # array came out sorted in
                                     # decreasing order, this test
                                     # wouldn't tell us anything.
    assert test_list1 == sorted(test_list2)   # sorted(), unlike the two functions above, 
                                              # returns a sorted list with the elements of the
                                              # passed-in array, without sorting the passed-in
                                              # array itself.