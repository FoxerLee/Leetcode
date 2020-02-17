# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        
        mid = count//2
        
        tmp = head
        for _ in range(mid-1):
            tmp = tmp.next
            
        b_mid_node = tmp
        mid_node = tmp.next
        
        
        root = TreeNode(mid_node.val)
        b_mid_node.next = None
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid_node.next)
        
        return root
    
    
    
