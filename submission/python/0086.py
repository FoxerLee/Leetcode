# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        before = be_head = ListNode(0)
        after = af_head = ListNode(0)
                
        while head:
            if head.val < x:
                before.next = head
                before = before.next
                # head = head.next
            else:
                after.next = head
                after = after.next
            head = head.next
            
        after.next = None   
        before.next = af_head.next
        
        return be_head.next
            
