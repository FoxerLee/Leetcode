# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        self.sum += root.val
        root.val = self.sum
        self.dfs(root.left)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        
        return root
            
