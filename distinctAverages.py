class Solution:
    def distinctAverages(self,nums:List[int])->int:
        nums.sort()
        averages=set()
        left=0
        right=len(nums)-1
        while left<right:
            avg=(nums[left]+nums[right])/2
            averages.add(avg)
            left+=1
            right-=1
        return len(averages)
#eXPLANATION:
​nums.sort()
👉 "We sort the list in ascending order so the smallest numbers are at the left and the largest are at the right."
​averages = set()
👉 "We create an empty set to store our calculated averages—sets automatically ignore duplicates!"
​left = 0
👉 "We place a pointer at the very start of the list to point to the smallest number."
​right = len(nums) - 1
👉 "We place a pointer at the very end of the list to point to the largest number."
​while left < right:
👉 "We keep looping until the left and right pointers meet in the middle."
​avg = (nums[left] + nums[right]) / 2
👉 "We calculate the average of the current smallest and largest numbers."
​averages.add(avg)
👉 "We add this calculated average into our set."
​left += 1
👉 "We move the left pointer one step forward to get the next smallest number."
​right -= 1
👉 "We move the right pointer one step backward to get the next largest number."
​return len(averages)
👉 "Finally, we return the total number of items in the set, which tells us how many unique averages we found."