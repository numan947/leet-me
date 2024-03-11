
import heapq
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        if not intervals:
            return 0
        intervals.sort(key = lambda a: a.start)
        ans = 1
        minHeap = []
        heapq.heappush(minHeap, (intervals[0].end,intervals[0].start)) # e and s
        for ot in intervals[1:]:            
            while minHeap and minHeap[0][0]<=ot.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, (ot.end, ot.start))
            ans = max(ans, len(minHeap))
        
        return ans