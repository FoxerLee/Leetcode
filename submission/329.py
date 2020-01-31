class Solution:
    def dfs(self, mem, matrix, i, j):
        if mem[i][j] != 0:
            return mem[i][j]
        
        steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for s in steps:
            ii = i + s[0]
            jj = j + s[1]
            
            if 0 <= ii < len(matrix) and 0 <= jj < len(matrix[0]) and matrix[ii][jj] > matrix[i][j]:
                mem[i][j] = max(mem[i][j], self.dfs(mem, matrix, ii, jj))
        
        mem[i][j] += 1
        # ans = max(mem[ii][jj])
        return mem[i][j]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        mem = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mem[i][j] = self.dfs(mem, matrix, i, j)
                ans = max(mem[i][j], ans)
                
        return ans
        
