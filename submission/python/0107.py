# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        stack = [root]
        res = []
        
        while stack:
            tmp = []
            for i in stack:
                if i.left != None:
                    tmp.append(i.left)
                if i.right != None:
                    tmp.append(i.right)
            res.append([x.val for x in stack])
            stack = tmp[:]
            
        return res[::-1]
