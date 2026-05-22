class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right] or len(nums) == 1:
            return nums[0]

        while nums[left] != nums[right]:
            mid = (left + right) // 2

            if nums[mid-1] > nums[mid]:
                return nums[mid]

            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid

            if left + 1 == right and nums[left] > nums[right]:
                return nums[right]

        return -1