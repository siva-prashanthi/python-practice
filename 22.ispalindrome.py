class Solution:
    def isPalindrome(self,x:int)->bool:
        if x<0:
            return False
        original=x
        reversed_num=0
        while x>0:
            last_digit=x%10
            reversed_num=(reversed_num*10)+last_digit
            x=x//10
        return original==reversed_num       
#Explanation:
​Line 1 (class Solution:):
Set up the code box.
​Line 2 (def countPairs(...)):
Start the function to find pairs.
​Line 3 (nums.sort()):
Sort list from low to high.
​Line 4 (count = 0):
Start pair total at zero.
​Line 5 (left = 0):
Put left mark at the start.
​Line 6 (right = len(nums) - 1):
Put right mark at the end.
​Line 7 (while left < right:):
Keep going until marks cross.
​Line 8 (if nums[left] + nums[right] < target:):
Check if two numbers add up to less than target.
​Line 9 (count += right - left):
Add all valid pairs at once.
​Line 10 (left += 1):
Move left mark one step right.
​Line 11 & 12 (else: right -= 1):
If sum is big, move right mark one step left.
​Line 13 (return count):
Give back the total count.