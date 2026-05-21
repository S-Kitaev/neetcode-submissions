class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def isValid(self, s: str) -> bool:
        mistakes = 0

        if len(s) == 1:
            return False

        head = Node(s[0])
        tail = head

        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                elem = Node(s[i])
                elem.prev = tail
                tail.next = elem
                tail = elem

            elif s[i] == ')':
                if tail.data == '(':
                    elem = tail
                    tail = tail.prev
                    tail.next = None
                    elem.prev = None
                else:
                    mistakes = 1
                    break

            elif s[i] == '}':
                if tail.data == '{':
                    elem = tail
                    tail = tail.prev
                    tail.next = None
                    elem.prev = None
                else:
                    mistakes = 1
                    break

            elif s[i] == ']':
                if tail.data == '[':
                    elem = tail
                    tail = tail.prev
                    tail.next = None
                    elem.prev = None
                else:
                    mistakes = 1
                    break

        if mistakes == 0 and head == tail:
            return True
        else:
            return False