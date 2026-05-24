"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canMerge(self, int_1: Interval, int_2: Interval) -> bool:
        return max(int_1.start, int_2.start) < min(int_1.end, int_2.end)
    
    def mergeMeetings(self, int_1: Interval, int_2: Interval) -> Interval:
        return Interval(min(int_1.start, int_2.start), max(int_1.end, int_2.end))

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) < 2:
            return True

        intervals.sort(key=lambda x: x.start)
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            if self.canMerge(results[-1], intervals[i]):
                return False
            else:
                results.append(intervals[i])

        return True



