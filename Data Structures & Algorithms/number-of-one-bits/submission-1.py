class Solution:
    def hammingWeight(self, n: int) -> int:

        counter = 0

        if n == 0:
            return counter

        while n > 1:
            res = n % 2
            if res == 1:
                counter += 1
            n = n // 2
        return counter + 1
        