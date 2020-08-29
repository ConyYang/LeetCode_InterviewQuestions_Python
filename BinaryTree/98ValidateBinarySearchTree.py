# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidNode(root, -float('inf'), float('inf'))
    def isValidNode(self, node, min_val, max_val):
        if node is None:
            return True
        if (node.val <= min_val) or (node.val>=max_val):
            return False
        return self.isValidNode(node.left, min_val, node.val) and self.isValidNode(node.right, node.val, max_val)

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         self.prev = None
#         return self.inOrder(root)
#
#     def inOrder(self, root):
#         if root is None:
#             return True
#         if self.inOrder(root.left) is None:
#             return False
#         if self.prev is not None and (root.val <= self.prev.val):
#             return False
#         self.prev = root
#         return self.inOrder(root.right)