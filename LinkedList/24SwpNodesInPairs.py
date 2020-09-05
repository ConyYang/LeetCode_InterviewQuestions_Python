# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        new_start = p.next
        while True:
            q = p.next
            temp = q.next
            q.next = p
            if temp is None or temp.next is None:
                p.next = temp
                break
            p.next = temp.next
            p = temp
        return new_start