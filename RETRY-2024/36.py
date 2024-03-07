from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def rowOk(i):
            seenMap = [0]*10
            for c in range(len(board[0])):
                curChar = ord(board[i][c]) - ord('0')
                if curChar<0:
                    continue
                if seenMap[curChar] == 1:
                    return False
                seenMap[curChar] = 1
            return True
        def colOk(i):
            seenMap = [0]*10
            for r in range(len(board)):
                curChar = ord(board[r][i]) - ord('0')
                if curChar<0:
                    continue
                if seenMap[curChar] == 1:
                    return False
                seenMap[curChar] = 1
            return True
        
        def subBoxOk(startR, startC):
            seenMap = [0]*10
            for r in range(startR, startR+3):
                for c in range(startC, startC+3):
                    curChar = ord(board[r][c]) - ord('0')
                    if curChar<0:
                        continue
                    if seenMap[curChar] == 1:
                        return False
                    seenMap[curChar] = 1
            return True
        
        for r in range(len(board)):
            if not rowOk(r):
                return False
        for c in range(len(board[0])):
            if not colOk(c):
                return False
        
        for r in range(0, len(board), 3):
            for c in range(0, len(board[0]), 3):
                if not subBoxOk(r, c):
                    return False
        
        return True


s = Solution()

print(s.isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]))