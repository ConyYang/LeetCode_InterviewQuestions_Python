class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None: return [0.0]
        sum_count = []
        ans = []

        self.preorder(root, 0, sum_count)

        for s in sum_count:
            ans.append(float(s[0]) / s[1])

        return ans

    def preorder(self, root, depth, sum_count):
        if root == None: return
        if (depth >= len(sum_count)): sum_count.append([0, 0])
        sum_count[depth][0] += root.val
        sum_count[depth][1] += 1

        self.preorder(root.left, depth + 1, sum_count)
        self.preorder(root.right, depth + 1, sum_count)
