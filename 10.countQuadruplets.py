#-->1
class Solution:
    def countQuadruplets(self, nums:List[int])->int:
        count=0
        tot2=defaultdict(int)
        for c in range(2,len(nums)-1):
            b=c-1
            for a in range(b):
                tot2[nums[a]+nums[b]]+=1
            for d in range(c+1,len(nums)):
                count+=tot2[nums[d]-nums[c]]
        return count
#-->2
class Solution:
    def countQuadruplets(self, nums:List[int])->int:
        count=0
        tot2=defaultdict(int)
        for c in range(2,len(nums)-1):
            b=c-1
            for a in range(b):
                tot2[nums[a]+nums[b]]+=1
            for d in range(c+1,len(nums)):
                count+=tot2[nums[d]-nums[c]]
        return count       