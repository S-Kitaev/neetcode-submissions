class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        m = 0

        while n >= 2**m:
            m += 1

        differ = 2**m - n

        old = [0, 1]

        for i in range(1, m):
            new = old.copy()

            for j in range(len(new)):
                new[j] += 1

            old = old + new
        print(old, differ)
        if differ - 1 == 0:
            return old
        else:
            return old[:-(differ-1)]
                



        