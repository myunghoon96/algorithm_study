#https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        vals.sort()
        cur = head
        for i in range(len(vals)):
            cur.val = vals[i]
            cur = cur.next
        
        return head
