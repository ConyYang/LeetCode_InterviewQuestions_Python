class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linkedlist(object):
    def __init__(self):
        self.head = ListNode()

    def append(self, data):
        new_node = ListNode(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def __repr__(self):
        elements = list()
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            elements.append(cur_node.val)
        print('Elements are: {}'.format(elements))