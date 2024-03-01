from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        
        left = 1
        
        for i in range(len(nums)):
            left*=nums[i]
            output[i] = left
        
        right = 1
        
        for i in range(len(nums)-1, -1, -1):
            tmp = nums[i] # needed for updating rightpointer
            if(i-1>=0): 											## NOTE: I got stuck here, i-1>=0, not i-1>0 
                output[i] = right * output[i-1]
            else:
                output[i] = right
            right *=tmp
        
        return output





s = Solution()

print(s.productExceptSelf([0,0]))
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))