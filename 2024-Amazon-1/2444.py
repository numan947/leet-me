from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minPos = maxPos = -1
        start = r = 0
        
        ans = 0
        
        while r<len(nums):
            if nums[r]<minK or nums[r]>maxK:
                start = r+1 # start needs to be at least after this element
                r+=1
                minPos = -1 # invalidate
                maxPos = -1
                continue
            
            if nums[r] == minK:
                minPos = r
            if nums[r] == maxK:
                maxPos = r
            
            if minPos!=-1 and maxPos!=-1:
                # print(minPos, maxPos)
                ans += min(minPos, maxPos) - start + 1 # number of subarrays from start ... min(minPos, maxPos) + subarray minPos...maxPos
            r+=1
        
        return ans

s = Solution()

print(s.countSubarrays([5,3,1,2,7,5], 1, 5))