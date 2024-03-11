from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        
        for i in range(len(nums)):
            cur = nums[i]
            l = i+1
            r = len(nums)-1
            
            while l<r:
                curSum = cur + nums[l] + nums[r]
                
                if abs(curSum-target)<abs(ans-target):
                    ans = curSum
                    if abs(curSum - target) == 0:
                        return curSum # early stopping
                
                if curSum>target:
                    r-=1
                else:
                    l+=1
        return ans