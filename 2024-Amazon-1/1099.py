from typing import (
    List,
)

class Solution:
    """
    @param nums: An array of integer
    @param target: An integer
    @return: The sum of two numbers smaller than target
    """
    def two_sum_less_than_target(self, nums: List[int], target: int) -> int:
        # write your code here
        nums.sort()
        l = 0
        r = len(nums)-1
        
        ansFound = False
        ans = float('-inf')
        
        while l<r:
            if nums[l] + nums[r]>=target:
                r-=1
            else:
                ansFound = True
                ans = max(ans, nums[l]+nums[r])
                l+=1
        if ansFound:
            return ans
        return -1