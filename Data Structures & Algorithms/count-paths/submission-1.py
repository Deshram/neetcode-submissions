class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i,j):
            if i == m-1 and j == n-1:
                return 1
            
            if i<0 or j<0 or i >= m or j >= n:
                return 0
            
            if (i, j) in memo:
                res = memo[(i, j)]
            else:
                res = dfs(i+1, j) + dfs(i, j+1)
                memo[(i,j)] = res

            return res

        return dfs(0,0)