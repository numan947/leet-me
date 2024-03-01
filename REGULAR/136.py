class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for t in nums:
            res^=t
        return res