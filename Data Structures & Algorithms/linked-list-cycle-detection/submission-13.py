# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None or head.next.next is None:
            return False
        i = head
        j = head.next.next
        while i and j and j.next:
            if i == j:
                return True
            i = i.next
            j = j.next.next
        
        return False