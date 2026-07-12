class Solution:
    def repeatedCharacter(self,s:str)->str:
        sets=set()
        for x in s:
            if x in sets:
                return x
            else:
                sets.add(x)