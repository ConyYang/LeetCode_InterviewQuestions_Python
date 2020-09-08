# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        node = self.sum_helper(root, sum)
        left_node = self.pathSum(root.left, sum)
        right_node = self.pathSum(root.right, sum)
        return node + left_node + right_node

    def sum_helper(self, root, sum):
        res = 0
        if root is None:
            return 0
        if root.val == sum:
            res += 1
        return res + self.sum_helper(root.left, sum - root.val) + self.sum_helper(root.right, sum - root.val)