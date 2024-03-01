from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dist = {} # dist[(r,c)] = distance from the rotting orange
        m,n = len(grid), len(grid[0])
        dq = deque()
        freshCount = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    dq.append((r,c))
                    dist[(r,c)] = 0
                elif grid[r][c] == 1:
                    freshCount += 1
        
        maxTime = 0
        def isOk(nr, nc):
            return not(nr<0 or nr>=m or nc<0 or nc>=n or (nr, nc) in dist.keys() or grid[nr][nc] == 0)  
        
        while dq:
            tr, tc = dq.popleft()
            
            for dr, dc in [[1, 0], [0,1], [-1, 0], [0, -1]]:
                nr, nc = tr+dr, tc+dc
                
                if isOk(nr, nc):
                    dist[(nr, nc)] = 1 + dist[(tr, tc)]
                    maxTime = max(maxTime, dist[(nr, nc)])
                    dq.append((nr, nc))
                    freshCount -= 1
        
        if freshCount:
            return -1
        return maxTime
        
        