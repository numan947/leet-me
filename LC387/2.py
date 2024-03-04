from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        gridSum = [[0] * len(grid[0]) for _ in range(len(grid))]
        gridSum[0][0] = grid[0][0]
        
        for i in range(1, len(grid[0])):
            gridSum[0][i] = gridSum[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):
            gridSum[i][0] = gridSum[i-1][0] + grid[i][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                gridSum[i][j] = gridSum[i-1][j] + gridSum[i][j-1] - gridSum[i-1][j-1] + grid[i][j]
        
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if gridSum[i][j]<=k:
                    cnt+=1
        return cnt

s = Solution()

print(s.countSubmatrices( [[7,6,3],[6,6,1]], 18))

print(s.countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20))