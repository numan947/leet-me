from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        mx = 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    dp[j] = max(dp[j], 1+dp[i])
                    mx = max(mx, dp[j])
        return mx
s = Solution()

print(s.lengthOfLIS([4,10,4,3,8,9]))
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))