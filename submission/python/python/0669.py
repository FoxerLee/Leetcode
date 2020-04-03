# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def dfs(root, L, R):
            if not root:
                return None
                        
            if L <= root.val <= R:
                root.left = dfs(root.left, L, R)
                root.right = dfs(root.right, L, R)
                return root
            
            elif root.val < L:
                return dfs(root.right, L, R)
            elif root.val > R:
                return dfs(root.left, L, R)
            
        return dfs(root, L, R)
            
