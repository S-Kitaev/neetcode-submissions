class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hashmap = dict()

        for num in nums:
            hashmap[num] = None

        for num in nums:
            if num + 1 not in hashmap and num < len(nums):
                return num + 1
        
        return 0

        