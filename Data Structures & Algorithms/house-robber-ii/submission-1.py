class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 4:
            return max(nums)
        # without last
        max_amount_1 = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums) - 1):
            money = nums[i]
            amount = max(money + max_amount_1[-2], max_amount_1[-1])
            max_amount_1.append(amount)

        # without first
        
        max_amount_2 = [nums[1], max(nums[2], nums[1])]

        for i in range(3, len(nums)):
            money = nums[i]
            amount = max(money + max_amount_2[-2], max_amount_2[-1])
            max_amount_2.append(amount)

        return max(max(max_amount_1), max(max_amount_2))
        