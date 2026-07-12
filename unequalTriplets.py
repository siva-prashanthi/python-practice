class Solution:
    def unequalTriplets(self, nums:List[nums])->int:
        c=Counter(nums)
        res=0
        left=0
        right=len(nums)
        for _, freq in c.items():
            right-=freq
            res+=left*right*freqleft+=freq
    return res
        