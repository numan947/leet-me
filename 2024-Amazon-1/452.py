from functools import cmp_to_key
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return 1
        
        def cmp(a,b):
            if a[1] == b[1]:
                if a[0]<b[0]:
                    return -1
                else:
                    return 1
            else:
                if a[1]<b[1]:
                    return -1
                else:
                    return 1
        
        # points = sorted(points, key=cmp_to_key(cmp))
        points.sort(key=lambda x: x[1])
        res = 0
        curE = points[0][1]
        cur = 1
        
        # print(points)
        while cur < len(points):
            
            ## greedy step
            while cur<len(points) and points[cur][0]<=curE:
                cur+=1
            res+=1
            if cur<len(points):
                curE = points[cur][1]
        return res

s = Solution()

print(s.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))