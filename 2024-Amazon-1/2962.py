from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        totalSubArrays = len(nums)*(len(nums)+1)
        totalSubArrays//=2
        
        maxVal = max(nums)
        lessThanK = 0
        l = r = 0
        totalMaxSeen = 0
        while r<len(nums):
            if nums[r] == maxVal:
                totalMaxSeen += 1
            while l<r and totalMaxSeen>=k:
                if nums[l] == maxVal:
                    totalMaxSeen-=1
                l+=1
            if totalMaxSeen<k:
                lessThanK += (r-l+1)
            r+=1
        return totalSubArrays - lessThanK

s = Solution()
print(s.countSubarrays(nums = [1,3,2,3,3], k = 2))
print(s.countSubarrays([28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49], 1))