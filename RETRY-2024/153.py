from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:        
        l,r = 0, len(nums)-1

        if nums[l]<=nums[r]:
            return nums[l]  # already in perfect sort
        
        def minCheck(p):
            left = nums[p-1] if p-1>=0 else float('inf')
            right = nums[p+1] if p+1<len(nums) else float('inf')
            # print(left, nums[p], right)
            return left>=nums[p]<=right
        
        m = -1
        while l<=r:
            m = l + (r-l)//2
            
            if minCheck(m):
                return nums[m]
            
            if nums[l]<=nums[m]: # so l...m is sorted
                if nums[l]>=nums[r]: # so we cannot get a smaller element going left
                    l = m + 1  # go right
                else:
                    r = m - 1 # go left
            else: # so m...r is sorted
                if nums[l]>=nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return nums[m]


s = Solution()

print(s.findMin([4,5,6,7,0,1,2,3]))
print(s.findMin([4,5,6,7,8,1,2,3]))
                  