from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        
        
        @cache
        def possible(idx, target):
            if target == 0:
                return True
            if idx>=len(nums) or target < 0:
                return False
            if target-nums[idx]>=0:
                if possible(idx+1, target-nums[idx]):
                    return True
            return possible(idx+1, target)
        
        return possible(0, total//2)
        