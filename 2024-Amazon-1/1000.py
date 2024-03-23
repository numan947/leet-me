from functools import cache
from heapq import merge
from sys import prefix
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
        if (len(stones)-1)%(k-1): ## Not possible
            return -1
        
        
        prefSum = [0]*len(stones)
        prefSum[0] = stones[0]
        for i in range(1, len(stones)):
            prefSum[i] = prefSum[i-1]+stones[i]
        @cache
        def findMinCost(l,r):
            if r - l + 1 < k: # cannot be merged
                return 0
            minCost = float('inf')
            
            for mid in range(l, r, k-1):
                minCost = min(minCost, findMinCost(l, mid) + findMinCost(mid+1, r)) # merging the smaller piles
            
            
            if ((r - l + 1 - 1)% (k-1)) == 0:
                tmpV = prefSum[l-1] if l-1>=0 else 0
                minCost += (prefSum[r] - tmpV)
            return minCost
        return findMinCost(0, len(stones)-1)
    
s = Solution()

print(s.mergeStones(stones = [3,2,4,1], k = 2))
print(s.mergeStones(stones = [3,5,1,2,6], k = 3))
        
        
        
        
    