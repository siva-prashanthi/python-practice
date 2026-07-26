# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head:Optional[ListNode])->Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
#Explanation:
​Goal: Turn all the arrows in a linked list backwards.
​Key Pointers:
​prev: Points to the previous node (starts at None).
​curr: Points to the node you are currently on (starts at head).
​The 4 Steps inside the loop:
​Save: next_node = curr.next (Remember where to go next)
​Flip: curr.next = prev (Point current arrow backwards)
​Move prev: prev = curr (Step prev forward)
​Move curr: curr = next_node (Step curr forward)
​Result: Return prev as the new head when curr becomes None.