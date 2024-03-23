from functools import cache
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp = {}
        # @cache
        # def findMaxSquare(r,c):
        #     if r>=len(matrix) or c>=len(matrix[0]) or r<0 or c<0:
        #         return 0
        #     if (r,c) in dp:
        #         return dp[(r,c)]
        #     diag = findMaxSquare(r+1, c+1)
        #     rigt = findMaxSquare(r, c+1)
        #     botm = findMaxSquare(r+1, c)
        #     mxSq = 0
        #     if matrix[r][c] == '1':
        #         mxSq = max(mxSq, 1 + min(diag, rigt, botm))
            
        #     dp[(r,c)] = mxSq
        #     return mxSq
        
        # findMaxSquare(0,0)
        # ans = max(dp.values())
        # return ans*ans
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        mx = 0
        
        for r in range(len(matrix)):
            dp[r][0] = ord(matrix[r][0])-ord('0')
            mx = max(mx, dp[r][0])
        for c in range(len(matrix[0])):
            dp[0][c] = ord(matrix[0][c])-ord('0')
            mx = max(mx, dp[0][c])
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    mx = max(mx, dp[r][c])
        return mx*mx
        

s = Solution()
print(s.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalSquare(matrix = [["0","1"],["1","0"]]))