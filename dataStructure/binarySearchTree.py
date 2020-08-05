from random import randint

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value>cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already exists!")


    def __repr__(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node, level=5):
        if cur_node is not None:
            self._print_tree(cur_node.left, level-1)
            
            self._print_tree(cur_node.right, level-1)


def fill_tree(tree, num_elements=10, max_int=50):
    for _ in range(num_elements):
        cur_element = randint(0, max_int)
        tree.insert(cur_element)
    return tree


tree = BinarySearchTree()
tree = fill_tree(tree)
tree.__repr__()