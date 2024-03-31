


from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = {}
        l = r = 0
        ans = 0
        
        while r<len(nums):
            counter[nums[r]] = counter.get(nums[r], 0) + 1
            
            while l<r and counter[nums[r]]>k:
                counter[nums[l]] = counter.get(nums[l])-1
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans
s = Solution()
print(s.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))