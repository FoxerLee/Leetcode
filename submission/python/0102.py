# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level = [root]
        while root and level:
            res.append([l.val for l in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [l for l in tmp if l]
        return res
