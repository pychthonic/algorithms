""" 
Initialization: 
i = len(arr_C) - 1
arr_C holds only bits that are a sum of the related indexes in arr_A and
arr_B. Since there are no bits to the right of i, this must be true.

Maintenance:
After every decrement of i, the two indices in arr_A and arr_B are also
decremented, and the newly exposed element of arr_C is changed to 1 or
kept as 0 depending on what the addition of the newly exposed elements
in arr_A and arr_B and on whether the carry bit is set. Therefore, at 
the end of each iteration, there are no bits to the right of i that
do not reflect this addition.

Termination:
After the loop is finished, the most significant bit of arr_C reflects
whether a final carry bit was set, and all bits in arr_C reflect the
sum of the concomitant bits in arr_A and arr_B.
"""


from typing import List

def add_binary_arrays(arr_A: List, arr_B: List) -> List:

    carry = 0
    len_A = len(arr_A)
    len_B = len(arr_B)

    # Find lenth of return array, and create return array:
    len_C = max(len_A, len_B) + 1
    arr_C = [0] * len_C
    
    # Find different between lenth of the input arrays and the return
    # array. This will be used in the for loop to calculate which
    # index will be used when grabbing numbers from the input arrays
    # to add:
    arr_A_diff = len_C - len_A
    arr_B_diff = len_C - len_B

    for i in reversed(range(len_C)):
        arr_A_index = i - arr_A_diff
        num_A = arr_A[arr_A_index] if arr_A_index >= 0 else 0
        
        arr_B_index = i - arr_B_diff

        num_B = arr_B[arr_B_index] if arr_B_index >= 0 else 0
        
        carry, num_C = divmod(num_A + num_B + carry, 2)
        arr_C[i] = num_C

    return arr_C


if __name__ == '__main__':
    arr_A = [1, 1, 0, 1, 1]
    arr_B = [1, 1, 1, 1, 1]
    arr3 = add_binary_arrays(arr_A, arr_B)
    print(arr3)