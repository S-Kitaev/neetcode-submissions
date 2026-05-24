class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)
        
        max_amount = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            money = nums[i]
            amount = max(money + max_amount[-2], max_amount[-1])
            max_amount.append(amount)
        print(max_amount)
        return max(max_amount)