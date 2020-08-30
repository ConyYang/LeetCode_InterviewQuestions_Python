class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def getlength(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def print_element(self):
        cur = self._head
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print("")

    def add_element_start(self, val):
        new_node = Node(val=val)
        if self.is_empty():
            self._head = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    def add_element_end(self, val):
        new_node = Node(val=val)
        if self.is_empty():
            self._head = new_node
        else:
            cur = self._head
            while cur is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def search_element(self, item):
        # Return Bool
        cur = self._head
        while cur is not None:
            if cur.val == item:
                return True

        return False

    def insert(self, val, pos):
        # insert to first
        if pos <=0:
            self.add_element_start(val)
        # insert to last
        elif pos >(self.getlength()-1):
            self.add_element_end(val)
        # insert to mid position
        else:
            cur = self._head
            new_node = Node(val)
            for i in range(0, pos-1):
                cur = cur.next
            new_node.prev = cur
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node

    def remove(self, val):
        # if empty just return
        if self.is_empty():
            return
        else:
            cur = self._head
            # if head is the item to delete
            if cur.val == val:
                # if has only this element
                if cur.next is None:
                    self._head = None
                # set the second element to be head
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return

            while cur is not None:
                if cur.val == val:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    return
                cur = cur.next


