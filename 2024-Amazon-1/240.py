from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        b = ROWS-1
        
                
        while l<COLS and b>=0:
            val = matrix[b][l]
            if val == target:
                return True
            elif target < val:
                b -= 1
            elif target > val:
                l+=1
        return False

s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))