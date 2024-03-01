from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, cur in enumerate(intervals):
            s, e = cur[0], cur[1]
            if s>newInterval[1]:# current interval is completely right to the new interval
                return res + [newInterval] + intervals[i:]
            elif e<newInterval[0]: # current interval is completely left to the new interval
                res.append([s,e])
            else:
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
        
        res.append(newInterval)
        return res        