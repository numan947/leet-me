from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        
        
        def visit(r, c):
            if (r,c) in self.visited or r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!='1':
                return
            self.visited.add((r,c))
            visit(r+1, c)
            visit(r-1, c)
            visit(r, c+1)
            visit(r, c-1)
            
            
        
        
        ans = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in self.visited:
                    ans += 1
                    visit(r,c)
        
        return ans
        




s = Solution()

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))