"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = {}
        for meet in intervals:
            mp[meet.start] = mp.get(meet.start, 0) + 1
            mp[meet.end] = mp.get(meet.end, 0) - 1

        res, prev = 0,0
        for key in sorted(mp.keys()):
            prev += mp[key]
            res = max(res, prev)

        return res            

