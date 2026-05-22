class Solution:
    def maxArea(self, heights: List[int]) -> int:

        water = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            new_water = min(heights[left], heights[right]) * (right - left)
            if new_water > water:
                water = new_water

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return water