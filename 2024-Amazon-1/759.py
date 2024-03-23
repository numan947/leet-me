from typing import (
    List,
)
from unittest import result


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
        
class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        all_intervals = []
        for s in schedule:
            for t in range(0,len(s), 2):
                all_intervals.append((s[t],s[t+1]))
        
        all_intervals.sort(key=lambda x:x[0])
        
        results = []
        
        curS = all_intervals[0][0]
        curE = all_intervals[0][1]
        
        for i in range(1, len(all_intervals)):
            nxtS = all_intervals[i][0]
            nxtE = all_intervals[i][1]
            
            if nxtS<=curE:# overlaps
                curE = max(curE, nxtE)
            else: # no overlap
                results.append(Interval(curE, nxtS))
                curS = nxtS
                curE = nxtE
        return results
        
        
        
    
    
    
s = Solution()
print(s.employee_free_time(schedule = [[1,2,5,6],[1,3],[4,10]]))
