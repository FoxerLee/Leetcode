# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def DFS(self, root, data):
        if not root:
            data += 'null,'
            return data
        
        # if not root.right and not root.left:
        #     data.append(root.val)
        #     return
        data += str(root.val) + ','
        data = self.DFS(root.left, data)
        data = self.DFS(root.right, data)
        
        return data
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """       
        return self.DFS(root, "")
        
    def DFS_2(self, data):
        if data[0] == 'null':
            data.pop(0)
            return None
        
        val = int(data.pop(0))
        
        root = TreeNode(val)
        root.left = self.DFS_2(data)
        root.right = self.DFS_2(data)
        
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        return self.DFS_2(data_list)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
