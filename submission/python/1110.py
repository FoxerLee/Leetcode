# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, to_delete):
            if not root:
                return None
            
            if root.val in to_delete:
                if root.left:
                    self.queue.append(root.left)
                if root.right:
                    self.queue.append(root.right)
                return None
            
            root.left = self.dfs(root.left, to_delete)
            root.right = self.dfs(root.right, to_delete)
            
            return root
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # to_delete = set(to_delete)
        
        self.queue = []
        self.queue.append(root)
        res = []
        while self.queue != []:
            cur = self.queue.pop(0)
            tmp = self.dfs(cur, to_delete)
            if tmp:
                res.append(tmp)
                
        return res
                    
        
