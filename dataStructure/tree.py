class Node(object):
    def __init__(self, val):
        self.val = val  # node element
        self.left = None  # left node
        self.right = None  # right node

    def __str__(self):
        # print str value of Node
        return str(self.val)


class Tree(object):
    def __init__(self):
        # root is defined as 'root', which will never be delete
        self.root = Node('root')

    def add(self, val):
        # add node into tree
        node = Node(val)
        # if binary tree is empty, insert node into root
        if self.root is None:
            self.root = node
        else:
            # add root to a queue list
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # if left subtree is empty, add
                if pop_node.left is None:
                    pop_node.left = node
                    return
                # if right subtree is empty, add
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, val):
        # find the parent root of val
        if self.root.val == val:
            # if root has no parent node
            return None
        # add binary tree root node to tmp list
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            # if node left subtree is the node to find
            if pop_node.left and pop_node.left.val == val:
                # return this node, the aimed parent node
                return pop_node
            # if node right subtree is the node to find
            if pop_node.right and pop_node.right.val == val:
                # return this node, the aimed parent node
                return pop_node
            # add node to tmp
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, val):
        # if root is empty, do nothing
        if self.root is None:
            return False

        parent = self.get_parent(val)
        if parent:
            # determine node to be deleted
            del_node = parent.left if parent.left.val == val else parent.right
            # if leftsubtree of deleted node is empty
            if del_node.left is None:
                # if del_node is left child of parent node
                if parent.left.val == val:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            # if right subtree of deleted node is empty
            elif del_node.right is None:
                # if del_node is left child of parent node
                if parent.left.val == val:
                    parent.left = del_node.left
                # if del_node is right child of parent node
                else:
                    parent.right = del_node.left
                del del_node
                return True
            # left and right subtree are both not empty
            else:
                tmp_pre = del_node
                # right sub tree of deleted node
                tmp_next = del_node.right
                # find the most left leaf node of right subtree and substitude
                if tmp_next.left is None:
                    # substitude
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    # make tmp_next point to left most node of right subtree
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # substitude
                # if to be deleted node is left child of parent node
                if parent.left.val == val:
                    parent.left = tmp_next
                # if to be deleted node is right child of parent node
                else:
                    parent.right = tmp_next
                del del_node
                return Tree
        else:
            return False

    def inorder(self, node):
        if node is None:
            return []
        result = [node.val]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item

    def postoder(self, node):
        if node is None:
            return []
        result = [node.val]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + right_item + result

    def preorder(self, node):
        if node is None:
            return []
        result = [node.val]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return result + left_item + right_item


if __name__ == '__main__':
    t = Tree()
    for i in range(1, 11):
        t.add(i)
    print('Inorder traverse: ', t.inorder(t.root))
    print('Preorder traverse: ', t.preorder(t.root))
    print('Postorder traverse: ', t.postoder(t.root))

