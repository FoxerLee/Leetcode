# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        t = []
        level = [root]
        flag = 1
        while root and level:
            t = [l.val for l in level]
            if flag == 1:
                flag = -1
            elif flag == -1:
                flag = 1
                t.reverse()
            res.append(t)
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [l for l in tmp if l]
        return res
        
