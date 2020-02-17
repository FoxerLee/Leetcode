class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        neis = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for nei in neis:
                        x = i + nei[0]
                        y = j + nei[1]
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
                            ans += 1
                            
        return ans
        
