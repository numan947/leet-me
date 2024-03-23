from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curSum = 0
        for n in nums:
            curSum = max(n, curSum+n)
            res = max(curSum, res)
        return res