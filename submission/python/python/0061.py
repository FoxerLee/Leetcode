# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        o_tail = head
        n = 1
        while o_tail.next != None:
            o_tail = o_tail.next
            n += 1
        
        o_tail.next = head
        
        n_tail = head
        for _ in range(n-k%n-1):
            n_tail = n_tail.next
        
        n_head = n_tail.next
        
        n_tail.next = None
        
        return n_head
