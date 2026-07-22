class Solution:
    def ceil(self, a: int, b: int) -> int:
        return int(a / b) if a % b == 0 else a // b + 1

    def boolEatingSpeed(self, piles: List[int], h: int, k: int) -> bool:

        result = []

        for i in range(len(piles)):
            result.append(self.ceil(piles[i], k))

        return sum(result) <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        answer = r

        while r - l + 1 > 0:
            m = l + (r - l) // 2

            if self.boolEatingSpeed(piles, h, m):
                r = m - 1
                answer = m
            else:
                l = m + 1

        return answer