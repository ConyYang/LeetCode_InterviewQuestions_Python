# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        total_len = 0
        root = head
        while root:
            total_len += 1
            root = root.next

        ans = [None for _ in range(k)]

        l, r = total_len // k, total_len % k

        prev, root = None, head

        for i in range(k):
            ans[i] = root
            for j in range(l + (1 if r > 0 else 0)):
                prev, root = root, root.next
            if prev: prev.next = None
            r -= 1

        return ans

if __name__ == '__main__':
    sol = Solution()
    # d = ListNode(4, None)
    c = ListNode(3, None)
    b = ListNode(2, c)
    a = ListNode(1, b)
    ans = sol.splitListToParts(a, 2)
    print(ans)