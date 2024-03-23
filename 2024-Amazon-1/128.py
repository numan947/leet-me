from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0
        for n in setNums:
            t = 0
            if n-1 not in setNums:
                while n in setNums:
                    n+=1
                    t+=1
                res = max(res, t)
        return res
    