from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0
        
        for _ in range(k+1):
            tmpPrices = [x for x in prices]
            
            for u,v,w in flights:
                if prices[u] == float('inf'):
                    continue
                tmpPrices[v] = min(w + prices[u], tmpPrices[v])
            
            prices = tmpPrices
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]