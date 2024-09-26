# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        Length = 1
        curr = head 

        while curr.next:
            Length+=1
            curr=curr.next
        
        Remainder = k%Length
        if Remainder==0:
            return head
        
        tail = head

        for _ in range(Length-Remainder-1):
            tail=tail.next
        
        new_nodes = tail.next
        tail.next = None
        curr.next = head

        return new_nodes
