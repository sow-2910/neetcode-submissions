"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        s, e = 0, 0
        res, count = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res
        


