def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
        
""" 
Initialization:
i = 0. So, the "state" that will be maintained is that
there are no elements to the left of index i that are equal to k.
Since there are no elements to the left of i, there are no elements
equal to k to the left of i.

Maintenance:
Since i will be returned at the end of each iteration if the element
at i is equal to k, and we know there are no elements to the left of
i that are equal to k, it remains true before the next iteration that
there are no elements to the left of i (or at i) that are equal to k.

Termination:
When the loop terminates, i is equal to len(arr). This
number as an index is one greater than the last index in the array.
We therefore will know, after the loop terminates, whether there is at
least one element in the array that is equal to k.

"""