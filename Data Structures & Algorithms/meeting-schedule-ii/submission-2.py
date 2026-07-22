"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def makerPoints(self, interval: Interval) -> List[List[int]]:

        first = [interval.start, 1]
        second = [interval.end, -1]

        return first, second

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        new_intervals = []
        for i in range(len(intervals)):
            points = self.makerPoints(intervals[i])
            new_intervals.append(points[0])
            new_intervals.append(points[1])

        new_intervals.sort(key=lambda x: (x[0], x[1]))
        print(new_intervals)
        max_rooms = 0
        cur_rooms = 0

        for inter in new_intervals:
            if inter[1] == 1:
                cur_rooms += 1
            elif inter[1] == -1:
                cur_rooms -= 1
            
            if max_rooms < cur_rooms:
                max_rooms = cur_rooms

        return max_rooms

        