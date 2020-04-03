class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        self.data = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.data[i][j+1] = self.data[i][j] + matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            res += self.data[i][col2+1] - self.data[i][col1]
            
        return res
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
