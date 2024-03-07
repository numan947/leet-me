from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def maxProfit(idx):
            if idx>=len(nums):
                return 0
            return max(nums[idx]+maxProfit(idx+2), maxProfit(idx+1))
        
        return maxProfit(0)
    