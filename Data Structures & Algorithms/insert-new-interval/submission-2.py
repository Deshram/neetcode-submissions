class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []
        new_start, new_end = newInterval
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < new_start:
            output.append(intervals[i])
            i+=1

        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i+=1

        output.append([new_start, new_end])
        output.extend(intervals[i:])

        return output