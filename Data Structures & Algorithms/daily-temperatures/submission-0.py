class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        right = len(temperatures) - 1

        while right >= 0:
            while stack and temperatures[right] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[right] = stack[-1] - right

            stack.append(right)
            right -= 1

        return result
                    


