# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def get_kth_node(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        return dummy.next