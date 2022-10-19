"""

Write a O(n*log n)-time algo that, given a set S of n integers and
another integer x, determines whether or not there exist two elements in
S whose sum is exactly x.

If by "set", we're talking about a Python set, then lookup time for any
element in the set is O(1), since set lookups operate with a hash
table.

Therefore, we can use this algo at O(n) time, i.e. faster than
O(n log n):

"""


def pair_sum_exists(S: set, x: int):
    
    for num in S:
        target = x - num
        if target != num and target in S:
            return True
    return False

"""

However, if by "set", they mean an unsorted array, then we first need
to sort the array, then iterate across it, and for each element in the
iteration, calculate the target by subtracting the element from x,
then use binary search to check if the element is in the array.

In chapter two, the two sorting algos were insertion sort and merge-
sort. Insertion sort takes O(n^2) time, and merge-sort takes O(n log n),
so the fastest is O(n log n)

Therefore, we use merge sort to sort the incoming array, then we need
to find out how long it takes to iterate across it and then binary
search for a target element. That would be O(n log n)

So total time is 2 * O(n log n), and removing constant 2, O(n log n)

"""