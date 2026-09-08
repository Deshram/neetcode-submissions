class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        prev_start, prev_end = intervals[0]
        min_remo = 0
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start < prev_end: 
                min_remo+=1
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end
        

        return min_remo