# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        elem_prev = None
        elem = head

        while elem:
            elem_next = elem.next
            elem.next = elem_prev
            elem_prev = elem
            elem = elem_next
        
        return elem_prev

