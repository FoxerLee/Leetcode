# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def recurse(self, root, p, q):
        if not root:
            return False

        left_check = self.recurse(root.left, p, q)
        right_check = self.recurse(root.right, p, q)

        cur_check = False

        if root == p or root == q:
            cur_check = True

        if cur_check + left_check + right_check >= 2:
            self.ans = root

        return left_check or right_check or cur_check
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        self.recurse(root, p, q)
        return self.ans
