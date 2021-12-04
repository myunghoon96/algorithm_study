#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        cur_node = head
        
        node1 = list1
        node2 = list2       
        
        while True:        
            if node1 is None:
                cur_node.next=node2
                break
            elif node2 is None:
                cur_node.next=node1
                break
            if node1.val<=node2.val:
                cur_node.next=node1
                node1=node1.next
            elif node1.val>node2.val:
                cur_node.next=node2
                node2=node2.next
        
            cur_node = cur_node.next
        return head.next