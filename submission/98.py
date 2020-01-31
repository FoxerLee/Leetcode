# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, left, right):
        if not root:
            return True
        
        value = root.val
        if value <= left or value >= right:
            return False
        
        if not self.helper(root.right, value, right):
            return False
        if not self.helper(root.left, left, value):
            return False
        
        return True
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
