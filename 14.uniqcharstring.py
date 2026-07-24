class Solution:
    def firstUniqChar(self, s:str)->int:
        count=collections.Counter(s)
        for index, char in enumerate(s):
            if count[char]==1:
                return index
        return -1
    ##Explanation:
​Line 1 & 2 (class Solution...): Sets up the LeetCode function to take a word and give back a number.

​Line 3 (count = collections.Counter(s)): Counts how many times each letter appears in the word (e.g., 'e' appears 3 times).

​Line 4 (for index, char in enumerate(s)): Goes through the word letter by letter, keeping track of the position (index) and the letter (char).

​Line 5 & 6 (if count[char] == 1: return index): Checks if the current letter appears only 1 time. If yes, it stops and gives back its position number immediately.

​Line 7 (return -1): If no letter appears only 1 time, it gives back -1.    