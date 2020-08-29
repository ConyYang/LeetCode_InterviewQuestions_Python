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
        :rtype: List[List[int]]
        """
        self.result_arr = []
        self.pathSumArr(root, sum, [])
        return self.result_arr

    def pathSumArr(self, root, sum, cur_arr):
        if root is None:
            return []

        if root.left is None and root.right is None and sum == root.val:
            self.result_arr.append(cur_arr + [root.val])

        l = self.pathSumArr(root.left, sum - root.val, cur_arr + [root.val])
        r = self.pathSumArr(root.right, sum - root.val, cur_arr + [root.val])
        return l and r



