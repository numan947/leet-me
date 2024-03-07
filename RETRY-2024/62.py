from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def countPaths(curM, curN):
            if curM == m-1 and curN == n-1:
                return 1
            if curM>=m or curN>=n:
                return 0
            return countPaths(curM+1, curN) + countPaths(curM, curN+1)
        
        return countPaths(0,0)


s = Solution()
print(s.uniquePaths(m = 3, n = 7))
print(s.uniquePaths(m = 3, n = 2))