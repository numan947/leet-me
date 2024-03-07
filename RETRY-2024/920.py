#Definition of Interval:
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda a: a.start)
        curEnd = -1
        
        for ival in intervals:
            if ival.start<curEnd:
                return False
            curEnd = ival.end
        
        return True

s = Solution()

print(s.can_attend_meetings([(465,497),(386,462),(354,380),(134,189),(199,282),(18,104),(499,562),(4,14),(111,129),(292,345)]))