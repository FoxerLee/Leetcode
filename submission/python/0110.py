# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, root):
        if not root:
            return 0
        
        else:
            l = self.depth(root.left)
            r = self.depth(root.right)
            if abs(l-r) > 1:
                self.res = False
            return max(l, r) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        self.res = True        
        self.depth(root)
        
        
            
        return self.res
