# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, a: ListNode, b: ListNode):
        pre = None
        curr = a
        next_ = a

        while (curr != b):
            next_ = curr.next
            curr.next = pre
            pre = curr
            curr = next_

        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return None
        a = head
        b = head
        for i in range(0, k):
            if b == None: return head
            b = b.next

        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead