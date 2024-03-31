from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        nxt = 1-nums[0]
        l = r = 0
        total = 0
        
        while r<len(nums):
            if nums[r]!=nxt: # broken
                l = r
            nxt = 1 - nums[r]
            total += (r-l+1)
            r+=1
        
        return total

s = Solution()
print(s.countAlternatingSubarrays(nums = [0,1,1,1]))
print(s.countAlternatingSubarrays( [1,0,1,0]))