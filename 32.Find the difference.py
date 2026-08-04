class Solution:
    def findTheDifference(self, s: str, t: str)->str:
        sum(ord(c) for c in t)#ord(c)converts string into ASCII value
        sum(ord(c) for c in s)
        diff=sum(ord(c) for c in t)-sum(ord(c) for c in s)
        return chr(diff)
        