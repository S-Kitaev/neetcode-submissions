# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        elem = head

        if elem.next is None:
            return None

        length = 0
        while elem.next:
            elem = elem.next
            length += 1

        idx = length - n 
        print(length)
        if length + 1 == n:
            return head.next
        elem = head

        for i in range(idx):
            elem = elem.next

        rem_elem = elem.next
        if elem.next and elem.next.next:
            next_elem = elem.next.next
            rem_elem.next = None
            elem.next = next_elem
        else:
            elem.next = None

        return head
        