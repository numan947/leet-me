from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def countCoins(remain):
            if remain == 0:
                return 0
            if remain <0:
                return float('inf')
            
            cnt = float('inf')
            for c in coins:
                cnt = min(cnt, 1 + countCoins(remain - c))
            
            return cnt
        
        res = countCoins(amount)
        
        return -1 if res == float('inf') else int(res)

s = Solution()

print(s.coinChange([2], 3))