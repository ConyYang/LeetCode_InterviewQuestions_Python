from BaseLinkedList import Linkedlist


class Solution(Linkedlist):
    def deleteDuplicates(self):
        cur = self.head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
            cur.next = runner
            cur = runner


a_linkedlist = Solution()
a_list = [1, 1, 2]
for a in a_list:
    a_linkedlist.append(a)
a_linkedlist.__repr__()
a_linkedlist.deleteDuplicates()
a_linkedlist.__repr__()
