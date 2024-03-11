from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        
        
        def dfs(r, c, vis:set, prvHeight):
            if r<0 or r>=len(heights) or c<0 or c>=len(heights[0]) or (r,c) in vis or heights[r][c]<prvHeight:
                return
            
            vis.add((r,c))
            
            dfs(r+1, c, vis, heights[r][c])
            dfs(r-1, c, vis, heights[r][c])
            dfs(r, c+1, vis, heights[r][c])
            dfs(r, c-1, vis, heights[r][c])
        
        
        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[0])-1, atl, heights[r][len(heights[0])-1])
        
        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights)-1, c, atl, heights[len(heights)-1][c])
        
        
        ret = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in atl and (r,c) in pac:
                    ret.append([r,c])
        return ret    
