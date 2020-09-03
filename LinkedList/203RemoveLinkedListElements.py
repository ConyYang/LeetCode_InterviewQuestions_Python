# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        dummy.next = head
        prev, cur = dummy, head

        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
                continue
            prev = prev.next
            cur = cur.next
        return dummy.next