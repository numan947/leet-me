from re import L
from tracemalloc import start
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        bestPos = -1
        dst = float('inf')
        while l<=r:
            m = l+(r-l)//2
            tmpDst = abs(arr[m] - x)
            if tmpDst < dst:
                dst = tmpDst
                bestPos = m
            if arr[m]<x:
                l = m + 1
            else:
                r = m - 1
        startPoint = bestPos
        leftAdj = float('inf')
        rightAdj = float('inf')
        if startPoint-1>=0:
            leftAdj = abs(arr[startPoint-1] - x)
        if startPoint+1<len(arr):
            rightAdj = abs(arr[startPoint+1]-x)
        if abs(arr[startPoint]-x) >=leftAdj:
            startPoint = startPoint-1
        elif abs(arr[startPoint]-x)>rightAdj:
            startPoint = startPoint+1
        k-=1
        result = [arr[startPoint]]
        l = startPoint-1
        r = startPoint+1
        while k:
            distL = abs(arr[l] - x) if l>=0 else float('inf')
            distR = abs(arr[r]-x) if r<len(arr) else float('inf')
            if distL <= distR:
                result.append(arr[l])
                l-=1
            else:
                result.append(arr[r])
                r+=1
            k-=1
        result.sort()        
        return result

s = Solution()
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -5))
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 9))
# print(s.findClosestElements(arr = [1,2,3,4,10], k = 4, x = 7))

# print(s.findClosestElements(arr = [10,20,25, 27, 30, 32, 34, 40,100], k = 4, x = 23))
print(s.findClosestElements([0,2,2,3,4,20,20,20,20,20],1,5))