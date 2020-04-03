# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        val = preorder.pop(0)
        mid = inorder.index(val)
        
        root = TreeNode(val)
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])
        
        return root
