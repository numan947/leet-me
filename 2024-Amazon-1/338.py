from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        
        for n in range(1, n+1):
            if 2*offset == n:
                offset = n
            dp[n] = 1 + dp[n-offset]
        
        return dp
            