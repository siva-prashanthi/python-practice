class Solution:
    def minimumAverage(self,nums:List[int])->int:
        nums.sort()
        min_avg=float('inf')
        left=0
        right=len(nums)-1
        while left<right:
            avg=(nums[left]+nums[right])/2
            min_avg=min(min_avg,avg)
            left+=1
            right-=1
        return min_avg
    #Explanation:
​nums.sort()
👉 "We sort the list in ascending order so the smallest numbers are on the left and the largest are on the right."
​min_avg = float('inf')
👉 "We set our starting minimum average to infinity so that any real average we calculate will be smaller than it."
​left = 0
👉 "We place a pointer at index 0 to point to the current smallest number."
​right = len(nums) - 1
👉 "We place a pointer at the end of the list to point to the current largest number."
​while left < right:
👉 "We keep looping as long as there are pairs left to process."
​avg = (nums[left] + nums[right]) / 2
👉 "We calculate the average of the current smallest and largest numbers."
​min_avg = min(min_avg, avg)
👉 "We update min_avg if the current calculated average is smaller than what we've seen so far."
​left += 1
👉 "We move the left pointer one step right to get the next smallest number."
​right -= 1
👉 "We move the right pointer one step left to get the next largest number."
​return min_avg
👉 "Finally, we return the smallest average we found across all pairs."