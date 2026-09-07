class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        new_start, new_end = newInterval
        i = 0
        n = len(intervals)

        # 1. Add intervals that come completely before newInterval
        while i < n and intervals[i][1] < new_start:
            output.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        output.append([new_start, new_end])

        # 3. Add remaining intervals
        output.extend(intervals[i:])

        return output