class Solution:
    def isPalindrome(self,s:str)->bool:
        s= ''.join(c.lower() for c in s if c.isalnum())
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True        
#Expalnation:
​class Solution:
​Meaning: Defines a class named Solution (required structure for submitting solutions on LeetCode).
​def isPalindrome(self, s: str) -> bool:
​Meaning: Defines the function isPalindrome. It takes an input string s and returns a boolean (True or False).
​s = ''.join(c.lower() for c in s if c.isalnum())
​Meaning: Cleans the input string in one step:
​for c in s if c.isalnum() loops through each character c in s and keeps only alphanumeric characters (letters and numbers).
​c.lower() converts each kept character to lowercase.
​''.join(...) combines all these cleaned characters back into a single string and reassigns it to s.
​left = 0
​Meaning: Creates a pointer named left starting at index 0 (the first character of the cleaned string).
​right = len(s) - 1
​Meaning: Creates a pointer named right starting at index len(s) - 1 (the last character of the cleaned string).
​while left < right:
​Meaning: Starts a loop that runs as long as the left pointer is before the right pointer.
​if s[left] != s[right]:
​Meaning: Checks if the character at the left position does not match the character at the right position.
​return False
​Meaning: If a mismatch is found, it immediately stops and returns False (the string is not a palindrome).
​left += 1
​Meaning: Moves the left pointer one step to the right.
​right -= 1
​Meaning: Moves the right pointer one step to the left.
​return True
​Meaning: If the loop finishes without finding any mismatched characters, it returns True (it is a valid palindrome).