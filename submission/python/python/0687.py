# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def recursive(root):
            if not root:
                return 0
            
            left = recursive(root.left)
            right = recursive(root.right)
            
            tmp_left = 0
            tmp_right = 0
            if root.left and root.val == root.left.val:
                tmp_left = 1 + left
            if root.right and root.val == root.right.val:
                tmp_right = 1 + right
                
            self.ans = max(self.ans, tmp_left+tmp_right)
        
            return max(tmp_left, tmp_right)
        
        recursive(root)
        return self.ans
        
