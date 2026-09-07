class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        subset = []

        def backtrack(i):
            nonlocal res, subset
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            print(subset)
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)

        backtrack(0)

        return res