def binary_search(arr, start_index, end_index, k):
    if start_index == None:
        start_index = 0
    if end_index == None:
        end_index = len(arr) - 1
    
    arr_len = end_index - start_index + 1
    if not arr_len:
        return None
    
    med = start_index + (arr_len // 2)
    if arr[med] == k:
        return med
    elif arr[med] > k:
        return binary_search(arr, start_index, med - 1, k)
    elif arr[med] < k:
        return binary_search(arr, med+1, end_index, k)

""" 
Recurence is:
T(n) = O(1) if n == 1
T(n) = T(n/2) + O(1) if n > 1

T(n) in the worst case is the same as however many times n can be
divided by 2, which is O(log n).

"""

if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 10, 11, 50, 100, 101]

    for element in arr:
        assert binary_search(arr, 0, len(arr) - 1, element) == arr.index(element)
    
    bad_elements = [55, -3, 0, 1, 1000, 7]

    for element in bad_elements:
        assert binary_search(arr, 0, len(arr) - 1, element) == None