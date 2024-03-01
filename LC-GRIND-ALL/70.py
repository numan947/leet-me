from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(cur):
            if cur>n:
                return 0
            if cur == n:
                return 1
            tmp = climb(cur+1) + climb(cur+2)
            return tmp
        
        return climb(0)

s = Solution()

print(s.climbStairs(2))
print(s.climbStairs(43))
            