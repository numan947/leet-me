from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cur = 0
        # while cur<len(nums):
        #     i = cur        
        #     if nums[i]<=0 or nums[i]>len(nums) or nums[i]==(i+1) or nums[i]==nums[nums[i]-1]: # the original place already have a value
        #         cur+=1
        #         continue # ignore these
        #     nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        # print(nums)
        
        # for u in range(len(nums)):
        #     if nums[u]!=(u+1):
        #         return u+1
        # return len(nums)+1
        # Mark values with negative
        
        
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1<=val<=len(nums):
                if nums[val-1]>0:
                    nums[val-1]*=-1
                elif nums[val-1] ==0:
                    nums[val-1] = -1*(len(nums)+1)
        for i in range(1, len(nums)+1):
            if nums[i-1]>=0:
                return i
        return len(nums)+1
        


s = Solution()
print(s.firstMissingPositive([1,1]))
# print(s.firstMissingPositive([1,2,3,4,5,6]))
# print(s.firstMissingPositive(nums = [1,2,0]))
# print(s.firstMissingPositive([3,4,-1,1]))