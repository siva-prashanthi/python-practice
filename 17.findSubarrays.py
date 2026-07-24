class Solution:
    def findSubarrays(self,nums:List[int])->bool:
        seen=set()
        for i in range(len(nums)-1):
            s=nums[i]+nums[i+1]
            if s in seen:
                return True
            seen.add(s)
        return False
##Expalnation:
    seen = set()
👉 "This creates an empty memory box to keep track of the sums we calculate."
​for i in range(len(nums) - 1):
👉 "This loops through the list, stopping just before the last number so every number has a partner on its right."
​s = nums[i] + nums[i + 1]
👉 "This adds the current number and the number right next to it."
​if s in seen:
👉 "This checks: 'Have we already seen this sum before?'"
​return True
👉 "If yes, we found a duplicate sum, so we immediately say True and stop."
​seen.add(s)
👉 "If no, we store this new sum in our memory box for later."
​return False
👉 "If we checked all pairs and found no duplicate sums, we finally say False."