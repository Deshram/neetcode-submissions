class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def dfs(curr, amount):

            if amount == 0:
                return 1
            
            if amount < 0:
                return 0
            
            if (curr, amount) in memo:
                return memo[(curr, amount)]

            res = 0
            for i in range(curr, len(coins)):
                res += dfs(i, amount-coins[i])

            memo[(curr, amount)] = res

            return res

        return dfs(0, amount)