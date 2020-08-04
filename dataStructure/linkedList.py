class node:
    def __init__(self, data=None):
        self.data = data  # element store by this node
        self.next = None  # store pointer to next node


class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def __len__(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = list()
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print('elements are:\n{}'.format(elements))

    def get_element(self, index):
        # check if is in the range
        assert (index <= self.__len__())
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def delete_element(self, index):
        assert (index <= self.__len__())
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = LinkedList()

my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(4)
my_list.append(7)
my_list.display()

data = my_list.get_element(3)
print(data)

my_list.delete_element(1)
my_list.display()
