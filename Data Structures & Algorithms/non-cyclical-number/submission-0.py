class Solution:
    def sumSquares(self, n: int) -> int:

        s = 0
        while n > 0:
            part = n % 10
            n = n // 10
            s += part ** 2

        return s

    def isHappy(self, n: int) -> bool:

        stack = []
        s = self.sumSquares(n)

        while s not in stack:
            if s == 1:
                return True
            else:
                stack.append(s)
                s = self.sumSquares(s)

        return False

