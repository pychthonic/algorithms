"""

Since we know arr[0..j-1] is already sorted, we might think we can use
binary search to insert the next element into its proper place,
however since we also have to move every element to the right of the
new index for the next element, the worst case is still O(n) time.
In fact, it's actually O(n) + O(log n), since we spend time finding
the index first, before we can even begin moving the items, where as
with the previous insertion_sort, we've already moved the items by
the time we get to the proper index for the new element.


"""

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
