class Solution:
    def dfs(self, grid, r, c, row, col):
        grid[r][c] = '0'
        if c-1 >= 0 and grid[r][c-1] == '1':
            self.dfs(grid, r, c-1, row, col)
        if r-1 >= 0 and grid[r-1][c] == '1':
            self.dfs(grid, r-1, c, row, col)
        if c+1 < col and grid[r][c+1] == '1':
            self.dfs(grid, r, c+1, row, col)
        if r+1 < row and grid[r+1][c] == '1':
            self.dfs(grid, r+1, c, row, col)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        
        islands_nums = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    islands_nums += 1
                    self.dfs(grid, i, j, row, col)
                    
        return islands_nums
        
        
