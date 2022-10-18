"""

n is a power of two, so that means n % 2 = 0, AND n = 2 ^ k, for some
integer k.

Base case: n = 2

if n = 2, then T(n) = 2. 

2 * log 2 = 2 * 1 = 2

So for n = 2, T(n) = n * log n


Inductive step:

if T(n) = n log n, and n is a power of two, then we have:

T(2^k) = (2^k) log (2^k)  = k * (2^k)

To prove the inductive step, we need to prove that if this equation is 
true, it is also true for the *next* power of two, so we need to prove
that:

T(2^(k+1)) = (k + 1) (2^(k+1))

Simplifying, we find:

Refering back to the 2nd formula of the problem, we want to show that:

T(n) = 2T(n/2) + n

or using n = 2^(k+1):

T(2^(k+1)) = 2T((2^(k+1))/2) + (2^(k+1)) = 2T(2^k) + 2(2^k)
            = 2(T(2^k) + (2^k))

We know from above that:

T(2^k) = (2^k) log (2^k) 

So substituting for T(2^k):

T(2^(k+1)) = 2((2^k) log (2^k) + (2^k)) = 2((2^k) * k + (2^k))
           = 2(k*(2^(k+1))/2 + (2^(k+1))/2) = k(2^(k+1)) + (2^(k+1))
           = 2^(k+1) (k + 1)

We have thus proved the inductive step.


"""