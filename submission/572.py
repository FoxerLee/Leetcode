# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, s, t):
        if not s and not t:
            return True
        
        elif not s or not t:
            return False
        
        return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)
        
    def dfs(self, s, t):
        return s != None and (self.check(s, t) or self.dfs(s.left, t) or self.dfs(s.right, t))
    
    
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.dfs(s, t)
        
        
