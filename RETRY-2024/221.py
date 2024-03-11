from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # cache = {}
        # def helper(r, c):
        #     if r>=ROWS or c>=COLS or r<0 or c<0:
        #         return 0
        #     if (r,c) in cache.keys():
        #         return cache[(r,c)]
        #     down = helper(r+1, c)
        #     right = helper(r, c+1)
        #     diag = helper(r+1, c+1)
        #     cache[(r,c)] = 0
        #     if matrix[r][c] == '1':
        #         cache[(r,c)] = 1 + min(diag, right, down)
        #     return cache[(r,c)]
        
        # helper(0,0)
        # return max(cache.values())**2
        
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        mx = 0
        for r in range(len(matrix)):
            dp[r][0] = ord(matrix[r][0]) - ord('0')
            mx = max(mx, dp[r][0])
            
        for c in range(len(matrix[0])):
            dp[0][c] = ord(matrix[0][c]) - ord('0')
            mx = max(mx, dp[0][c])
            
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    mx = max(mx, dp[r][c])
        # print(dp)
        
        return mx*mx
    
s = Solution()
print(s.maximalSquare(matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]))