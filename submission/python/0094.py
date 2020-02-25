# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        tmp = []
        if root.left:
            tmp += self.inorderTraversal(root.left)           
        tmp += [root.val]     
        if root.right:
            tmp += self.inorderTraversal(root.right)
            
        return tmp
