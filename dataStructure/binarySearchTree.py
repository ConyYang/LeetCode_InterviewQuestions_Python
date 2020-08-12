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
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value >= cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        # else:
        #     print("Value already exists!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def printTree(self, cur_node, level=0):
        if cur_node is not None:
            self.printTree(cur_node.left, level + 1)
            print(' ' * 4 * level + '-', cur_node.value)
            self.printTree(cur_node.right, level + 1)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        else:
            # compare left and right to see which is taller
            left_height = self._height(cur_node.left, cur_height + 1)
            right_height = self._height(cur_node.right, cur_height + 1)
            return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._search(value, cur_node.right)
        return False


def fill_tree_random(userTree, num_elements=10, max_int=50):
    for _ in range(num_elements):
        cur_element = randint(0, max_int)
        userTree.insert(cur_element)
    return userTree


def fill_tree_userDefine(userTree, userArray):
    for arr in userArray:
        userTree.insert(arr)
    return userTree


tree = BinarySearchTree()
# tree = fill_tree_random(tree)
tree = fill_tree_userDefine(tree, [1, 2, 2])
tree.printTree(tree.root)
tree.print_tree()

print("Height is " + str(tree.height()))
value = 10
print("Can found " + str(value) + " is " + str(tree.search(10)))
