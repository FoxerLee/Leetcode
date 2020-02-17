# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def preorder(self, root, left_b, right_b, leaves, flag):
        if not root:
            return
        
        if flag == 2:
            right_b.append(root.val)
        elif flag == 0 or flag == 1:
            left_b.append(root.val)
        elif root.left == None and root.right == None:
            leaves.append(root.val)
        
        
        left_flag = 3
        if flag == 1 or flag == 0:
            left_flag = 1
        elif flag == 2 and root.right == None:
            left_flag = 2
            
        self.preorder(root.left, left_b, right_b, leaves, left_flag)
        
        right_flag = 3
        if flag == 2 or flag == 0:
            right_flag = 2
        elif flag == 1 and root.left == None:
            right_flag = 1
        
        self.preorder(root.right, left_b, right_b, leaves, right_flag)
        
        
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        left_b = []
        right_b = []
        leaves = []
        
        self.preorder(root, left_b, right_b, leaves, 0)
        
        left_b.extend(leaves)
        left_b.extend(reversed(right_b))
        
        return left_b
        
    
