# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.__successor = None

    def __reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
        # 记录第 n + 1 个节点
            self.__successor = head.next;
            return head;
      # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.__reverseN(head.next, n - 1);

        head.next.next = head;
      # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.__successor;
        return last;
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
              # base case
        if left == 1:
            return self.__reverseN(head, right);
      # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left - 1, right - 1);
        return head;