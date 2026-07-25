# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self,head:optional[ListNode])->bool:
        val=[]
        current=head
        while current:
            val.append(current.val)
            current=current.next
        left,right=0,len(val)-1
        while left<right:
            if val[left]!=val[right]:
                return False
            left+=1
            right-=1
        return True
#Explanation:
​Line 7: def isPalindrome(self, head: Optional[ListNode]) -> bool:
​Meaning: Defines the function isPalindrome. It takes the starting node of the linked list (head) as input and returns a boolean (True or False).
​Line 8: val = []
​Meaning: Creates an empty Python list named val to store all the numbers from the linked list.
​Line 9: current = head
​Meaning: Sets a variable named current to point to the start of the linked list so we can iterate through it.
​Line 10: while current:
​Meaning: Starts a loop that continues running as long as current points to a valid node (until it reaches None at the end).
​Line 11: val.append(current.val)
​Meaning: Takes the value inside the current node (current.val) and adds it to our val list.
​Line 12: current = current.next
​Meaning: Moves the current pointer to the next node in the linked list.
​Line 13: left, right = 0, len(val) - 1
​Meaning: Initializes two pointer indices: left starts at the first element (0), and right starts at the last element (len(val) - 1).
​Line 14: while left < right:
​Meaning: Starts a loop that runs until the two pointers meet in the middle.
​Line 15: if val[left] != val[right]:
​Meaning: Checks if the value at the left index is not equal to the value at the right index.
​Line 16: return False
​Meaning: If a mismatch is found, it immediately stops the function and returns False (it is not a palindrome).
​Line 17: left += 1
​Meaning: Moves the left pointer one position forward (to the right).
​Line 18: right -= 1
​Meaning: Moves the right pointer one position backward (to the left).
​Line 19: return True
​Meaning: If the loop finishes without finding any mismatches, it returns True (it is a valid palindrome).