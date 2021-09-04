# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        if head.next is None or head.next.next is None:
            return

        fast = head.next.next
        slow = head.next
        while fast.next is not None and fast.next.next is not None:
            if fast == slow:
                # return slow.next
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
            else:
                fast = fast.next.next
                slow = slow.next
        return