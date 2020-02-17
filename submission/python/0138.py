"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        if head.next == None:
            new_head = Node(head.val, head.next, None)
            if head.random == head:
                new_head.random = new_head
            return new_head
        
        
        node = head
        while node != None:
            new_node = Node(node.val, None, None)
            
            tmp = node.next
            node.next = new_node
            new_node.next = tmp
            
            node = new_node.next
            
        node = head
        while node != None:
            new_node = node.next
            if node.random != None:
                new_node.random = node.random.next
            node = new_node.next
            
        new_head = head.next
        node1 = head
        node2 = new_head
        while node2.next != None:
            node1.next = node1.next.next
            node1 = node1.next
            
            node2.next = node2.next.next
            node2 = node2.next
            
        node1.next = node1.next.next
        return new_head
