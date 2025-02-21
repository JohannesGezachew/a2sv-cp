# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        slow = dummy
        while slow and slow.next:
            if slow.val == slow.next.val:
                slow.next = slow.next.next
            slow = slow.next
            
        return dummy.next
        