class Solution:
    def findMaxK(self,nums:List[int])->int:
        ans=-1
        for i in nums:
            for j in nums:
                if i==-j:
                    ans=max(ans,abs(i))
        return ans
    #Explanation:
​ans = -1
👉 "We set the default answer to -1 in case we don't find any positive and negative matching pair."
​for i in nums:
👉 "This loops through every single number in the list one by one."
​for j in nums:
👉 "This runs a second loop through the same list to compare the first number with every other number."
​if i == -j:
👉 "This checks: 'Is one number the exact negative opposite of the other?' (like 3 and -3)."
​ans = max(ans, abs(i))
👉 "If we find a matching pair, we keep the largest value we've seen so far."
​return ans
👉 "Finally, we return the largest matching number (or -1 if no pair was found)."    