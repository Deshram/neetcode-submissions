class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = 0
        res = []
        curr = []

        def dfs(i, curr, total):
            nonlocal res
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(nums):
                return 

            total += nums[i]
            curr.append(nums[i])
            dfs(i, curr, total)
            
            total -= nums[i]
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, curr, total)
        return res



            