class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplet = tuple(sorted([nums[i], nums[left], nums[right]]))
                    triplets.append(triplet)
                    left += 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                else:
                    right -= 1

        triplets = list(set(triplets))
        triplets = [list(triplet) for triplet in triplets]
        return triplets