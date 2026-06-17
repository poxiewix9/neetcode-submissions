"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)

        for i in range (1, len(intervals)):
            ahead = intervals[i]
            behind = intervals[i-1]

            if ahead.start == behind.start:
                return False

            if ahead.start < behind.end:
                return False

        return True

        