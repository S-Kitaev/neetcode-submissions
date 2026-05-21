class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = dict()
        result = []

        max_num = 0

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for i in range(k):
            print(counter)
            result.append(-10**5)

            for k, v in counter.items():
                if v > max_num:
                    result[i] = k
                    max_num = v
                    # counter[k] = -1
            counter[result[i]] = -1

            max_num = 0

        return result
            