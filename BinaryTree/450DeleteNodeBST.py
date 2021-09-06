# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # case 1
        if root == None: return None

        if root.val == key:
            # case 2
            if root.left == None: return root.right
            if root.right == None: return root.left
            # case 3 need find largest of left or min of right
            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while (node.left != None):
            node = node.left
        return node
