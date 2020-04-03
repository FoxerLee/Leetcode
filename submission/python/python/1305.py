# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, ans = [], [], []
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
                
            while root2:
                stack2.append(root2)
                root2 = root2.left
                
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                tmp = stack1.pop()
                ans.append(tmp.val)
                root1 = tmp.right
            else:
                tmp = stack2.pop()
                ans.append(tmp.val)
                root2 = tmp.right
                
                
        return ans
