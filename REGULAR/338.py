class Solution:
    def countBits(self, n: int) -> List[int]:
        # can be solved in nlogn using brute force
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        
        return dp