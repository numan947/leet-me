from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])
        res = 0
        prevEnd = intervals[0][1]
        
        for s, e in intervals[1:]:
            if s>=prevEnd:
                prevEnd = e
            else:
                res+=1
                prevEnd = min(e, prevEnd)
        
        return res
        