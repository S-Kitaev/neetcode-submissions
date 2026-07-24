class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.prefix = []
        self.prefix.append([0] * (self.w+1))

        for i in range(len(matrix)):
            self.row = [0]
            for j in range(len(matrix[i])):
                upper = self.prefix[i][j + 1]
                lefter = self.row[j]
                inter = self.prefix[i][j]
                elem = matrix[i][j] + upper + lefter - inter
                self.row.append(elem)
            self.prefix.append(self.row)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        big = self.prefix[row2+1][col2+1]
        upper = self.prefix[row1][col2+1]
        lefter = self.prefix[row2+1][col1]
        inter = self.prefix[row1][col1]
        return big - upper - lefter + inter
        # return self.prefix
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)