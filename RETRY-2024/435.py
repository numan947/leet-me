from functools import cmp_to_key
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        ans = 0
        intervals.sort(key=lambda x: x[0])
        # def compare(i1, i2):
        #     if i1[0] == i2[0]:
        #         if i1[1] < i2[1]:
        #             return 1
        #         else:
        #             return -1
        #     if i1[0] < i2[0]:
        #         return -1
        #     else:
        #         return 1
        # intervals = sorted(intervals, key=cmp_to_key(compare))
        #print(intervals)
        curE = intervals[0][1]
        for i in range(1, len(intervals)):
            nxt = intervals[i]
            if nxt[0] < curE: # overlap
                ans+=1
                # remove the one with later ending point
                curE = min(curE, nxt[1])
            else:
                curE = nxt[1]
        return ans


s = Solution()

print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))
print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))