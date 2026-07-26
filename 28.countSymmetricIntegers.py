class Solution:
    def countSymmetricIntegers(self,low:int,high:int)->int:
        count=0
        for num in range(low,high+1):
            s=str(num)
            n=len(s)
            if n%2!=0:
                continue
            half=n//2
            left=sum(int(s[i]) for i in range(half))
            right=sum(int(s[i]) for i in range(half,n))
            if left==right:
                count+=1
        return count
    #EXplanation
​class Solution:
Defines the main Solution class required by LeetCode.
​def countSymmetricIntegers(self, low: int, high: int) -> int:
Defines the function that takes two numbers, low and high, and promises to return an integer count.
​count = 0
Starts a counter at 0 to keep track of how many symmetric numbers we find.
​Inside the Main Loop
​for num in range(low, high + 1):
Loops through every single number starting from low up to and including high.
​s = str(num)
Converts the current number into a string so we can easily count and access its individual digits.
​n = len(s)
Finds the total number of digits in s.
​if n % 2 != 0:
Checks if the number of digits is odd (e.g., 1, 3, or 5 digits).
​continue
If the digit count is odd, skips the rest of the loop and immediately jumps to the next number (because odd-digit numbers can't be symmetric).
​half = n // 2
Calculates the middle point (half length) of the number string.
​left = sum(int(s[i]) for i in range(half))
Adds up all the digits from index 0 up to half - 1 (the left half).
​right = sum(int(s[i]) for i in range(half, n))
Adds up all the digits from index half to n - 1 (the right half).
​if left == right:
Checks if the sum of the left half matches the sum of the right half.
​count += 1
If the sums match, adds 1 to our symmetric number counter.
​Final Output
​return count
Returns the final total count of symmetric numbers after checking the entire range.