class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using XOR
        res = len(nums)
        for i in range(len(nums)):
            res^=(i^nums[i])
        return res
        # SUM(expected array) - SUM(given array) = given number
        # res = 0
        # for i in range(len(nums)):
        #     res += (i-nums[i])
        # res+=len(nums)
        # return res