# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd  = ListNode(0)
        even = ListNode(0)
        temp = 0

        x = odd
        y = even

        while head:
            temp += 1
            if temp % 2 != 0:
                x.next = head
                x = x.next
    
            else:
                y.next = head
                y = y.next
            head = head.next

        y.next = None
        x.next = even.next
        return odd.next

        