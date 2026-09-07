class Solution:
    def rob(self, nums: List[int]) -> int:
        i_1 = nums[0]
        if len(nums)<2:
            return i_1
        i_2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(i_2, nums[i]+i_1)
            i_1 = i_2
            i_2 = temp

        return i_2