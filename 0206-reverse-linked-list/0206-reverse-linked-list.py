# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next

        back = None
        while slow:
            temp = slow.next
            slow.next = back
            back = slow
            slow = temp
        return back