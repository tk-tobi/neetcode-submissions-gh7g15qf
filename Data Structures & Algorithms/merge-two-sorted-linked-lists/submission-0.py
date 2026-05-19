# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the starting anchor
        dummy = ListNode()
        tail = dummy

        # 2. Iterate while both lists have remaining nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Link the smaller node
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2  # Link the smaller node
                list2 = list2.next  # Move list2 pointer forward

            tail = tail.next  # Move the tail tracker forward

        # 3. If one list runs out, append the remainder of the other list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # 4. Return the actual head of the sorted list (skipping the dummy)
        return dummy.next
            


        