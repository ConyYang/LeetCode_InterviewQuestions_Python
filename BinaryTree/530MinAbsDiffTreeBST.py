class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr_tree = []
        self.inorder_traverse(arr_tree, root)

        min_diff = float('inf')
        for i in range(1, len(arr_tree)):
            min_diff = min(min_diff, arr_tree[i] - arr_tree[i-1])

        return min_diff

    def inorder_traverse(self, arr_tree, root):
        if root is None: return
        self.inorder_traverse(arr_tree, root.left)
        arr_tree.append(root.val)
        self.inorder_traverse(arr_tree, root.right)


if __name__ == '__main__':
        node1 = TreeNode(1, None, None)
        node3 = TreeNode(3, None, None)
        node2 = TreeNode(2, node1, node3)
        node6 = TreeNode(6, None, None)
        node4 = TreeNode(4, node2, node6)

        a = Solution()

        arr_tree = a.getMinimumDifference(node4)
        print(arr_tree)


