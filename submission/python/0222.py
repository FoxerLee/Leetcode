# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def exist(self, idx, d, root):
        l = 0
        r = 2**d - 1
        for _ in range(d):
            mid = l+(r-l)//2
            if idx <= mid:
                r = mid
                root = root.left
            else:
                l = mid + 1
                root = root.right
                
        return root is not None
    
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = 0
        tmp = root
        while tmp.left != None:
            d += 1
            tmp = tmp.left
        
        if d == 0:
            return 1
        
        l = 0
        r = 2**d - 1
        
        while l <= r:
            mid = l+(r-l)//2
            if self.exist(mid, d, root):
                l = mid + 1
            else:
                r = mid - 1
        
        
        return 2**d - 1 + l
