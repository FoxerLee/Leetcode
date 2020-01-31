# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
    
        stack = [[root.left, root.right]]
        
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2: # make sure not None
                if node1.val != node2.val:
                    return False
                else:
                    stack.append([node1.left, node2.right])
                    stack.append([node1.right, node2.left])
            else:
                if node1 == node2:
                    continue
                else:
                    return False
        
        return True
