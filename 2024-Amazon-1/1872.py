import heapq
from typing import (
    List,
)

class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """
    def minimum_cost(self, sticks: List[int]) -> int:
        # write your code here
        totalcost = 0
        heapq.heapify(sticks)
        
        while len(sticks)>1:
            f = heapq.heappop(sticks)
            s = heapq.heappop(sticks)
            totalcost += (f+s)
            heapq.heappush(sticks, f+s)
        return totalcost
