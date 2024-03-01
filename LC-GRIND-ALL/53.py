class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        runningSum = 0
        
        for n in nums:
            if runningSum < 0:
                runningSum = 0
            runningSum += n
            maxSum = max(maxSum, runningSum)
        
        return int(maxSum)