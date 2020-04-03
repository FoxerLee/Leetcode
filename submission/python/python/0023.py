# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for l in lists:
            while l:
                val = l.val
                heapq.heappush(heap, val)
                l = l.next
                
        head = ListNode(-1)
        tmp = head
        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            tmp.next = node
            tmp = tmp.next
            
        return head.next
