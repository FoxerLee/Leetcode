# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, par=None):
        if not root:
            return
        root.par = par
        self.dfs(root.left, root)
        self.dfs(root.right, root)
    
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.dfs(root)
        
        queue = collections.deque([(target, 0)])
        
        visited = [target]
        while queue:
            node, d = queue.popleft()
            if d == K:
                return [node.val] + [node.val for node, _ in queue]
            
            for t in (node.left, node.right, node.par):
                if t and t not in visited:
                    visited.append(t)
                    queue.append((t, d+1))
        
        return []
