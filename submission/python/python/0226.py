# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        
        
        root.left = left
        root.right = right
        
        return root
