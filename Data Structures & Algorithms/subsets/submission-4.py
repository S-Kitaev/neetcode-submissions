class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        pointer = 0

        while nums.sort() not in result and pointer < len(result):

            for i in range(len(nums)):
                # print(result)
                if nums[i] not in result[pointer]:
                    item = result[pointer]  + [nums[i]]
                    item.sort()
                    if item not in result:
                        result.append(item)

            pointer += 1


        return result
