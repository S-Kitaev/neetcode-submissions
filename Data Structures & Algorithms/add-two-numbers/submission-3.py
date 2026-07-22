# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ln1 = 0
        ln2 = 0

        h1 = l1
        h2 = l2

        while h1:
            ln1 += 1
            h1 = h1.next

        while h2:
            ln2 += 1
            h2 = h2.next

        if ln1 > ln2:
            long = l1
            short = l2
        else:
            long = l2
            short = l1

        additional = 0

        head = ListNode()
        tail = head

        while long:
        
            if short:
                num = long.val + short.val + additional
            else:
                num = long.val + additional

            additional = num // 10
            num = num % 10
            print(additional)
            print(num)

            node = ListNode(num)
            head.next = node
            head = node

            long = long.next
            if short:
                short = short.next

        if additional == 1:
            node = ListNode(additional)
            head.next = node
            head = node

        return tail.next

            