# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 1) Compute the total length of the list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # Dummy head to simplify merges at the head
        dummy = ListNode(0)
        dummy.next = head

        step = 1
        while step < length:
            prev, curr = dummy, dummy.next
            # process all pairs of runs of size `step`
            while curr:
                # 2a) Split off the first run of length `step`
                left = curr
                right = self._split(left, step)
                curr = self._split(right, step)
                # 2b) Merge the two runs and attach to prev
                merged_head, merged_tail = self._merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            step <<= 1

        return dummy.next

    def _split(self, head: ListNode, n: int) -> ListNode:
        """
        Splits off the first n nodes from head, returns the head of the remainder.
        Also terminates the first part (sets its last.next = None).
        """
        for i in range(n - 1):
            if head:
                head = head.next
            else:
                break
        if not head:
            return None
        next_part = head.next
        head.next = None
        return next_part

    def _merge(self, l1: ListNode, l2: ListNode) -> (ListNode, ListNode):
        """
        Merges two sorted lists l1 and l2, returns (head, tail) of the merged list.
        """
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        # attach the remainder
        tail.next = l1 if l1 else l2
        # advance tail to the end
        while tail.next:
            tail = tail.next
        return dummy.next, tail
