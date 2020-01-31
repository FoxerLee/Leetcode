class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        Grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            Grid[i][0] = 1

        for j in range(n):
            Grid[0][j] = 1


        for i in range(1, m):
            for j in range(1, n):
                Grid[i][j] = Grid[i-1][j] + Grid[i][j-1]
                
        return Grid[m-1][n-1]
