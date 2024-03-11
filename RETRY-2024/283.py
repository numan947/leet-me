from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeros = 0
        
        startPoint = 0
        cur = 0
        
        while cur < len(nums):
            if nums[cur] != 0:
                nums[startPoint], nums[cur] = nums[cur], nums[startPoint]
                startPoint+=1
            cur+=1
        # while startPoint<len(nums):
        #     nums[startPoint] = 0
        #     startPoint+=1
            