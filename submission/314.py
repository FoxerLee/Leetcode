# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bfs(self):
        if not self.queue:
            return
        item = self.queue.pop(0)
        node = item[0]
        idx = item[1]
        self.ans_dict[idx].append(node.val)
        
        if node.left != None:
            self.queue.append((node.left, idx-1))
        if node.right != None:
            self.queue.append((node.right, idx+1))
        
        self.bfs()
        
    
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.ans_dict = collections.defaultdict(list)
                                  
        self.queue = [(root, 0)]
        self.bfs()         
        
        ans = [self.ans_dict[key] for key in sorted(self.ans_dict.keys())]
        
        return ans
        
        
