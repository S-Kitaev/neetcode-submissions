class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        inv_nums = nums.copy()

        mydict = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mydict:
                return [mydict[diff], i]
            mydict[n] = i



        