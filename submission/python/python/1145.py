# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.l = 0
        self.r = 0
        
        def count(root):
            if not root:
                return 0
            
            l_nodes, r_nodes = count(root.left), count(root.right)
            if root.val == x:
                self.l, self.r = l_nodes, r_nodes
            return l_nodes + 1 + r_nodes
        
        count(root)
        return n/2 < max(max(self.l, self.r), n - self.l - self.r - 1)

            
