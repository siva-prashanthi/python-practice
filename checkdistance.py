class Solution:
    def checkDistances(self,s:str,distance:List[int])->bool:
        for i in range(len(s)):
            current=s[i]
            for j in range(i+1,len(s)):
                if current==s[j]:
                    distBetween=j-i-1
                    if distBetween!=distance[ord(current)-ord('a')]:
                        return False
        return True
        ##Explanation:
​Lines 1 & 2 (class Solution...): Sets up the LeetCode function to take a string s and a distance list, returning True or False

​Line 3 (for i in range(len(s)):): Starts a loop (i) to pick each letter in the string one by one.

​Line 4 (current = s[i]): Stores the current letter at position i into a variable named current.

​Line 5 (for j in range(i + 1, len(s)):): Starts a second loop (j) to look at all the letters after position i.

​Line 6 (if current == s[j]:): Checks if the second loop found the matching pair for current.

​Line 7 (distBetween = j - i - 1): Calculates how many characters are sitting between the first position (i) and second position (j).

​Line 8 (if distBetween != distance[ord(current) - ord('a')]:): Converts current letter to a number
 ('a' -> 0, 'b' ->1) and checks if distBetween matches the expected number in distance.

​Line 9 (return False): If the gap size is wrong, it immediately stops and gives back False.

​Line 10 (return True): If all letter pairs matched their given distances perfectly, it gives back True.