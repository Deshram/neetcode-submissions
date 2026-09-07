class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        prev_start, prev_end = intervals[0]
        outputs = [[prev_start, prev_end]]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start <= prev_end:
                prev_start = min(prev_start, curr_start)
                prev_end = max(prev_end, curr_end)
                outputs[-1] = [prev_start, prev_end]
            else:
                outputs.append([curr_start, curr_end])
        
            prev_start, prev_end = outputs[-1]

        return outputs
            