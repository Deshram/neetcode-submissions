class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            curr_sum = 1
            curr_sum += dfs(i-1, j)
            curr_sum += dfs(i+1, j)
            curr_sum += dfs(i, j-1)
            curr_sum += dfs(i, j+1)

            return curr_sum

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(area, maxArea)

        return maxArea



                

