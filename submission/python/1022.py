# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = 0
    
    def helper(self, root, path):
        if root == None:
            return
        
        
        self.helper(root.left, path+str(root.val))
        self.helper(root.right, path+str(root.val))
        
        if root.left == None and root.right == None:
            path += str(root.val)
            path = int(path, 2)
            self.res += path
            return
        
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
#         if root == None:
#             return 0
#         if root.left == None or root.right == None:
#             return root.val
        
        
        # self.helper(root.left, str(root.val))
        self.helper(root, "")
        
        return self.res
        
