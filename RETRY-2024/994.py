from collections import deque
from typing import List

from numpy import empty


class Solution:
    ## NOTE: Basic idea is to just use multi-source bfs, the orange with the largest distance is the maxtime
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        dist = {}
        maxTime = 0
        totalFresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.appendleft((i,j))
                    dist[(i,j)] = 0
                elif grid[i][j] == 1:
                    totalFresh+=1
        
        if totalFresh == 0:
            return 0
        
        
        
        while dq:
            cR, cC = dq.popleft()
            dst = dist.get((cR,cC), 0)
            for rr, cc in [(1,0), (0,1), (-1,0), (0, -1)]:
                tR = cR + rr
                tC = cC + cc
                if tR>=0 and tC>=0 and tR<len(grid) and tC<len(grid[0]) and grid[tR][tC] == 1 and (tR, tC) not in dist.keys():
                    dist[(tR,tC)] = dst + 1
                    maxTime = max(maxTime, dst+1)
                    totalFresh -= 1
                    dq.append((tR,tC))
        
        if totalFresh != 0:
            return -1
        else:
            return maxTime
            
        
    


s = Solution()


print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))