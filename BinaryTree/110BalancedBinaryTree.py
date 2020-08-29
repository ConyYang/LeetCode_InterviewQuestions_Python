# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return (abs(left_height - right_height) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1