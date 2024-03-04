from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        y_cells = []
        for i in range((len(grid)//2)+1):
            y_cells.append((i,i))
            y_cells.append((i, len(grid)-i-1))
        y_cells = list(set(y_cells))
        for i in range(1+(len(grid)//2), len(grid)):
            y_cells.append((i, (len(grid))//2))
        y_cells = set(y_cells)
        
        
        yMap = {}
        ynot_map = {}
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if (i,j) in y_cells:
                    yMap[grid[i][j]] = yMap.get(grid[i][j], 0) + 1
                else:
                     ynot_map[grid[i][j]] = ynot_map.get(grid[i][j], 0) + 1
        
        
        best_min = len(grid)*len(grid)
        yMapSum = sum(list(yMap.values()))
        ynotMapSum = sum(list(ynot_map.values()))
        print(yMapSum, ynotMapSum)
        
        # make 0 key
        total_changes = yMapSum - yMap.get(0, 0) + (ynot_map.get(0,0) + (min(ynot_map.get(1,0),ynot_map.get(2,0))))
        best_min = min(best_min, total_changes)
        total_changes = yMapSum - yMap.get(1, 0) + (ynot_map.get(1,0) + (min(ynot_map.get(0,0),ynot_map.get(2,0))))
        best_min = min(best_min, total_changes)
        total_changes = yMapSum - yMap.get(2, 0) + (ynot_map.get(2,0) + (min(ynot_map.get(1,0),ynot_map.get(0,0))))
        best_min = min(best_min, total_changes)
        
        print(best_min)
        return best_min
s = Solution()

s.minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]])
s.minimumOperationsToWriteY([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]])