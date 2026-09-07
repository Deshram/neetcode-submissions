class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j):

            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "0":
                return 

            grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        totalIslands = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    totalIslands += 1
                    dfs(r, c)
                
        return totalIslands