from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = defaultdict(set)
        cols  = defaultdict(set)
        boxes = defaultdict(set)
        
        ROWS, COLS = 9, 9
        
        for row in range(ROWS):
            for col in range(COLS):
                tmp = board[row][col]
                if tmp != '.':
                    rows[row].add(int(tmp))
                    cols[col].add(int(tmp))
                    boxes[(row//3, col//3)].add(int(tmp))
        
        def next_place(row, col):
            if col == COLS - 1:
                return (row+1, 0)
            return (row, col+1)
        
        
        
        def backtrack(row, col):
            if row>=ROWS:
                return True
            n_row, n_col = next_place(row, col)
            
            if board[row][col]!='.':
                return backtrack(n_row, n_col)
            
            for i in range(1, ROWS+1):
                if i not in rows[row] and i not in cols[col] and i not in boxes[(row//3, col//3)]:
                    board[row][col] = str(i)
                    rows[row].add(i)
                    cols[col].add(i)
                    boxes[row//3, col//3].add(i)
                    if(backtrack(n_row, n_col)):
                        return True
                    rows[row].remove(i)
                    cols[col].remove(i)
                    boxes[row//3, col//3].remove(i)
                    board[row][col] = "."
            return False
        backtrack(0,0)
