# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list2 is None:
            return list1

        elif list1 is None:
            return list2

        elif list1.val < list2.val:
            new_head = list1
            list1 = list1.next
        else:
            new_head = list2
            list2 = list2.next

        new_tail = new_head

        while list1 or list2:
            elem = None

            if list2 is None:
                elem = list1
                list1 = list1.next

            elif list1 is None:
                elem = list2
                list2 = list2.next

            elif list1.val < list2.val:
                elem = list1
                list1 = list1.next
            else:
                elem = list2
                list2 = list2.next

            new_tail.next = elem
            new_tail = elem

        return new_head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        new_head = lists[0]

        for i in range(1, len(lists)):
            new_head = self.mergeTwoLists(new_head, lists[i])

        return new_head
        