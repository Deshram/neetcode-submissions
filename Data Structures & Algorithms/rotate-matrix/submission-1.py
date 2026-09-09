class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = temp

        for i in range(n):
            for j in range(n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = temp 





