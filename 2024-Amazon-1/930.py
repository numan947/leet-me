from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x): # count number of subarrays with curSum<=x
            if x < 0: # edge case
                return 0
            res = 0
            l = 0
            cur = 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur>x:
                    cur -= nums[l]
                    l+=1
                res += (r-l+1)
            return res
        # number of subarrays with curSum = x ==> COUNT(curSum<=x) - COUNT(curSum<=(x-1))
        return helper(goal) - helper(goal-1)