from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def findMaxDist(lst):
            minSum = maxSum = lst[0][0] + lst[0][1]
            minDif = maxDif = lst[0][0] - lst[0][1]
            pt1 = pt2 = pt3 = pt4 = 0 # pt1, pt2 => tracks the diff between sums, and pt3 and pt4 => tracks the diff between difs
            for i in range(1, len(lst)):
                p = lst[i]
                tmpSum = p[0]+p[1]
                tmpDif = p[0]-p[1]
                
                if tmpSum < minSum:
                    minSum = tmpSum
                    pt1 = i
                elif tmpSum>maxSum:
                    maxSum = tmpSum
                    pt2 = i
                
                if tmpDif<minDif:
                    minDif = tmpDif
                    pt3 = i
                elif tmpDif>maxDif:
                    maxDif = tmpDif
                    pt4 = i
            if abs(minSum - maxSum) >= abs(minDif-maxDif):
                return abs(minSum-maxSum), pt1, pt2
            return abs(minDif - maxDif), pt3, pt4
        
        _, pt1, pt2 = findMaxDist(points)
        
        tmpList1 = points[:pt1] + points[pt1+1:]
        ans1, _, _ = findMaxDist(tmpList1)
        
        tmpList2 = points[:pt2] + points[pt2+1:]
        ans2, _, _ = findMaxDist(tmpList2)
        
        return min(ans1, ans2)
        
s = Solution()
print(s.minimumDistance(points = [[3,10],[5,15],[10,2],[4,4]]))
print(s.minimumDistance(points = [[1,1],[1,1],[1,1]]))
print(s.minimumDistance([[5,3],[4,6],[2,4],[1,8],[3,9],[1,6]])) # 6
print(s.minimumDistance([[1,5],[9,7],[8,1],[1,1],[10,8],[5,8]])) #12
print(s.minimumDistance([[4,7],[8,2],[3,9],[1,10],[1,9],[5,4],[5,1],[10,8]]))#13