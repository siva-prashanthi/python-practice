class Solution:
    def sumBase(self, n:int,k:int)->int:
        total_sum=0
        while n>0:
            n,remainder=divmod(n,k)
            total_sum+=remainder
        return total_sum
#Explanation:
​Line 1: class Solution:
Defines the main Solution class required by LeetCode.
​Line 2: def sumBase(self, n: int, k: int) -> int:
Defines the function named sumBase. It takes two integer inputs (n and base k) and promises to return an integer result.
​Line 3: total_sum = 0
Creates a variable total_sum starting at 0 to keep track of the sum of the digits.
​Inside the Loop (Lines 4–6)
​Line 4: while n > 0:
Keeps looping as long as n is greater than 0 (until all digits in base k are extracted).
​Line 5: n, remainder = divmod(n, k)
Does two operations in a single step:
​Divides n by k and updates n with the quotient (n // k).
​Extracts the remainder (n % k), which is the last digit in base k.
​Line 6: total_sum += remainder
Adds that extracted digit (remainder) directly to total_sum.
​Final Return
​Line 7: return total_sum
Once n reaches 0 and all digits have been extracted and added, it returns the final total sum.