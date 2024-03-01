from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = intervals[0]
        res = []
        for ival in intervals[1:]:
            s, e = ival
            cs, ce = cur
            
            if ce < s : # so current is already gone
                res.append(cur)
                cur = ival
            else:
                cs = min(s, cs)
                ce = max(e, ce)
                cur = [cs, ce]
        
        res.append(cur)
        return res
        
                