# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BFS(self, root, sum):
        if root == None:
            return 
        elif root.left == None and root.right == None:
            self.res += sum*10 + root.val
        else:
            self.BFS(root.left, sum*10+root.val)
            self.BFS(root.right, sum*10+root.val)
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.BFS(root, 0)
        
        return self.res
