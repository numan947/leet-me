from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # Write your code here
        intervals.sort(key=lambda a:a.start)
        
        prevE = intervals[0].end
        
        for o in intervals[1:]:
            s = o.start
            e = o.end
            if s<prevE:
                return False
            else:
                prevE = e
        return True