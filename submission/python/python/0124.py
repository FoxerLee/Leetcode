# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = float('-inf')
    
    def max_sum(self, root):
        if not root:
            return 0
        
        l = max(self.max_sum(root.left), 0)
        r = max(self.max_sum(root.right), 0)
        
        tmp = root.val + l + r
        self.res = max(self.res, tmp)
        return root.val + max(l, r)
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum(root)
        return self.res
        
