"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def dfs(self, root, depth):
        if not root:
            return None
        
        
        self.dfs(root.right, depth+1)
        self.dfs(root.left, depth+1)
        
        
        if depth in self.res:
            root.next = self.res[depth]
        else:
            root.next = None
        
        self.res[depth] = root
        
        return root
    
    def connect(self, root: 'Node') -> 'Node':
        
        self.res = {}
        node = self.dfs(root, 0)
        
        return node
