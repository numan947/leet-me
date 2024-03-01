from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.vis = set()
        m,n = len(grid), len(grid[0])
        
        def visit(r, c):
            if r>=m or c>=n or r<0 or c<0 or (r,c) in self.vis or grid[r][c] == '0':
                return
            self.vis.add((r,c))
            visit(r+1, c)
            visit(r-1, c)
            visit(r, c+1)
            visit(r, c-1)
        
        cnt = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == '1' and (r, c) not in self.vis):
                    cnt += 1
                    visit(r, c)
        
        return cnt


s = Solution()

print(s.numIslands([
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]
    ]))