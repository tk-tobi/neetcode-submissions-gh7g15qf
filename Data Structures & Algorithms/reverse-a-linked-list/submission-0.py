# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_ptr = head
        prv_ptr = None
        while curr_ptr:
            next_head = curr_ptr.next
            curr_ptr.next = prv_ptr
            prv_ptr = curr_ptr
            curr_ptr = next_head
            
            
        
        return prv_ptr
            
