# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        prev = temp

        while prev.next and prev.next.next:
            
            first = prev.next
            second = prev.next.next

            # First is now pointing to 3rd Node and 2nd Node is no Longer Availbe
            first.next = second.next

            # second is pointing to first
            second.next = first

            # prev is pointing to second after switch
            prev.next = second

            # after swapping it is now our new prev to continue
            prev = first

        return temp.next
