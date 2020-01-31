# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.left or not root.right:
            return l + r + 1
        return min(l, r) + 1
        
