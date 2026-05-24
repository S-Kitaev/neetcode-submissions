class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        paths = [1, 1]

        for i in range(1, n):
            ways = paths[-1] + paths[-2]
            paths.append(ways)

        return ways
        