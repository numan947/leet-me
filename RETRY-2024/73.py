from typing import List


class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        


s = Solution()

# s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
s.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])