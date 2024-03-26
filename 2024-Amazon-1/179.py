from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        
        def cmp(x, y):
            if (x + y) > (y + x):
                return -1
            return 1
        nums = sorted(nums, key=cmp_to_key(cmp))
        return str(int("".join(nums))) # strips leading 0s