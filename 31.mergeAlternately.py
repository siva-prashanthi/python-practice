class Solution:
    def mergeAlternately(self, word1:str,word2:str)->int:
        m=len(word1)
        n=len(word2)
        i=0
        j=0
        result=[]
        while i<m or j<n:
            if i<m:
                result+=word1[i]
                i+=1
            if j<n:
                result+=word2[j]
                j+=1
        return "".join(result)
#Explanation:
1.Create two variables, m and n, to store the length of word1 and word2.
2.Create an empty string variable result to store the result of merged words.
3.Create two pointers, i and j to point to indices of word1 and word2. We initialize both of them to 0.
4.While i < m || j < n:
-->If i < m, it means that we have not completely traversed word1. As a result, we append word1[i] to result. We increment i to point to next index of word1.
-->If j < n, it means that we have not completely traversed word2. As a result, we append word2[j] to result. We increment j to point to next index of word2.
5.Return result.