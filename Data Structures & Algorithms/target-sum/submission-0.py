class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curr_sum):
            if i == len(nums) and curr_sum == target:
                return 1
            
            if i == len(nums):
                return 0

            if (i, curr_sum) in memo:
                return memo[(i,curr_sum)]

            res = dfs(i+1, curr_sum+nums[i])
            res += dfs(i+1, curr_sum-nums[i])

            memo[(i, curr_sum)] = res

            return res

        return dfs(0, 0)