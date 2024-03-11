from typing import List


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
        if not schedule:
            return []
        result = []
        # Write your code here
        all_intervals = []
        for s in schedule:
            for p in range(0, len(s), 2):
                all_intervals.append((s[p], s[p+1]))
        
        if not all_intervals:
            return []
        
        all_intervals.sort()
        
        lastStart = all_intervals[0][0]
        lastEnd = all_intervals[0][1]
        merged = []
        cur = 1
        
        while cur<len(all_intervals):
            curS, curE = all_intervals[cur][0], all_intervals[cur][1]
            
            if curS<=lastEnd:
                lastEnd = max(lastEnd, curE)
            else:
                result.append(Interval(lastEnd, curS))
                lastStart = curS
                lastEnd = curE
            cur+=1
        # merged.append((lastStart, lastEnd))
        
        # if len(merged)<=1:
        #     return []
        
        # nxt = 1
        
        # while nxt<len(merged):
        #     result.append(Interval(merged[nxt-1][1], merged[nxt][0])) 
        #     nxt+=1
        
        return result


s = Solution()

print(s.employee_free_time([[1,2,5,6],[1,3],[4,10]]))
print(s.employee_free_time([[1,3,6,7],[2,4],[2,5,9,12]]))
        
        