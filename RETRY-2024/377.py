from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def countSum(rem):
            if rem == 0:
                return 1
            if rem <0:
                return 0
            cnt = 0
            for i in range(len(nums)):
                cnt += countSum(rem - nums[i])    
            return cnt
        return countSum(target)
s = Solution()

print(s.combinationSum4([1,2,3], 4))
print(s.combinationSum4(nums = [9], target = 3))