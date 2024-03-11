from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS-1
        targetRow = None
        while top<=bot:
            row = (top+bot)//2
            if matrix[row][0]<=target<=matrix[row][-1]:
                targetRow = row
                break
            if target>matrix[row][-1]:
                top = row+1
            else:
                bot = row-1
        if targetRow is not None and targetRow>=0 and targetRow<ROWS:
            left, right = 0, COLS-1
            while left<=right:
                mid = left + (right-left)//2
                if matrix[targetRow][mid] == target:
                    return True
                if matrix[targetRow][mid]>target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False    
            