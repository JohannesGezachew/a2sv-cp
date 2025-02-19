# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        back = None
        while slow:
            temp = slow.next
            slow.next = back
            back = slow
            slow = temp
        left = head
        right = back 

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True