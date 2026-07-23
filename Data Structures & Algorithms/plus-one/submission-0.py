class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        additional = 1
        pointer = len(digits) - 1
        result = []

        while pointer >= 0:

            num = digits[pointer] + additional

            if num == 10:
                num = 0
                additional = 1
            else:
                additional = 0

            result.append(num)
            pointer -= 1

        if additional == 1:
            result.append(additional)

        return result[::-1]

        
        