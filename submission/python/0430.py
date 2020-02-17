"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def find(self, node):
        if not node:
            return
        self.find(node.next)
        self.find(node.child)
        
        node.next = self.last
        if self.last:
            self.last.prev = node
        self.last = node
        node.child = None
        
        
    def flatten(self, head: 'Node') -> 'Node':
        self.last = None
        self.find(head)
        
        return self.last
            
