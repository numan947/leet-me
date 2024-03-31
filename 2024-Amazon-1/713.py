from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        curMul = 1
        l = r = 0
        while r<len(nums):
            curMul*=nums[r]
            while curMul>=k and l<r:
                curMul/=nums[l]
                l+=1
            
            if curMul < k:
                count += (r-l+1)
            r+=1
        return count
     
s = Solution()

print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
print(s.numSubarrayProductLessThanK(nums = [1,2,3], k = 0))