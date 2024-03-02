from functools import cache


class Solution:
    @cache
    def climb(self, left):
        if left == 0: # reached the top
            return 1
        if left < 0: # impossible this way
            return 0
        
        return self.climb(left-1) + self.climb(left-2)
    
    def climbStairs(self, n: int) -> int:
        return self.climb(n)



s = Solution()

print(s.climbStairs(2))
print(s.climbStairs(3))