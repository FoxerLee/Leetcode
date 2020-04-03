# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.hash_table = collections.defaultdict(int)
        def dfs(root):
            if not root:
                return
            
            if root.left != None:
                self.hash_table[root.val*2+1] = 1
                root.left.val = root.val*2+1
                dfs(root.left)
            if root.right != None:
                self.hash_table[root.val*2+2] = 1
                root.right.val = root.val*2+2
                dfs(root.right)
        
        root.val = 0
        self.hash_table[0] = 1
        dfs(root)
        

    def find(self, target: int) -> bool:
        return True if target in self.hash_table.keys() else False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
