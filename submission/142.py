# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return
        
        
        slow = head.next
        fast = head.next.next
        
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
        
            
        if fast is None or fast.next is None:
            return
        
        slow1 = head
        while slow1 != slow:
            slow1 = slow1.next
            slow = slow.next
            
        return slow
