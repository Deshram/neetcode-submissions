class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        totalPaths = 0

        def dfs(i,j):
            nonlocal totalPaths
            if i == m-1 and j == n-1:
                totalPaths += 1
                return 
            
            if i<0 or j<0 or i >= m or j >= n:
                return
            
            dfs(i+1,j)
            dfs(i, j+1)

        dfs(0,0)
        return totalPaths