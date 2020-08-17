# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def tobst(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = tobst(nums, start, mid - 1)
            node.right = tobst(nums, mid + 1, end)
            return node

        return tobst(nums, 0, len(nums) - 1)