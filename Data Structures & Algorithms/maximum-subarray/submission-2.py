class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]

        for x in nums:
            prefix.append(prefix[-1] + x)

        min_prefix = prefix[0]
        max_sum = nums[0]

        for i in range(1, len(prefix)):
            max_sum = max(max_sum, prefix[i] - min_prefix)
            min_prefix = min(min_prefix, prefix[i])

        return max_sum
        