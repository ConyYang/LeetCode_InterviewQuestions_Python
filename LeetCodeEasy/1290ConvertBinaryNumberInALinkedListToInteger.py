# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head is None:
            return 0
        result = 0
        i = 1
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        arr = arr[::-1]
        for i in range(len(arr)):
            if arr[i]:
                result += pow(2, i)
        return result