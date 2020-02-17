# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        count = 0
        p = head
        while p != None:
            count += 1
            p = p.next
            
        v = ListNode(-999)
        v.next = None
        
        p, q, tail = v, head, head
        
        while count >= k:
            for i in range(k):
                if i == 0:
                    tail = q
                    
                tmp = q.next
                q.next = p.next
                p.next = q
                q = tmp
                
            p = tail
            p.next = None
            count -= k
            
        if count != 0:
            p.next = q
            
        return v.next
                
