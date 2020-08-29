class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return self.height(root, 0)

    def height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        else:
            left_height = self.height(cur_node.left, cur_height + 1)
            right_height = self.height(cur_node.right, cur_height + 1)
            return max(left_height, right_height)
