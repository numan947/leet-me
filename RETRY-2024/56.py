from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # No guarentee of sorted intervals, so we sort first
        if len(intervals) <=1:
            return intervals
        
        intervals.sort()
        result = []
        
        lst = intervals[0]
        
        for i in range(1, len(intervals)):
            cur = intervals[i]
            
            # case -- current interval is outside of the last interval
            if lst[1]<cur[0]:
                result.append(lst)
                lst = cur
            
            # case -- current interval is completely inside the last interval
            elif lst[0] < cur[0] and cur[1] < lst[1]:
                continue ## just skip
            else: # case -- partial overlap
                lst[0] = min(lst[0], cur[0])
                lst[1] = max(lst[1], cur[1])
        
        result.append(lst)           
         
        return result


s = Solution()

print(s.merge( [[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))