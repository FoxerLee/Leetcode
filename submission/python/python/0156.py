# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        
        left = self.upsideDownBinaryTree(root.left)
        
        root.left.left = root.right
        root.left.right = root
        
        root.left, root.right = None, None
        
        return left
