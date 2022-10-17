from collections import deque
import copy
import random



def my_merge(A, p, q, r):
    l1 = q - p + 1
    l2 = r - q
    l_total = r - p + 1
    left = deque()
    right = deque()

    for i in range(p, q + 1):
        left.append(A[i])
    for i in range(q+1, r+1):
        right.append(A[i])

    left.append(float('inf'))
    right.append(float('inf'))
    
    for i in range(l_total):
        if left[0] <= right[0]:
            A[p+i] = left.popleft()
        else:
            A[p+i] = right.popleft()
    
    return None


def my_merge_sort(A, p, r):
    if p < r:
        q = (r + p) // 2
        
        my_merge_sort(A, p, q)
        my_merge_sort(A, q+1, r)
        my_merge(A, p, q, r)


if __name__ == "__main__":
    test_list1 = []
    test_list2 = []
    for i in range(101):
        test_list1.append(random.randint(0, 100))

    test_list2 = copy.deepcopy(test_list1)
    assert test_list1 == test_list2  # sanity check
    my_merge_sort(test_list1, 0, len(test_list1) - 1)
    
    assert test_list1 != test_list2  # in the very rare case where the array came out sorted,
                                     # this test wouldn't tell us anything.

    assert test_list1 == sorted(test_list2)   # sorted(), unlike the two functions above, 
                                              # returns a sorted list with the elements of the
                                              # passed-in array, without sorting the passed-in
                                              # array itself.

