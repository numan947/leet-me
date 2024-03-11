from collections import deque
from typing import (
    List,
)
# from lintcode import (
#     Point,
# )

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        dist = {}
        dist[(source.x, source.y)] = 0
        
        dq = deque()
        dq.append(source)
        
        
        while dq:
            cur:Point = dq.popleft()
            if cur.x == destination.x and cur.y == destination.y:
                return dist[(cur.x, cur.y)]
            
            for dx, dy in zip([1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]):
                nx, ny = cur.x + dx, cur.y + dy
                
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx, ny) not in dist.keys() and grid[nx][ny] == 0:
                    dist[(nx, ny)] = 1 + dist[(cur.x, cur.y)]
                    dq.append(Point(nx, ny))
        return -1


s = Solution()

print(s.shortest_path([[0,0,0],[0,0,0],[0,0,0]], [2,0], [2,2]))