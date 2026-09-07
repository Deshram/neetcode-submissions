class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countdict = {}

        for n in nums:
            countdict[n] = countdict.get(n,0) + 1

        for n in countdict:
            if countdict[n] > 1:
                return True

        return False