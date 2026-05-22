class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod_left = 1
        prod_right = 1

        left_prod = [1]
        right_prod = [1]

        for i in nums[:-1]:
            prod_left *= i
            left_prod.append(prod_left)

        r_nums = nums[::-1]

        for i in r_nums[:-1]:
            prod_right *= i
            right_prod.append(prod_right)

        right_prod = right_prod[::-1]

        for i in range(len(left_prod)):
            left_prod[i] = left_prod[i] * right_prod[i]

        return left_prod