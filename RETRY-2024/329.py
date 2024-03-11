from functools import cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = {}
        
        def findLongestPath(r, c, prevVal):
            if r<0 or r>=len(matrix) or c<0 or c>=len(matrix[0]) or matrix[r][c]<=prevVal:
                return 0
            if (r,c) in dp.keys():
                return dp[(r,c)]
            longest = 1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                tr, tc = dr + r, dc + c
                longest = max(longest, 1 + findLongestPath(tr, tc, matrix[r][c]))
            
            dp[(r,c)] = longest
            return longest
        
        ans = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                tmp  = findLongestPath(r, c, -1)
                if  tmp > ans:
                    ans = tmp
        
        return ans


s = Solution()

print(s.longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))
print(s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(s.longestIncreasingPath( [[1]]))