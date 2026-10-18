# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode

        num_1 = ""
        while l1:
            num_1 = str(l1.val) + num_1
            l1 = l1.next
            
        num_2 = ""
        while l2:
            num_2 = str(l2.val) + num_2
            l2 = l2.next
        
        num_1, num_2 = int(num_1), int(num_2)

        res = str(num_1+num_2)

        root = ListNode
        initial_pointer = root
        for i in range(len(res), 0, -1):

            new_val = res[i-1]
            root.next = ListNode(new_val)
            root = root.next

        return initial_pointer.next


