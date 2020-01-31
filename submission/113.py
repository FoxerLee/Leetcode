# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calculate(self, root, tmp, sum):
        
        if root:
             
            if not root.left and not root.right:
                if root.val == sum:
                    tmp.append(root.val)
                    self.res.append(tmp.copy())
                    tmp.pop()
            else:
                tmp.append(root.val)

                self.calculate(root.left, tmp, sum - root.val)
                self.calculate(root.right, tmp, sum - root.val)

                tmp.pop()
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        self.res = []
        
        self.calculate(root, [], sum)
        
        return self.res
        
        
        
        
