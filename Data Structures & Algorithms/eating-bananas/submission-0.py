class Solution:
    def timeToFinish(self, piles, rate):
        time = 0
        for i in piles:
            time += math.ceil(i / rate)

        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_r = 1
        max_r = max(piles)

        while min_r <= max_r:
            mid_r = (min_r + max_r) // 2

            if self.timeToFinish(piles, mid_r) <= h:
                max_r = mid_r-1
            else:
                min_r = mid_r + 1

        return min_r