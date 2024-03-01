from functools import cache
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        memo = {}

        def calculate(remain, curIdx):
            if (remain, curIdx) in memo:
                return memo[(remain, curIdx)]
            if remain == 0:
                return 0
            if curIdx >=n or remain < 0:
                return float('-inf')

            res = max(
                1+calculate(remain-nums[curIdx], curIdx+1), calculate(remain, curIdx+1))
            memo[(remain, curIdx)] = res
            return res

        ans = calculate(target, 0)
        memo.clear()
        if ans <= 0:
            return -1
        return ans


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        memo = {}

        def dp(index: int, total: int) -> int:
            if (index, total) in memo:
                return memo[(index, total)]
            if total == 0:
                return 0
            if index == n or total < nums[index]:
                return -float("inf")
            res = max(1 + dp(index + 1, total -
                      nums[index]), dp(index + 1, total))
            memo[(index, total)] = res
            return res

        res = dp(0, target)
        memo.clear()  # absence of this would result in a MLE
        return res if res != -float("inf") else -1
