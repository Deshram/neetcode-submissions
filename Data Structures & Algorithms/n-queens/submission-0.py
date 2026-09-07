class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiagnol = set()
        negDiagnol = set()

        board = [["."]*n for i in range(n)]
        output = []
        def backtrack(r):
            nonlocal col, posDiagnol, negDiagnol
            
            if r == n:
                res = ["".join(row) for row in board]
                output.append(res)
                return 
            
            for c in range(n):
                if c in col or r+c in posDiagnol or r-c in negDiagnol:
                    continue

                col.add(c)
                posDiagnol.add(r+c)
                negDiagnol.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiagnol.remove(r+c)
                negDiagnol.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return output
