# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recursion(self, root, path):
        if not root:
            return
        path += str(root.val)
        
        if not root.left and not root.right:
            self.paths.append(path)
            return
        path += '->'
        self.recursion(root.left, path)
        self.recursion(root.right, path)
        
        
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.recursion(root, '')
        
        return self.paths
