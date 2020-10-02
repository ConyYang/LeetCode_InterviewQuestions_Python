class heap(object):
    def __init__(self):
        # initialize an empty stack, use array to put heap element
        self.data_list = []

    def get_parent_index(self, index):
        if index==0 or index > len(self.data_list)-1:
            return None
        # return index of parent node
        else:
            return (index-1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = \
            self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        # first put element at last, and then heap from last to front
        # Here we use example of Max Heap
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        # loop, until this element become heap top or less then parent node
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            # swap
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def removeMax(self):
        # delete heap top element, put the last element to heap top, and heapify from bottom to top
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        # heapify
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        # heapify from top to down (max heap)
        total_index = len(self.data_list) -1
        while True:
            maxvalue_index = index
            if 2*index +1 <= total_index and self.data_list[2*index+1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index +1
            if 2*index +2 <= total_index and self.data_list[2*index+2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index+2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


if __name__ == '__main__':
    myheap = heap()
    for i in range(10):
        myheap.insert(i+1)
    print('Build heap', myheap.data_list)
    print('Delete Max', [myheap.removeMax() for _ in range(10)])