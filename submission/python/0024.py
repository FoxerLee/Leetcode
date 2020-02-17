# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
#         node = self.swapPairs(head.next.next)
#         tmp = head
#         head = head.next
#         tmp.next = node
#         head.next = tmp
        
        
#         return head
        count = 0
        p = head
        while p != None:
            count += 1
            p = p.next
        
        v = ListNode(-999)
        v.next = None
        p, q, tail = v, head, head
        
        while count > 1:
            for i in range(2):
                if i == 0:
                    tail = q
                tmp = q.next
                q.next = p.next
                p.next = q
                q = tmp
            
            p = tail
            count -= 2
            
        if count != 0:
            p.next = q
            
        return v.next
            
            
            
            
            
