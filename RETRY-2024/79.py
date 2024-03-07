from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def wordFound(r, c, idx):
            if r>=len(board) or c>=len(board[0]) or r<0 or c<0:
                return False
            if idx == len(word)-1:
                return board[r][c] == word[idx]
            if board[r][c] != word[idx]:
                return False
            
            possible = False
            
            if r+1<len(board) and (r+1,c) not in visited:
                visited.add((r+1,c))
                possible = possible or wordFound(r+1, c, idx+1)
                visited.remove((r+1,c))
            if r-1>=0 and (r-1,c) not in visited:
                visited.add((r-1,c))
                possible = possible or wordFound(r-1, c, idx+1)
                visited.remove((r-1,c))
            if c+1<len(board[0]) and (r,c+1) not in visited:
                visited.add((r,c+1))
                possible = possible or wordFound(r, c+1, idx+1)
                visited.remove((r,c+1))
            if c-1>=0 and (r,c-1) not in visited:
                visited.add((r,c-1))
                possible = possible or wordFound(r, c-1, idx+1)
                visited.remove((r,c-1))
            return possible
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited.add((r,c))
                    if wordFound(r, c, 0):
                        return True
                    visited.remove((r,c))
        
        return False

s = Solution()

print(s.exist([["a","a"]], "aaa"))