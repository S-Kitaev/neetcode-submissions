# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        p1 = head
        p2 = head

        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        # split and reverse second half
        middle = p1.next
        p1.next = None

        elem = middle

        prev_elem = None
        while elem is not None:
            next_elem = elem.next
            elem.next = prev_elem
            prev_elem = elem
            elem = next_elem

        # prev_elem - head of 2nd ll part == n-1

        # merge lists
        first = head
        second = prev_elem
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2