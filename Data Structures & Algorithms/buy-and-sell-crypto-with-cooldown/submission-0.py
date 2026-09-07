class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in memo:
                return memo[(i,buying)]

            profit = dfs(i+1, buying)

            if buying:
                profit = max(profit, dfs(i+1, False) - prices[i] )
            else:
                profit = max(profit, dfs(i+2, True) + prices[i])


            memo[(i, buying)] = profit
            return profit

        return dfs(0, True)