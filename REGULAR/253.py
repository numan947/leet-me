from typing import (
    List,
)
from lintcode import (
    Interval,
)

import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class MyInterval:
    def __init__(self, s, e):
        self.s = s
        self.e = e
    def __lt__(self, other):
        return self.e < other.e
    def __repr__(self):
        return '['+str(self.s)+','+str(self.e)+']'

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])
        
        # res,count = 0, 0
        # s,e = 0,0
        
        # while s<len(intervals):
        #     if start[s]<end[e]:
        #         s+=1
        #         count+=1
        #     else:
        #         e += 1
        #         count-=1
        #     res = max(res, count)
        
        # return res
        intervals.sort(key=lambda a:a.start)
        
        heap = [MyInterval(intervals[0].start, intervals[0].end)]
        heapq.heapify(heap)
        
        ans = len(heap)
        
        for o in intervals[1:]:
            # print(heap)
            s = o.start
            e = o.end
            
            # print(s, e)
            if s<heap[0].e:
                heapq.heappush(heap, MyInterval(s,e))
            else:
                while heap and s>=heap[0].e:
                    heapq.heappop(heap)
                heapq.heappush(heap, MyInterval(s,e))
            
            ans = max(len(heap), ans)
        
        return ans
        

        
