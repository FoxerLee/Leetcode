class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-(i+1)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[-1-j][i]
                matrix[-1-j][i] = matrix[-1-i][-1-j]
                matrix[-1-i][-1-j] = matrix[j][-1-i]
                matrix[j][-1-i] = tmp
