from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        maxProfit = 0
        buyPrice = prices[0]
        
        for sp in prices[1:]:
            if sp <buyPrice:
                buyPrice = sp
                continue
            maxProfit = max(maxProfit, sp-buyPrice)
        return maxProfit