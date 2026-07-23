class Solution:
    def shortestToChar(self,s:str,c:str)->List(int):
        a,n=[],len(s)
        for i in range(n):
            if s[i]==c:
                a.append(i)
        answer=[]
        j=0
        for i in range(n):
            if s[i]==c:
                answer.append(0)
                j+=1
            elif i<a[0]:
                answer.append(a[0]-i)
            elif i>a[-1]:
                answer.append(i-a[-1])
            else:
                answer.append(min((a[j]-i),(i-a[j-1])))
        return answer
    #Explanation:
-->​a, n = [], len(s)  Creates an empty list a for indices of c and gets the total string length n.
--->​for i in range(n):  Loops through every character index in the string s.
--->​if s[i] == c: a.append(i)  If the character matches c, save its position number into list a.
​--->answer, j = [], 0  Creates the result list answer and pointer j (which tracks the next c in a).
​--->for i in range(n):  Loops through the string a second time to calculate distances.
--->​if s[i] == c:  Case 1: If current letter is c itself:
--->​answer.append(0) Distance is 0.
--->​j += 1 Move pointer j to the next upcoming c.
​--->elif i < a[0]: answer.append(a[0] - i)
​In Simple Words: This handles characters at the very start of the word, before we even reach the first 'e'.elif i > a[-1]: answer.append(i - a[-1])
​In Simple Words: This handles characters at the very end of the word, after we have passed the last 'e'.
​Note: In Python, a[-1] means the last item in the list a.
--->else: answer.append(min((a[j] - i), (i - a[j-1])))
​In Simple Words: This handles characters that sit in between two 'e's. We measure the distance to both sides and pick the smaller one.
---​return answer  Returns the final list of calculated shortest distances.