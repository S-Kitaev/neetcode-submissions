class Solution:
    def y_bs(self, matrix: List[List[int]], target: int) -> int:
        l = 0
        r = len(matrix) - 1

        while r - l + 1 > 0:
            m = l + (r - l) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                return m

            else:
                if matrix[m][0] > target:
                    r = m - 1
                elif matrix[m][-1] < target:
                    l = m + 1
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        idx = self.y_bs(matrix, target)

        if idx == -1:
            return False

        l = 0
        r = len(matrix[idx]) - 1
        
        while r - l + 1 > 0:
            m = l + (r - l) // 2

            if matrix[idx][m] == target:
                return True

            else:
                if matrix[idx][m] <= target:
                    l = m + 1
                else:
                    r = m - 1

        return matrix[idx][m] == target

        
        
        