class Solution:
    def romanToInt(self,s:str)->int:
        values={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total=0
        for i in range(len(s)):
            if i+1<len(s) and values[s[i]]<values[s[i+1]]:
                total-=values[s[i]]
            else:
                total+=values[s[i]]
        return total
    #Explaantion:

​Line 1–2: Start function and accept Roman string s.
​Lines 3–11: Save each Roman letter's number value in values.
​Line 12: Set total = 0 for running sum.
​Line 13: Loop through each letter in s.
​Line 14: Check if current letter is smaller than next letter.
​Line 15: If smaller, subtract its value from total.
​Lines 16–17: Otherwise, add its value to total.
​Line 18: Return the final total.