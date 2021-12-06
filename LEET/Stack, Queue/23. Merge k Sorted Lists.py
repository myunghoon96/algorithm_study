#https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode(None)
        cur = head
        
        
        for i,root in enumerate(lists):
            if root != None:
                heapq.heappush(heap, (root.val, i, root))
            
        while heap:
            pop_val, i, pop_node = heapq.heappop(heap)
            cur.next = pop_node
            cur = cur.next
            
            if cur.next != None:
                heapq.heappush(heap, (cur.next.val, i, cur.next))
                               
        return head.next