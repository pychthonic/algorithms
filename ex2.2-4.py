"""

Make it return the string "ALL DONE" on the first line of the function.
Just kidding. 

If we want to have the function finish as quickly as possible for the
best-case scenario, we first assume the best case is true, and figure
out how to check to see if the best case is true, before we get to
"the meat" of the algorithm. So for selection sort, we could just check
to see if the array is already sorted before the nested for loops begin,
and if it's already sorted, the algorithm will finish in O(n) time.
This could work for a scenario where most of the arrays that are fed
to the algorithm will be best-cases. However, if they aren't, it adds
to the time the algorithm takes since it adds an extra O(n) time to first
check for best-case. So the algorithm technically becomes O(n^2 + n)
for non-best-case scenarios. This might still be worth it since for
very large sets of data (in this case, very large arrays), O(n^2 + n)
effectively becomes O(n^2). 


"""